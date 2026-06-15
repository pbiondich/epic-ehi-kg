# HSP_ACCT_VALU_HAR

> This table contains hospital account value codes information from the Hospital Account Receivable (HAR) master file.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital account. |
| 2 | `LINE` | INTEGER | PK | This column stores the line number in the results of a query. Because multiple value codes can be stored in one hospital account, each value code will have a unique line number. |
| 3 | `VALUE_CODE_C_NAME` | VARCHAR | org | A value code stored in the hospital account. |
| 4 | `VALUE_AMOUNT` | VARCHAR |  | The monetary amount associated with a value code stored in the hospital account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

