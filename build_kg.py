#!/usr/bin/env python3
"""
build_kg.py
===========
Parse Epic's EHI Export documentation (the open.epic "DocGen" HTML set) into a
structured schema dataset and a knowledge graph.

INPUT   a .zip (or directory) of EHI table .htm files.
OUTPUT  data/schema.jsonl     one JSON record per table (full, incl. descriptions)
        data/meta.json        provenance: source, version, counts
        data/stats.json       computed statistics
        graph/epic_ehi.ttl    RDF / Turtle knowledge graph
        graph/epic_ehi.graphml property graph (Neo4j / Gephi / Cytoscape)

PROVENANCE / LICENSING
----------------------
Epic publishes the EHI Export Specification to satisfy ONC Cures Act
information-blocking / EHI-export requirements. The table/column *structure*
(names, types, keys, organization-specific flags) is factual schema metadata.
The per-column *descriptions* are Epic's text. If you intend to publish the
graph publicly and want to be conservative about that text, build with
    --no-descriptions
which omits descriptions from the .ttl and .graphml (schema.jsonl always keeps
the full record, since that is your own local extract). See README.md.

USAGE
-----
    pip install beautifulsoup4 lxml networkx
    python build_kg.py --src /path/to/Epic_EHI_Tables.zip --out .
    python build_kg.py --src ./pages_dir --out . --no-descriptions
"""
from __future__ import annotations
import argparse, json, re, sys, zipfile, datetime
from pathlib import Path
from collections import Counter, defaultdict

from bs4 import BeautifulSoup

PARSER = "lxml"  # falls back to html.parser if lxml missing
ORG_RE = re.compile(r"organization-specific values\s*:?\s*(yes|no)", re.I)

# IRIs are identifiers only; they need not resolve.
BASE = "https://open.epic.com/ehi"
EHI = f"{BASE}/schema#"


# --------------------------------------------------------------------------- #
# Input
# --------------------------------------------------------------------------- #
def iter_pages(src: Path):
    """Yield (table_name, html_text) for every table page in a zip or dir."""
    if src.is_file() and src.suffix.lower() == ".zip":
        z = zipfile.ZipFile(src)
        for n in z.namelist():
            base = n.replace("\\", "/").split("/")[-1]
            if base.lower().endswith(".htm") and base.lower() != "_index.htm":
                yield base[:-4], z.read(n).decode("cp1252", "replace")
    elif src.is_dir():
        for p in sorted(src.rglob("*.htm")):
            if p.name.lower() != "_index.htm":
                yield p.stem, p.read_text(encoding="cp1252", errors="replace")
    else:
        sys.exit(f"Unsupported --src: {src} (want a .zip or a directory)")


def provenance(src: Path) -> dict:
    """Pull the DocGen version token, its timestamp, and the released version."""
    info = {"source": "https://open.epic.com/EHITables (EHI Export Specification)",
            "docgen_folder": None, "docgen_token": None, "docgen_timestamp": None,
            "released_version": None}
    idx_text = ""
    if src.is_file() and src.suffix.lower() == ".zip":
        z = zipfile.ZipFile(src)
        for n in z.namelist():
            folder = n.replace("\\", "/").split("/")[0]
            if folder.startswith("DocGen"):
                info["docgen_folder"] = folder
                m = re.match(r"DocGen_([^_]+)_([\d.\-_]+)", folder)
                if m:
                    info["docgen_token"] = m.group(1)
                    info["docgen_timestamp"] = m.group(2)
                break
        idx = [n for n in z.namelist() if n.lower().endswith("_index.htm")]
        if idx:
            idx_text = z.read(idx[0]).decode("cp1252", "replace")
    m = re.search(r"released version of ([A-Za-z]+\s+\d{4})", idx_text)
    if m:
        info["released_version"] = m.group(1).strip()
    return info


# --------------------------------------------------------------------------- #
# Parsing one page
# --------------------------------------------------------------------------- #
def _txt(el) -> str:
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip() if el else ""


def _int(s):
    try:
        return int(re.sub(r"[^\d]", "", s))
    except (ValueError, TypeError):
        return None


def parse_columns(table) -> list[dict]:
    """Column Information table -> list of column dicts."""
    cols, cur = [], None
    body = table.find("tbody") or table
    for tr in body.find_all("tr", recursive=False):
        if tr.find("th"):                       # header row of the column table
            continue
        nested = tr.find("table")
        if nested is not None:                  # detail row: description + flag
            if cur is None:
                continue
            joined = _txt(nested)
            m = ORG_RE.search(joined)
            if m:
                cur["org_specific"] = m.group(1).lower() == "yes"
            desc_td = nested.find("td", style=lambda s: s and "white-space" in s)
            desc = _txt(desc_td) if desc_td else None
            if desc:
                desc = ORG_RE.sub("", desc).strip()
                cur["description"] = desc or None
            continue
        vals = [_txt(td) for td in tr.find_all("td", recursive=False)]
        if vals and re.fullmatch(r"\d+", vals[0]) and len([v for v in vals if v]) >= 3:
            cur = {"ordinal": _int(vals[0]), "name": vals[1], "type": vals[2],
                   "discontinued": len(vals) > 3 and vals[3].lower().startswith("y"),
                   "description": None, "org_specific": False}
            cols.append(cur)
    return cols


def parse_generic_rows(table) -> list[dict]:
    """Best-effort row reader for the (rare) Foreign Key section."""
    out = []
    body = table.find("tbody") or table
    trs = body.find_all("tr", recursive=False)
    if not trs:
        return out
    headers = [_txt(c) for c in trs[0].find_all(["th", "td"])]
    for tr in trs[1:]:
        cells = [c for c in (_txt(td) for td in tr.find_all("td")) if c]
        if not cells:
            continue
        out.append(dict(zip(headers, cells)) if headers and len(headers) >= len(cells)
                   else {"values": cells})
    return out


def parse_page(name: str, html_text: str) -> dict:
    soup = BeautifulSoup(html_text, PARSER)
    rec = {"table": name, "description": None,
           "primary_key": [], "columns": [], "foreign_keys": []}

    kv = soup.find("table", class_="KeyValue")
    if kv:
        v = kv.find("td", class_="T1Value")
        if v:
            rec["description"] = _txt(v)

    for sh in soup.find_all("table", class_="SubHeader3"):
        label = _txt(sh).lower()
        data = sh.find_next("table")
        if data is None:
            continue
        if label.startswith("primary key"):
            body = data.find("tbody") or data
            for tr in body.find_all("tr", recursive=False):
                tds = tr.find_all("td", recursive=False)
                if len(tds) >= 2 and _txt(tds[0]) and _txt(tds[0]).lower() != "column name":
                    rec["primary_key"].append(
                        {"column": _txt(tds[0]), "ordinal": _int(_txt(tds[1]))})
        elif label.startswith("column information"):
            rec["columns"] = parse_columns(data)
        elif "foreign key" in label:
            rec["foreign_keys"] = parse_generic_rows(data)
    return rec


# --------------------------------------------------------------------------- #
# Graph emit helpers
# --------------------------------------------------------------------------- #
def ttl_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def t_iri(name): return f"<{BASE}/table/{name}>"
def c_iri(table, col): return f"<{BASE}/column/{table}/{col}>"


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description="Build Epic EHI schema dataset + KG.")
    ap.add_argument("--src", required=True, type=Path, help=".zip or directory of EHI .htm pages")
    ap.add_argument("--out", default=Path("."), type=Path, help="output repo root")
    ap.add_argument("--no-descriptions", action="store_true",
                    help="omit Epic's prose descriptions from .ttl and .graphml")
    args = ap.parse_args()

    global PARSER
    try:
        BeautifulSoup("<x/>", PARSER)
    except Exception:
        PARSER = "html.parser"

    data_dir = args.out / "data"
    graph_dir = args.out / "graph"
    data_dir.mkdir(parents=True, exist_ok=True)
    graph_dir.mkdir(parents=True, exist_ok=True)

    prov = provenance(args.src)

    # ---- parse all pages, stream to schema.jsonl ----
    records = []
    with (data_dir / "schema.jsonl").open("w", encoding="utf-8") as fh:
        for i, (name, html_text) in enumerate(iter_pages(args.src), 1):
            rec = parse_page(name, html_text)
            records.append(rec)
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            if i % 1000 == 0:
                print(f"  parsed {i} tables ...", flush=True)
    print(f"Parsed {len(records)} tables.")

    # ---- indexes for FK inference ----
    # single-column PK ownership, unambiguous only
    pk_cols = defaultdict(list)            # colname -> [tables for which it is the sole PK]
    table_names = {r["table"] for r in records}
    for r in records:
        if len(r["primary_key"]) == 1:
            pk_cols[r["primary_key"][0]["column"]].append(r["table"])
    pk_owner = {col: tbls[0] for col, tbls in pk_cols.items() if len(tbls) == 1}

    # ---- build edges + stats ----
    type_counter = Counter()
    n_columns = n_org = n_disc = 0
    composite_pk = 0
    inferred_edges = []      # (table, column, target)
    explicit_edges = []      # (table, column?, target)
    inbound = Counter()
    pk_set = {(r["table"], pk["column"]) for r in records for pk in r["primary_key"]}

    for r in records:
        if len(r["primary_key"]) > 1:
            composite_pk += 1
        for c in r["columns"]:
            n_columns += 1
            type_counter[c["type"]] += 1
            n_org += bool(c["org_specific"])
            n_disc += bool(c["discontinued"])
            tgt = pk_owner.get(c["name"])
            if tgt and tgt != r["table"]:
                inferred_edges.append((r["table"], c["name"], tgt))
                inbound[tgt] += 1
        # explicit FK rows: keep any value that names a known table
        for fkrow in r["foreign_keys"]:
            for v in (fkrow.values() if isinstance(fkrow, dict) else []):
                for tok in re.findall(r"[A-Z][A-Z0-9_]{2,}", str(v)):
                    if tok in table_names and tok != r["table"]:
                        explicit_edges.append((r["table"], None, tok))
                        inbound[tok] += 1

    stats = {
        "tables": len(records),
        "columns_total": n_columns,
        "avg_columns_per_table": round(n_columns / max(len(records), 1), 1),
        "largest_table": max(((len(r["columns"]), r["table"]) for r in records),
                             default=(0, None))[::-1],
        "columns_org_specific": n_org,
        "pct_columns_org_specific": round(100 * n_org / max(n_columns, 1), 1),
        "tables_with_org_specific_col": sum(
            1 for r in records if any(c["org_specific"] for c in r["columns"])),
        "columns_discontinued": n_disc,
        "tables_with_composite_pk": composite_pk,
        "tables_with_explicit_fk_section": sum(1 for r in records if r["foreign_keys"]),
        "inferred_reference_edges": len(inferred_edges),
        "explicit_reference_edges": len(explicit_edges),
        "top_referenced_tables": inbound.most_common(15),
        "top_data_types": type_counter.most_common(12),
    }
    (data_dir / "stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")

    meta = {**prov,
            "parsed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "n_tables": len(records), "n_columns": n_columns,
            "descriptions_in_graph": not args.no_descriptions}
    (data_dir / "meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

    # ---- RDF / Turtle ----
    write_turtle(graph_dir / "epic_ehi.ttl", records, pk_set,
                 inferred_edges, explicit_edges, prov, not args.no_descriptions)

    # ---- GraphML ----
    write_graphml(graph_dir / "epic_ehi.graphml", records, pk_set,
                  inferred_edges, explicit_edges, not args.no_descriptions)

    print("\n=== SUMMARY ===")
    print(json.dumps(stats, indent=2))


def write_turtle(path, records, pk_set, inferred_edges, explicit_edges, prov, with_desc):
    edges_by_col = defaultdict(list)
    for (t, c, tgt, inferred) in (
            [(t, c, tgt, True) for (t, c, tgt) in inferred_edges] +
            [(t, c, tgt, False) for (t, c, tgt) in explicit_edges if c]):
        edges_by_col[(t, c)].append((tgt, inferred))

    with path.open("w", encoding="utf-8") as f:
        f.write(f"""@prefix ehi:  <{EHI}> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix dct:  <http://purl.org/dc/terms/> .

<{BASE}/dataset> a ehi:Dataset ;
    dct:source <https://open.epic.com/EHITables> ;
    dct:hasVersion {ttl_str((prov.get('docgen_token') or '') + ' / released ' + (prov.get('released_version') or 'unknown'))} ;
    rdfs:comment "Knowledge graph derived from Epic's EHI Export Specification (open.epic DocGen export). Structure is factual schema metadata; descriptions are Epic's text." .

ehi:Table a rdfs:Class . ehi:Column a rdfs:Class .
ehi:inTable a rdfs:Property . ehi:hasColumn a rdfs:Property .
ehi:references a rdfs:Property . ehi:dataType a rdfs:Property .

""")
        for r in records:
            t = r["table"]
            f.write(f"{t_iri(t)} a ehi:Table ; rdfs:label {ttl_str(t)}")
            if with_desc and r["description"]:
                f.write(f" ;\n    rdfs:comment {ttl_str(r['description'])}")
            for pk in r["primary_key"]:
                f.write(f" ;\n    ehi:hasPrimaryKeyColumn {c_iri(t, pk['column'])}")
            f.write(" .\n")
            for c in r["columns"]:
                f.write(f"{c_iri(t, c['name'])} a ehi:Column ; rdfs:label {ttl_str(c['name'])} ;\n")
                f.write(f"    ehi:inTable {t_iri(t)} ; ehi:ordinal {c['ordinal'] or 0} ;\n")
                f.write(f"    ehi:dataType {ttl_str(c['type'] or '')} ;\n")
                f.write(f"    ehi:discontinued {'true' if c['discontinued'] else 'false'} ;\n")
                f.write(f"    ehi:mayContainOrgSpecificValues {'true' if c['org_specific'] else 'false'}")
                if (t, c["name"]) in pk_set:
                    f.write(" ;\n    ehi:isPrimaryKey true")
                for tgt, inferred in edges_by_col.get((t, c["name"]), []):
                    f.write(f" ;\n    ehi:references {t_iri(tgt)} ;\n    ehi:referenceInferred {'true' if inferred else 'false'}")
                if with_desc and c["description"]:
                    f.write(f" ;\n    rdfs:comment {ttl_str(c['description'])}")
                f.write(" .\n")
        f.write("\n")
    print(f"Wrote {path}")


def write_graphml(path, records, pk_set, inferred_edges, explicit_edges, with_desc):
    import networkx as nx
    G = nx.DiGraph()
    for r in records:
        tid = "T:" + r["table"]
        G.add_node(tid, kind="table", label=r["table"],
                   description=(r["description"] or "") if with_desc else "")
        for c in r["columns"]:
            cid = f"C:{r['table']}.{c['name']}"
            G.add_node(cid, kind="column", label=c["name"], table=r["table"],
                       data_type=c["type"] or "", ordinal=c["ordinal"] or 0,
                       discontinued=bool(c["discontinued"]),
                       org_specific=bool(c["org_specific"]),
                       is_primary_key=(r["table"], c["name"]) in pk_set,
                       description=(c["description"] or "") if with_desc else "")
            G.add_edge(tid, cid, rel="HAS_COLUMN")
    for (t, c, tgt) in inferred_edges:
        G.add_edge(f"C:{t}.{c}", "T:" + tgt, rel="REFERENCES", inferred=True)
    for (t, c, tgt) in explicit_edges:
        src = f"C:{t}.{c}" if c else "T:" + t
        if src in G:
            G.add_edge(src, "T:" + tgt, rel="REFERENCES", inferred=False)
    nx.write_graphml(G, path)
    print(f"Wrote {path}  ({G.number_of_nodes()} nodes, {G.number_of_edges()} edges)")


if __name__ == "__main__":
    main()
