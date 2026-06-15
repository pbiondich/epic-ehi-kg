# TC_REQUEST_STATUS_HX

> This table stores information related to the status change history for Transfer Center requests.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique identifier for the communication record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REQUEST_STATUS_C_NAME` | VARCHAR |  | This item stores the audit trail for the status of the request. |
| 4 | `STATUS_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The datetime at which the request's status changed, stored in UTC. For local time, use TC_REQUEST_STATUS_HX.STATUS_UPDATE_LOCAL_DTTM. |
| 5 | `STATUS_UPDATE_USER_ID` | VARCHAR |  | This item stores the user who changed the status of the request. |
| 6 | `STATUS_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `DEST_DECLINE_RSN_C_NAME` | VARCHAR | org | This item stores the audit trail for the decline reason of the destination planning record. |
| 8 | `CANCEL_STATUS_RSN_C_NAME` | VARCHAR | org | This item stores the audit trail for the cancel reason of the request. |
| 9 | `STATUS_UPDATE_LOCAL_DTTM` | DATETIME (Local) |  | The datetime at which the request's status changed, stored in local time. For UTC, use TC_REQUEST_STATUS_HX.STATUS_UPDATE_UTC_DTTM. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

