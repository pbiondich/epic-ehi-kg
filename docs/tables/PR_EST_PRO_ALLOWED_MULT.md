# PR_EST_PRO_ALLOWED_MULT

> Allowed amount for all applicable coverages for the professional charge in the price estimate. This table has data for dental estimates using multiple coverages only. Refer to the ALLOWED_AMT column in PR_EST_PROFEE_PROC for all other cases.

**Primary key:** `ESTIMATE_ID`, `PROC_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the patient estimate record. |
| 2 | `PROC_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `ALLOWED_AMT` | NUMERIC |  | The expected allowed amount specified for this procedure and corresponding coverage (I PES 168). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

