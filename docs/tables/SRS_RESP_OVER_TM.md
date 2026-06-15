# SRS_RESP_OVER_TM

> This table stores the answers for a questionnaire series.

**Primary key:** `SERIES_ANS_ID`, `CONTACT_DATE_REAL`  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SERIES_ANS_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the series answer record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The contact serial number (CSN) of the contact. |
| 5 | `CONTACT_NUM` | INTEGER |  | This column stores the contact number of the series answer record. |
| 6 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 7 | `FORM_ID` | VARCHAR | FK→ | This column stores the ID of an individual questionnaire in a questionnaire series record. |
| 8 | `FORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 9 | `QUESTIONNAIRE_CSN` | NUMERIC |  | This column stores the questionnaire's contact date (DAT) in a series of questionnaires. |
| 10 | `QUESR_INST_NUM` | INTEGER |  | To store the bucket number of an answer to a specific questionnaire. |
| 11 | `QUESR_STATUS_C_NAME` | VARCHAR |  | To store the status of a particular questionnaire (in-progress, disabled, expired, etc.). |
| 12 | `STATUS_CHANGE_DTTM` | DATETIME (UTC) |  | To store the change instant of a status of a questionnaire. |
| 13 | `INSTANT_OF_ENT_DTTM` | DATETIME (UTC) |  | Stores the instant of entry when a record is edited |
| 14 | `QUESR_ANS_ENC_CSN` | NUMERIC | FK→ | This column stores the contact date (DAT) of the encounter for which questionnaire answers are saved. Note that there will be a contact date only if a message is being routed or if the questionnaire is part of an appointment. |
| 15 | `QUESR_ANS_WPR_ID` | VARCHAR |  | This column stores the patient web portal ID of the user who answered the questionnaire. |
| 16 | `QUESR_DUE_DATE` | DATETIME |  | This column stores the due date of an individual questionnaire for this series answer record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FORM_ID` | [CL_QFORM1](CL_QFORM1.md) | sole_pk | high |
| `QUESR_ANS_ENC_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `SERIES_ANS_ID` | [SRS_ASGN_INFO](SRS_ASGN_INFO.md) | sole_pk | high |

