# CASE_HISTORY

> The CASE_HISTORY table contains the case history information associated with each case record stored in the CASE_MGMT table. It contains details of all changes that have ever been made to the case record. It stores such information as the action performed, the time and date the action was performed, and the user that performed the action.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | NUMERIC | PK shared | The internal ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The line number of the case history. For example, if the case has two history events, the first will have a line value of 1, while the second will have a line value of 2. |
| 3 | `ACTION_DATETIME` | DATETIME (Local) |  | The date and time associated with the case history action entry. |
| 4 | `ACTION_C_NAME` | VARCHAR |  | The category number of the action associated with this history entry. |
| 5 | `PREV_VALUE` | VARCHAR |  | The "Note or Previous Value" information from the case history action. |
| 6 | `ACTION_USER_ID` | VARCHAR |  | The internal ID of the user who performed the action associated with this line of the change history. |
| 7 | `ACTION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `HISTORY_REV_DUE_DATE` | DATETIME |  | Tracks the current review due date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

