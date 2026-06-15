# PATIENT_4

> This table supplements the PATIENT table. It contains basic information about patients.

**Overflow of:** [PATIENT](PATIENT.md)  
**Primary key:** `PAT_ID`  
**Columns:** 72  
**Org-specific columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `INTERPRT_NEEDED_CMT` | VARCHAR |  | Comments regarding the patient's interpreter needs |
| 3 | `DENT_COMMENT` | VARCHAR |  | This item stores the comment of the current dental classification |
| 4 | `ESRD_G_START_DT` | DATETIME |  | The first date that the acute comorbidity of gastrointestinal bleeding was present during maintenance dialysis treatments for End Stage Renal Disease (ESRD). |
| 5 | `ESRD_B_START_DT` | DATETIME |  | The first date that the acute comorbidity of bacterial pneumonia was present during maintenance dialysis treatments for End Stage Renal Disease (ESRD). |
| 6 | `ESRD_P_START_DT` | DATETIME |  | The first date that the acute comorbidity of pericarditis was present during maintenance dialysis treatments for End Stage Renal Disease (ESRD). |
| 7 | `CMS_OP_ESRD_TRAIN_H` | INTEGER |  | The number of training session that have been performed for a patient's hemodialysis treatment through his/her life time. |
| 8 | `CMS_OP_ESRD_TRAIN_P` | INTEGER |  | The number of training session that have been performed for a patient's peritoneal dialysis treatment through his/her life time. |
| 9 | `FOH_ID` | NUMERIC |  | This item stores the filing order history ID for the member. |
| 10 | `TXP_PAT_YN` | VARCHAR |  | Indicates if the patient is a transplant patient. |
| 11 | `BLIND_YN` | VARCHAR |  | Indicates the patient is blind. |
| 12 | `DEAF_YN` | VARCHAR |  | Indicates the patient is deaf. |
| 13 | `EMPR_COUNTY_C_NAME` | VARCHAR | org | The category value corresponding to the county in which the patient's employer is located. |
| 14 | `ALRGY_REV_EPT_CSN` | NUMERIC |  | This column contains the source encounter where allergies were most recently reviewed. If allergies were most recently reviewed outside the context of an encounter, the value is blank. |
| 15 | `OCCUPATION_C_NAME` | VARCHAR | org | Category list for the patient's occupation. |
| 16 | `INDUSTRY_C_NAME` | VARCHAR | org | Category list for the industry in which the patient works. |
| 17 | `EDUCATION_LEVEL_C_NAME` | VARCHAR | org | The patient's highest level of education achieved. |
| 18 | `LOC_EDUCATION_C_NAME` | VARCHAR | org | Location of the patient's highest level of education. |
| 19 | `PARENT_EDU_LEVEL_C_NAME` | VARCHAR |  | Parent/guardian's highest level of education achieved. |
| 20 | `PARENT_LOC_EDU_C_NAME` | VARCHAR |  | Location of parent/guardian's highest level of education. |
| 21 | `RES_OF_STATE_C_NAME` | VARCHAR | org | The state of residence category ID for the patient. |
| 22 | `US_CITIZEN_YN` | VARCHAR |  | Indicates whether the patient is a citizen of the USA. |
| 23 | `PERMANENT_RESIDENT_YN` | VARCHAR |  | Indicates whether the patient is a permanent resident of the USA. |
| 24 | `CNTRY_SUBDIV_CODE_C_NAME` | VARCHAR | org | Capture the patient's country subdivision code. |
| 25 | `RACE_COLL_MTHD_C_NAME` | VARCHAR | org | The race and ethnicity collection method category ID for the patient. |
| 26 | `PAT_NO_COMM_PREF_C_NAME` | VARCHAR |  | This column stores why the patient doesn't have a preference for receiving communication related to reminders and follow-up care. |
| 27 | `FST_LIVE_BIRTH_AGE` | INTEGER |  | The patient's age at first live birth. |
| 28 | `RSH_PREF_C_NAME` | VARCHAR |  | Indicates the patient's explicit research recruitment preference. |
| 29 | `RSH_PREF_UTC_DTTM` | DATETIME (UTC) |  | Indicates the instant that the patient last indicated an explicit research recruitment preference. |
| 30 | `RSH_PREF_USER_ID` | VARCHAR |  | Indicates the user who last recorded the patient's explicit research recruitment preference. |
| 31 | `RSH_PREF_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 32 | `EXTERNAL_DEATH_DATE` | DATETIME |  | The patient's date of death as reported by an external organization. This column is typically populated by importing data through the Patient Load utility. |
| 33 | `DEATH_DATA_IMPORT_DATE` | DATETIME |  | The date the Patient Load utility populated EXTERNAL_DEATH_DATE for this patient. |
| 34 | `DEATH_LOC_C_NAME` | VARCHAR | org | Describes the location where the patient died. |
| 35 | `INDIGENOUS_STAT_C_NAME` | VARCHAR | org | Indicates whether a patient is considered indigenous. |
| 36 | `PAT_LIVING_STAT_C_NAME` | VARCHAR |  | This column uses information from the chart to determine if the patient represents a real patient. If considered a patient the column returns whether or not the patient is Alive or Deceased. If the record does not represent a real patient then Not A Patient is returned. Patients with blank and custom statuses in the patient status item EPT 102 are assumed Alive. The logic for Not A Patient is identical to EPT 109 - Valid Patient except that test patients can be considered Alive or Deceased. |
| 37 | `IS_FETAL_DEMISE_YN` | VARCHAR |  | This column is used to indicate the state of patient's chart due to fetal demise. |
| 38 | `ERROR_NEWBORN_YN` | VARCHAR |  | This column is used to indicate that the newborn chart was created in error. |
| 39 | `MEDSYNC_IS_PARTICIPANT_YN` | VARCHAR |  | Indicates whether the patient is a participant in the outpatient pharmacy medication synchronization program. |
| 40 | `MEDSYNC_RECURRENCE` | INTEGER |  | Stores the number of days that are to be between a patient's medication synchronization refills. |
| 41 | `MEDSYNC_REFILLDATE_DATE` | DATETIME |  | Stores a medication synchronization dispense date for the patient. |
| 42 | `REFILLMGMT_NOTE_ID` | VARCHAR |  | Stores the ID for a General Use Notes (HNO) record for comments regarding the patient's refill management. |
| 43 | `IHS_ENROLLMENT_NUM` | VARCHAR |  | This is the American Indian tribal enrollment ID number for the patient. |
| 44 | `IHS_BENEFICIARY_CLASS_C_NAME` | VARCHAR | org | Classification of the type of patient, indicating a category under which an individual can become eligible for Indian Health Services (IHS) benefits. |
| 45 | `IHS_PRIMARY_TRIBE_C_NAME` | VARCHAR | org | The patient's primary tribe. |
| 46 | `IHS_PRIM_TRIBE_BLOOD_QUANTUM_C_NAME` | VARCHAR | org | This item designates the blood quantum for the patient's primary tribe. |
| 47 | `IHS_COMMUNITY_OF_RESIDENCE_C_NAME` | VARCHAR | org | The patient's community of residence is a subdivision of the state and county in which the patient resides. |
| 48 | `IHS_RESIDENCE_SINCE_DATE` | DATETIME |  | Date when the patient first moved to this community of residence (I EPT 4104). |
| 49 | `IHS_SERVICE_ELIGIBILITY_C_NAME` | VARCHAR | org | Specifies the types of services for which this patient is eligible. |
| 50 | `GENDER_IDENTITY_C_NAME` | VARCHAR | org | The patient's gender identity. |
| 51 | `CURRENT_JOB_START_DATE` | DATETIME |  | The date a patient started in her current job. |
| 52 | `SEX_ASGN_AT_BIRTH_C_NAME` | VARCHAR | org | Stores the patient's sex assigned at birth. |
| 53 | `PREFERENCES_ID` | NUMERIC | FK→ | The ID number of the communication preferences record for the patient. |
| 54 | `DEATH_INFO_SOURCE_C_NAME` | VARCHAR | org | Stores the source that provided the information on the patient's death outside of the organization. This item will allow for more tracking on the patients who died outside of the organization, and allow for more accurate data on deceased patients. |
| 55 | `BLOOD_REQTS_UTC_DTTM` | DATETIME (UTC) |  | Instant the blood special requirements were last edited |
| 56 | `BLOOD_REQTS_USER_ID` | VARCHAR |  | Stores the user that set the current special requirements for a patient |
| 57 | `BLOOD_REQTS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 58 | `ADDR_CHG_USER_ID` | VARCHAR |  | The user who initiated the linked address changes. |
| 59 | `ADDR_CHG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 60 | `ADDR_CHG_INSTANT_DTTM` | DATETIME (Local) |  | The instant that the linked address changes were initiated. |
| 61 | `ADDR_CHG_SOURCE` | VARCHAR |  | The source record that initiated the linked address changes. |
| 62 | `EDD_BASIS_OB_DT_EVENT_C_NAME` | VARCHAR | org | Basis for the patient's expected date of delivery (EDD). Used to track the dating basis for the patient's EDD when the patient does not have a pregnancy episode. |
| 63 | `VETERAN_DENTAL_CVG_LEVEL_C_NAME` | VARCHAR | org | Each patient can have up to one dental coverage. The dental coverage denotes how much dental services a veteran can receive prior to being billed. This column is frequently used to link to the ZC_VETERAN_DENTAL_CVG table. |
| 64 | `VETERAN_IS_COMBAT_COVERED_YN` | VARCHAR |  | This column stores a Yes/No value that indicates whether or not a patient is covered for their service in combat. |
| 65 | `VETERAN_COMBAT_EXP_DATE` | DATETIME |  | This column stores the expiration date of a patient's combat-level coverage. |
| 66 | `VETERAN_PRIORITY_GROUP_C_NAME` | VARCHAR | org | Each patient can have up to one priority group. The priority group is a list of veteran coverage priorities that is maintained by the Department of Veteran Affairs. This column is frequently used to link to the ZC_VETERAN_PRIORITY_GROUP table. |
| 67 | `VETERAN_ENROLLMENT_STATUS_C_NAME` | VARCHAR | org | Each patient can have up to one enrollment status. This denotes whether or not a patient's coverage levels are active or otherwise. This column is frequently used to link to the ZC_VETERAN_ENROLL_STATUS table. |
| 68 | `LEGACY_HICN` | VARCHAR |  | Stores the patient's Health Insurance Claim Number (HICN) if one was previously available and we've received their Medicare Beneficiary Number (MBI) (stored in PATIENT.MEDICARE_NUM). This value may be needed to look up members during the transition to MBI. |
| 69 | `RSH_PREF_MYPT_ID` | VARCHAR |  | Indicates the MyChart user who last recorded the patient's explicit research recruitment preference. |
| 70 | `NEPH_ESRD_START_DT` | DATETIME |  | This item is used to store the date of the patient's first regular chronic dialysis treatment. |
| 71 | `NEPH_PCRF_LPL_ID` | NUMERIC |  | This item is used to store the dialysis patient's primary cause of renal failure. |
| 72 | `NEPH_2728_VERIFY_YN` | VARCHAR |  | This item stores whether the dialysis patient's form-2728 was verified. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PREFERENCES_ID` | [COMM_PREF_ADDL_ITEMS](COMM_PREF_ADDL_ITEMS.md) | sole_pk | high |

## Joined in

Inbound joins are tracked on the logical base [PATIENT](PATIENT.md).

