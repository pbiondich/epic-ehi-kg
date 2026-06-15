# SPEC_AP_RESULT

> This table contains information related to results entered on a specimen's anatomic pathology result.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 4 | `AP_RES_TYPE_C_NAME` | VARCHAR |  | The note type category ID for this AP specimen result note. |
| 5 | `AP_RES_NOTE_ID` | VARCHAR |  | The unique ID of this AP specimen result note. |
| 6 | `AP_RES_STATUS_C_NAME` | VARCHAR |  | The status category ID for this AP specimen result note. |
| 7 | `NOTIF_SENT_UTC_DTTM` | DATETIME (UTC) |  | The first instant when a result notification was sent for this AP result in UTC. |
| 8 | `ACK_COMM_ID` | VARCHAR |  | The communication that was logged when the result is acknowledged. |
| 9 | `AP_RES_PUSH_EVAL_C_NAME` | VARCHAR |  | Stores the outcome of frozen result evaluation and push notification recipient resolution. |
| 10 | `NOTIF_SENT_LOCAL_DTTM` | DATETIME (Local) |  | The first instant when a result notification was sent for this AP result in the local time zone. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

