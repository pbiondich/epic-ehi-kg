# DENT_TREAT_FIND_HIST_RM

> This table extracts the dental treatment historical findings.

**Primary key:** `TREATMENT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_ID` | NUMERIC | PK FK→ | The unique identifier for the treatment plan record |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the historical instant in the treatment record. Together with TREATMENT_ID, this forms the foreign key to the DENTAL_TPL_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number for one of the multiple findings associated with the treatment and the historical instant from the DENTAL_TPL_HX table |
| 4 | `TR_FINDINGS_HX_ID` | NUMERIC |  | stores revision history of findings within a treatment |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `TREATMENT_ID` | [DENT_TREATMENT](DENT_TREATMENT.md) | sole_pk | high |

