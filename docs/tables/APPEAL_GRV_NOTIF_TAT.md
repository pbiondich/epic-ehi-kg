# APPEAL_GRV_NOTIF_TAT

> This table holds information about notifications that complete required turnaround time events for appeals and grievances. Each row corresponds to an individual turnaround time requirement and the communication that satisfied that requirement.

**Primary key:** `APPEAL_GRV_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `APPEAL_GRV_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the appeal/grievance record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTIF_TAT_TIME_STANDARD_C_NAME` | VARCHAR | org | The timeliness standard category ID that corresponds to this notification requirement. |
| 4 | `APPEAL_GRV_LETTER_TYPE_C_NAME` | VARCHAR | org | The notification type category ID for this notification requirement. |
| 5 | `NOTIF_TAT_RECIP_CLASS_ID` | VARCHAR |  | The unique ID of the recipient class that this notification is required to be sent to. |
| 6 | `NOTIF_TAT_RECIP_CLASS_ID_EVENT_NAME` | VARCHAR |  | The name of the event. |
| 7 | `NOTIF_TAT_METHOD_C_NAME` | VARCHAR |  | The category ID for how this notification is required to be sent. (Oral vs Written) |
| 8 | `NOTIF_TAT_DUE_UTC_DTTM` | DATETIME (UTC) |  | The date and time that this notification requirement is due. Stored in UTC. |
| 9 | `NOTIF_TAT_OCCUR_UTC_DTTM` | DATETIME (UTC) |  | The date and time that this notification was submitted. NULL indicates that the notification is still outstanding. Stored in UTC. |
| 10 | `NOTIF_LETTER` | VARCHAR |  | The letter GUID (I TAG 5020) that satisfies this notification requirement. |
| 11 | `NOTIF_CALL_COMM_ID` | VARCHAR |  | The unique ID of the communication that satisfies this notification requirement. |
| 12 | `NOTIF_TAT_DUE_LOCAL_DTTM` | DATETIME (Attached) |  | The date and time that this notification requirement is due. Stored in the time zone determined by column APPEAL_GRV.TAT_RPT_TIME_ZONE_C. |
| 13 | `NOTIF_TAT_OCCUR_LOCAL_DTTM` | DATETIME (Attached) |  | The date and time that this notification was submitted. NULL indicates that the notification is still outstanding. Stored in the time zone determined by column APPEAL_GRV.TAT_RPT_TIME_ZONE_C. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `APPEAL_GRV_ID` | [APPEAL_GRV](APPEAL_GRV.md) | sole_pk | high |

