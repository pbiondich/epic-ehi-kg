# PAT_EMAILS_TO_MEMBER

> Emails sent to the member via Tapestry Auto Actions.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SENT_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time when an email was sent to the member by an automatic action. |
| 4 | `EMAIL_ADDRESS` | VARCHAR |  | The email address to which the message was sent. |
| 5 | `NOTE_ID` | VARCHAR | shared | The unique ID of the note record of the email sent to the member. |
| 6 | `EMAIL_SUBJECT_SMARTTEXT_ID` | VARCHAR |  | The unique ID of the SmartText record used as the subject line of the email sent to the member. |
| 7 | `EMAIL_SUBJECT_SMARTTEXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 8 | `EMAIL_PLAIN_TEXT_SMARTTEXT_ID` | VARCHAR |  | The unique ID of the SmartText record used as the plain text template for the email sent to the member. |
| 9 | `EMAIL_PLAIN_TEXT_SMARTTEXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 10 | `EMAIL_HTML_SMARTTEXT_ID` | VARCHAR |  | The unique ID of the SmartText record used as the HTML body for the email sent to the member. |
| 11 | `EMAIL_HTML_SMARTTEXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 12 | `FROM_USER_ID` | VARCHAR |  | The unique ID of the user who sent the email to the member. |
| 13 | `FROM_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

