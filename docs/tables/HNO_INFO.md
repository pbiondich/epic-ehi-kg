# HNO_INFO

> This table contains common information from General Use Notes items. This table focuses on time-insensitive, once-per-record data while other HNO tables (e.g., NOTES_ACCT, CODING_CLA_NOTES) contain the data for different note types.

**Overflow family:** [HNO_INFO_2](HNO_INFO_2.md)  
**Primary key:** `NOTE_ID`  
**Columns:** 39  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique ID of the note record. |
| 2 | `NOTE_TYPE_NOADD_C_NAME` | VARCHAR | org | Starting in November 2025 this column has the value for Note - Type No-Add (I HNO 51) to identify the type of note this record is for non clinical notes. For clinical notes, instead use the column IP_NOTE_TYPE_C in table HNO_INFO to get the UCN note type (I HNO 34033) value. Versions prior to November 2025 used the following logic: This virtual item (I HNO 17051) is populated with a category value from Note - Type No-Add (I HNO 51) according to the following logic: * if Note - Type No-Add (I HNO 51) is populated, use the value directly * if Note - Type No-Add (I HNO 51) is null and the note is not ambulatory, return null * if Note - Type No-Add (I HNO 51) is null and the note has an ambulatory encounter context, obtain a category from the UCN note type (I HNO 34033) and map that value to an equivalent category from Note - Type No Add (I HNO 51), if possible |
| 3 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for the patient encounter to which the note is attached. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 4 | `ENTRY_USER_ID` | VARCHAR |  | The unique ID of the user who created this note. This column is frequently used to link to the CLARITY_EMP table. |
| 5 | `ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `NOTE_DESC` | VARCHAR |  | This is a free text description of the note. |
| 7 | `IP_NOTE_TYPE_C_NAME` | VARCHAR | org | The note type associated with this note. |
| 8 | `ORIGINAL_HP_ID` | VARCHAR |  | For View-Only H&P notes only - original note record identifier |
| 9 | `ORIG_HP_DATE_REAL` | NUMERIC |  | For View-Only H&P notes only - original note record contact |
| 10 | `SOURCE_HP_ID` | VARCHAR |  | For Interval H&P only - ID of H&P Note being modified by interval note |
| 11 | `SOURCE_HP_DATE_REAL` | NUMERIC |  | For Interval H&P only - contact of H&P Note being modified by interval note |
| 12 | `ECG_TECHNICIAN_ID` | VARCHAR |  | The Electrocardiogram/Spirometry Technician |
| 13 | `PAT_LINK_ID` | VARCHAR |  | Virtual item that will check all HNO items linked to EPT and return the first EPT ID it finds. The items are checked in the following order: 505, 38970, 21001, 600 (which gives us an order, then we look at ord 210), 1605, 1643, 1640. |
| 14 | `LETTER_SUMMARY` | VARCHAR |  | The summary of the letter. |
| 15 | `TX_IB_FOLDER_C_NAME` | NUMERIC | org | Stores the Type of Message (I EOW 30) In Basket folder to be used by the Transcription interface to generate In Basket messages |
| 16 | `CREATE_INSTANT_DTTM` | DATETIME (UTC) |  | The note's create instant. |
| 17 | `UNSIGNED_YN` | VARCHAR |  | A flag for if the note record is considered an unsigned note. |
| 18 | `DELETE_INSTANT_DTTM` | DATETIME (UTC) |  | The instant when the note is deleted. |
| 19 | `DELETE_USER_ID` | VARCHAR |  | User who deleted the note |
| 20 | `DELETE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 21 | `COSIGNED_NOTE_LINK` | NUMERIC |  | Contains a contact serial number (CSN) that points to the resident's note being cosigned. Cosigning Note Link (I HNO 34158) is a link for the opposite direction. |
| 22 | `DATE_OF_SERVIC_DTTM` | DATETIME (UTC) |  | The note's date of service. |
| 23 | `SIGNED_NOTE_ID` | VARCHAR |  | This item points to the ID of the signed note that this note is addending/editing/cosigning. |
| 24 | `LST_FILED_INST_DTTM` | DATETIME (UTC) |  | The instant the note was last edited. |
| 25 | `UPDATE_DATE` | DATETIME (Local) |  | The date and time when this row was created or last updated in Clarity. |
| 26 | `CURRENT_AUTHOR_ID` | VARCHAR |  | This item stores the current author of the note for indexing purposes. |
| 27 | `CURRENT_AUTHOR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 28 | `LETTER_TYPE_C_NAME` | VARCHAR | org | Type of professional billing letter. |
| 29 | `VISIT_NUM` | VARCHAR |  | Professional billing visit number attached to this note. |
| 30 | `CRT_INST_LOCAL_DTTM` | DATETIME (Local) |  | This is a virtual item that gets the create instant (I HNO 17105), in local time format. |
| 31 | `PRIORITY_YN` | VARCHAR |  | The priority of the note (Yes = High, No = Routine). |
| 32 | `ACTIVE_FROM_DT` | DATETIME |  | The date on which the note becomes active. |
| 33 | `ACTIVE_TO_DT` | DATETIME |  | The date after which the note becomes inactive. |
| 34 | `TREAT_SUM_RLS_TO_MYC_YN` | VARCHAR |  | Indicates whether a Treatment Summary is released to MyChart. |
| 35 | `TREAT_SUM_RLS_TO_MYC_CSN` | NUMERIC |  | Stores the CSN of the Treatment Summary (HNO) that is released to MyChart. If you use IntraConnect, this column stores the Unique Contact Identifier (UCI). |
| 36 | `COMMENT_USER_ID` | VARCHAR |  | The unique ID of the last user to edit the internal comment in either the Continued Care and Services Coordination or Payer Communication workflows. |
| 37 | `COMMENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 38 | `COMMENT_EDIT_INST_DTTM` | DATETIME (UTC) |  | Instant the comment was last edited in either the Continued Care and Services Coordination or Payer Communication workflows. In UTC. |
| 39 | `CONVERSATION_MSG_ID` | VARCHAR |  | The record for the message that was also filed as a note. The text filed in the message and the quicknote will be the same and displaying one of these to the end user should be sufficient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

