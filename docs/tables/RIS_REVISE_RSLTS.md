# RIS_REVISE_RSLTS

> This table provides an audit trail of dates, times, and user IDs of revisions to finalized study results through the Revise Results activity.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record associated with this procedure order. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REVISING_USER_ID` | VARCHAR |  | The user ID who revised the finalized result. |
| 4 | `REVISING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `REVISED_DATETIME` | DATETIME (Local) |  | The date and time that the finalized result was revised. If the date is null, the default value is 01/01/1900; If the time is null, the default value is 00:00. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

