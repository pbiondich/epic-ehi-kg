# CAL_COMM_TRACKING

> The CAL_COMM_TRACKING table contains information about your communication tracking records. This includes such information as communication type, the date and time the contact was made, and caller details.

**Overflow family:** [CAL_COMM_TRACKING_2](CAL_COMM_TRACKING_2.md)  
**Primary key:** `COMM_ID`  
**Columns:** 28  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | VARCHAR | PK shared | The unique ID for the Communication Tracking record. |
| 2 | `USER_ID` | VARCHAR | FK→ | The user who entered the communication. |
| 3 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 4 | `COMM_INSTANT_DTTM` | DATETIME (UTC) |  | The date and time of the communication, stored in UTC format. |
| 5 | `COMM_COMMENT` | VARCHAR |  | A comment to go with the communication. |
| 6 | `CALLER_NAME` | VARCHAR |  | For incoming calls, this item stores the name of the caller. For outgoing calls, it stores the name of the person who was contacted for this logged communication. |
| 7 | `PHONE_NUMBER` | VARCHAR |  | Phone number for the communication. |
| 8 | `CONTACT_ACCT_ID` | NUMERIC |  | The unique ID of the guarantor account that is associated with the communication. |
| 9 | `REF_DOCUMENT_ID` | VARCHAR |  | If there is a scanned document related to the communication, this field will contain the ID of the document's DCS record. |
| 10 | `COMM_CMT_NOTE_ID` | VARCHAR |  | Note record containing comment about communication |
| 11 | `CONTACT_PHR_ID` | NUMERIC |  | The unique ID of the pharmacy that is associated with the communication. |
| 12 | `CONTACT_PHR_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 13 | `EXTERNAL_ID` | VARCHAR |  | This item stores the external identifier for this contact. This may be populated when the contact was automatically generated. |
| 14 | `COMM_IN_CMT_NOTE_ID` | VARCHAR |  | The unique ID of the note that is associated with the lab comment. |
| 15 | `CONTACT_WORKER_ID` | NUMERIC |  | The unique ID of the hospital service employee that is associated with this communication. |
| 16 | `CONTACT_WORKER_PAGER_C_NAME` | VARCHAR | org | The pager this communication was sent to. |
| 17 | `MESSAGE_SUBJECT` | VARCHAR |  | The subject line of a message sent to a pager. |
| 18 | `MESSAGE_AD_HOC_YN` | VARCHAR |  | Indicates whether or not the message was ad hoc (entered by a user in Hyperspace) rather than a system-generated message triggered by some kind of action. |
| 19 | `TC_REQ_COMM_CONTACT_IDENTIFIER` | INTEGER |  | This item stores the identifier for the entry in the contact log of the associated Transfer Center request that corresponds with the contact on the communication. |
| 20 | `CONTACT_SUBMITTER_ID` | NUMERIC |  | The unique ID of the laboratory submitter that is associated with the communication. |
| 21 | `CONTACT_SUBMITTER_ID_RECORD_NAME` | VARCHAR |  | The name of the submitter record. |
| 22 | `SOURCE_COMM_ID` | VARCHAR |  | The unique ID of the communication record that this communication was copied from when it was moved to a different transfer center request. |
| 23 | `CONTACT_REP_GUID` | VARCHAR |  | This is the line identifier for the representative of the member being contacted as part of this communication. The line identifier corresponds to the coverage responsible person line identifier (MEMBER_RESP_PERSON.MEM_RESP_GUID). |
| 24 | `MESSAGE_PREFERRED_LANGUAGE_C_NAME` | VARCHAR | org | The preferred language of the message recipient, if not the native language for the environment. |
| 25 | `APPEAL_GRV_LETTER_TYPE_C_NAME` | VARCHAR | org | The purpose of this communication as it relates to health plan appeal and grievance turnaround time requirements and notifications |
| 26 | `CONTACT_RECIP_CLASS_ID` | VARCHAR |  | The Recipient Class (FEV record) used to find the recipient of the call. |
| 27 | `CONTACT_RECIP_CLASS_ID_EVENT_NAME` | VARCHAR |  | The name of the event. |
| 28 | `COMM_AUTODIAL_AGENT_MESSAGE` | VARCHAR |  | Message shown to agent answering an auto dial call |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

