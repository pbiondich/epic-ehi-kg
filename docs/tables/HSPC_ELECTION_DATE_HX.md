# HSPC_ELECTION_DATE_HX

> This table contains the history of the hospice election date.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ELECTION_DATE` | DATETIME |  | History of the Hospice Election Date |
| 4 | `EDIT_UTC_DTTM` | DATETIME (UTC) |  | Instant that the election date was changed |
| 5 | `EDIT_USER_ID` | VARCHAR |  | User that changed the hospice election date. |
| 6 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `ELECTION_DATE_RTE_SRC_C_NAME` | VARCHAR |  | This item stores whether the hospice election date was entered manually or pulled from RTE. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

