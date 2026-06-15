# OR_LOG_RTLS

> This table contains information about a procedure's Real-Time Location System (RTLS) tracking.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the log record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RTLS_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `RTLS_START_UTC_DTTM` | DATETIME (UTC) |  | This item stores the start time of the RTLS event and is part of a related group storing raw RTLS data for audit purposes. The time stored here does not necessarily reflect the staff or surgeon's time on the log. |
| 5 | `RTLS_END_UTC_DTTM` | DATETIME (UTC) |  | This item stores the end time of the RTLS event and is part of a related group storing raw RTLS data for audit purposes. The time stored here does not necessarily reflect the staff or surgeon's time on the log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

