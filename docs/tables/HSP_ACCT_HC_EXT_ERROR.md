# HSP_ACCT_HC_EXT_ERROR

> This table contains error information returned by an external system for hospital coding workflows.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the hospital account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXT_ERROR_CODE` | VARCHAR |  | The error code returned by an external system. |
| 4 | `EXT_ERROR_TYPE_C_NAME` | VARCHAR |  | The type of error returned by an external system. |
| 5 | `EXT_ERR_WORKFLOW_C_NAME` | VARCHAR |  | The hospital coding workflow associated with the external error code. |
| 6 | `EXT_ERROR_TEXT` | VARCHAR |  | The user-facing message supplied with the external error code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

