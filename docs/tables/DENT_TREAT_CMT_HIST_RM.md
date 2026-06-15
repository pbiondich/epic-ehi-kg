# DENT_TREAT_CMT_HIST_RM

> This table extracts the dental treatment historical comments.

**Primary key:** `TREATMENT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_ID` | NUMERIC | PK FK→ | The unique identifier for the treatment plan record |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the historical instant in the treatment record. Together with TREATMENT_ID, this forms the foreign key to the DENTAL_TPL_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number for one of the multiple treatment comments associated with the treatment and the historical instant from the DENTAL_TPL_HX table |
| 4 | `TREATMENT_CMT_HIST` | VARCHAR |  | stores revision history of comment for a treatment |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `TREATMENT_ID` | [DENT_TREATMENT](DENT_TREATMENT.md) | sole_pk | high |

