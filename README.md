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
(:Table)-[:hasColumn / ehi:hasPrimaryKeyColumn]->(:Column)
(:Column)-[ehi:inTable]->(:Table)
(:Column)-[ehi:references]->(:Table)        # foreign-key-like; mostly inferred
```

Column nodes carry: `ordinal`, `dataType`, `discontinued`, `isPrimaryKey`,
`mayContainOrgSpecificValues`, and (optionally) a description. The
`mayContainOrgSpecificValues` flag is the most analytically useful property: it
marks exactly the columns whose *values* are configured per Epic site and are
therefore **not comparable across installations** without local mapping — the
same standard-container / local-semantics boundary that makes cross-site Epic
research hard, surfaced as a machine-readable flag.

## Rebuild

```bash
pip install -r requirements.txt
python build_kg.py --src /path/to/Epic_EHI_Tables.zip --out .
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

- **Reference edges are conservative.** Epic's EHI pages rarely include an
  explicit foreign-key section (0 in this build), so `ehi:references` edges are
  *inferred* by matching a column name to another table's **single-column**
  primary key. Two consequences: (1) references into **composite-key** tables
  (the majority — 6,740 of 7,797 tables have multi-column keys) are not captured,
  and (2) where Epic uses overflow tables that share one key (`PATIENT`,
  `PATIENT_2`, `PATIENT_3`, …), the key is ambiguous and is intentionally
  dropped, which suppresses marquee hubs like `PATIENT`. A better reference model
  would collapse `_2`/`_3` overflow families into one logical entity and resolve
  composite keys — a natural next step.
- Descriptions are normalized to single-line whitespace.
```
```
