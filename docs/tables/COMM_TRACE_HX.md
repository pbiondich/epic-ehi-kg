# COMM_TRACE_HX

> The history of a communication trace.

**Primary key:** `COMM_TRACE_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_TRACE_ID` | NUMERIC | PK | The unique identifier (.1 item) for the outreach record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `COMM_ACTION_UTC_DTTM` | DATETIME (UTC) |  | Table of audit events logged against a trace. This item stores the UTC of the event. |
| 5 | `COMM_ACTION_C_NAME` | VARCHAR |  | Table of audit events logged against a trace. This item stores the action taken on this trace. This can be from the system, or user intervention. |
| 6 | `COMM_ACTION_STATUS_C_NAME` | VARCHAR |  | Table of audit events logged against a trace. This item stores status of the trace at the time the audit happened. NOT the status that resulted. |
| 7 | `COMM_ACTION_COMMENT` | VARCHAR |  | Table of audit events logged against a trace. This item stores comments about the event. Initial use case was to store the true status string from cloud since it may change with vendors / cloud changes where cache may not have a chance to update in time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

