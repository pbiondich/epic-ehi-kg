# PAT_ENC_PAYOR_NOTF

> This table extracts the payor notification status information.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `MSG_TYPE_C_NAME` | VARCHAR |  | The type of notification that is sent to the payor. |
| 7 | `COVERAGE_ID` | NUMERIC | FK→ | The coverage ID for the notification message sent to the payor |
| 8 | `PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 9 | `BENEFIT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 10 | `MSG_SENT_DTTM` | DATETIME (UTC) |  | Instant that notification message has been sent in UTC |
| 11 | `MSG_RECEIVED_DTTM` | DATETIME (UTC) |  | Instant that notification response has been received in UTC |
| 12 | `MSG_STATUS_C_NAME` | VARCHAR |  | Notification message status. |
| 13 | `NOTE_ID` | VARCHAR | shared | ID of the note that corresponds with the notification message. |
| 14 | `USER_COMMENT` | VARCHAR |  | The user-entered text when manually verifying notification status. |
| 15 | `NOTIF_REFERENCE_NUMBER` | VARCHAR |  | Notification reference ID |
| 16 | `REASON_CODE` | VARCHAR |  | Notification message status reason code |
| 17 | `NOTIF_ORGANIZATION_ID` | NUMERIC |  | Notification organization ID |
| 18 | `NOTIF_ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 19 | `NOTIF_EVENT_LOCAL_DTTM` | DATETIME (Local) |  | Instant in local time of the associated event that the notification is for. For an observation admission this is the observation admission instant, for an inpatient admission this is the inpatient admission instant, and discharge notifications use the discharge instant. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

