# OR_LOG_METRIC_PT_SHIFTS

> Stores details for primetime shift minutes. The values for each log in this table correspond to the values contributing to the numerator values in OpTime CSF (Cogito Summarized Facts) metrics.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the log record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORG_PRIMETIME_SHIFT_MINS` | INTEGER |  | The organization's primetime shift room utilization case in room minutes for a log. |
| 4 | `ORG_PRIMETIME_SHIFT_SET_MINS` | INTEGER |  | The organization's primetime shift room utilization setup minutes for a log. |
| 5 | `ORG_PRIMETIME_SHIFT_CLN_MINS` | INTEGER |  | The organization's primetime shift room utilization cleanup minutes for a log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

