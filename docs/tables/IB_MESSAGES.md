# IB_MESSAGES

> The IB_MESSAGES table contains basic information about In Basket messages.

**Overflow family:** [IB_MESSAGES_2](IB_MESSAGES_2.md), [IB_MESSAGES_3](IB_MESSAGES_3.md), [IB_MESSAGES_4](IB_MESSAGES_4.md), [IB_MESSAGES_5](IB_MESSAGES_5.md)  
**Primary key:** `MSG_ID`  
**Columns:** 55  
**Org-specific columns:** 3  
**Joined by:** 32 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MSG_ID` | VARCHAR | PK | The unique ID of the In Basket Message. |
| 2 | `CREATE_TIME` | DATETIME (Local) |  | The time the message record was created. |
| 3 | `REGARDING_TOPIC` | VARCHAR |  | A short description of the message contents. |
| 4 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 5 | `PAT_ENC_DATE_REAL` | FLOAT |  | The encounter date of the patient associated with this message. |
| 6 | `SENDER_USER_ID` | VARCHAR |  | The unique ID of the sender (networked to the User master file). |
| 7 | `SENDER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `NAME_OF_CALLER` | VARCHAR |  | The name of the caller. |
| 9 | `TRANSCRIPTION_LINE` | VARCHAR |  | This is the ID of the dictation transcription for a transcription created outside of Epic and sent to In Basket through an interface. It is networked to the Notes (HNO) master file. |
| 10 | `ORDER_PROC_ID` | NUMERIC | FK→ | The unique ID of the order procedure (networked to the Orders master file). |
| 11 | `ORDER_MED_ID` | NUMERIC | FK→ | The unique ID of the order procedure (networked to the Orders master file). |
| 12 | `ORD_DATE_REAL` | FLOAT |  | The internal date of the ordered procedure. |
| 13 | `PAT_EMAIL_RESP_YN` | VARCHAR |  | Indicates if the patient wants an e-mail response to their In Basket message. Y indicates that the patient does want an e-mail response and N indicates that the patient does not want an e-mail response. |
| 14 | `APPT_STATUS_C` | INTEGER |  | Appointment Notification Email Message Type - The Appointment Status of the specific encounter |
| 15 | `CANCEL_REASON_C` | INTEGER |  | Appointment Notification Email Message Type - If the APPT_STATUS_C column is canceled, this column contains the link to the reason for cancellation |
| 16 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. This column should be replaced with IB_MESSAGE_PAT_ENCS.PAT_ENC_CSN_ID instead. Historical records will still have this data populated, as well as data moving forward, but it may not contain all of the encounter contact serial numbers (CSNs) as the new column and table would |
| 17 | `PAT_ORDENC_DT_REAL` | FLOAT |  | The new orders only encounter associated with this message. This will be used if a reflex action is performed on a result and the original contact is owned elsewhere. |
| 18 | `DICT_HNO_ID` | VARCHAR |  | This is the ID of the dictation transcription for a dictation transcribed in Epic (not in a third party system). It is networked to the notes (HNO) master file. |
| 19 | `TASK_ID_ID` | VARCHAR |  | Stores the task ID this message is associated with |
| 20 | `REFERRAL_ID` | NUMERIC | FK→ | Stores referral record that is related to the In Basket message |
| 21 | `CLAIM_ID` | NUMERIC | FK→ | Stores claim record that is related to the In Basket message |
| 22 | `ORGANIZATION_ID` | NUMERIC | FK→ | Stores the Care Everywhere organization related to this message |
| 23 | `ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 24 | `QUERY_OUTCOME_C_NAME` | VARCHAR |  | Outcome of the Care Everywhere search. |
| 25 | `QUERY_INSTANT` | DATETIME (Attached) |  | Instant the query was performed |
| 26 | `QUERY_USER_NAME` | VARCHAR |  | User who performed the query |
| 27 | `QUERY_ENC` | VARCHAR |  | Encounter associated with the query |
| 28 | `QUERY_ENC_PROV` | VARCHAR |  | Provider for the encounter associated with the query |
| 29 | `QUERY_DEPT` | VARCHAR |  | Login department for the user performing the query |
| 30 | `QUERY_REASON_C_NAME` | VARCHAR |  | Reason for performing the query |
| 31 | `QUERY_PAT_NAME` | VARCHAR |  | Patient name used for the query |
| 32 | `QUERY_PAT_STATE` | VARCHAR |  | State used for the patient query |
| 33 | `QUERY_PAT_ZIP` | VARCHAR |  | Zip code used for the patient query |
| 34 | `QUERY_PAT_SEX_C_NAME` | VARCHAR | org | Sex used during the patient query |
| 35 | `QUERY_PAT_DOB_DT` | DATETIME |  | Date of birth used for the patient query |
| 36 | `QUERY_PAT_SSN` | VARCHAR |  | SSN used for the patient query |
| 37 | `QUERY_PAT_HOME_PH` | VARCHAR |  | Home phone number used for the patient query |
| 38 | `QUERY_PAT_WORK_PH` | VARCHAR |  | Work phone number used during the patient query |
| 39 | `QUERY_PAT_CELL_PH` | VARCHAR |  | Cell phone number used during the patient query |
| 40 | `MYCHART_HNO_ID` | VARCHAR |  | Note ID for a message that is a result of a 3rd party questionnaire being submitted. |
| 41 | `PEF_MSG_TYP_C_NAME` | VARCHAR |  | Type of a patient-entered flowsheet message, either Alert or Notification. |
| 42 | `PEF_EPISODE_ID` | NUMERIC |  | For patient-entered flowsheet messages, the episode ID that the flowsheet is a part of. |
| 43 | `PEF_LAST_NOTIF_DAT` | DATETIME |  | Last notification date of a patient-entered flowsheet message. |
| 44 | `PEF_INSTANT_SVD_TM` | DATETIME (Local) |  | For patient-entered flowsheet messages, the date and time the patient entered the data that triggered this message. |
| 45 | `NCS_ID` | NUMERIC |  | This column extracts the linked Customer Relationship Management record (NCS master file). |
| 46 | `DENTAL_TRT_PLAN_ID` | VARCHAR |  | Stores dental treatment plan ID. |
| 47 | `DTP_PMT_PLAN_LINE` | INTEGER |  | Stores orthodontic payment plan line. |
| 48 | `DEFICIENCY_TYPE_C_NAME` | VARCHAR | org | The deficiency type category number for the In Basket message. |
| 49 | `TRANSCRIPT_NOTE_ID` | VARCHAR |  | The unique ID of the note that this In Basket deficiency creation error occurred for. |
| 50 | `LAB_RESULT_ID` | VARCHAR |  | The unique ID of the result record of the In Basket message. |
| 51 | `LAB_HOLD_LN` | INTEGER |  | The line number of the hold of the specimen associated with this In Basket message. |
| 52 | `LAB_REQ_ID` | NUMERIC |  | Stores a pointer to a requisition record (REQ). The REQ record may be a requisition, a case, or both. |
| 53 | `LAB_AP_CASE_NUM` | VARCHAR |  | The case number is the Anatomic Pathology accession number. |
| 54 | `AN_MSG_REASON_C_NAME` | VARCHAR | org | The reason the message was sent from Anesthesia. |
| 55 | `FREE_TEXT_SIG` | VARCHAR |  | Free text sig received from a pharmacy interface. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |
| `ORGANIZATION_ID` | [ORG_DETAILS](ORG_DETAILS.md) | sole_pk | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

## Joined in — referenced by (32)

| From | Column | Confidence |
|------|--------|------------|
| [ACIB_MISC_HD_INF](ACIB_MISC_HD_INF.md) | `MSG_ID` | high |
| [AI_INTRCT_INFO](AI_INTRCT_INFO.md) | `MSG_ID` | high |
| [CE_IB_RELATED_NOTES](CE_IB_RELATED_NOTES.md) | `MSG_ID` | high |
| [DP_COMM_EOW_RM](DP_COMM_EOW_RM.md) | `MSG_ID` | high |
| [EOW_ALLERGY_LIST](EOW_ALLERGY_LIST.md) | `MSG_ID` | high |
| [EOW_APPOINTMENT_REQUESTS](EOW_APPOINTMENT_REQUESTS.md) | `MSG_ID` | high |
| [EOW_CALL_ENC_NOTES](EOW_CALL_ENC_NOTES.md) | `MSG_ID` | high |
| [EOW_LINKED_PATS](EOW_LINKED_PATS.md) | `MSG_ID` | high |
| [EOW_LINKED_RQGS](EOW_LINKED_RQGS.md) | `MSG_ID` | high |
| [EOW_MED_ALG_INT](EOW_MED_ALG_INT.md) | `MSG_ID` | high |
| [HH_VO_IB_LINK](HH_VO_IB_LINK.md) | `MSG_ID` | high |
| [IB_APPTS](IB_APPTS.md) | `MSG_ID` | high |
| [IB_CALL_ACTION](IB_CALL_ACTION.md) | `MSG_ID` | high |
| [IB_CASES_LINKED](IB_CASES_LINKED.md) | `MSG_ID` | high |
| [IB_LAB_SPECIMEN_ID](IB_LAB_SPECIMEN_ID.md) | `MSG_ID` | high |
| [IB_LAB_TEST](IB_LAB_TEST.md) | `MSG_ID` | high |
| [IB_MEDICATION_CONCERNS](IB_MEDICATION_CONCERNS.md) | `MSG_ID` | high |
| [IB_MED_CONCERNS_RECPNTS](IB_MED_CONCERNS_RECPNTS.md) | `MSG_ID` | high |
| [IB_MED_CONCERNS_SUPPORT](IB_MED_CONCERNS_SUPPORT.md) | `MSG_ID` | high |
| [IB_MESSAGES_CLAIM_LETTERS](IB_MESSAGES_CLAIM_LETTERS.md) | `MSG_ID` | high |
| [IB_MESSAGE_PAT_ENC](IB_MESSAGE_PAT_ENC.md) | `MSG_ID` | high |
| [IB_MSG_COMMENTS](IB_MSG_COMMENTS.md) | `MSG_ID` | high |
| [IB_MSG_IMG_FINDINGS](IB_MSG_IMG_FINDINGS.md) | `MSG_ID` | high |
| [IB_NOTES](IB_NOTES.md) | `MSG_ID` | high |
| [IB_OVERDUE_MSG_ID](IB_OVERDUE_MSG_ID.md) | `MSG_ID` | high |
| [IB_PHRM_ORDER_ID](IB_PHRM_ORDER_ID.md) | `MSG_ID` | high |
| [IB_RSH_ASSOC_MSG](IB_RSH_ASSOC_MSG.md) | `MSG_ID` | high |
| [IB_RSH_MSG](IB_RSH_MSG.md) | `MSG_ID` | high |
| [IB_RTF_NOTES](IB_RTF_NOTES.md) | `MSG_ID` | high |
| [PAGE_DETAILS](PAGE_DETAILS.md) | `MSG_ID` | high |
| [PAT_CONTACT_LIST](PAT_CONTACT_LIST.md) | `MSG_ID` | high |
| [PROC_ALRGY_INTRCT_MSG](PROC_ALRGY_INTRCT_MSG.md) | `MSG_ID` | high |

