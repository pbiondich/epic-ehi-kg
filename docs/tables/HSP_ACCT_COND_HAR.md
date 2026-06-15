# HSP_ACCT_COND_HAR

> This table contains hospital account claim condition codes from the Hospital Account Receivable (HAR) master file.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital account. |
| 2 | `LINE` | INTEGER | PK | This column stores the line number in the results of a query. Because multiple condition codes can be stored in one hospital account, each condition code will have a unique line number. |
| 3 | `CONDITION_CODE_C_NAME` | VARCHAR | org | A condition code used for claims associated with the hospital account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

