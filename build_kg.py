#!/usr/bin/env python3
"""
build_kg.py
===========
Parse Epic's EHI Export documentation (the open.epic "DocGen" HTML set) into a
structured schema dataset and a knowledge graph.

INPUT   a .zip (or directory) of EHI table .htm files, OR (--from-schema) an
        existing data/schema.jsonl to re-resolve without re-parsing the HTML.
OUTPUT  data/schema.jsonl       one JSON record per table (full, incl. descriptions)
        data/meta.json          provenance: source, version, counts
        data/stats.json         computed statistics
        data/references.jsonl   resolved reference edges (table,column,references,method,confidence)
        data/logical_tables.json overflow families: base -> [BASE_2, BASE_3, ...]
        data/shared_keys.json   generic keys deliberately left unresolved (+ candidate owners)
        graph/epic_ehi.ttl      RDF / Turtle knowledge graph
        graph/epic_ehi.graphml  property graph (Neo4j / Gephi / Cytoscape)

REFERENCE RESOLUTION (on by default; --no-resolve-references for the old behavior)
----------------------------------------------------------------------------------
Epic's pages have no explicit FK section. This builder collapses BASE/BASE_2/...
overflow families into one logical entity (ehi:overflowOf / ehi:logicalTable) and
resolves each identifier column to a single canonical master table where one is
defensible, tagging every edge with ehi:referenceMethod + ehi:referenceConfidence.
Generic shared keys (RESULT_ID, RECORD_ID, ...) are left unresolved (ehi:sharedKey)
rather than guessed. See resolve_references() and README.

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
    python build_kg.py --from-schema data/schema.jsonl --out .   # re-resolve, no zip
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
# Reference resolution
# --------------------------------------------------------------------------- #
# Epic's EHI pages carry no explicit foreign-key section, and a naive
# "column name == some table's sole-column PK" rule mis-fires for two reasons:
#   1. Overflow families. A logical entity is split across BASE, BASE_2, BASE_3,
#      ... that share one key (PATIENT/PATIENT_2.., PAT_ENC/PAT_ENC_2..). Each
#      member claims the same sole PK, so the key looks "ambiguous" and the
#      marquee hub (PATIENT, PAT_ENC) gets dropped entirely.
#   2. Generic shared keys. Identifiers like RESULT_ID, RECORD_ID, ORDER_ID and
#      TX_ID are the sole PK of dozens of co-equal tables; there is no single
#      master to point at.
# This pass collapses (1) into one logical entity per family and, for (2),
# under-claims: it emits an edge only when a single master is defensible, and
# records the rest in shared_keys rather than guessing.
OVERFLOW_RE = re.compile(r"^(.*)_(\d+)$")
ID_SUFFIXES = ("_CSN_ID", "_ID")


def _pk_columns(rec):
    return [p["column"] for p in sorted(rec["primary_key"],
                                        key=lambda x: x["ordinal"] or 0)]


def _stems(key):
    """Identifier name stems, e.g. PAT_ENC_CSN_ID -> {PAT_ENC, PAT_ENC_CSN}."""
    return {key[:-len(s)] for s in ID_SUFFIXES if key.endswith(s)}


def _related(stem, table):
    return table == stem or table.startswith(stem) or stem.startswith(table)


def overflow_families(table_names):
    """base_table -> [overflow members BASE_2, BASE_3, ...] (base must exist)."""
    fam = defaultdict(list)
    for n in table_names:
        m = OVERFLOW_RE.match(n)
        if m and m.group(1) in table_names:
            fam[m.group(1)].append(n)
    return {b: sorted(ms, key=lambda x: int(OVERFLOW_RE.match(x).group(2)))
            for b, ms in fam.items()}


def logical_base(name, table_names):
    m = OVERFLOW_RE.match(name)
    return m.group(1) if (m and m.group(1) in table_names) else name


def resolve_references(records):
    """Resolve column references to a canonical 'master' table per identifier.

    For each column that is a *sole* primary key somewhere, choose the master
    (after collapsing overflow families to one logical owner):
        * exactly one logical owner            -> high   (sole_pk)
        * the owner whose name == the key stem  -> high   (name_stem)
        * exactly one name-related owner that
          itself carries overflow tables        -> medium (overflow_master)
        * otherwise                             -> shared/generic key, no edge
    A column C in table T references master(K) when C.name == K and the master's
    logical family differs from T's (no intra-family / self edges).

    Returns (edges, shared_keys, families, logical_of) where
        edges       = [(table, column, target, method, confidence), ...]
        shared_keys = {key: [logical owner tables]}  (deliberately unresolved)
    """
    table_names = {r["table"] for r in records}
    families = overflow_families(table_names)
    has_overflow = set(families)
    logical_of = {n: logical_base(n, table_names) for n in table_names}

    sole = defaultdict(set)                       # key -> {logical owner tables}
    for r in records:
        if len(r["primary_key"]) == 1:
            sole[_pk_columns(r)[0]].add(logical_of[r["table"]])

    master, method, confidence, shared_keys = {}, {}, {}, {}
    for key, owners in sole.items():
        owners = set(owners)
        if len(owners) == 1:
            master[key] = next(iter(owners))
            method[key], confidence[key] = "sole_pk", "high"
            continue
        stem_hit = [o for o in owners if o in _stems(key)]
        if len(stem_hit) == 1:
            master[key] = stem_hit[0]
            method[key], confidence[key] = "name_stem", "high"
            continue
        ov = [o for o in owners
              if o in has_overflow and any(_related(s, o) for s in _stems(key))]
        if len(ov) == 1:
            master[key] = ov[0]
            method[key], confidence[key] = "overflow_master", "medium"
            continue
        shared_keys[key] = sorted(owners)          # under-claim, do not guess

    edges = []
    for r in records:
        tbase = logical_of[r["table"]]
        for c in r["columns"]:
            tgt = master.get(c["name"])
            if tgt and tgt != tbase:
                edges.append((r["table"], c["name"], tgt,
                              method[c["name"]], confidence[c["name"]]))
    return edges, shared_keys, families, logical_of


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description="Build Epic EHI schema dataset + KG.")
    ap.add_argument("--src", type=Path, help=".zip or directory of EHI .htm pages")
    ap.add_argument("--from-schema", type=Path,
                    help="rebuild graphs/stats from an existing data/schema.jsonl "
                         "(skips HTML parsing; lets you re-resolve without the zip)")
    ap.add_argument("--out", default=Path("."), type=Path, help="output repo root")
    ap.add_argument("--no-descriptions", action="store_true",
                    help="omit Epic's prose descriptions from .ttl and .graphml")
    ap.add_argument("--no-resolve-references", action="store_true",
                    help="skip the reference-resolution pass; emit only the legacy "
                         "conservative single-column-PK edges")
    args = ap.parse_args()
    if not args.src and not args.from_schema:
        ap.error("provide --src (zip/dir of .htm) or --from-schema (existing schema.jsonl)")

    global PARSER
    try:
        BeautifulSoup("<x/>", PARSER)
    except Exception:
        PARSER = "html.parser"

    data_dir = args.out / "data"
    graph_dir = args.out / "graph"
    data_dir.mkdir(parents=True, exist_ok=True)
    graph_dir.mkdir(parents=True, exist_ok=True)

    # ---- provenance (carried over from existing meta.json when rebuilding) ----
    if args.src:
        prov = provenance(args.src)
    else:
        prov = {"source": "https://open.epic.com/EHITables (EHI Export Specification)",
                "docgen_folder": None, "docgen_token": None,
                "docgen_timestamp": None, "released_version": None}
        existing = data_dir / "meta.json"
        if existing.exists():
            old = json.loads(existing.read_text(encoding="utf-8"))
            for k in ("source", "docgen_folder", "docgen_token",
                      "docgen_timestamp", "released_version"):
                if old.get(k):
                    prov[k] = old[k]

    # ---- obtain records: parse HTML pages, or load an existing schema.jsonl ----
    if args.from_schema:
        with args.from_schema.open(encoding="utf-8") as fh:
            records = [json.loads(line) for line in fh if line.strip()]
        print(f"Loaded {len(records)} tables from {args.from_schema}.")
    else:
        records = []
        with (data_dir / "schema.jsonl").open("w", encoding="utf-8") as fh:
            for i, (name, html_text) in enumerate(iter_pages(args.src), 1):
                rec = parse_page(name, html_text)
                records.append(rec)
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
                if i % 1000 == 0:
                    print(f"  parsed {i} tables ...", flush=True)
        print(f"Parsed {len(records)} tables.")

    table_names = {r["table"] for r in records}
    pk_set = {(r["table"], pk["column"]) for r in records for pk in r["primary_key"]}

    # ---- references ----
    if args.no_resolve_references:
        # legacy conservative inference: unambiguous single-column PK ownership only
        pk_cols = defaultdict(list)
        for r in records:
            if len(r["primary_key"]) == 1:
                pk_cols[r["primary_key"][0]["column"]].append(r["table"])
        pk_owner = {c: t[0] for c, t in pk_cols.items() if len(t) == 1}
        ref_edges = [(r["table"], c["name"], pk_owner[c["name"]], "legacy_sole_pk", "low")
                     for r in records for c in r["columns"]
                     if pk_owner.get(c["name"]) and pk_owner[c["name"]] != r["table"]]
        shared_keys = {}
        families = overflow_families(table_names)
        logical_of = {n: logical_base(n, table_names) for n in table_names}
    else:
        ref_edges, shared_keys, families, logical_of = resolve_references(records)

    # ---- explicit FK rows (rare; none in the current EHI release) ----
    explicit_edges = []      # (table, column?, target)
    for r in records:
        for fkrow in r["foreign_keys"]:
            for v in (fkrow.values() if isinstance(fkrow, dict) else []):
                for tok in re.findall(r"[A-Z][A-Z0-9_]{2,}", str(v)):
                    if tok in table_names and tok != r["table"]:
                        explicit_edges.append((r["table"], None, tok))

    # ---- column-level statistics ----
    type_counter = Counter()
    n_columns = n_org = n_disc = composite_pk = 0
    for r in records:
        if len(r["primary_key"]) > 1:
            composite_pk += 1
        for c in r["columns"]:
            n_columns += 1
            type_counter[c["type"]] += 1
            n_org += bool(c["org_specific"])
            n_disc += bool(c["discontinued"])

    inbound = Counter()
    by_method = Counter()
    by_conf = Counter()
    for (_t, _c, tgt, meth, conf) in ref_edges:
        inbound[tgt] += 1
        by_method[meth] += 1
        by_conf[conf] += 1
    for (_t, _c, tgt) in explicit_edges:
        inbound[tgt] += 1

    member_tables = sum(len(v) for v in families.values())
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
        "overflow_families": len(families),
        "overflow_member_tables": member_tables,
        "logical_tables": len(records) - member_tables,
        "resolved_reference_edges": len(ref_edges),
        "explicit_reference_edges": len(explicit_edges),
        "reference_edges_by_method": dict(by_method.most_common()),
        "reference_edges_by_confidence": dict(by_conf.most_common()),
        "shared_keys_unresolved": len(shared_keys),
        "top_referenced_tables": inbound.most_common(15),
        "top_data_types": type_counter.most_common(12),
    }
    (data_dir / "stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")

    # ---- reference side-cars (diffable, queryable without the full graph) ----
    with (data_dir / "references.jsonl").open("w", encoding="utf-8") as fh:
        for (t, c, tgt, meth, conf) in ref_edges:
            fh.write(json.dumps({"table": t, "column": c, "references": tgt,
                                 "method": meth, "confidence": conf},
                                ensure_ascii=False) + "\n")
    (data_dir / "shared_keys.json").write_text(
        json.dumps(shared_keys, indent=2), encoding="utf-8")
    (data_dir / "logical_tables.json").write_text(
        json.dumps(dict(sorted(families.items())), indent=2), encoding="utf-8")

    meta = {**prov,
            "parsed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "n_tables": len(records), "n_columns": n_columns,
            "descriptions_in_graph": not args.no_descriptions,
            "references_resolved": not args.no_resolve_references}
    (data_dir / "meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

    # ---- RDF / Turtle ----
    write_turtle(graph_dir / "epic_ehi.ttl", records, pk_set, ref_edges,
                 explicit_edges, families, logical_of, shared_keys, prov,
                 not args.no_descriptions)

    # ---- GraphML ----
    write_graphml(graph_dir / "epic_ehi.graphml", records, pk_set, ref_edges,
                  explicit_edges, families, logical_of, shared_keys,
                  not args.no_descriptions)

    print("\n=== SUMMARY ===")
    print(json.dumps(stats, indent=2))


def write_turtle(path, records, pk_set, ref_edges, explicit_edges,
                 families, logical_of, shared_keys, prov, with_desc):
    edges_by_col = defaultdict(list)
    for (t, c, tgt, meth, conf) in ref_edges:
        edges_by_col[(t, c)].append((tgt, meth, conf))
    for (t, c, tgt) in explicit_edges:        # table-level (rare)
        if c:
            edges_by_col[(t, c)].append((tgt, "explicit_fk", "high"))
    shared = set(shared_keys)

    with path.open("w", encoding="utf-8") as f:
        f.write(f"""@prefix ehi:  <{EHI}> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix dct:  <http://purl.org/dc/terms/> .

<{BASE}/dataset> a ehi:Dataset ;
    dct:source <https://open.epic.com/EHITables> ;
    dct:hasVersion {ttl_str((prov.get('docgen_token') or '') + ' / released ' + (prov.get('released_version') or 'unknown'))} ;
    rdfs:comment "Knowledge graph derived from Epic's EHI Export Specification (open.epic DocGen export). Structure is factual schema metadata; descriptions are Epic's text. Reference edges and overflow-family grouping are INFERRED -- inspect ehi:referenceMethod / ehi:referenceConfidence." .

ehi:Table a rdfs:Class . ehi:Column a rdfs:Class .
ehi:inTable a rdfs:Property . ehi:hasColumn a rdfs:Property .
ehi:references a rdfs:Property . ehi:dataType a rdfs:Property .
ehi:overflowOf a rdfs:Property . ehi:logicalTable a rdfs:Property .
ehi:referenceMethod a rdfs:Property . ehi:referenceConfidence a rdfs:Property .
ehi:sharedKey a rdfs:Property .

""")
        for r in records:
            t = r["table"]
            base = logical_of.get(t, t)
            f.write(f"{t_iri(t)} a ehi:Table ; rdfs:label {ttl_str(t)}")
            f.write(f" ;\n    ehi:logicalTable {ttl_str(base)}")
            if base != t:
                f.write(f" ;\n    ehi:overflowOf {t_iri(base)}")
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
                if c["name"] in shared:
                    f.write(" ;\n    ehi:sharedKey true")
                for tgt, meth, conf in edges_by_col.get((t, c["name"]), []):
                    f.write(f" ;\n    ehi:references {t_iri(tgt)} ;\n"
                            f"    ehi:referenceMethod {ttl_str(meth)} ;\n"
                            f"    ehi:referenceConfidence {ttl_str(conf)}")
                if with_desc and c["description"]:
                    f.write(f" ;\n    rdfs:comment {ttl_str(c['description'])}")
                f.write(" .\n")
        f.write("\n")
    print(f"Wrote {path}")


def write_graphml(path, records, pk_set, ref_edges, explicit_edges,
                  families, logical_of, shared_keys, with_desc):
    import networkx as nx
    G = nx.DiGraph()
    shared = set(shared_keys)
    for r in records:
        t = r["table"]
        tid = "T:" + t
        base = logical_of.get(t, t)
        G.add_node(tid, kind="table", label=t, logical_table=base,
                   is_overflow=(base != t),
                   description=(r["description"] or "") if with_desc else "")
        for c in r["columns"]:
            cid = f"C:{t}.{c['name']}"
            G.add_node(cid, kind="column", label=c["name"], table=t,
                       data_type=c["type"] or "", ordinal=c["ordinal"] or 0,
                       discontinued=bool(c["discontinued"]),
                       org_specific=bool(c["org_specific"]),
                       is_primary_key=(t, c["name"]) in pk_set,
                       shared_key=c["name"] in shared,
                       description=(c["description"] or "") if with_desc else "")
            G.add_edge(tid, cid, rel="HAS_COLUMN", method="", confidence="")
    # overflow member -> logical base
    for base, members in families.items():
        for m in members:
            if ("T:" + m) in G and ("T:" + base) in G:
                G.add_edge("T:" + m, "T:" + base, rel="OVERFLOW_OF",
                           method="", confidence="")
    # resolved column -> master references
    for (t, c, tgt, meth, conf) in ref_edges:
        src = f"C:{t}.{c}"
        if src in G and ("T:" + tgt) in G:
            G.add_edge(src, "T:" + tgt, rel="REFERENCES",
                       method=meth, confidence=conf)
    for (t, c, tgt) in explicit_edges:
        src = f"C:{t}.{c}" if c else "T:" + t
        if src in G and ("T:" + tgt) in G:
            G.add_edge(src, "T:" + tgt, rel="REFERENCES",
                       method="explicit_fk", confidence="high")
    nx.write_graphml(G, path)
    print(f"Wrote {path}  ({G.number_of_nodes()} nodes, {G.number_of_edges()} edges)")


if __name__ == "__main__":
    main()
