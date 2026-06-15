# PAT_ENC_REMINDER

> The PAT_ENC_REMINDER table contains information about follow up messages sent to users. These include the number of days after the visit to send the message, the text of the message, and a flag indicating whether the message has been sent or not.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 3 | `PAT_REMD_SEND_DAYS` | INTEGER |  | Contains the number of days after the visit that a reminder/follow up message should be sent to the user. |
| 4 | `PATIENT_REMD_SENT_NAME` | VARCHAR |  | This column indicates whether or not a reminder message has been sent to the user. A 1 indicates that a reminder message has been sent. |
| 5 | `PAT_REMINDER_MSG` | VARCHAR |  | Contains the text of the reminder/follow up message sent to the user. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

