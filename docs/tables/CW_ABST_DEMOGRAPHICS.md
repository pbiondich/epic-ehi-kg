# CW_ABST_DEMOGRAPHICS

> General abstraction details and demographic information reported to the United States ESRD patient registry.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 98  
**Org-specific columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `MCARE_STATUS_C_NAME` | VARCHAR |  | The current Medicare status of the dialysis patient. |
| 3 | `MCARE_EFF_DATE` | DATETIME |  | The effective date of the current Medicare status of the dialysis patient. |
| 4 | `EMPY_STATUS_C_NAME` | VARCHAR |  | The current employment status of the dialysis patient. |
| 5 | `EMPY_EFF_DATE` | DATETIME |  | The effective date of the current employment status of the dialysis patient. |
| 6 | `SCHOOL_STATUS_C_NAME` | VARCHAR | org | The current school status of the dialysis patient. |
| 7 | `SCHOOL_EFF_DATE` | DATETIME |  | The effective date of the current school status of the dialysis patient. |
| 8 | `VOCATIONAL_REHAB_STATUS_C_NAME` | VARCHAR | org | The current vocational rehab status of the dialysis patient. |
| 9 | `VOCATIONAL_REHAB_EFF_DATE` | DATETIME |  | The effective date of the current vocational rehab status of the dialysis patient. |
| 10 | `ADMSN_FACILITY_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 11 | `ADMSN_DATE` | DATETIME |  | The date when the dialysis patient started dialysis treatment in this facility. |
| 12 | `ADMSN_RSN_C_NAME` | VARCHAR | org | The reason for dialysis admission. |
| 13 | `TRANSIENT_RSN_C_NAME` | VARCHAR | org | The reason for the dialysis patient being transient. |
| 14 | `TRANSFER_RSN_C_NAME` | VARCHAR | org | The transfer discharge reason of a dialysis patient. |
| 15 | `DISCH_DATE` | DATETIME |  | The date when a patient is discharged from the dialysis outpatient facility. |
| 16 | `DISCH_RSN_C_NAME` | VARCHAR | org | The reason for discharging a patient from the dialysis facility. |
| 17 | `PRIMARY_TRT_LOCATION_C_NAME` | VARCHAR | org | The primary setting of the patient's dialysis treatment. |
| 18 | `TRT_START_DATE` | DATETIME |  | The treatment start date for dialysis. |
| 19 | `TRT_TYPE_C_NAME` | VARCHAR | org | The treatment type of dialysis patient. |
| 20 | `SESSIONS_PER_WEEK` | NUMERIC |  | The number of hemodialysis sessions per week for the dialysis patient. |
| 21 | `SESSION_LENGTH` | INTEGER |  | The hemodialysis session length. |
| 22 | `TRT_PROVIDER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 23 | `IS_TRANSIENT_YN` | VARCHAR |  | Shows whether the dialysis patient is transient or not. |
| 24 | `TRAINING_TYPE_C_NAME` | VARCHAR |  | The type of training obtained by dialysis patient. |
| 25 | `OTHER_TRAINING_TYPE` | VARCHAR |  | The type of training type if not in the list of common types. |
| 26 | `TRAINING_TIME_OF_DAY_C_NAME` | VARCHAR | org | The information on whether the patient obtained training for day or nocturnal dialysis. |
| 27 | `TRAINING_START_DATE` | DATETIME |  | The training start date for the dialysis patient. |
| 28 | `TRAINING_END_DATE` | DATETIME |  | The training end date for the dialysis patient. |
| 29 | `SELFCARE_TYPE_C_NAME` | VARCHAR |  | Shows whether the dialysis patient is expected to perform self-care at home or in-center after dialysis training. |
| 30 | `NO_CLINICAL_DATA_YN` | VARCHAR |  | Shows whether the dialysis patient's monthly clinical submission information is available or not. |
| 31 | `EQRS_IDENT` | VARCHAR |  | The dialysis patient's End Stage Renal Disease Quality Reporting System (EQRS) ID used in CMS reporting. |
| 32 | `ADMISSION_IDENTIFIER` | VARCHAR |  | Unique identifier for dialysis admission. |
| 33 | `TREATMENT_IDENTIFIER` | VARCHAR |  | It stores the dialysis treatment modality ID of a patient. |
| 34 | `PAT_FIRST_NAME` | VARCHAR |  | It stores the dialysis patient's first name. |
| 35 | `PAT_MIDDLE_INITIAL` | VARCHAR |  | It stores a dialysis patient's middle name initial. |
| 36 | `PAT_LAST_NAME` | VARCHAR |  | It stores a dialysis patient's last name. |
| 37 | `PAT_NAME_SUFFIX_C_NAME` | VARCHAR | org | It stores a dialysis patient's name suffix. |
| 38 | `PAT_SEX_C_NAME` | VARCHAR |  | It stores the dialysis patient's sex assigned at birth. |
| 39 | `PAT_BIRTH_DATE` | DATETIME |  | It stores a dialysis patient's date of birth. |
| 40 | `PAT_DEATH_DATE` | DATETIME |  | It stores a dialysis patient's date of death. |
| 41 | `PAT_MBI_NUM` | VARCHAR |  | It stores a dialysis patient's Medicare Beneficiary Identifier number. |
| 42 | `PAT_SSN` | VARCHAR |  | It stores a dialysis patient's social security number. |
| 43 | `PHYS_ADDRESS_STREET_1` | VARCHAR |  | It stores a dialysis patient's physical address street line 1. |
| 44 | `PHYS_ADDRESS_STREET_2` | VARCHAR |  | It stores a dialysis patient's physical address street line 2. |
| 45 | `PHYS_ADDRESS_STATE_C_NAME` | VARCHAR | org | It stores a dialysis patient's physical address state. |
| 46 | `PHYS_ADDRESS_COUNTY_C_NAME` | VARCHAR | org | It stores a dialysis patient's physical address county. |
| 47 | `PHYS_ADDRESS_ZIP` | VARCHAR |  | It stores a dialysis patient's ZIP code. |
| 48 | `PHYS_ADDRESS_ZIP_EXT` | VARCHAR |  | It stores a dialysis patient's physical address ZIP extension. |
| 49 | `MAIL_ADDRESS_STREET_1` | VARCHAR |  | It stores a dialysis patient's mailing address street line 1. |
| 50 | `MAIL_ADDRESS_STREET_2` | VARCHAR |  | It stores a dialysis patient's mailing address street line 2. |
| 51 | `PHYS_ADDRESS_CITY` | VARCHAR |  | It stores a dialysis patient's physical address city. |
| 52 | `MAIL_ADDRESS_CITY` | VARCHAR |  | It stores a dialysis patient's mailing address city. |
| 53 | `MAIL_ADDRESS_STATE_C_NAME` | VARCHAR |  | It stores a dialysis patient's mailing address state. |
| 54 | `MAIL_ADDRESS_COUNTY_C_NAME` | VARCHAR |  | It stores a dialysis patient's mailing address county. |
| 55 | `MAIL_ADDRESS_ZIP` | VARCHAR |  | It stores a dialysis patient's mailing address zip code. |
| 56 | `MAIL_ADDRESS_ZIP_EXT` | VARCHAR |  | It stores a dialysis patient's mailing address zip code extension. |
| 57 | `WORK_PHONE_AREA_CODE` | INTEGER |  | It indicates a dialysis patient's work phone number area code. |
| 58 | `WORK_PHONE_NUMBER` | VARCHAR |  | It indicates a dialysis patient's work phone number without the area code. |
| 59 | `WORK_PHONE_EXTENSION` | INTEGER |  | It indicates a dialysis patient's work phone number extension. |
| 60 | `HOME_PHONE_AREA_CODE` | INTEGER |  | It stores the area code from a dialysis patient's phone number. |
| 61 | `HOME_PHONE_NUMBER` | VARCHAR |  | It stores a dialysis patient's phone number. |
| 62 | `HOME_PHONE_EXTENSION` | INTEGER |  | It stores the phone number extension of a dialysis patient. |
| 63 | `FAX_PHONE_AREA_CODE` | INTEGER |  | It indicates a dialysis patient's fax number area code. |
| 64 | `FAX_PHONE_NUMBER` | VARCHAR |  | It indicates a dialysis patient's fax number without the area code. |
| 65 | `FAX_PHONE_EXTENSION` | INTEGER |  | It indicates a dialysis patient's fax number extension. |
| 66 | `MOBILE_PHONE_AREA_CODE` | INTEGER |  | It indicates a dialysis patient's mobile phone number area code piece. |
| 67 | `MOBILE_PHONE_NUMBER` | VARCHAR |  | It indicates a dialysis patient's mobile phone number without the area code. |
| 68 | `PAGER_PHONE_AREA_CODE` | INTEGER |  | It indicates a dialysis patient's pager number area code piece. |
| 69 | `PAGER_PHONE_NUMBER` | VARCHAR |  | It indicates a dialysis patient's pager number without the area code. |
| 70 | `PAGER_PHONE_EXTENSION` | INTEGER |  | It indicates a dialysis patient's pager number extension. |
| 71 | `OTHER_PHONE_AREA_CODE` | INTEGER |  | It indicates a dialysis patient's other phone number area code. |
| 72 | `OTHER_PHONE_NUMBER` | VARCHAR |  | It indicates a dialysis patient's other phone number without the area code. |
| 73 | `OTHER_PHONE_EXTENSION` | INTEGER |  | It indicates a dialysis patient's other phone number extension. |
| 74 | `TRANSIENT_ADDRESS_STREET_1` | VARCHAR |  | It stores a transient dialysis patient's street address line 1. |
| 75 | `TRANSIENT_ADDRESS_STREET_2` | VARCHAR |  | It stores a transient dialysis patient's street address line 2. |
| 76 | `TRANSIENT_ADDRESS_CITY` | VARCHAR |  | It stores the city name of a dialysis patient's transient address. |
| 77 | `TRANSIENT_ADDRESS_STATE_C_NAME` | VARCHAR |  | It stores a dialysis patient's transient address state. |
| 78 | `TRANSIENT_ADDRESS_ZIP` | VARCHAR |  | It stores a dialysis patient's transient address ZIP code. |
| 79 | `TRANSIENT_ADDRESS_ZIP_EXT` | VARCHAR |  | It stores a dialysis patient's transient address ZIP code extension. |
| 80 | `TRANSIENT_PHONE_TYPE_C_NAME` | VARCHAR | org | It stores a transient dialysis patient's preferred phone number type. |
| 81 | `TRANSIENT_PHONE_AREA_CODE` | INTEGER |  | It stores the area code from a transient dialysis patient's phone number. |
| 82 | `TRANSIENT_PHONE_NUMBER` | VARCHAR |  | It stores the transient phone number of a dialysis patient. |
| 83 | `TRANSIENT_PHONE_EXTENSION` | INTEGER |  | It stores the extension from a dialysis patient's transient phone number. |
| 84 | `TRANSIENT_ADDRESS_COUNTY_C_NAME` | VARCHAR |  | It stores a dialysis patient's transient address county. |
| 85 | `PAT_ETHNICITY_C_NAME` | VARCHAR | org | It stores a dialysis patient's ethnicity. |
| 86 | `PAT_COUNTRY_OF_ORIGIN_C_NAME` | VARCHAR |  | It stores a dialysis patient's country of origin. |
| 87 | `PAT_ETHNICITY_SOURCE_C_NAME` | VARCHAR |  | It stores the source of a dialysis patient's race and ethnicity information. |
| 88 | `PAT_CITIZENSHIP_STATUS_C_NAME` | VARCHAR |  | It stores the current citizenship status of a dialysis patient. |
| 89 | `PAT_CITIZENSHIP_EFF_DATE` | DATETIME |  | It stores the effective date of the current citizenship status of a dialysis patient. |
| 90 | `PAT_HIC_NUM` | VARCHAR |  | It stores a dialysis patient's Medicare health insurance claim number. |
| 91 | `PAT_TRIBE_CODE` | INTEGER |  | This column has been replaced by DIA_PAT_TRIBE_C (RDI/28584) in table CW_ABST_DEMOGRAPHICS. To look up the deprecated column's value after the Clarity Compass upgrade, join column CW_ABST_DEMOGRAPHICS.DIA_PAT_TRIBE_C to table ZC_PAT_TRIBE column PAT_TRIBE_C and get the TITLE value. |
| 92 | `INVOLUNTARY_DISCH_RSN_C_NAME` | VARCHAR | org | It stores the reason of involuntary discharge for a dialysis patient. |
| 93 | `DLYS_ABSTRACTION_PURPOSE_C_NAME` | VARCHAR |  | It stores the purpose of a patient's dialysis regulatory reporting form, such as an admission, a discharge, or a monthly submission. |
| 94 | `PAT_IN_NURSING_HOME_YN` | VARCHAR |  | It stores whether the dialysis patient was in a nursing home setting as of the end of the reporting period. |
| 95 | `DIALYSIS_NURSING_HOME_C_NAME` | VARCHAR |  | It stores the dialysis patient's nursing home setting. |
| 96 | `PAT_ORG_IDENT` | VARCHAR |  | The dialysis patient's organization identifier used in CMS reporting. |
| 97 | `PAT_ENTERED_NURSING_HOME_DATE` | DATETIME |  | The date when the dialysis patient entered the nursing home. |
| 98 | `DIA_PAT_TRIBE_C_NAME` | VARCHAR | org | The dialysis patient tribe category ID for the registry data. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

