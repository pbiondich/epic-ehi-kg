# HSP_ACCT_OCUR_HAR

> This table contains the Occurrence Codes and Occurrence Dates for a Hospital Accounts Receivable (HAR) record.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital account. |
| 2 | `LINE` | INTEGER | PK | This column stores the line number in the results of a query. Because multiple occurrence codes can be stored in one hospital account, each code will have a unique line number. |
| 3 | `OCCURRENCE_CODE_C_NAME` | VARCHAR | org | An occurrence code stored in the hospital account. |
| 4 | `OCCURRENCE_DATE` | DATETIME |  | The date associated with an occurrence code stored in the hospital account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

