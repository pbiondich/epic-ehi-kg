#!/usr/bin/env python3
"""
query_kg.py -- a small natural-language-ish query layer over the Epic EHI
schema knowledge graph. Answers STRUCTURE questions ("where does X live",
"how do I join A to B", "what references PATIENT", "what's org-specific"),
not patient-data questions.

    python query_kg.py search weight bmi          # columns matching keywords
    python query_kg.py table PAT_ENC              # profile a table
    python query_kg.py refs-to PATIENT            # what joins to PATIENT
    python query_kg.py refs-from ABN_DOCUMENT_ID  # what this table joins to
    python query_kg.py path IP_FLWSHT_MEAS PATIENT  # join path A <-> B
"""
import json, sys, re
from collections import defaultdict, deque
from pathlib import Path

DATA = Path(__file__).parent / "data"


def load():
    recs = [json.loads(l) for l in (DATA / "schema.jsonl").open(encoding="utf-8")]
    refs = [json.loads(l) for l in (DATA / "references.jsonl").open(encoding="utf-8")]
    logical = json.loads((DATA / "logical_tables.json").read_text())
    member_to_base = {m: b for b, ms in logical.items() for m in ms}
    by_name = {r["table"]: r for r in recs}
    return recs, refs, by_name, member_to_base


def base_of(t, m2b):
    return m2b.get(t, t)


def search_columns(recs, *keywords, limit=25):
    """Columns whose name OR description matches all keywords (case-insensitive)."""
    kws = [k.lower() for k in keywords]
    hits = []
    for r in recs:
        for c in r["columns"]:
            hay = (c["name"] + " " + (c.get("description") or "")).lower()
            if all(k in hay for k in kws):
                hits.append((r["table"], c["name"], c["type"],
                             bool(c.get("org_specific")), c.get("description") or ""))
    return hits[:limit], len(hits)


def profile_table(by_name, refs, m2b, table):
    r = by_name.get(table)
    if not r:
        return None
    pk = [p["column"] for p in sorted(r["primary_key"], key=lambda x: x["ordinal"] or 0)]
    org = [c["name"] for c in r["columns"] if c.get("org_specific")]
    out_edges = [(e["column"], e["references"], e["confidence"])
                 for e in refs if e["table"] == table]
    in_edges = [(e["table"], e["column"], e["confidence"])
                for e in refs if e["references"] == base_of(table, m2b)]
    return {"description": r.get("description"), "n_columns": len(r["columns"]),
            "primary_key": pk, "org_specific_columns": org,
            "joins_out": out_edges, "joins_in": in_edges}


def join_path(refs, by_name, m2b, a, b):
    """Shortest path between two tables over reference edges (treated undirected
    at the logical-table level). Returns a list of (table, via_column, table)."""
    a, b = base_of(a, m2b), base_of(b, m2b)
    adj = defaultdict(list)                      # node -> [(neighbor, column, direction)]
    for e in refs:
        s, t, col = base_of(e["table"], m2b), e["references"], e["column"]
        adj[s].append((t, col, "->"))
        adj[t].append((s, col, "<-"))
    seen = {a}
    q = deque([(a, [])])
    while q:
        node, path = q.popleft()
        if node == b:
            return path
        for nbr, col, d in adj[node]:
            if nbr not in seen:
                seen.add(nbr)
                q.append((nbr, path + [(node, col, d, nbr)]))
    return None


def _print_search(hits, total, kws):
    print(f'columns matching {kws}: {total} (showing {len(hits)})\n')
    for tbl, col, typ, org, desc in hits:
        flag = "  [ORG-SPECIFIC]" if org else ""
        print(f"  {tbl}.{col}  ({typ}){flag}")
        if desc:
            print(f"      {desc[:140]}")


def main(argv):
    recs, refs, by_name, m2b = load()
    if not argv:
        print(__doc__); return
    cmd, rest = argv[0], argv[1:]
    if cmd == "search":
        hits, total = search_columns(recs, *rest)
        _print_search(hits, total, rest)
    elif cmd == "table":
        p = profile_table(by_name, refs, m2b, rest[0])
        if not p:
            print(f"no such table: {rest[0]}"); return
        print(f"{rest[0]} -- {p['description']}")
        print(f"  columns: {p['n_columns']}   PK: {p['primary_key']}")
        print(f"  org-specific columns ({len(p['org_specific_columns'])}): "
              f"{p['org_specific_columns'][:12]}")
        print(f"  joins OUT ({len(p['joins_out'])}): {p['joins_out'][:10]}")
        print(f"  joins IN ({len(p['joins_in'])}): {p['joins_in'][:10]}")
    elif cmd == "refs-to":
        ins = [(e["table"], e["column"], e["confidence"]) for e in refs
               if e["references"] == base_of(rest[0], m2b)]
        print(f"{len(ins)} columns join to {rest[0]}:")
        for t, c, conf in ins[:40]:
            print(f"  {t}.{c}  [{conf}]")
    elif cmd == "refs-from":
        outs = [(e["column"], e["references"], e["confidence"]) for e in refs
                if e["table"] == rest[0]]
        print(f"{rest[0]} joins out via {len(outs)} columns:")
        for c, tgt, conf in outs:
            print(f"  .{c} -> {tgt}  [{conf}]")
    elif cmd == "path":
        path = join_path(refs, by_name, m2b, rest[0], rest[1])
        if path is None:
            print(f"no reference path found between {rest[0]} and {rest[1]}")
        else:
            print(f"join path {rest[0]} <-> {rest[1]} ({len(path)} hop(s)):")
            for node, col, d, nbr in path:
                arrow = f"--{col}-->" if d == "->" else f"<--{col}--"
                print(f"  {node}  {arrow}  {nbr}")
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
