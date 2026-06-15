# HH_INTVTN_VARIANCE

> Contains Home Health care plan intervention noadd multiple items information.

**Primary key:** `INTERVENTION_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INTERVENTION_ID` | VARCHAR | PK FK→ | Unique identifier for the care plan intervention. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VARIANCE_ID` | VARCHAR | FK→ | Care plan intervention variance ID. Links to table VARIANCE. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |
| `VARIANCE_ID` | [VARIANCE](VARIANCE.md) | sole_pk | high |

