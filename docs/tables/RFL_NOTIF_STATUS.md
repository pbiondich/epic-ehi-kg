# RFL_NOTIF_STATUS

> This table contains information about the status of failed faxes from a referral.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 16  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTIFICATION_ID` | INTEGER |  | Holds the unique ID within a referral for a particular referral notification |
| 4 | `LAST_UPDATED_DTTM` | DATETIME (UTC) |  | This holds the last instant this particular fax line was updated. |
| 5 | `ATTEMPTS` | INTEGER |  | The number of times this fax has been submitted |
| 6 | `STATUS_C_NAME` | VARCHAR |  | Current status of the notification |
| 7 | `FAILURE_REASON_C_NAME` | VARCHAR |  | Failure reason for the fax |
| 8 | `RECIPIENT_C_NAME` | VARCHAR |  | The recipient of the fax |
| 9 | `LETTER_ID` | VARCHAR |  | Letter from the original notification event |
| 10 | `LETTER_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 11 | `PRINT_CLASS_C_NAME` | VARCHAR | org | This holds the original print class used to generate the notification. |
| 12 | `NOTE_ID` | VARCHAR | shared | The General Use Note (HNO) record that was sent during the letter review process, used to resend the updated letter. |
| 13 | `FAX_NAME` | VARCHAR |  | Stores the name of the recipient for a fax. This will be used as the recipient name in the event the failed fax is resent. |
| 14 | `FAX_NUM` | VARCHAR |  | Stores the fax number for a fax. This will be used as the fax number in the event the failed fax is resent. |
| 15 | `FAILURE_ERR_MSG` | VARCHAR |  | For a failed notification, the error message associated with the failure. |
| 16 | `NOTIF_DOC_ROI_ID` | VARCHAR |  | The document associated with the original notification. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

