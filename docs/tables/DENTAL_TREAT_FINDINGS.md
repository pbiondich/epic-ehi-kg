# DENTAL_TREAT_FINDINGS

> Table for the findings linked to a dental treatment plan.

**Primary key:** `TREATMENT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_ID` | NUMERIC | PK FK→ | The unique identifier for the treatment plan record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TR_FINDINGS_ID` | NUMERIC |  | findings associated with a treatment |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `TREATMENT_ID` | [DENT_TREATMENT](DENT_TREATMENT.md) | sole_pk | high |

