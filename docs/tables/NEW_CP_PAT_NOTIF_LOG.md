# NEW_CP_PAT_NOTIF_LOG

> This table contains information regarding the new care plan notifications that were sent.

**Primary key:** `CAREPLAN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CAREPLAN_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the care plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTIF_UTC_DTTM` | DATETIME (UTC) |  | The timestamp in UTC instant when the enrollment notification was sent to the patient and/or their proxy. |
| 4 | `NOTF_SEND_MTHD_C` | VARCHAR |  | The send method of the enrollment notification sent. |
| 5 | `NOTIF_RECIP_PAT_ID` | VARCHAR | FK→ | EPT ID of the recipient of the enrollment notification. |
| 6 | `NOTIF_RECIP_MYPT_ID` | VARCHAR |  | WPR ID of the recipient of the enrollment notification. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `NOTIF_RECIP_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

