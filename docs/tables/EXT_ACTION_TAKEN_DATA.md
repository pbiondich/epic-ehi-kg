# EXT_ACTION_TAKEN_DATA

> Clarity table for action taken data on external data.

**Primary key:** `EXTERNAL_CVG_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EXTERNAL_CVG_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the external coverage record record. |
| 2 | `EXT_ACTION_TAKEN_C_NAME` | VARCHAR |  | This is the action that was taken on this External Data record. |
| 3 | `EXT_ACTION_USER_ID` | VARCHAR |  | This is the user that took an action on this External Data record. |
| 4 | `EXT_ACTION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `EXT_ACTION_INST_UTC_DTTM` | DATETIME (UTC) |  | This is the UTC instant an action was taken on this External Data record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

