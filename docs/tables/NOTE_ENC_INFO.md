# NOTE_ENC_INFO

> This table contains information from overtime single-response items about General Use Notes (HNO) records. Contact creation logic for clinical notes is as follows: 1. If a note doesn't exist, a new note is created. This represents the first contact on that note. 2. If a revision is filed by the incoming transcription interface, a new contact is created on the note being revised regardless of note status.

**Overflow family:** [NOTE_ENC_INFO_2](NOTE_ENC_INFO_2.md)  
**Primary key:** `CONTACT_SERIAL_NUM`  
**Columns:** 70  
**Org-specific columns:** 12  
**Joined by:** 49 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | shared | The unique identifier for the note record. |
| 2 | `CONTACT_SERIAL_NUM` | NUMERIC | PK shared | The contact serial number (CSN) of the contact. |
| 3 | `CONTACT_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `COSIGN_INSTANT_DTTM` | DATETIME (UTC) |  | The instant when the note was cosigned. |
| 5 | `COSIGNUSER_ID` | VARCHAR |  | The user who cosigned the note. |
| 6 | `COSIGNUSER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `COSIGN_NOTE_LINK` | NUMERIC |  | A note contact serial number (CSN) that points to the attending's note that cosigned this one. |
| 8 | `COSIGN_REQUIRED_C_NAME` | VARCHAR | org | The cosign requirement for the current note contact. |
| 9 | `AUTH_LNKED_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 10 | `AUTHOR_SERVICE_C_NAME` | VARCHAR | org | The author's clinical service. |
| 11 | `ENTRY_INSTANT_DTTM` | DATETIME (UTC) |  | UTC formatted instant of entry for a note. |
| 12 | `UPD_AUTHOR_INS_DTTM` | DATETIME (UTC) |  | UTC instant of update by a specific user. |
| 13 | `SPEC_NOTE_TIME_DTTM` | DATETIME (UTC) |  | The note's specified date paired with the specified time. |
| 14 | `NOTE_FILE_TIME_DTTM` | DATETIME (UTC) |  | UTC formatted instant of when a note is filed. |
| 15 | `AUTHOR_PRVD_TYPE_C_NAME` | VARCHAR | org | Author's provider type on a specific contact. |
| 16 | `NOTE_STATUS_C_NAME` | VARCHAR | org | The status of the note. |
| 17 | `UPDATE_USER_ID` | VARCHAR |  | The id of the user who updated this contact of the note. |
| 18 | `UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 19 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 20 | `TRN_DOC_AVAIL_STA_C_NAME` | VARCHAR | org | The availability status of the transcription. |
| 21 | `TRN_DOC_TYPE_C_NAME` | VARCHAR | org | The document type of the transcription. |
| 22 | `SENSITIVE_STAT_C_NAME` | VARCHAR | org | Sensitive status of a note. |
| 23 | `AUTHOR_USER_ID` | VARCHAR |  | The unique ID associated with the user who is the author of the note. |
| 24 | `AUTHOR_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 25 | `NOTE_FORMAT_C_NAME` | VARCHAR | org | The format of the note text like Plain Text, Rich Text, HTML etc. |
| 26 | `UPD_BY_AUTH_DTTM` | DATETIME (Local) |  | The instant when the note is updated by the author. |
| 27 | `ACTIVITY_DTTM` | DATETIME (Local) |  | The activity date and time of the partial dictation/transcription. |
| 28 | `AUTH_STAT_C_NAME` | VARCHAR | org | The authentication status category number for this activity if this note is a transcription. This is also known as the completion status. |
| 29 | `CONTACT_NUM` | VARCHAR |  | Contact number for the record. |
| 30 | `UPD_AUT_LOCAL_DTTM` | DATETIME (Local) |  | Update by author instant in local format. |
| 31 | `ENT_INST_LOCAL_DTTM` | DATETIME (Local) |  | Note entry instant in local format. |
| 32 | `SPEC_TIME_LOC_DTTM` | DATETIME (Local) |  | Note specified instant in local format. |
| 33 | `NOT_FILETM_LOC_DTTM` | DATETIME (Local) |  | Note file time in local format. |
| 34 | `EDIT_USER_ID` | VARCHAR |  | The unique ID associated with the user record who edited the note for this particular contact. This is populated for notes with note type 76-Simple Med Note, 77-Medication History, etc. This column is frequently used to link to the CLARITY_EMP table. |
| 35 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 36 | `DOCUMENT_NAME` | VARCHAR |  | Contains the name of the multi-part document. |
| 37 | `UMRG_SRC_MEDPROB_ID` | NUMERIC |  | The unique ID of the Med Problem List record. |
| 38 | `ECG_COMMENTS` | VARCHAR |  | Comments about the Electrocardiogram (ECG/EKG). |
| 39 | `ECG_EDITED_USER_ID` | VARCHAR |  | The person who edited the Electrocardiogram (ECG/EKG). |
| 40 | `ECG_DIASTOLIC_BP` | VARCHAR |  | The diastolic blood pressure taken from the Electrocardiogram (ECG/EKG). |
| 41 | `ECG_SYSTOLIC_BP` | VARCHAR |  | The systolic blood pressure taken from the Electrocardiogram (ECG/EKG). |
| 42 | `ECG_HEARTRATE` | VARCHAR |  | The heartrate from the Electrocardiogram (ECG/EKG). |
| 43 | `ECG_PR_INTERVAL` | VARCHAR |  | The interval from the beginning of the P wave to the beginning of the QRS wave on the Electrocardiogram (ECG/EKG). |
| 44 | `ECG_PWAVEAXIS` | VARCHAR |  | The P wave axis on the Electrocardiogram (ECG/EKG). |
| 45 | `ECG_QRS_DURATION` | VARCHAR |  | The duration of the QRS complex/wave on the Electrocardiogram (ECG/EKG). |
| 46 | `ECG_QRS_WAVEAXIS` | VARCHAR |  | The QRS complex/wave axis on the Electrocardiogram (ECG/EKG). |
| 47 | `ECG_QT_INTERVAL` | VARCHAR |  | The interval from the start of the QRS complex/wave to the end of the T wave on the Electrocardiogram (ECG/EKG). |
| 48 | `ECG_QTC_INTERVAL` | VARCHAR |  | The corrected QT interval for the Electrocardiogram (ECG/EKG). |
| 49 | `ECG_T_WAVEAXIS` | VARCHAR |  | The T wave axis for the Electrocardiogram (ECG/EKG). |
| 50 | `SPIRO_BRON` | VARCHAR |  | Stores the type of bronchodilator given to the patient (ex: Albuterol). |
| 51 | `CARE_PLAN_CSN_ID` | NUMERIC |  | Link to care plan contact. Used to recreate historic versions of care plan. |
| 52 | `PROGRESS_NOTE_ID` | VARCHAR |  | Progress note ID for the careplan goal note. |
| 53 | `TRANSCRIPTION_DTTM` | DATETIME (Local) |  | The transcription date and time. |
| 54 | `CSGN_RECPNT_USER_ID` | VARCHAR |  | The unique ID associated with the user who is supposed to cosign the note. |
| 55 | `CSGN_RECPNT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 56 | `TREAT_SUMM_PAT_DTTM` | DATETIME (UTC) |  | This column stores the UTC instant that a treatment summary note is given to the patient. |
| 57 | `TREAT_SUMM_PROV_DTTM` | DATETIME (UTC) |  | This column stores the UTC instant that a treatment summary note is given to the follow-up provider. |
| 58 | `TREAT_SUMM_CPLT_DTTM` | DATETIME (UTC) |  | This column saves the UTC instant that a treatment summary note is marked as complete. |
| 59 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | This column stores the patient encounter contact serial number (CSN) in which the note was edited. Used for persistent notes to determine in which encounter the note was edited. |
| 60 | `END_OF_TREAT_DATE` | DATETIME |  | This column saves the end of treatment date for a treatment summary. |
| 61 | `UNMERGE_SRC_NOTE_ID` | VARCHAR |  | The source note ID before patient merge. |
| 62 | `NOTE_SHARED_W_PAT_HX_YN` | VARCHAR |  | Was this note contact marked as eligible for sharing with the patient when it was last saved? Notes will only be displayed in MyChart if their most recent contact is marked for sharing. If you want to determine if a note is currently shared, use the NOTE_SHARED_W_PAT_YN column in the HNO_INFO table instead of this one. |
| 63 | `NOTE_TYPE_C_NAME` | VARCHAR | org | Identifies what type of note this record is. |
| 64 | `POC_NOTE_DISC_C_NAME` | VARCHAR | org | This item stores the hospice Plan of Care note discipline. |
| 65 | `COSIGN_INST_LOCAL_DTTM` | DATETIME (Local) |  | The instant in local time when the note was cosigned. |
| 66 | `IS_PRECHARTED_YN` | VARCHAR |  | This indicates whether or not the note is currently a pre-charted note (in appointment encounter). |
| 67 | `LINK_DXR_CSN_ID` | NUMERIC |  | Link to the DXR contact that holds the NoteReader data for this note's contact. |
| 68 | `CLINICAL_NOTE_SUMMARY` | VARCHAR |  | This item stores a plain text summary of the note contents. |
| 69 | `BLOCK_REASON_C_NAME` | VARCHAR | org | Stores a discrete reason why a note was blocked from the patient. |
| 70 | `BLOCK_REASON_TXT` | VARCHAR |  | Stores a free text comment with additional information about why a note was blocked from the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

## Joined in — referenced by (49)

| From | Column | Confidence |
|------|--------|------------|
| [ABN_FOLLOW_UP](ABN_FOLLOW_UP.md) | `NOTE_CSN_ID` | medium |
| [ABN_NOTE_COMMENTS](ABN_NOTE_COMMENTS.md) | `NOTE_CSN_ID` | medium |
| [BLOCK_NOTE_COPIES](BLOCK_NOTE_COPIES.md) | `NOTE_CSN_ID` | medium |
| [CP_NOTE_READING_HX](CP_NOTE_READING_HX.md) | `NOTE_CSN_ID` | medium |
| [CUST_SERV_LETTER_DOC_PART](CUST_SERV_LETTER_DOC_PART.md) | `NOTE_CSN_ID` | medium |
| [CUST_SERV_LETTER_RTF](CUST_SERV_LETTER_RTF.md) | `NOTE_CSN_ID` | medium |
| [CUST_SERV_LETTER_RTF_P2](CUST_SERV_LETTER_RTF_P2.md) | `NOTE_CSN_ID` | medium |
| [CUST_SERV_LETTER_RTF_P3](CUST_SERV_LETTER_RTF_P3.md) | `NOTE_CSN_ID` | medium |
| [CUST_SERV_LETTER_RTF_P4](CUST_SERV_LETTER_RTF_P4.md) | `NOTE_CSN_ID` | medium |
| [CUST_SERV_LETTER_RTF_P5](CUST_SERV_LETTER_RTF_P5.md) | `NOTE_CSN_ID` | medium |
| [CUST_SERV_LETTER_TEXT](CUST_SERV_LETTER_TEXT.md) | `NOTE_CSN_ID` | medium |
| [CUST_SERV_LETTER_TEXT_P2](CUST_SERV_LETTER_TEXT_P2.md) | `NOTE_CSN_ID` | medium |
| [CUST_SERV_LETTER_TEXT_P3](CUST_SERV_LETTER_TEXT_P3.md) | `NOTE_CSN_ID` | medium |
| [CUST_SERV_LETTER_TEXT_P4](CUST_SERV_LETTER_TEXT_P4.md) | `NOTE_CSN_ID` | medium |
| [CUST_SERV_LETTER_TEXT_P5](CUST_SERV_LETTER_TEXT_P5.md) | `NOTE_CSN_ID` | medium |
| [ED_DISPO_AUDIT](ED_DISPO_AUDIT.md) | `NOTE_CSN_ID` | medium |
| [HNO_CONSULT_ORD_ID](HNO_CONSULT_ORD_ID.md) | `NOTE_CSN_ID` | medium |
| [HNO_ECG_DX](HNO_ECG_DX.md) | `NOTE_CSN_ID` | medium |
| [HNO_LET_DICTN](HNO_LET_DICTN.md) | `NOTE_CSN_ID` | medium |
| [HNO_PLAIN_TEXT](HNO_PLAIN_TEXT.md) | `NOTE_CSN_ID` | medium |
| [HNO_SMARTFORM_LINK](HNO_SMARTFORM_LINK.md) | `NOTE_CSN_ID` | medium |
| [HNO_SOURCE_LOG_ID](HNO_SOURCE_LOG_ID.md) | `NOTE_CSN_ID` | medium |
| [INTERV_NOTE_INFO](INTERV_NOTE_INFO.md) | `NOTE_CSN_ID` | medium |
| [LETTER_EDIT_INFO](LETTER_EDIT_INFO.md) | `NOTE_CSN_ID` | medium |
| [LETTER_PRINT_AUDIT](LETTER_PRINT_AUDIT.md) | `NOTE_CSN_ID` | medium |
| [MYC_PAT_NTE_AUD](MYC_PAT_NTE_AUD.md) | `NOTE_CSN_ID` | medium |
| [NOTES_HISTORY_LOG](NOTES_HISTORY_LOG.md) | `NOTE_CSN_ID` | medium |
| [NOTES_TRANS_AUTH](NOTES_TRANS_AUTH.md) | `NOTE_CSN_ID` | medium |
| [NOTES_TRANS_IB](NOTES_TRANS_IB.md) | `NOTE_CSN_ID` | medium |
| [NOTE_BLOCKING](NOTE_BLOCKING.md) | `NOTE_CSN_ID` | medium |
| [NOTE_CONTENT_INFO](NOTE_CONTENT_INFO.md) | `NOTE_CSN_ID` | medium |
| [NOTE_ENC_SUMMARY](NOTE_ENC_SUMMARY.md) | `NOTE_CSN_ID` | medium |
| [NOTE_EXT_REL_ORD](NOTE_EXT_REL_ORD.md) | `NOTE_CSN_ID` | medium |
| [NOTE_EXT_REL_PREDX](NOTE_EXT_REL_PREDX.md) | `NOTE_CSN_ID` | medium |
| [NOTE_EXT_REL_PROB](NOTE_EXT_REL_PROB.md) | `NOTE_CSN_ID` | medium |
| [NOTE_EXT_REL_PROC](NOTE_EXT_REL_PROC.md) | `NOTE_CSN_ID` | medium |
| [NOTE_EXT_REL_PSTDX](NOTE_EXT_REL_PSTDX.md) | `NOTE_CSN_ID` | medium |
| [NOTE_EXT_SIGNERS](NOTE_EXT_SIGNERS.md) | `NOTE_CSN_ID` | medium |
| [NOTE_EXT_WRN_TYP](NOTE_EXT_WRN_TYP.md) | `NOTE_CSN_ID` | medium |
| [NOTE_SMARTSECTION_IDS](NOTE_SMARTSECTION_IDS.md) | `NOTE_CSN_ID` | medium |
| [PART_DICT_MRG_HNO](PART_DICT_MRG_HNO.md) | `NOTE_CSN_ID` | medium |
| [SEP1_AUTOPOP_RE_ASMT](SEP1_AUTOPOP_RE_ASMT.md) | `NOTE_CSN_ID` | medium |
| [SEP1_AUTOPOP_SEPSIS_DOC](SEP1_AUTOPOP_SEPSIS_DOC.md) | `NOTE_CSN_ID` | medium |
| [SEP1_AUTOPOP_SEV_PAL](SEP1_AUTOPOP_SEV_PAL.md) | `NOTE_CSN_ID` | medium |
| [SEP1_AUTOPOP_SEV_REFUSE](SEP1_AUTOPOP_SEV_REFUSE.md) | `NOTE_CSN_ID` | medium |
| [SEP1_AUTOPOP_SHOCK_PAL](SEP1_AUTOPOP_SHOCK_PAL.md) | `NOTE_CSN_ID` | medium |
| [SEP1_AUTOPOP_SHOCK_REFUSE](SEP1_AUTOPOP_SHOCK_REFUSE.md) | `NOTE_CSN_ID` | medium |
| [SPIRO_INTRPRTATION](SPIRO_INTRPRTATION.md) | `NOTE_CSN_ID` | medium |
| [TX_ADDENDUM_NOTES](TX_ADDENDUM_NOTES.md) | `NOTE_CSN_ID` | medium |

