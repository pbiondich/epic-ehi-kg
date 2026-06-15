# HSP_ACCT_ORG_DON

> This table holds the abstracted organ(s) donated by the patient associated with the hospital account.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital account with the abstracted donated organ information. |
| 2 | `LINE` | INTEGER | PK | This column stores the line number in the results of a query. Because multiple organs can be donated by a patient and stored on one hospital account, each abstracted donated organ will have a unique line number. |
| 3 | `ORG_TO_DONATE_C_NAME` | VARCHAR | org | This abstracting item indicates the organ(s) donated by the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

