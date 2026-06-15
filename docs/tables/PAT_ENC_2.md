# PAT_ENC_2

> This table supplements the PAT_ENC table. It contains additional information related to patient encounters or appointments.

**Overflow of:** [PAT_ENC](PAT_ENC.md)  
**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 77  
**Org-specific columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK | The unique system identifier of the patient encounter. Contact serial number is unique across all patients and all contacts. |
| 2 | `CONTACT_DATE` | DATETIME |  | The date on which this patient encounter took place. |
| 3 | `COPAY_COINS_FLAG` | VARCHAR |  | Set to 1 if copay is coinsurance. |
| 4 | `CAN_LET_C_NAME` | NUMERIC | org | This column links to the type of canceled appointment letter sent for this patient encounter. Some examples are "No Letter", "No Show","Cancelation Letter", etc. This category column is linked to ZC_LET.LET_C. |
| 5 | `SUP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `SUP_PROV_C_NAME` | VARCHAR | org | This column links to information about the Type of Supervising provider. |
| 7 | `SUP_PROV_REV_TM` | DATETIME (Local) |  | This column contains the date and time when the supervising provider submitted his or her review |
| 8 | `MEDS_REQUEST_PHR_ID` | NUMERIC |  | The pharmacy identifier from which the medications were requested. |
| 9 | `MEDS_REQUEST_PHR_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 10 | `MEDS_REQUEST_OP_C_NAME` | VARCHAR |  | This column contains information about the fill option for the medication request. |
| 11 | `PHYS_BP` | VARCHAR |  | This contains the patient's blood pressure that was entered during the patient encounter. |
| 12 | `VITALS_TAKEN_TM` | DATETIME (Local) |  | Holds the time the vitals were taken |
| 13 | `PHYS_TEMP_SRC_C_NAME` | VARCHAR | org | The source of the patient's temperature measurement. |
| 14 | `PAT_PAIN_SCORE_C_NAME` | VARCHAR | org | This column indicates how much pain the patient was in via pain score. |
| 15 | `PAT_PAIN_LOC_C_NAME` | VARCHAR | org | This column contains information about which body part is experiencing discomfort. |
| 16 | `PAT_PAIN_EDU_YN` | VARCHAR |  | This column contains information as to whether pain education questions were asked. |
| 17 | `PAT_PAIN_CMT` | VARCHAR |  | This column contains comments that were entered pertaining to the patient's pain |
| 18 | `PAT_PAIN_SCALE_CAT` | VARCHAR |  | This item stores the pain scale category under which the pain score is collected. |
| 19 | `SMOKING_STATUS_C_NAME` | VARCHAR |  | This simply stores information about whether the patient smokes, is quitting, etc. |
| 20 | `PHYS_SPO2` | INTEGER |  | Contains the blood oxygen saturation value for this encounter. |
| 21 | `SYS_GEN_LOS_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 22 | `DOC_HX_SOURCE_C_NAME` | VARCHAR | org | Stores the source of entry for the history documentation. This category column is linked to ZC_HISTORY_SOURCE.HISTORY_SOURCE_C. |
| 23 | `APPT_LET_C_NAME` | NUMERIC |  | This column links to the type of appointment letter that was sent to this patient for this patient encounter. Some examples are "No Letter", "Appt Letter", etc. This category column is linked to ZC_LET.LET_C. |
| 24 | `PARENT_ENC_CSN_ID` | NUMERIC |  | This item is a link to an encounter's parent encounter through the parent's contact serial number. The contact serial number is the unique identifier for the encounter. |
| 25 | `SYNC_IP_DATA_C_NAME` | VARCHAR |  | This is a contact-specific flag to tell Chart Sync whether inpatient clinical data for this visit (such as medication administration or documentation flowsheet data) should be synchronized between deployments. A value of 1 (or Yes) means that inpatient clinical data has been, and will continue to be, synchronized for this visit. Note that this item can only be set for a contact whose type is (or was at some point) an inpatient admission. |
| 26 | `APPTMT_LET_INST` | DATETIME (Local) |  | If an appointment letter has been printed for this patient encounter, this column will list the date and time it was printed. If multiple letters were printed, we'll list the date and time of the most recent one. |
| 27 | `RESULT_LET_INST` | DATETIME (Local) |  | If a result letter has been printed for this patient encounter, this column will list the date and time it was printed. If multiple letters were printed, we'll list the date and time of the most recent one. |
| 28 | `RESCHED_LET_INST` | DATETIME (Local) |  | If a reschedule letter has been printed for this patient encounter, this column will list the date and time it was printed. If multiple letters were printed, we'll list the date and time of the most recent one. |
| 29 | `FOLLOW_LET_INST` | DATETIME (Local) |  | If a follow-up letter has been printed for this patient encounter, this column will list the date and time it was printed. If multiple letters were printed, we'll list the date and time of the most recent one. |
| 30 | `PHYS_PEAK_FLOW` | INTEGER |  | This column contains a measurement of the flow of air from the lungs: Peak Flow. If this column contains data, the measurement was taken during the associated encounter. |
| 31 | `ENC_SPEC_C_NAME` | VARCHAR | org | The encounter specialty item holds which of the encounter provider's specialties should be used for billing and reporting purposes for this encounter. |
| 32 | `LD_STATUS_YN` | VARCHAR |  | Flag to denote if the encounter is for a mother who will deliver |
| 33 | `ADT_PAT_CLASS_C_NAME` | VARCHAR | org | The category value corresponding to the Admission/Discharge/Transfer (ADT) patient classification for this patient contact. |
| 34 | `OTHER_BLOCK_ID` | NUMERIC |  | Stores "Other" Summary Blocks (non-IP, ED, OpTime) |
| 35 | `OTHER_BLOCK_TYPE_C_NAME` | VARCHAR |  | Indicates the specific type of the episode summary, whose ID is stored in I EPT 1970. |
| 36 | `BILL_NUM` | VARCHAR |  | Billing number, often used as an identifier in downstream systems. |
| 37 | `IP_DOC_CONTACT_CSN` | NUMERIC |  | For Hospital Outpatient Visit (HOV) encounters, this column stores the unique contact serial number for the patient contact which is used for clinical documentation. This can be set for appointment contacts if they are not converted to HOVs. |
| 38 | `TEMP_PT_HIS_C_NAME` | VARCHAR |  | This item shows the temporary patient history. |
| 39 | `PRIMARY_PROCONT_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 40 | `PRIMARY_TEAM_ID` | NUMERIC |  | The unique ID of the primary Provider Care Team for this patient encounter. |
| 41 | `PRIMARY_TEAM_ID_RECORD_NAME` | VARCHAR |  | The name of the record. |
| 42 | `MCIR_VACCINE_CODE_C_NAME` | VARCHAR | org | The patient's eligibility code for Michigan's vaccination registry. This item only applies for the state of Michigan. |
| 43 | `VISIT_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 44 | `NO_INTERP_RSN_C_NAME` | VARCHAR | org | This column holds the reason an interpreter is not needed for the visit (in the case of a patient who would normally require one). It is meant to be populated when the corresponding EPT 495-INTERPRETER NEEDED? value is "no". |
| 45 | `CVG_ADD_DT` | DATETIME |  | The add date returned in the response message by the payor for the encounter. The add date is defined as the date that the payor added the patient as being covered. |
| 46 | `FARM_WORKER_C_NAME` | VARCHAR | org | The category number of the patient's farm worker status for the encounter or appointment. |
| 47 | `KIOSK_HH_QUEST_ID` | VARCHAR |  | The unique ID of the health history template that is assigned to the patient encounter. |
| 48 | `KIOSK_HH_QUEST_ID_RECORD_NAME` | VARCHAR |  | The name of the Visit Navigator (VN) History Template Definition (LQH) record. |
| 49 | `HSP_ACCT_ADV_DTTM` | DATETIME (Local) |  | If the Hospital Account Advisor is turned on, this item records the date and time that the advisor's recommendation was accepted or rejected. |
| 50 | `VISIT_VERIFIED_YN` | VARCHAR |  | Indicates whether the visit is verified. |
| 51 | `VERIF_VISIT_DT` | DATETIME |  | The current date the visit contact was verified. |
| 52 | `VERIF_DATE_INIT_DT` | DATETIME |  | The initial date the visit contact was verified. |
| 53 | `VERIF_USER_ID` | VARCHAR |  | This collects the user ID of the user who verified the visit. |
| 54 | `ENC_LACT_STAT_C_NAME` | VARCHAR |  | The lactation status category ID for the patient. |
| 55 | `PAT_LACT_CMNT` | VARCHAR |  | The comments entered when the patient's lactation status has been edited. |
| 56 | `COSIGNER_USER_ID` | VARCHAR |  | The unique ID of the user who cosigned the patient's chart. |
| 57 | `COSIGNER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 58 | `COSIGN_REV_INS_DTTM` | DATETIME (Local) |  | The date and time the chart was cosigned. |
| 59 | `PAR_DICT_COUNTER` | INTEGER |  | The counter for partial dictation. |
| 60 | `IS_LOS_UPDATE_C_NAME` | VARCHAR |  | Stores the status of any Level of Service updates. |
| 61 | `FORM_ID_COUNTER` | INTEGER |  | Stores the counter of form IDs. |
| 62 | `CONSNT_REV_USER_ID` | VARCHAR |  | The unique ID of the user who reviewed patient consent. |
| 63 | `CONSNT_REV_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 64 | `VISIT_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 65 | `VISIT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 66 | `SOCIO_SRC_C_NAME` | VARCHAR |  | Stores the source of entry for the sociological history. |
| 67 | `TEL_ENC_MSG_RGRDING` | VARCHAR |  | Free-text field containing user entered information regarding a telephone encounter message. |
| 68 | `MSG_PRIORITY_C_NAME` | VARCHAR |  | Indicates the priority of the routed message. |
| 69 | `RESEARCH_ENC_FLG_C_NAME` | VARCHAR | org | Category ID of the research encounter flag used to mark the patient encounter as having all charges billed to a research study, the patient, or a mixture. This is used for charge routing. |
| 70 | `FAM_SPOUSE_NAME` | VARCHAR |  | The name of the patient's spouse |
| 71 | `MSG_CALLER_NAME` | VARCHAR |  | The name of the caller who left this message |
| 72 | `CONSENT_EXP_DATE` | DATETIME |  | This is the expiration date of any consent forms that are attached to the patient. |
| 73 | `CV_ACC4_PAT_RESP_YN` | VARCHAR |  | Indicates whether a patient wants identifying information to be excluded from submission to the American College of Cardiology-National Cardiovascular Data Registry's (ACC-NCDR) Catheterization and/or Percutaneous Coronary Intervention (CathPCI) registry. |
| 74 | `FAMILY_MEM_PREFIX_C_NAME` | VARCHAR | org | This column stores the relationship between the patient and the patient's guarantor. |
| 75 | `AVS_REFUSED_DTTM` | DATETIME (UTC) |  | The date and time when an end user documented that the patient declined the After Visit Summary. |
| 76 | `AVS_LAST_PRINT_DTTM` | DATETIME (UTC) |  | Records the instant the After Visit Summary was last printed |
| 77 | `MED_LIST_UPDATE_DTTM` | DATETIME (UTC) |  | If a patient's prescriptions or Facility-Administered Medications (FAMs) are updated (signed, modified, or discontinued; or other med reconciliation actions are changed) after the After Visit Summary (AVS) has been printed, this item is updated to hold a timestamp indicating the last time that such updates were made. It is left blank if no AVS has been printed yet. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [PAT_ENC](PAT_ENC.md).

