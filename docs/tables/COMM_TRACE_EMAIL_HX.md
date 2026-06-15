# COMM_TRACE_EMAIL_HX

> This table contains an audit history of events for an outgoing email.

**Primary key:** `OUTREACH_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OUTREACH_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the outreach record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `AUDIT_UTC_DTTM` | DATETIME (UTC) |  | The UTC Instant a status update was received for the email. |
| 5 | `COMM_CONTACT_ID` | NUMERIC |  | The recipient CCR ID associated with the status update. |
| 6 | `EML_AUD_STATUS_C_NAME` | VARCHAR |  | The status of the email. |
| 7 | `SMTP_CODE` | INTEGER |  | The SMTP reply code of the email. |
| 8 | `SMTP_ENHANCED_CODE` | VARCHAR |  | The SMTP enhanced reply code of the email. |
| 9 | `DESCRIPTION` | VARCHAR |  | A plaintext description about the status of the email. |
| 10 | `DELIVERY_ATTEMPT_NUM` | INTEGER |  | The number of times this email was attempted to be delivered. |
| 11 | `RETRY_UTC_DTTM` | DATETIME (UTC) |  | The instant the email will retry delivery after a temporary failure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OUTREACH_ID` | [MC_NOTIF_INFO](MC_NOTIF_INFO.md) | sole_pk | high |

