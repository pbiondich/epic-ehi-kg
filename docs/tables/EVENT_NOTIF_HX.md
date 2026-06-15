# EVENT_NOTIF_HX

> The Event Notification History records notifications that were sent about a patient encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 15  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `SENT_DTTM` | DATETIME (UTC) |  | This date/time when the notification was sent. |
| 7 | `EVENT_TYPE_C_NAME` | VARCHAR | org | The event notification event type category number for the notification delivery. This indicates the type of event that triggered event notification. |
| 8 | `PEND_ID` | VARCHAR | FK→ | The unique ID of the pending event or bed request that triggered Bed Planning Event Notification. Only notifications sent for Bed Planning events have a value populated for this column. |
| 9 | `SEND_TO_C_NAME` | VARCHAR |  | The send to category number for the notification delivery. This indicates who was supposed to receive the notification. |
| 10 | `PCP_TYPE_C_NAME` | VARCHAR | org | The category number of the type of primary care provider for the notification delivery. Only rows that have a Send To of PCP have a value populated for this item. This column indicates the type of PCP that was supposed to receive the notification. |
| 11 | `SENT_TO_FAX_NUMBER` | VARCHAR |  | This is the fax number that a faxed notification was sent to. |
| 12 | `SENT_TO_EMAIL_ADDR` | VARCHAR |  | This is the email address that was used when a notification was delivered via email. There may be multiple email addresses listed. |
| 13 | `SEND_METHOD_C_NAME` | VARCHAR |  | The delivery method category number for the notification delivery. |
| 14 | `EVENT_ID` | VARCHAR | FK→ | This item holds the event notification record that was triggered |
| 15 | `EVENT_ID_EVENT_NAME` | VARCHAR |  | The name of the event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `PEND_ID` | [PEND_ACTION](PEND_ACTION.md) | sole_pk | high |

