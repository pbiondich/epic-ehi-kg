# CLP_OCCUR_SPAN

> This table extracts the occurrence span codes and the from and through dates to print on an institutional claim.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The ID of the claim print record. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `OCCURRENCE_SPAN_C_NAME` | VARCHAR | org | Occurrence Span Code to print on institutional claims |
| 4 | `OCCUR_SPAN_FROM_DT` | DATETIME |  | Occurrence Span Code From Date to print on institutional claims |
| 5 | `OCCUR_SPAN_TO_DT` | DATETIME |  | Occurrence Span Code From Date to print on institutional claims |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

