# HSP_ACCT_COD_ERROR_HX

> This table contains the coding-related error history for external system errors.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the hospital account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COD_ERROR_TYPE_C_NAME` | VARCHAR |  | Lists the type of error for each error that occurred for the hospital account. |
| 4 | `ERROR_START_UTC_DTTM` | DATETIME (UTC) |  | Lists the UTC instant for when each error first appeared for the hospital account. |
| 5 | `ERROR_END_UTC_DTTM` | DATETIME (UTC) |  | Lists the UTC instant for when each error was resolved for the hospital account. |
| 6 | `EXT_ERROR_CODE` | VARCHAR |  | Lists the external error code for each external error that occurred for the hospital account. |
| 7 | `ERROR_IS_ACTIVE_YN` | VARCHAR |  | Lists whether or not each error is currently applicable for the hospital account. If the error is not active then there will also be an end time for the error. |
| 8 | `ERROR_MESSAGE` | VARCHAR |  | Lists the error message for each error that occurred for the hospital account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

