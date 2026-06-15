# HSP_ACCT_SPAN_HAR

> This table contains account claim pan codes information from the Hospital Account Receivable (HAR) master file.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital account. |
| 2 | `LINE` | INTEGER | PK | This column stores the line number in the results of a query. Because multiple occurrence span codes can be stored in one hospital account, each code will have a unique line number. |
| 3 | `OCCURRENCE_SPAN_C_NAME` | VARCHAR | org | An occurrence span code stored in the hospital account. |
| 4 | `OCCUR_SPAN_F_DATE` | DATETIME |  | The date from which the occurrence span code stored in the hospital account applies. |
| 5 | `OCCUR_SPAN_T_DATE` | DATETIME |  | The date until which the occurrence span code stored in the hospital account applies. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

