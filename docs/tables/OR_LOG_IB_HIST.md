# OR_LOG_IB_HIST

> The OR_LOG_IB_HIST table contains OR management system log In Basket history.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the log record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the In Basket history for the log. |
| 3 | `IB_HIST_ACTION_C_NAME` | VARCHAR | org | The category value which indicates the type of action the message serves to notify. |
| 4 | `IB_HIST_DATE` | DATETIME (Local) |  | The date and time the message was sent. |
| 5 | `IB_HIST_BODY_LINE` | INTEGER |  | The line number where the message body begins in the OR_LOG_IB_BODY record. |
| 6 | `IB_HIST_BODY_LEN` | INTEGER |  | The length of the message body in the OR_LOG_IB_BODY record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

