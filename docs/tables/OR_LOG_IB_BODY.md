# OR_LOG_IB_BODY

> The OR_LOG_IB_BODY table contains OR management system log In Basket messages.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the log record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the In Basket message for the log. |
| 3 | `IB_HIST_BODY` | VARCHAR |  | The body of the In Basket messages for the log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

