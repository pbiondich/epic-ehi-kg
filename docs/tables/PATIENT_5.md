# PATIENT_5

> This table supplements the PATIENT table. It contains basic information about patients.

**Overflow of:** [PATIENT](PATIENT.md)  
**Primary key:** `PAT_ID`  
**Columns:** 47  
**Org-specific columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `PHYSICAL_IMPAIRED_C_NAME` | VARCHAR | org | The Physically Impaired? category ID for the patient. |
| 3 | `MEMORY_IMPAIRED_C_NAME` | VARCHAR | org | The Memory Impaired? category ID for the patient. |
| 4 | `SPEECH_IMPAIRED_C_NAME` | VARCHAR | org | The Speech Impaired? category ID for the patient. |
| 5 | `DISABLED_VETERAN_C_NAME` | VARCHAR | org | The Disabled Veteran? category ID for the patient. |
| 6 | `VA_RECOGNIZED_C_NAME` | VARCHAR | org | The VA Recognized? category ID for the patient. |
| 7 | `HEARING_IMPAIRED_C_NAME` | VARCHAR | org | The Hard of Hearing? category ID for the patient. |
| 8 | `VISUALLY_IMPAIRED_C_NAME` | VARCHAR | org | The Low Vision? category ID for the patient. |
| 9 | `DIFFICULTY_DRESS_BATHE_C_NAME` | VARCHAR | org | The Difficulty Dressing or Bathing? category ID for the patient. |
| 10 | `DIFFICULTY_WITH_ERRAND_C_NAME` | VARCHAR | org | The Difficulty with Errands? category ID for the patient. |
| 11 | `SC_PERM_FORM_OF_RES_C_NAME` | VARCHAR | org | The social care client's permanent form of residence. |
| 12 | `SC_GROUNDS_FOR_RES_PERM_C_NAME` | VARCHAR | org | Reason why the social care client is able to hold a residence permit. |
| 13 | `SC_RES_PERMIT_VALID_TO_DATE` | DATETIME |  | Date the social care client's residence permit is valid to. |
| 14 | `SC_TYPE_OF_RELATIONSHIP_C_NAME` | VARCHAR | org | Further specify marriage details for the social care client. |
| 15 | `SOCIAL_CARE_PASSPORT_TYPE_C_NAME` | VARCHAR | org | The passport type. |
| 16 | `SOCIAL_CARE_PASSPORT_EXP_DATE` | DATETIME |  | Date passport expires. |
| 17 | `RSH_PREFS_ANSWER_ID` | VARCHAR |  | The unique ID of the questionnaire answers of the patient's most recent research preference questionnaire submission. |
| 18 | `RX_AUTO_REFILL_DELIV_MTHD_C_NAME` | VARCHAR | org | The delivery method to use for refills initiated via auto refill. If not set, the default delivery method is used. |
| 19 | `PAT_PHOTO` | VARCHAR |  | This stores the file name of the current patient photo. |
| 20 | `PEND_PAT_PHOTO` | VARCHAR |  | This stores the file name of a photo pending approval to be added to the chart. It has most likely been submitted by the patient via Welcome or MyChart. |
| 21 | `TYPE_AND_SCR_ELIG_YN` | VARCHAR |  | This stores whether or not the patient is eligible for a type and screen. |
| 22 | `NEPH_PCRF_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 23 | `CONSENT_ABILITY_YN` | VARCHAR |  | If the patient is able to consent or not. Leaving this item blank will be treated as an answer of "Unknown." |
| 24 | `SCHOOL_DISTRICT_NUM` | VARCHAR |  | School district number. |
| 25 | `MIGRATION_TYPE_C_NAME` | VARCHAR | org | The migrant type: either emigrant or immigrant. |
| 26 | `MIGRANT_COUNTRY_C_NAME` | VARCHAR | org | If the patient is a migrant, this is the country which the patient is immigrating from or emigrating to. |
| 27 | `CONGREGATE_CARE_RESIDENT_YN` | VARCHAR |  | Denotes whether a patient is a resident of a congregate care setting such as a group home, residential treatment facility, or maternity home. |
| 28 | `SEEN_DOMESTIC_TRAVEL_ALERT_YN` | VARCHAR |  | Indicates whether the patient has seen the alert in MyChart or Welcome warning them that they can now enter trips that they've taken inside of the United States. |
| 29 | `KI_SELF_GUAR_ACCT_VERIF_DATE` | DATETIME |  | This item indicates the most recent date the patient verified whether the self-guarantor billing information is correct in Welcome. |
| 30 | `KI_SELF_GUAR_ACCT_VERIF_STS_C_NAME` | VARCHAR |  | This item indicates the most recent answer a patient selected when prompted to verify whether the self-guarantor billing information is correct in Welcome. |
| 31 | `PAT_PHONETIC_NAME` | VARCHAR |  | Stores the phonetic spelling of the patient's name. |
| 32 | `PAT_RETIREMENT_DATE` | DATETIME |  | The date of a patient's retirement for MSPQ purposes. |
| 33 | `SPOUSE_RETIREMENT_DATE` | DATETIME |  | The date of a patient's spouse's retirement for MSPQ purposes. |
| 34 | `DRIVERS_LICENSE_NUM` | VARCHAR |  | The patient's driver's license number. |
| 35 | `DRIVERS_LICENSE_STATE_C_NAME` | VARCHAR | org | The state category ID for the patient's driver's license. |
| 36 | `EMPLOYMENT_HIRE_DATE` | DATETIME |  | The date that a patient was hired at their employer. |
| 37 | `EMPLOYER_FAX` | VARCHAR |  | the fax number of the patient's employer. |
| 38 | `WORK_PHONE` | VARCHAR |  | The patient's work phone number. |
| 39 | `H1B_WORK_VISA_YN` | VARCHAR |  | Indicates whether the patient has an H1B work visa. |
| 40 | `STUDENT_VISA_YN` | VARCHAR |  | Indicates whether the patient has a student visa. |
| 41 | `BIRTH_COUNTY_C_NAME` | VARCHAR | org | The county category ID for where the patient was born. |
| 42 | `CORRESP_CONTACT` | VARCHAR |  | This name of the contact person associated with a patient's correspondence address. |
| 43 | `CUR_INP_SUMMARY_BLOCK_ID` | NUMERIC |  | The current Inpatient summary block ID. |
| 44 | `PREFERRED_FORM_ADDRESS` | VARCHAR |  | How the patient prefers to be addressed. |
| 45 | `PAT_ACADEMIC_DEGREE_C_NAME` | VARCHAR | org | Stores the academic degree of the patient as it would appear with the patient's name. For example, James Smith, PhD. |
| 46 | `PREFERRED_NAME_TYPE_C_NAME` | VARCHAR | org | Stores the type for the patient's preferred name. |
| 47 | `AHCIC_NUM` | VARCHAR |  | The patient's AHCIC number. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [PATIENT](PATIENT.md).

