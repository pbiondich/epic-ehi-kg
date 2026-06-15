# PEF_ADD_ED_TMSP

> This table contains information on the patient-entered flowsheet MyChart add/edit timestamp.

**Primary key:** `EPISODE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the summary/episode block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PEF_MYC_ADD_ED_TMSP` | VARCHAR |  | This column stores the timestamp of when patient-entered flowsheet data was added or edited. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

