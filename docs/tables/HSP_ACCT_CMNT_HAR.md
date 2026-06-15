# HSP_ACCT_CMNT_HAR

> This table contains the Claim Remark field from the Hospital Account Receivable (HAR) master file.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital account. |
| 2 | `LINE` | INTEGER | PK | This column stores the line number in the results of a query. Because multiple value codes can be stored in one hospital account, each code will have a unique line number. |
| 3 | `REMARK_CMS1500` | VARCHAR |  | Claim Remark: User-entered notes associated with claims attached to a hospital account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

