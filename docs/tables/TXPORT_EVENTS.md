# TXPORT_EVENTS

> Contains the sequence of events for the transport request.

**Primary key:** `TXPORT_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TXPORT_ID` | NUMERIC | PK | The unique ID of the transport request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EVENT_INSTANT_DTTM` | DATETIME (UTC) |  | The instant at which the assignment status of the transport request was updated on the server, stored as UTC. For local time, use TXPORT_EVENTS.EVENT_INSTANT_LOCAL_DTTM. |
| 4 | `WORKER_ID` | NUMERIC |  | The unique ID of the transporter assigned to this transport request at the time of the status update. |
| 5 | `TXPORT_DLY_RSN_C_NAME` | VARCHAR | org | The delay reason category number if the transport request was marked as delayed. |
| 6 | `TXPORT_CANC_RSN_C_NAME` | VARCHAR | org | This column contains cancel reasons specified by the user if the transport request was canceled. |
| 7 | `HKR_TXPORT_ID` | NUMERIC |  | The ID of the transporter who changes the status of the request. |
| 8 | `EMP_TXPORT_ID` | VARCHAR |  | The ID of the user who changes the status of the request. |
| 9 | `EMP_TXPORT_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `EVENT_INSTANT_LOCAL_DTTM` | DATETIME (Local) |  | The local instant at which the assignment status of the transport request was updated. For UTC, use TXPORT_EVENTS.EVENT_INSTANT_DTTM. |
| 11 | `ENTRY_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant at which an update to the assignment status of the transport request was entered, stored as UTC. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

