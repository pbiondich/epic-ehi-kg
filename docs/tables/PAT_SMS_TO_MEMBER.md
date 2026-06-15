# PAT_SMS_TO_MEMBER

> Text messages sent to the member via Tapestry Auto Actions.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SENT_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time when a text message was sent to the member. |
| 4 | `PHONE_NUMBER` | VARCHAR |  | The phone number to which the text message was sent. |
| 5 | `NOTE_ID` | VARCHAR | shared | The unique ID of the note record of the SMS message sent to the member. |
| 6 | `SMS_SMARTTEXT_ID` | VARCHAR |  | The unique ID of the SmartText record used as the SMS message sent to the member. |
| 7 | `SMS_SMARTTEXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 8 | `SMS_SETTING_ID` | NUMERIC |  | The unique ID of the Hello World communication template (HST) for the SMS sent to the member. |
| 9 | `SMS_SETTING_ID_SETTING_NAME` | VARCHAR |  | Setting record name. |
| 10 | `FROM_USER_ID` | VARCHAR |  | The unique ID of the user who sent the text message to the member. |
| 11 | `FROM_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

