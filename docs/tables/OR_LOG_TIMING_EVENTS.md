# OR_LOG_TIMING_EVENTS

> The OR_LOG_TIMING_EVENTS table contains information about case timing events associated with a procedural case that has been performed.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID associated with the log record for this row. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TIMING_EVENT_C_NAME` | VARCHAR |  | The case timing event category ID for the procedure log. |
| 4 | `TIMING_EVENT_DTTM` | DATETIME (Local) |  | The case timing event instant for the procedure log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

