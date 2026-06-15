# Epic EHI Schema Knowledge Graph

A machine-readable knowledge graph of **Epic's EHI Export Specification** — the
public, ONC-Cures-Act-mandated documentation of Epic's Clarity-derived export
tables (published at `https://open.epic.com/EHITables`).

This repo turns ~7,800 HTML documentation pages into:

- a flat **structured dataset** (`data/schema.jsonl`),
- an **RDF / Turtle** knowledge graph (`graph/epic_ehi.ttl`) for SPARQL and for
  linking Epic columns to external vocabularies (OMOP, FHIR, LOINC, SNOMED,
  OpenMRS/CIEL), and
- a **GraphML** property graph (`graph/epic_ehi.graphml`) for Neo4j, Gephi, or
  Cytoscape exploration.

## Source & version

| | |
|---|---|
| Source | open.epic EHI Export Specification |
| Released version | **May 2026** |
| DocGen build | `su118s2p`, generated 2026-06-14 |
| Tables | 7,797 |
| Columns | 63,956 |

See `data/meta.json` for full provenance and `data/stats.json` for computed
statistics.

## Graph model

```
(:Table)-[ehi:hasColumn / ehi:hasPrimaryKeyColumn]->(:Column)
(:Column)-[ehi:inTable]->(:Table)
(:Column)-[ehi:references]->(:Table)        # foreign-key-like; inferred (see below)
(:Table)-[ehi:overflowOf]->(:Table)         # BASE_2/BASE_3/... -> logical base
```

Column nodes carry: `ordinal`, `dataType`, `discontinued`, `isPrimaryKey`,
`mayContainOrgSpecificValues`, and (optionally) a description. The
`mayContainOrgSpecificValues` flag is the most analytically useful property: it
marks exactly the columns whose *values* are configured per Epic site and are
therefore **not comparable across installations** without local mapping — the
same standard-container / local-semantics boundary that makes cross-site Epic
research hard, surfaced as a machine-readable flag.

Every table also carries `ehi:logicalTable` (its overflow-family base), every
inferred reference carries `ehi:referenceMethod` + `ehi:referenceConfidence`, and
columns whose key is a generic shared identifier are flagged `ehi:sharedKey`.

## Reference resolution (join graph)

Epic's EHI pages contain **no explicit foreign-key section**, so reference edges
must be inferred. A naive "column name == some table's sole-column PK" rule fails
two ways, both now handled:

1. **Overflow families.** A logical entity is split across `BASE`, `BASE_2`,
   `BASE_3`, … sharing one key (`PATIENT`/`PATIENT_2…6`, `PAT_ENC`/`PAT_ENC_2…8`).
   These are collapsed into one logical entity via `ehi:overflowOf` /
   `ehi:logicalTable` (92 families, 163 member tables), and intra-family / self
   edges are suppressed.
2. **Generic shared keys.** Identifiers like `RESULT_ID`, `RECORD_ID`,
   `ORDER_ID`, `TX_ID` are the sole PK of dozens of co-equal tables — there is no
   single master. These are **left unresolved** (recorded in
   `data/shared_keys.json`, flagged `ehi:sharedKey`) rather than guessed.

For every other identifier the builder picks one canonical **master** table and
tags the edge with a method and confidence:

| method | confidence | rule |
|---|---|---|
| `sole_pk` | high | the key has exactly one logical sole-PK owner |
| `name_stem` | high | an owner's name equals the key's stem (`PAT_ENC_CSN_ID` → `PAT_ENC`) |
| `overflow_master` | medium | exactly one *name-related* owner itself carries overflow tables (`PAT_ID` → `PATIENT`) |
| `alias_enc_csn` | low | renamed encounter contact-serial-number, e.g. `ALLERGY_PAT_CSN`, `*_ENC_CSN`, `*_ENC_CSN_ID`, `*_PAT_CSN` → `PAT_ENC` |
| `alias_pat_id` | low | renamed patient key, `<role>_PAT_ID` → `PATIENT` |

The last two recover **aliased foreign keys** — columns that point at the master
but were renamed, which exact matching misses. They are deliberately narrow: a
bare `*_CSN` is *not* used (CSNs also belong to non-encounter contacts such as
notes, rooms, beds and care plans), and `*PATIENT_ID` is excluded (those are
external MPI identifiers, not `PAT_ID` foreign keys).

This yields **4,072 reference edges** (vs. 1,076 in the original conservative
build), and the marquee hubs now surface correctly — top targets are `PAT_ENC`
(691), `PATIENT` (659), `CLAIM_INFO` (467), `REFERRAL`, `COVERAGE`,
`HSP_ACCOUNT`. Edges are written to `data/references.jsonl` for direct querying.

The pass is deliberately **conservative — it under-claims rather than emit wrong
edges.** Use `--no-resolve-references` to fall back to the original single-PK
inference.

## Querying the graph

`query_kg.py` is a small query layer over the resolved graph — a structure /
join-planning interface (it answers "where does X live" and "how do I join A to
B", **not** patient-data questions; the graph holds the schema, not the rows).

```bash
python query_kg.py search weight bmi            # columns matching keywords (name + description)
python query_kg.py table PAT_ENC                # profile: PK, org-specific cols, joins in/out
python query_kg.py refs-to PATIENT              # every column that joins to PATIENT
python query_kg.py refs-from IP_FLWSHT_MEAS     # what this table joins to
python query_kg.py path IP_FLWSHT_MEAS PATIENT  # shortest join path between two tables
```

Example — the join path from a flowsheet measurement to the patient:

```
IP_FLWSHT_MEAS  --FSD_ID-->  IP_FLWSHT_REC  --PAT_ID-->  PATIENT
```

This is the query-planning layer for downstream natural-language tooling: resolve
a question to tables/columns and a join path first, then (later) execute against a
Clarity/Caboodle SQL instance or a loaded EHI export.

## Data dictionary (markdown)

A browsable markdown rendering lives in [`docs/`](docs/index.md) — a per-table
page (columns, types, flags, primary key, joins in/out, overflow family) plus an
A–Z index, all cross-linked and rendered natively on GitHub. Regenerate it from
the `data/` files with:

```bash
python build_docs.py --out .
```

## Rebuild

```bash
pip install -r requirements.txt
python build_kg.py --src /path/to/Epic_EHI_Tables.zip --out .

# re-resolve / iterate without re-parsing the HTML zip:
python build_kg.py --from-schema data/schema.jsonl --out .
```

Re-run against a newer EHI export to get a diffable schema history across Epic
versions.

## On the documentation text (read before publishing publicly)

Epic publishes this specification to meet information-blocking / EHI-export
requirements. The **structure** captured here — table names, column names, data
types, keys, and the organization-specific flags — is factual schema metadata.
The per-column **descriptions** are Epic's own text.

`schema.jsonl` retains the full records (it is your own local extract). If you
intend to publish the *graph* publicly and want to be conservative about
redistributing the descriptive prose, rebuild with:

```bash
python build_kg.py --src ... --out . --no-descriptions
```

which omits descriptions from `epic_ehi.ttl` and `epic_ehi.graphml` while keeping
all structural facts and the org-specific flags.

## Known limitations

- **Reference edges remain inferred, not authoritative.** Epic ships no explicit
  foreign keys, so all `ehi:references` edges are derived (see *Reference
  resolution* above) and should be read together with their
  `ehi:referenceConfidence`. `overflow_master` (medium) and the `alias_*` rules
  (low) are heuristic; the alias rules currently cover only the two anchor
  entities (encounter, patient), so renamed FKs to *other* masters are not yet
  resolved. Generic shared keys are intentionally left unresolved.
- **Composite-key targets** (a column set referencing a multi-column PK) are not
  emitted as edges. The common, useful case — a detail table whose *leading* key
  column points at a master entity — is captured, because that leading column
  resolves to the master like any other identifier.
- Descriptions are normalized to single-line whitespace.
- Released-only schema: no site customizations, and no Chronicles INI/item
  lineage (those live only in the gated Clarity Data Handbook).
