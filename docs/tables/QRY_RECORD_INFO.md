# QRY_RECORD_INFO

> The QRY_RECORD_INFO table contains information about the no-add single response data for query records (records in the QRY master file).

**Primary key:** `QUERY_ID`  
**Columns:** 15  
**Joined by:** 12 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `QUERY_ID` | NUMERIC | PK | The unique identifier for the query record. |
| 2 | `EXTERNAL_IDENTIFIER` | VARCHAR |  | The ID received from a third party to uniquely identify the record in their system. |
| 3 | `STATUS_C_NAME` | VARCHAR |  | The overall status of the query. |
| 4 | `PAT_ID` | VARCHAR | FK→ | The patient ID the query refers to. |
| 5 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The patient contact (CSN) the query refers to. |
| 6 | `CREATION_UTC_DTTM` | DATETIME (UTC) |  | The instant the query was created in UTC. |
| 7 | `UPDATE_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant the query record was updated in UTC. |
| 8 | `QUERY_WORKFLOW_C_NAME` | VARCHAR |  | The workflow this query is a part of (Computer Assisted Physician Documentation (CAPD), Clinical Documentation Improvement, etc.). This value is used to drive functionality and reporting. |
| 9 | `QRY_HIDE_PHYS_YN` | VARCHAR |  | If this is set to 1-Yes, it will prevent physicians from seeing the query in the NoteReader Clinical Documentation Improvement (CDI) activity. If NoteReader CDI is in silent mode, all incoming queries will have this flag set automatically. CDI users can reset this flag by activating the query manually. |
| 10 | `RECORD_CREATION_DT` | DATETIME |  | Stores the date the record was created. |
| 11 | `INSTANT_OF_UPDATE_DTTM` | DATETIME (Local) |  | Stores the instant the record was last locked/unlocked. |
| 12 | `QUERY_CONDITION_C_NAME` | VARCHAR |  | This item stores the patient's condition that this query is related to. This is determined based on the target diagnosis (QRY-55) or the suggestions (QRY 1150 group). |
| 13 | `QRY_ACTION_TYPE_C_NAME` | VARCHAR |  | This item stores the action type of the query that determines how it will be acted on by a user. |
| 14 | `SHOWN_PHYS_UTC_DTTM` | DATETIME (UTC) |  | The timestamp that a user activated the query to be shown to physicians. This is not set when the query was initially shown to physicians. |
| 15 | `RESP_EDG_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (12)

| From | Column | Confidence |
|------|--------|------------|
| [QRY_ADDL_RECIPIENTS](QRY_ADDL_RECIPIENTS.md) | `QUERY_ID` | high |
| [QRY_ADDL_RESPONSE](QRY_ADDL_RESPONSE.md) | `QUERY_ID` | high |
| [QRY_CONTACT_INFO](QRY_CONTACT_INFO.md) | `QUERY_ID` | high |
| [QRY_EVIDENCE](QRY_EVIDENCE.md) | `QUERY_ID` | high |
| [QRY_EVIDENCE_EXCERPT_TEXT](QRY_EVIDENCE_EXCERPT_TEXT.md) | `QUERY_ID` | high |
| [QRY_EVIDENCE_LQL_ANSWERS](QRY_EVIDENCE_LQL_ANSWERS.md) | `QUERY_ID` | high |
| [QRY_EVIDENCE_NOTE_CSN_ID](QRY_EVIDENCE_NOTE_CSN_ID.md) | `QUERY_ID` | high |
| [QRY_EVIDENCE_NOTE_IDS](QRY_EVIDENCE_NOTE_IDS.md) | `QUERY_ID` | high |
| [QRY_SUGGESTION_INFO](QRY_SUGGESTION_INFO.md) | `QUERY_ID` | high |
| [QRY_TARGET_INFO](QRY_TARGET_INFO.md) | `QUERY_ID` | high |
| [QUERY_INSTRUCTIONS](QUERY_INSTRUCTIONS.md) | `QUERY_ID` | high |
| [QUERY_TEXT](QUERY_TEXT.md) | `QUERY_ID` | high |

