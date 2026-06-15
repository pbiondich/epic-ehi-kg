# HH_INTVTN_DISC

> Contains Home Health care plan intervention discipline information.

**Primary key:** `INTERVENTION_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INTERVENTION_ID` | VARCHAR | PK FK→ | Unique identifier for the care plan intervention. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INTERV_DISC_ID` | VARCHAR |  | Care plan intervention discipline ID. Links to table DISCIPLINE. |
| 4 | `INTERV_DISC_ID_DISC_NAME` | VARCHAR |  | The name of the discipline record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |

