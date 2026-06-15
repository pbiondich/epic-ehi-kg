# PATIENT_3

> This table supplements the information contained in the PATIENT table. It contains basic information about patients, such as the patient's ID, occupation, English fluency, etc.

**Overflow of:** [PATIENT](PATIENT.md)  
**Primary key:** `PAT_ID`  
**Columns:** 64  
**Org-specific columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LACT_STAT_CUR_C_NAME` | VARCHAR |  | The category number for the patient's current lactation status. |
| 3 | `LACT_STAT_INST_DTTM` | DATETIME (UTC) |  | The instant when the patient's lactation status was updated. |
| 4 | `LACT_STAT_CSN` | NUMERIC |  | The contact serial number of the encounter in which the lactation status updated. The contact serial number is the unique identifier for the encounter. |
| 5 | `LACT_STAT_USER_ID` | VARCHAR |  | The unique ID of the user who last updated the patient's lactation status. |
| 6 | `LACT_STAT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `AMBULATORY_STATUS_C_NAME` | VARCHAR | org | Information regarding a patient's ambulatory status. |
| 8 | `OCCUPATION` | VARCHAR |  | A patient's occupation. |
| 9 | `ADVANCED_DIR_YN` | VARCHAR |  | Indicates whether the patient has any advanced directives. |
| 10 | `ABST_DT` | DATETIME |  | The date of abstraction of the patient record. |
| 11 | `ALRGY_REV_REAS_C_NAME` | VARCHAR | org | Reason for the review status of allergy assessment. |
| 12 | `ALLOW_HALF_PILLS_YN` | VARCHAR |  | Indicates whether the patient uses half pills |
| 13 | `ALRG_LAST_UPDA_DTTM` | DATETIME (Local) |  | The latest instant in which allergies were updated. |
| 14 | `PED_BIRTH_LEN_NUM` | NUMERIC |  | Newborn birth length stored in inches. |
| 15 | `PED_BIRTH_WT_NUM` | NUMERIC |  | Newborn birth weight stored in ounces. |
| 16 | `PED_DISCHRG_WGT_NUM` | NUMERIC |  | Newborn discharge weight stored in ounces. |
| 17 | `PED_APGAR_ONE_C_NAME` | VARCHAR | org | Newborn 1 minute Apgar. |
| 18 | `PED_APGAR_FIVE_C_NAME` | VARCHAR |  | Newborn 5 minute Apgar. |
| 19 | `PED_APGAR_TEN_C_NAME` | VARCHAR |  | Newborn 10 minute Apgar. |
| 20 | `UNOS_PRIM_COD_C_NAME` | VARCHAR | org | The transplant patient's primary cause of death, as defined by UNOS (United Network for Organ Sharing). |
| 21 | `UNOS_PRIM_COD_SP` | VARCHAR |  | Free text description of the transplant patient's primary cause of death. |
| 22 | `UNOS_CTRB_COD1_C_NAME` | VARCHAR |  | The transplant patient's first contributory cause of death, as defined by UNOS (United Network for Organ Sharing). |
| 23 | `UNOS_CNTB_COD1_SP` | VARCHAR |  | Free text description of the transplant patient's first contributory cause of death. |
| 24 | `UNOS_CTRB_COD2_C_NAME` | VARCHAR |  | The transplant patient's second contributory cause of death, as defined by UNOS (United Network for Organ Sharing). |
| 25 | `UNOS_CNTB_COD2_SP` | VARCHAR |  | Free text description of the transplant patient's second contributory cause of death. |
| 26 | `PREFERRED_NAME` | VARCHAR |  | The preferred name for the patient. |
| 27 | `LAST_VERIFIED_BY_ID` | VARCHAR |  | The last user who verified the patient. |
| 28 | `LAST_VERIFIED_BY_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 29 | `LEARN_ASSMT_ID` | NUMERIC |  | Learning assessment ID. This can be used to check that the learning assessments are being given to the appropriate patients at the appropriate times. |
| 30 | `CURR_LOC_ID` | NUMERIC |  | The unique ID of the most recent confirmed patient location that is associated with the patient. |
| 31 | `PCOD_CAUSE_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 32 | `PCOD_REC_USER_ID` | VARCHAR |  | Stores the user that filed the preliminary cause of death |
| 33 | `PCOD_REC_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 34 | `PCOD_INST_REC_DTTM` | DATETIME (UTC) |  | Stores the instant that the preliminary cause of death was recorded |
| 35 | `EMPL_ID_NUM` | VARCHAR |  | The patient's employee identification number. |
| 36 | `SCHOOL_PHONE` | VARCHAR |  | The patient's school phone number. |
| 37 | `CONTRACT_ID_CONTRACT_NAME` | VARCHAR |  | The name of the pricing contract. |
| 38 | `SPOT_UPD_USER_ID` | VARCHAR |  | This item saves the user ID of the person who most recently updated the patient's Spotlight folder in the Synopsis activity by adding a row that previously had not been tracked by any other user. |
| 39 | `SPOT_UPD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 40 | `GYN_HX_CMT_NOTE_ID` | VARCHAR |  | ID of HNO (note) record for free-text gynecological information |
| 41 | `GYN_HX_MENARCHE_AGE` | INTEGER |  | The patient's age at menarche |
| 42 | `GYN_HX_FST_PREG_AGE` | INTEGER |  | The patient's age at first pregnancy |
| 43 | `GYN_HX_MO_BRSTFDG` | INTEGER |  | The number of months the patient spent breastfeeding |
| 44 | `GYN_HX_MENOPAUS_AGE` | INTEGER |  | The patient's age at menopause |
| 45 | `FAMILY_GROUPER` | VARCHAR |  | A family identifier that may be used to group family members together. Note that this is not guaranteed to be unique across deployments in IntraConnect. |
| 46 | `FETUS_YN` | VARCHAR |  | Indicates whether this row is a fetus record or a patient record. YES indicates that the row is a fetus record. NO indicates that the row is a patient record. |
| 47 | `DENT_CLASS_C_NAME` | VARCHAR |  | This item identifies the dental classification of the patient. |
| 48 | `DENT_LAST_USER_ID` | VARCHAR |  | This item stores the last user who edited the dental classification of the patient. |
| 49 | `DENT_LAST_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 50 | `DENT_INST_DTTM` | DATETIME (Local) |  | This item stores the instant when the dental classification of the patient was last edited. |
| 51 | `ENGLISH_FLUENCY_C_NAME` | VARCHAR | org | Record the patient's fluency in English. |
| 52 | `FORM_CONFIDENCE_C_NAME` | VARCHAR | org | Record the patient's confidence level in filling out medical forms. |
| 53 | `BRANCH_OF_SERVICE_C_NAME` | VARCHAR | org | This column stores the branch of service in which the patient serves. |
| 54 | `MILITARY_RANK_C_NAME` | VARCHAR | org | This column stores the patient's military rank. |
| 55 | `FMP_C_NAME` | VARCHAR | org | This column stores the relationship between the patient and the patient's sponsor. |
| 56 | `PAT_CAT_C_NAME` | VARCHAR | org | This column, patient category, combines the branch of service and eligibility type into a three-character code, such as A14. This code affects billing and other downstream systems. |
| 57 | `MIL_COMPONENT_C_NAME` | VARCHAR | org | This column stores the patient's military component, which is used to distinguish between patients who are on regular active duty and those who are members of one of the augmenting support groups. |
| 58 | `ASGN_MIL_UNIT_ID` | NUMERIC |  | This column stores the military unit ID to which the patient is assigned. |
| 59 | `ASGN_MIL_UNIT_ID_RECORD_NAME` | VARCHAR |  | This column stores the name of the military unit's record. |
| 60 | `MIL_PAY_GRADE_C_NAME` | VARCHAR | org | This column stores the patient's military pay grade. |
| 61 | `TEMP_MIL_UNIT_ID` | NUMERIC |  | This column stores the patient's temporary military unit ID. |
| 62 | `TEMP_MIL_UNIT_ID_RECORD_NAME` | VARCHAR |  | This column stores the name of the military unit's record. |
| 63 | `PED_GEST_AGE_DAYS` | INTEGER |  | Newborn gestational age at birth in total number of days |
| 64 | `PED_BIRTH_HD_CIRCUM` | NUMERIC |  | Newborn birth head circumference stored in inches. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [PATIENT](PATIENT.md).

