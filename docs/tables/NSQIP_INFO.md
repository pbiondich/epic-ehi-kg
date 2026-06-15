# NSQIP_INFO

> The NSQIP_INFO table contains NSQIP registry data for the surgeries that are selected for NSQIP submission.

**Overflow family:** [NSQIP_INFO_2](NSQIP_INFO_2.md)  
**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 101  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `REGISTRY_DATA_NAME` | VARCHAR |  | The registry record name. |
| 3 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The category ID for the record status (hidden, soft-deleted, etc...). |
| 4 | `REGISTRY_ID` | NUMERIC | shared | The unique ID of the registry associated with this RDI record. |
| 5 | `REGISTRY_ID_REGISTRY_NAME` | VARCHAR |  | The name of the registry record. |
| 6 | `REGISTRY_TYPE_C_NAME` | VARCHAR | org | The category ID for the type of registry. For this table the value will always be 20000 corresponding to ACS NSQIP. |
| 7 | `REG_OVRIDE_CONTEXT` | VARCHAR |  | The override context string to identify the correct override record for the registry settings record (HFR). |
| 8 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient associated with this registry record. |
| 9 | `PAT_DATE` | DATETIME |  | The date of patient encounter linked to the surgery. |
| 10 | `LOG_ID` | VARCHAR | shared | The unique ID of the surgery associated with this registry record. |
| 11 | `NSQIP_CYCLE_C_NAME` | VARCHAR |  | The category ID for the cycle number assigned to the case. A cycle number is assigned to every eight consecutive days in a calendar year. It is automatically generated based on the operation date. |
| 12 | `NSQIP_IDN` | VARCHAR |  | The unique identifier for the patient in the ACS NSQIP database. |
| 13 | `NSQIP_LMRN` | VARCHAR |  | The Medical Record Number (MRN) of the patient as assigned by the hospital. |
| 14 | `NSQIP_DOB_DT` | DATETIME |  | The patient's date of birth. |
| 15 | `NSQIP_GENDER_C_NAME` | VARCHAR |  | The category ID for the gender of the patient. |
| 16 | `NSQIP_RACE_C_NAME` | VARCHAR |  | The category ID for the race of the patient. Starting with the January 2021 specification updates, discrete race categories are now located in the column NSQIP_RACES.NSQIP_RACES_C. |
| 17 | `NSQIP_HISPANIC_C_NAME` | VARCHAR |  | Indicates whether the patient is of Hispanic or Latino ethnicity. |
| 18 | `NSQIP_NAME_FIRST` | VARCHAR |  | The patient's first name. |
| 19 | `NSQIP_NAME_MI` | VARCHAR |  | The patient's middle initial. |
| 20 | `NSQIP_NAME_LAST` | VARCHAR |  | The patient's last name. |
| 21 | `NSQIP_ADDRESS_LINE_1` | VARCHAR |  | Line 1 of the patient's address. |
| 22 | `NSQIP_ADDRESS_LINE_2` | VARCHAR |  | Line 2 of the patient's address. |
| 23 | `NSQIP_CITY` | VARCHAR |  | The patient's city. |
| 24 | `NSQIP_STATE_C_NAME` | VARCHAR |  | The category ID for the state of the patient. |
| 25 | `NSQIP_ZIP` | VARCHAR |  | The patient's ZIP code. |
| 26 | `NSQIP_COUNTRY_C_NAME` | VARCHAR |  | The category ID for the country of the patient. |
| 27 | `NSQIP_COUNTY` | VARCHAR |  | The patient's county. |
| 28 | `NSQIP_HOME_PHONE` | VARCHAR |  | The patient's home phone number. |
| 29 | `NSQIP_WORK_PHONE` | VARCHAR |  | The patient's work phone number. |
| 30 | `NSQIP_CELL_PHONE` | VARCHAR |  | The patient's cell phone number. |
| 31 | `NSQIP_PREF_LANG_C_NAME` | VARCHAR |  | The category ID for the preferred language of the patient. |
| 32 | `NSQIP_PRIN_PROC_PANEL` | VARCHAR |  | The panel number corresponding to the NSQIP principal operative procedure. It is used along with procedure ID from NSQIP_PRIN_PROC_ID to identify the row in OR_LOG_ALL_PROC table corresponding to the NSQIP principal operative procedure. |
| 33 | `NSQIP_PRIN_PROC_ID` | VARCHAR |  | The unique ID of the procedure record corresponding to the NSQIP principal operative procedure. It is used along with panel number from NSQIP_PRIN_PROC_PANEL to identify the row in OR_LOG_ALL_PROC table corresponding to the NSQIP principal operative procedure. |
| 34 | `NSQIP_PRIN_PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 35 | `NSQIP_PRIN_PROC_CPT` | VARCHAR |  | The CPT code of the principal NSQIP procedure. |
| 36 | `NSQIP_PRIN_PROC_NAME` | VARCHAR |  | The name of the principal operative procedure. |
| 37 | `NSQIP_ADMSN_STATUS_C_NAME` | VARCHAR |  | The category ID for the admission status of the case (inpatient or outpatient). |
| 38 | `NSQIP_ELECTIVE_C_NAME` | VARCHAR |  | Indicates whether the surgical case is considered an elective case. |
| 39 | `NSQIP_ORIGIN_C_NAME` | VARCHAR |  | The category ID for the origin status of the case. It indicates whether the patient was admitted from their home or from another type of facility. |
| 40 | `NSQIP_ADMSN_DT` | DATETIME |  | The date the patient was admitted to the hospital for the principal operative procedure. |
| 41 | `NSQIP_OPERATION_DT` | DATETIME |  | The date the patient entered the surgical suite for the principal operative procedure. |
| 42 | `NSQIP_PRIN_ANES_C_NAME` | VARCHAR |  | The category ID for the principal anesthesia type of the case. |
| 43 | `NSQIP_SPECIALTY_C_NAME` | VARCHAR |  | The category ID for the surgical specialty of the case. |
| 44 | `NSQIP_EMERG_CASE_YN` | VARCHAR |  | Indicates whether the surgical case is considered an emergency case. |
| 45 | `NSQIP_WOUND_CLASS_C_NAME` | VARCHAR |  | The category ID for the wound classification of the surgical wound at the time of principal operative procedure. |
| 46 | `NSQIP_WOUND_CLOSE_C_NAME` | VARCHAR |  | The category ID for the wound closure associated with the surgical wound at the time of principal operative procedure. |
| 47 | `NSQIP_ASA_CLASS_C_NAME` | VARCHAR |  | The category ID for the ASA class associated with the case. |
| 48 | `NSQIP_PROC_START_DTTM` | DATETIME (UTC) |  | The time the principal operative procedure began. |
| 49 | `NSQIP_PROC_FINISH_DTTM` | DATETIME (UTC) |  | The time the principal operative procedure was completed. |
| 50 | `NSQIP_LABS_ALL_UNKNOWN_YN` | VARCHAR |  | Indicates whether all preop labs are unknown. |
| 51 | `NSQIP_HEIGHT` | NUMERIC |  | The patient's height. |
| 52 | `NSQIP_HEIGHT_UNIT_C_NAME` | VARCHAR |  | The category ID for the unit of the height entered in the height column. |
| 53 | `NSQIP_HEIGHT_UNKNOWN_YN` | VARCHAR |  | Indicates whether the patient's height is unknown. |
| 54 | `NSQIP_WEIGHT` | NUMERIC |  | The patient's weight. |
| 55 | `NSQIP_WEIGHT_UNIT_C_NAME` | VARCHAR |  | The category ID for the unit of the weight entered in the weight column. |
| 56 | `NSQIP_WEIGHT_UNKNOWN_YN` | VARCHAR |  | Indicates whether the patient's weight is unknown. |
| 57 | `NSQIP_DIABETES_C_NAME` | VARCHAR |  | The category ID for the diabetes mellitus variable. It determines whether the patient had diabetes mellitus that required therapy with non-insulin agents or insulin. |
| 58 | `NSQIP_SMOKER_YN` | VARCHAR |  | Indicates whether the patient was a smoker within 12 months prior to surgery. |
| 59 | `NSQIP_DYSPNEA_C_NAME` | VARCHAR |  | The category ID for the dyspnea variable. It determines the usual and typical level of dyspnea. |
| 60 | `NSQIP_FHS_C_NAME` | VARCHAR |  | The category ID for the Functional Health Status variable. It determines the best functional status of self-care as demonstrated by the patient prior to the onset of acute illness. |
| 61 | `NSQIP_VENT_DEP_YN` | VARCHAR |  | Indicates whether the patient required ventilator-assisted respirations within 48 hours prior to the principal operative procedure. |
| 62 | `NSQIP_COPD_YN` | VARCHAR |  | Indicates whether the patient suffered from Chronic Obstructive Pulmonary Disease (COPD) prior to surgery. |
| 63 | `NSQIP_ASCITES_YN` | VARCHAR |  | Indicates whether the patient had fluid accumulation in the abodmen due to advanced liver disease or malignancy prior to surgery. |
| 64 | `NSQIP_CHF_YN` | VARCHAR |  | Indicates whether the patient had newly diagnosed Congestive Heart Failure (CHF) or a diagnosis of chronic CHF prior to surgery. |
| 65 | `NSQIP_HYPERTENSION_YN` | VARCHAR |  | Indicates whether the patient had hypertension that required medication prior to surgery. |
| 66 | `NSQIP_ARF_YN` | VARCHAR |  | Indicates whether the patient had renal compromise within 24 hours prior to surgery. |
| 67 | `NSQIP_DIALYSIS_YN` | VARCHAR |  | Indicates whether the patient required dialysis two weeks prior to surgery. |
| 68 | `NSQIP_CANCER_YN` | VARCHAR |  | Indicates whether the patient had advanced malignancy reflecting serious physiologic compromise. |
| 69 | `NSQIP_OPEN_WOUND_YN` | VARCHAR |  | Indicates whether the patient had an open wound prior to surgery. |
| 70 | `NSQIP_STEROID_USE_YN` | VARCHAR |  | Indicates whether the patient was receiving long-term pharmaceutical immunosuppresants. |
| 71 | `NSQIP_WEIGHT_LOSS_YN` | VARCHAR |  | Indicates whether the patient had 10% decrease in body weight in the six month interval prior to surgery. |
| 72 | `NSQIP_BLEEDING_YN` | VARCHAR |  | Indicates whether the patient was at an increased risk for bleeding prior to surgery due to a hematologic disorder or chronic anticoagulation. |
| 73 | `NSQIP_PREOP_TRANSFUSION_YN` | VARCHAR |  | Indicates whether the patient received a preop blood transfusion. |
| 74 | `NSQIP_SEPSIS_C_NAME` | VARCHAR |  | The category ID for the sepsis variable. It determines the most significant level of sepsis prior to surgery. |
| 75 | `NSQIP_WCN` | VARCHAR |  | The Web Case Number (WCN) ID of the NSQIP case. |
| 76 | `NSQIP_FOLLOW_UP_30_DAYS_YN` | VARCHAR |  | Indicates whether the case was followed for the full 30 days. |
| 77 | `NSQIP_FOLLOW_UP_NUM_DAYS` | INTEGER |  | The number of days the case was followed. It is used only if the case was not followed for full 30 days. |
| 78 | `NSQIP_NUM_PHONE_ATTEMPTS` | INTEGER |  | The number of phone attempts that were done to follow the case. It is used only if the case was not followed for full 30 days. |
| 79 | `NSQIP_NUM_LETTER_ATTEMPTS` | INTEGER |  | The number of letter attempts that were done to follow the case. It is used only if the case was not followed for full 30 days. |
| 80 | `NSQIP_POST_OCCURRENCE_YN` | VARCHAR |  | Indicates whether the postoperative occurrence was present. |
| 81 | `NSQIP_DISCHG_DT` | DATETIME |  | The acute hospital discharge date. |
| 82 | `NSQIP_DISCHG_DEST_C_NAME` | VARCHAR |  | The category ID for the discharge destination. |
| 83 | `NSQIP_DISCHG_POSTOP_ICD9` | VARCHAR |  | The ICD-9 code associated with the postoperative discharge. |
| 84 | `NSQIP_DISCHG_STILL_HOSP_YN` | VARCHAR |  | Indicates whether the patient was still in hospital 30 days after surgery. |
| 85 | `NSQIP_DISCHG_DEATH_LT_30_YN` | VARCHAR |  | Indicates whether the death occurred during operation or within 30 days of procedure. |
| 86 | `NSQIP_DISCHG_DEATH_GT_30_YN` | VARCHAR |  | Indicates whether the postoperative death occurred more than 30 days after procedure. |
| 87 | `NSQIP_DISCHG_DEATH_DT` | DATETIME |  | The date of death. |
| 88 | `NSQIP_DISCHG_DEATH_UNKWN_YN` | VARCHAR |  | Indicates whether the date of death is unknown. |
| 89 | `NSQIP_FST_REOP_YN` | VARCHAR |  | Indicates whether the patient returned to the OR within 30 days after principal procedure for the first reoperation. |
| 90 | `NSQIP_FST_REOP_DT` | DATETIME |  | The date the patient returned to the OR for the first reoperation. |
| 91 | `NSQIP_FST_REOP_DT_UNKWN_YN` | VARCHAR |  | Indicates whether the date of the first return to the OR is not known. |
| 92 | `NSQIP_FST_REOP_RELATED_C_NAME` | VARCHAR |  | The category ID of the value that indicates whether the first return to the OR was related to principal operative procedure. |
| 93 | `NSQIP_SEC_REOP_YN` | VARCHAR |  | Indicates whether the patient returned to the OR within 30 days after principal procedure for the second reoperation. |
| 94 | `NSQIP_SEC_REOP_DT` | DATETIME |  | The date the patient returned to the OR for the second reoperation. |
| 95 | `NSQIP_SEC_REOP_DT_UNKWN_YN` | VARCHAR |  | Indicates whether the date of the second return to the OR is not known. |
| 96 | `NSQIP_SEC_REOP_RELATED_C_NAME` | VARCHAR |  | The category ID of the value that indicates whether the second return to the OR was related to principal operative procedure. |
| 97 | `NSQIP_REOP_MORE_THAN_TWO_YN` | VARCHAR |  | Indicates if there were more than two unplanned returns to the OR. |
| 98 | `NSQIP_DISCHG_POSTOP_ICD10` | VARCHAR |  | The ICD-10 code associated with the postoperative discharge. |
| 99 | `NSQIP_ENC_NUM` | VARCHAR |  | The encounter number associated with the NSQIP case. It is an additional optional unique tracking number that hospitals can use for NSQIP cases. |
| 100 | `NSQIP_READMISSION_YN` | VARCHAR |  | Indicates whether the patient was readmitted. 'Y' indicates that the patient was readmitted. 'N' indicates that the patient was not readmitted. |
| 101 | `NSQIP_DISCHG_TRANS_HLC_YN` | VARCHAR |  | Indicates whether the patient was transferred to a higher level of care. 'Y' indicates that the patient was transferred to a higher level of care. 'N' indicates that the patient was not transferred to a higher level of care. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

