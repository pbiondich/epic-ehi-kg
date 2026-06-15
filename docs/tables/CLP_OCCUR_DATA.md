# CLP_OCCUR_DATA

> This table extracts the occurrence codes and occurrence dates for each claim.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The ID of the claim print record. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `OCCURRENCE_CODE_C_NAME` | VARCHAR | org | The occurrence code category list for an institutional claim. |
| 4 | `OCCURRENCE_DT` | DATETIME |  | Stores Occurrence Date to print on institutional claims |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

