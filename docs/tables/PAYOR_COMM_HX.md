# PAYOR_COMM_HX

> The PAYOR_COMM_HX table contains a history of communications sent to payers by inpatient case managers. This data is from the Payer Communication navigator section. Each row represents a communication that was sent to a payer. If no communication was sent to a specific payer, a row will appear for that payer with the current fax, phone number, and contact name. In addition, a row will also be displayed for any fax, phone number, and/or contact name updates, if the update happened after sending the last communication. Therefore, the last row for a given payer contains the most current contact information for them.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `AGENCY_ID` | VARCHAR | FK→ | The unique ID of the payor communication recipient. |
| 6 | `AGENCY_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |
| 7 | `ROI_ID` | VARCHAR |  | The unique ID of the release of information disclosure record; the disclosure stores all information about the communication itself, such as sending time and user. |
| 8 | `LRP_ID` | VARCHAR | FK→ | The unique ID of the report that was sent to the payor. This column is always populated when a report is sent, but should only be used as a fallback if no Release of Information (ROI) is available in ROI_ID (such as in an IntraConnect scenario). Starting in the May 2023 version, this item extracted by this column will no longer be populated. |
| 9 | `LRP_ID_REPORT_NAME` | VARCHAR |  | The name of the report |
| 10 | `SENT_DTTM` | DATETIME (UTC) |  | The instant that the report was sent. This column is always populated when a report is sent, but should only be used as a fallback if no Release of Information (ROI) is available in ROI_ID (such as in an IntraConnect scenario). |
| 11 | `OVERRIDE_FAX` | VARCHAR |  | The fax number that was used or will be used for faxing the communication. |
| 12 | `OVERRIDE_PHONE` | VARCHAR |  | The phone number for the recipient at the time the communication was sent, or the most current phone number for the recipient. |
| 13 | `COMM_MODE_C_NAME` | VARCHAR |  | Method by which the communication was sent. |
| 14 | `OVERRIDE_CT_NAME` | VARCHAR |  | The contact person name for the recipient at the time the communication was sent, or the most current contact person name for the recipient. |
| 15 | `ORIG_SEND_LN` | INTEGER |  | If this line documents a resent report, this column includes the LINE number (in this table) of the line documenting the original sending of that report. This column is NULL on lines documenting an original sending. |
| 16 | `COMM_MEMO_NOTE_ID` | VARCHAR |  | This column contains the note ID of a note containing user comments about the related communication sent to the payer. |
| 17 | `IS_CUSTOM_DOCUMENT_YN` | VARCHAR |  | This indicates whether the communication included a custom document generated using document builder. |
| 18 | `ECA_REQUEST_REALTIME_TX_CSN_ID` | NUMERIC |  | The contact serial number of the realtime transaction record generated for an electronic authorization request in Payer Comm. |
| 19 | `SENDER_USER_ID` | VARCHAR |  | This stores the user that sent a questionnaire. It is currently only populated for outgoing questionnaire submissions. |
| 20 | `SENDER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 21 | `QUESTIONNAIRE_ANSWER_ID` | VARCHAR |  | This stores the questionnaire record that was submitted to the payer. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AGENCY_ID` | [CLARITY_AGENCY](CLARITY_AGENCY.md) | sole_pk | high |
| `LRP_ID` | [REPORT_DETAILS](REPORT_DETAILS.md) | sole_pk | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

