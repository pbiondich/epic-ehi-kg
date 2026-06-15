# HSP_CLP_DIAGNOSIS

> This table contains diagnosis related information for claim print records associated with the hospital account/liability bucket.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 3 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `DX_POA_C_NAME` | VARCHAR | org | Diagnosis present on admission indicator. Will only print on institutional claim forms. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

