# BEN_RECORD_STATUS_HX

> This table contains historical information about the change in benefit statuses.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the benefits record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EDIT_DTTM` | DATETIME (Local) |  | Stores the instant that the record status was changed. |
| 4 | `EDIT_USER_ID` | VARCHAR |  | Stores the user who changed the record status. |
| 5 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `EDIT_ACTION_C_NAME` | VARCHAR |  | Stores the action that was applied to the record status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

