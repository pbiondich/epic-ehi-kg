# CHAT_MESSAGE_CONTENT

> Table for PHI message contents sent in secure chat.

**Primary key:** `CONVERSATION_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 25  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONVERSATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the secure chat conversation record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `MSG_TEXT` | VARCHAR |  | Stores the message text for a single secure chat message. Note: It is stored in a super-item, because the super-item global structure is more efficient. No additional items should be added to its super item. |
| 5 | `MEDIA_DOCUMENT_ID` | VARCHAR |  | This item stores a link to a media record containing information about the media file sent in a Secure Chat message. |
| 6 | `LINK_CONTENT_TYPE_C_NAME` | VARCHAR | org | The type of content linked to in this message. |
| 7 | `LINK_REPORT_INFO_ID` | NUMERIC |  | The SlicerDicer Session ID linked to in this message. |
| 8 | `LINK_REPORT_INFO_ID_REPORT_INFO_NAME` | VARCHAR |  | The name of the report. |
| 9 | `LINK_ORDER_SESSION_EVENT_ID` | VARCHAR |  | Store the pended order session that is linked to this message in the conversation. |
| 10 | `LINK_ORDER_SESSION_EVENT_LINE` | INTEGER |  | Store the event line for the pended order session that is linked to this message in the conversation. |
| 11 | `LINK_RDS_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Stores the patient CSN to link the message to the patient in the remote dual sign workflow |
| 12 | `LINK_PENDING_ADT_EVENT_PEND_ID` | VARCHAR |  | Store the ID for the pending ADT event (PND) that is linked to this message in the conversation. |
| 13 | `LINK_TRANSFER_CENTER_COMM_ID` | NUMERIC |  | Store the ID for the Transfer Center request (NCS) that is linked to this message in the conversation. |
| 14 | `ORDER_ID` | NUMERIC | shared | Signed Order linked to in this message. |
| 15 | `CAPTION_SS` | VARCHAR |  | Caption of the order or saved work linked to this message. |
| 16 | `DESCRIPTION_SS` | VARCHAR |  | Description of the order or saved work linked to this message. |
| 17 | `ORDER_SNAPSHOT_UTC_DTTM` | DATETIME (UTC) |  | The instant at which order data for this message line was current. |
| 18 | `RECORD_CONTACT` | NUMERIC |  | Record contact linked to the chat message |
| 19 | `LINKED_AUTH_REQUEST_ID` | NUMERIC |  | The unique ID of the authorization request (AUG) linked to this conversation. |
| 20 | `ESCALATION_ID` | NUMERIC | FK→ | Chat request linked to this message. |
| 21 | `LINKED_TREATMENT_PLAN_ID` | NUMERIC |  | The unique ID of the treatment plan or therapy plan (TPL) record linked to the message. |
| 22 | `LINKED_MOUTH_ID` | NUMERIC |  | The unique ID of the patient mouth record linked to the message. |
| 23 | `LINKED_DENT_PLAN_ID` | NUMERIC |  | The unique ID of the dental treatment plan record linked to the message. |
| 24 | `LINKED_ACTION_C_NAME` | VARCHAR |  | The action taken for the linked content type |
| 25 | `SHIFT_BUNDLE_ID` | NUMERIC |  | Stores the ID of the Staffing Plan (SHB) linked to the message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ESCALATION_ID` | [ESCALATION_DYN](ESCALATION_DYN.md) | sole_pk | high |
| `LINK_RDS_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

