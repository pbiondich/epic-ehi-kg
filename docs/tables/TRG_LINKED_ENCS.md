# TRG_LINKED_ENCS

> The linked encounters for a treatment day.

**Primary key:** `REGIMEN_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGIMEN_ID` | NUMERIC | PK shared | The ID of the treatment day in this row. |
| 2 | `LINE` | INTEGER | PK | A line number that uniquely identifies each linked encounter entry. |
| 3 | `TX_VISIT_TYPE_ID_PRC_NAME` | VARCHAR |  | The name of the visit type. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The contact serial number (CSN) of a patient encounter linked to the treatment day in this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

