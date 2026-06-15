#!/usr/bin/env python3
"""
build_docs.py -- render the Epic EHI schema knowledge graph as a browsable
markdown data dictionary.

    python build_docs.py --out .

Reads data/{schema.jsonl, references.jsonl, logical_tables.json,
shared_keys.json, stats.json, meta.json} and writes:

    docs/index.md            stats, top hubs, A-Z table index (links)
    docs/tables/<TABLE>.md    one page per table: description, primary key,
                              column list (type + flags + description),
                              joins OUT (references) and joins IN (referenced by),
                              and overflow-family links.

Renders natively on GitHub. Regenerate whenever data/ is rebuilt.
"""
import argparse, json, re
from pathlib import Path
from collections import defaultdict

MAX_JOINS_IN = 300       # cap inbound list on a page (with a note when exceeded)


def esc(s):
    """Make text safe for a markdown table cell."""
    return re.sub(r"\s+", " ", (s or "")).replace("|", "\\|").strip()


def load(data):
    recs = [json.loads(l) for l in (data / "schema.jsonl").open(encoding="utf-8")]
    refs = [json.loads(l) for l in (data / "references.jsonl").open(encoding="utf-8")]
    logical = json.loads((data / "logical_tables.json").read_text())   # base -> [members]
    shared = json.loads((data / "shared_keys.json").read_text())
    stats = json.loads((data / "stats.json").read_text())
    meta = json.loads((data / "meta.json").read_text())
    return recs, refs, logical, shared, stats, meta


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=Path("."), type=Path, help="repo root")
    args = ap.parse_args()
    data = args.out / "data"
    recs, refs, logical, shared, stats, meta = load(data)

    by_name = {r["table"]: r for r in recs}
    member_to_base = {m: b for b, ms in logical.items() for m in ms}
    base_of = lambda t: member_to_base.get(t, t)
    shared_set = set(shared)

    out_by_table = defaultdict(list)        # table -> [(col, target, method, conf)]
    in_by_table = defaultdict(list)         # base table -> [(src_table, col, conf)]
    for e in refs:
        out_by_table[e["table"]].append((e["column"], e["references"], e["method"], e["confidence"]))
        in_by_table[e["references"]].append((e["table"], e["column"], e["confidence"]))
    inbound_count = {t: len(v) for t, v in in_by_table.items()}

    docs = args.out / "docs"
    tdir = docs / "tables"
    tdir.mkdir(parents=True, exist_ok=True)

    # ---------- per-table pages ----------
    for r in recs:
        t = r["table"]
        base = base_of(t)
        pk = [p["column"] for p in sorted(r["primary_key"], key=lambda x: x["ordinal"] or 0)]
        pkset = set(pk)
        outs = out_by_table.get(t, [])
        out_cols = {c for c, *_ in outs}
        L = []
        L.append(f"# {t}\n")
        if r.get("description"):
            L.append(f"> {esc(r['description'])}\n")
        # header facts
        facts = []
        if base != t:
            facts.append(f"**Overflow of:** [{base}]({base}.md)")
        elif t in logical:
            members = ", ".join(f"[{m}]({m}.md)" for m in logical[t])
            facts.append(f"**Overflow family:** {members}")
        facts.append(f"**Primary key:** {', '.join(f'`{c}`' for c in pk) if pk else '_(none)_'}")
        facts.append(f"**Columns:** {len(r['columns'])}")
        norg = sum(1 for c in r["columns"] if c.get("org_specific"))
        if norg:
            facts.append(f"**Org-specific columns:** {norg}")
        inb = inbound_count.get(t, 0)
        if inb:
            facts.append(f"**Joined by:** {inb} columns")
        L.append("  \n".join(facts) + "\n")
        L.append("[← index](../index.md)\n")

        # columns
        L.append("## Columns\n")
        L.append("| # | Column | Type | Flags | Description |")
        L.append("|--:|--------|------|-------|-------------|")
        for c in r["columns"]:
            flags = []
            if c["name"] in pkset:
                flags.append("PK")
            if c.get("org_specific"):
                flags.append("org")
            if c.get("discontinued"):
                flags.append("discont.")
            if c["name"] in out_cols:
                flags.append("FK→")
            if c["name"] in shared_set:
                flags.append("shared")
            L.append(f"| {c['ordinal'] or ''} | `{c['name']}` | {esc(c['type'])} | "
                     f"{' '.join(flags)} | {esc(c.get('description'))} |")
        L.append("\n_Flags: PK = primary key · org = may contain organization-specific "
                 "values · discont. = discontinued · FK→ = inferred reference (see below) · "
                 "shared = generic key, intentionally unresolved._\n")

        # joins out
        if outs:
            L.append("## Joins out — this table references\n")
            L.append("| Column | → References | Method | Confidence |")
            L.append("|--------|--------------|--------|------------|")
            for col, tgt, meth, conf in sorted(outs):
                L.append(f"| `{col}` | [{tgt}]({tgt}.md) | {meth} | {conf} |")
            L.append("")

        # joins in (only on the logical base page)
        if base == t:
            ins = sorted(in_by_table.get(t, []))
            if ins:
                L.append(f"## Joined in — referenced by ({len(ins)})\n")
                L.append("| From | Column | Confidence |")
                L.append("|------|--------|------------|")
                for src, col, conf in ins[:MAX_JOINS_IN]:
                    L.append(f"| [{src}]({src}.md) | `{col}` | {conf} |")
                if len(ins) > MAX_JOINS_IN:
                    L.append(f"\n_… and {len(ins) - MAX_JOINS_IN} more (see "
                             f"`data/references.jsonl`)._")
                L.append("")
        elif inbound_count.get(base):
            L.append(f"## Joined in\n\nInbound joins are tracked on the logical base "
                     f"[{base}]({base}.md).\n")

        (tdir / f"{t}.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    # ---------- index ----------
    I = []
    I.append("# Epic EHI Schema — Data Dictionary\n")
    I.append(f"Generated from Epic's EHI Export Specification "
             f"(released **{meta.get('released_version','?')}**, DocGen "
             f"`{meta.get('docgen_token','?')}`). See the "
             f"[README](../README.md) for methodology and caveats.\n")
    I.append(f"- **Tables:** {stats['tables']:,}  ·  **Columns:** {stats['columns_total']:,}"
             f"  ·  **Inferred join edges:** {stats['resolved_reference_edges']:,}")
    I.append(f"- **Overflow families:** {stats['overflow_families']}  ·  "
             f"**Org-specific columns:** {stats['columns_org_specific']:,} "
             f"({stats['pct_columns_org_specific']}%)  ·  "
             f"**Generic shared keys (unresolved):** {stats['shared_keys_unresolved']}\n")

    I.append("## Top hubs (most joined-to)\n")
    for t, n in stats["top_referenced_tables"][:25]:
        d = esc(by_name[t]["description"]) if t in by_name else ""
        I.append(f"- [{t}](tables/{t}.md) — {n} inbound — {d[:90]}")
    I.append("")

    I.append("## All tables (A–Z)\n")
    by_letter = defaultdict(list)
    for t in sorted(by_name):
        by_letter[t[0].upper() if t[0].isalpha() else "#"].append(t)
    for letter in sorted(by_letter):
        links = " · ".join(f"[{t}](tables/{t}.md)" for t in by_letter[letter])
        I.append(f"### {letter}\n\n{links}\n")

    (docs / "index.md").write_text("\n".join(I) + "\n", encoding="utf-8")
    print(f"Wrote {len(recs)} table pages + index to {docs}/")


if __name__ == "__main__":
    main()
