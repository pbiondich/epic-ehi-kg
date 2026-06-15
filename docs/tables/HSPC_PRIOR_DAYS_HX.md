# HSPC_PRIOR_DAYS_HX

> This table contains the history of the hospice prior days on service.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PRIOR_DAYS` | INTEGER |  | History of the Prior Days on Service |
| 4 | `EDIT_UTC_DTTM` | DATETIME (UTC) |  | Instant that the prior days on service item was changed |
| 5 | `EDIT_USER_ID` | VARCHAR |  | User that changed the prior days on service. |
| 6 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `PRIOR_DAYS_RTE_SRC_C_NAME` | VARCHAR |  | This item stores whether the prior days on service was entered manually or pulled from RTE. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

