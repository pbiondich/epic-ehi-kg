# SPEC_TRANSMTL_LOG

> The SPEC_TRANSMTL_LOG table holds an audit log for transmitting results for specimens.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique ID of the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TRANSMTL_EVENT_ID` | VARCHAR |  | The unique ID of the event that caused the result transmittal to occur. |
| 4 | `TRANSMTL_EVENT_ID_RECORD_NAME` | VARCHAR |  | The name of the event template. |
| 5 | `TRANSMTL_DTTM` | DATETIME (Local) |  | The date and time of the result transmittal log entry. |
| 6 | `TRANSMTL_RESULT_ID` | VARCHAR |  | The unique ID of the result record that was transmitted. |
| 7 | `TRANSMTL_COMMENT` | VARCHAR |  | Additional comments for the result transmittal audit log entry. |
| 8 | `TRANSMTL_STATUS_C_NAME` | VARCHAR |  | The status category number of the result transmittal audit log entry. |
| 9 | `TRANSMIT_UTC_DTTM` | DATETIME (UTC) |  | The instant when result transmittal occurred in UTC. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

