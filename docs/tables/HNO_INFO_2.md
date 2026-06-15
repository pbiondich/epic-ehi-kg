# HNO_INFO_2

> This table contains common information from General Use Notes items. This table focuses on one time only data while other HNO tables (e.g., NOTES_ACCT, CODING_CLA_NOTES) contain the data for different note types.

**Overflow of:** [HNO_INFO](HNO_INFO.md)  
**Primary key:** `NOTE_ID`  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The note ID for the note record. |
| 2 | `RELEVANT_REC_EVENT_ID` | VARCHAR |  | Holds the Events (IEV) record which contains records marked relevant to the Note such as problems, allergies, lab results, etc. |
| 3 | `GROUP_NOTE_ID` | VARCHAR |  | This item stores the group note ID for notes that are created in a group documentation context. |
| 4 | `LETTER_DEST_C_NAME` | VARCHAR |  | The letter destination category ID for the note. This column is only populated if this row is for a Customer Relationship Management letter. |
| 5 | `LETTER_FINAL_UTC_DTTM` | DATETIME (UTC) |  | The instant the letter was finalized. This column is only populated if this row is for a Customer Relationship Management letter. |
| 6 | `HNO_RECORD_TYPE_C_NAME` | VARCHAR |  | Record type. |
| 7 | `RFL_LETTER_ENC_CSN` | NUMERIC | FK→ | Stores the encounter in which the referral communication letter was written |
| 8 | `CONV_MSG_CID` | NUMERIC |  | This item contains the Community ID (CID) of a related In Basket Message (EOW) record. |
| 9 | `OUTREACH_TEMPLATE_ID` | NUMERIC |  | This item stores the campaign outreach template that created the letter. |
| 10 | `SOURCE_EDITS_CSN` | NUMERIC |  | Stores a Contact Serial Number (CSN) pointer to the General Use Notes (HNO) record that holds edits to the parent note while an attestation is in progress. |
| 11 | `EXT_DOC_EVNT_ID` | VARCHAR |  | External autoreconciled note event identifier |
| 12 | `EXT_NOTE_TYPE` | VARCHAR |  | Autoreconciled external note type name |
| 13 | `EXT_DUP_NOTE_ID` | VARCHAR |  | Autoreconciled extneral note duplicate source note |
| 14 | `EXT_DUP_NOTE_C_NAME` | VARCHAR |  | Autoreconciled external note duplicate note type |
| 15 | `PARENT_NOTE_ID` | VARCHAR |  | The parent note ID of a soft-deleted transcription record. |
| 16 | `ACTIVE_C_NAME` | VARCHAR |  | Whether the note is active. This item is not populated for all notes. |
| 17 | `EXT_AUTHOR` | VARCHAR |  | Name of the external note's author. The name is stored as pieces delimited by character 127 and is ordered as follows: Last Name, Last Name from Spouse, First Name, Middle Name, Last Name Prefix, Spouse Last Name Prefix, Title, Suffix, Academic Initials. |
| 18 | `NOTE_UPDATE_INST_UTC_DTTM` | DATETIME (UTC) |  | The last time this note was received through Care Everywhere. The value of Received Assessment and Plan Existence Days (I DXC 17000) defines how long notes with this item set exist before they are deleted. Scheduled task Remove HNO Records (E1J 88032) deletes notes and all of their references that have not been received within the amount of days defined by Received Assessment and Plan Existence Days (I DXC 17000) Received Assessment and Plan Existence Days (I DXC 17000) defaults to 30 days if not set. |
| 19 | `ROUT_RECPNT_COMMUNICATION_ID` | NUMERIC |  | This is a Communication Management (LCA) record that contains information about recipients that users selected for routing in the clinical note editor. |
| 20 | `EXTERNAL_SOURCE_IDENT` | VARCHAR |  | If this note is associated with information in an outside system, the ID of that information can be stored here. |
| 21 | `EXTERNAL_PROBLEM_IDENT` | VARCHAR |  | The reference ID for the external problem linked to the note. |
| 22 | `TRANSLATION_IDENTIFIER` | VARCHAR |  | Stores the unique identifier to link back to the source information that the note is a translation for. This should only be set on Translation (Item HNO 50 = 61) type HNO records. The format of the identifier is intended to capture the INI and ID of the source record, along with the requested language to be translated in. |
| 23 | `TRANSLATION_LANGUAGE_ID` | NUMERIC |  | The unique identifier (.1 item) for the Epic Languages record associated with a translation HNO record. Should only be set for Translation (Item HNO 50 = 61) type notes. |
| 24 | `TRANSLATION_LANGUAGE_ID_LANGUAGE_NAME` | VARCHAR |  | The language name. If the language is written and uses more than one script to represent it, the name will contain the script in parentheses after the language name. |
| 25 | `NOT_RESEARCH_RELATED_YN` | VARCHAR |  | Indicates whether the current note has been explicitly marked as not being related to research for this note. 'Y' indicates that the note has been marked as not research related. 'N' indicates that the note is related to research. NULL indicates that a decision has not been made yet. |
| 26 | `PRIVATE_YN` | VARCHAR |  | Stores whether this note is considered private to the author or visible by others. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `RFL_LETTER_ENC_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

