# V_EHI_COVERAGE_SUBS

> This view contains information about a coverage's subscriber. Used for Electronic Health Information (EHI) export.

**Primary key:** `COVERAGE_ID`  
**Columns:** 66  
**Org-specific columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique ID assigned to the coverage record. This ID may be encrypted if you have elected to use enterprise reporting’s encryption utility. |
| 2 | `SUBSCRIBER_PAT_ID` | VARCHAR | FK→ | If the subscriber is the same person as a patient, this item contains the patient ID. |
| 3 | `SUBSCRIBER_CONFDENTIAL_NAME` | VARCHAR |  | This item contains the confidential name of the associated patient, if it exists. The name is used to determine the confidential nature of the subscriber. |
| 4 | `SUBSCRIBER_NUMBER` | VARCHAR |  | The identification number assigned to the subscriber for the coverage. When the subscriber is also a member on the coverage, this is the same as the subscriber’s member number. This column may be hidden if you have elected to use enterprise reporting’s security utility. |
| 5 | `SUBSCRIBER_ID_FROM_SOURCE_FILE` | VARCHAR |  | Subscriber ID received on the source file for the subscriber on the coverage. |
| 6 | `SUBSCRIBER_MEDICARE_NUMBER` | VARCHAR |  | Stores the subscriber's Medicare number, if applicable. This will be a Medicare Beneficiary Number (MBI) if available, or a Health Insurance Claim Number (HICN) if not. |
| 7 | `SUBSCRIBER_MEDICARE_HIC_NUMBER` | VARCHAR |  | Contains the subscriber Health Insurance Claim Number (HICN) once it has been replaced by the Medicare Beneficiary Number (MBI). |
| 8 | `SUBSCRIBER_SEX_C_NAME` | VARCHAR | org | The sex of the subscriber on the coverage. |
| 9 | `SUBSCRIBER_GENDER_IDENTITY_C_NAME` | VARCHAR | org | Stores the category ID of the subscriber's gender identity as stored on the coverage. This value may not be the same as the gender identity stored on the subscriber's patient record. |
| 10 | `SUBSCRIBER_RACE_C_NAME` | VARCHAR | org | The race of the subscriber. |
| 11 | `SUBSCRIBER_PREFERRED_NAME` | VARCHAR |  | Stores the preferred name of the subscriber as present on the coverage record at the time of coverage creation. This value may not be the same as the preferred name stored on the subscriber's patient record. |
| 12 | `SUBSCRIBER_NAME` | VARCHAR |  | The name of the subscriber for the coverage. This column may be hidden if you have elected to use enterprise reporting’s security utility. |
| 13 | `SUBSCRIBER_EMPLOYER_COUNTY_C_NAME` | VARCHAR | org | The county of the subscriber's employer's address on a coverage |
| 14 | `SUBSCRIBER_REL_TO_GUAR_C_NAME` | VARCHAR | org | The category number for the subscriber's relationship to the guarantor. |
| 15 | `SUBSCRIBER_EMPLOYER_HOUSE_NUM` | VARCHAR |  | The house number of the subscriber's employer's address on a coverage |
| 16 | `SUBSCRIBER_EMPLOYER_DISTRICT_C_NAME` | VARCHAR | org | The district of the subscriber's employer's address on a coverage |
| 17 | `SUBSCRIBER_EMPLOYER_ID` | VARCHAR |  | This is the unique ID of the employer of the patient subscribing to the coverage if EAF 6410 is set to 1. This is free text if EAF 6410 is set to 2. |
| 18 | `SUBSCRIBER_EMPLOYER_ID_EMPLOYER_NAME` | VARCHAR |  | The name of the employer. |
| 19 | `SUBSCRIBER_EMPLOYER_COMMENT` | VARCHAR |  | A free text comment that can be entered when the value that is considered to be "Other" is selected as the employer. This option is available only if your organization has chosen to link the subscriber employer to the Employer (EEP) master file in the Facility Profile. |
| 20 | `SUBSCRIBER_EMPLOYER_CITY` | VARCHAR |  | The City field of the subscriber's employer's address on the coverage. |
| 21 | `SUBSCRIBER_EMPLOYER_STATE_C_NAME` | VARCHAR | org | The state of the subscriber's employer's address on a coverage. |
| 22 | `SUBSCRIBER_EMPLOYER_ZIP` | VARCHAR |  | The zip code of the subscriber's employer's address on a coverage |
| 23 | `SUBSCRIBER_EMPLOYMENT_STATUS_C_NAME` | VARCHAR | org | The employment status of the subscriber's employer on a coverage (i.e. full, part, etc.). |
| 24 | `SUBSCRIBER_EMPLOYER_COUNTRY_C_NAME` | VARCHAR | org | The category number for the country of the subscriber's employer. |
| 25 | `SUBSCRIBER_EMPLOYER_PHONE` | VARCHAR |  | The phone number of the subscriber's employer on a coverage |
| 26 | `SUBSCRIBER_EMPLOYER_FAX` | VARCHAR |  | The fax number of the coverage subscriber's employer. |
| 27 | `SUBSCRIBER_EMPLOYEE_ID_NUMBER` | VARCHAR |  | The coverage subscriber's employee ID number. |
| 28 | `SUBSCRIBER_ADDR_IS_UNDELIV_YN` | VARCHAR |  | Indicates if subscriber home address is undeliverable. |
| 29 | `SUBSCRIBER_HOUSE_NUMBER` | VARCHAR |  | Subscriber House Number for non-US locales |
| 30 | `SUBSCRIBER_CITY` | VARCHAR |  | The city of the mailing address for the subscriber on the coverage. |
| 31 | `SUBSCRIBER_STATE_C_NAME` | VARCHAR |  | The state of the mailing address for the subscriber on the coverage. |
| 32 | `SUBSCRIBER_SUBDIVISION_CODE_C_NAME` | VARCHAR | org | Capture the subscriber's country subdivision code. |
| 33 | `SUBSCRIBER_ZIP` | VARCHAR |  | The postal code of the mailing address for the subscriber on the coverage. |
| 34 | `SUBSCRIBER_COUNTRY_C_NAME` | VARCHAR |  | The country of the mailing address for the subscriber on the coverage. |
| 35 | `SUBSCRIBER_COUNTY_C_NAME` | VARCHAR |  | The county of the mailing address for the subscriber on the coverage. |
| 36 | `SUBSCRIBER_IS_US_CITIZEN_YN` | VARCHAR | org | Indicates whether the subscriber is a U.S. citizen. |
| 37 | `SUBSCRIBER_DISTRICT_C_NAME` | VARCHAR |  | The district of the mailing address for the subscriber on the coverage. |
| 38 | `SUBSCRIBER_PHONE` | VARCHAR |  | The home phone number for the subscriber on the coverage. |
| 39 | `SUBSCRIBER_FAX` | VARCHAR |  | The fax number for the subscriber on the coverage. |
| 40 | `SUBSCRIBER_WORK_PHONE` | VARCHAR |  | The work phone number for the subscriber on the coverage. |
| 41 | `SUBSCRIBER_BIRTH_DATE` | DATETIME |  | The date of birth for the subscriber on the coverage. |
| 42 | `SUBSCRIBER_MARITAL_STATUS_C_NAME` | VARCHAR | org | The marital status of the subscriber. |
| 43 | `SUBSCRIBER_SSN` | VARCHAR |  | The SSN number of the subscriber on a coverage |
| 44 | `SUBSCRIBER_OCCUPATION` | VARCHAR |  | The coverage subscriber's occupation. |
| 45 | `SUBSCRIBER_RETIRE_DATE` | DATETIME |  | The date when the coverage subscriber retired. |
| 46 | `SUBSCRIBER_SPOUSE_RETIRE_DATE` | DATETIME |  | The date when the coverage subscriber's spouse retired. |
| 47 | `SUBSCRIBER_ADDRESS_IS_VALID_C_NAME` | VARCHAR |  | The category ID which indicates whether the subscriber address has been validated. |
| 48 | `SUBSCRIBER_ADDR_VALID_MTHD_C_NAME` | VARCHAR |  | The category ID which indicates the validation method by which the subscriber address was validated. |
| 49 | `SUBSCRIBER_ADDR_VALID_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time when the subscriber address was last validated. |
| 50 | `SUBSCRIBER_BNK_ID` | VARCHAR |  | Banking details of the subscriber. |
| 51 | `SUBSCRIBER_ALT_BILL_NAME` | VARCHAR |  | The alternate billing name for the coverage subscriber. |
| 52 | `SUBSCRIBER_ALT_BIRTH_DATE` | DATETIME |  | The alternate subscriber date of birth override for use with interfaces. |
| 53 | `SUBSCRIBER_ALT_SEX_C_NAME` | VARCHAR |  | The subscriber's sex as known to the payor. |
| 54 | `SUBSCRIBER_CHAMPUS_STATUS` | VARCHAR |  | The CHAMPUS/Tricare subscriber status. |
| 55 | `SUBSCRIBER_EMPLOYMENT_DATE` | DATETIME |  | The date on which the subscriber began working for the employer associated with the employer group. |
| 56 | `SUBSCRIBER_APPLICATION_DATE` | DATETIME |  | The date on which the subscriber applied for coverage. |
| 57 | `MEDICARE_SUBSCRIBER_IDENT` | VARCHAR |  | The unique ID of the subscriber that will be used for supplemental claims. |
| 58 | `RQG_REL_TO_SUBSCRIBER_C_NAME` | VARCHAR | org | The patient to subscriber relationship category number for this coverage. |
| 59 | `SUBSCRIBER_HAS_ICHRA_YN` | VARCHAR |  | Indicator for whether the subscriber is enrolled in an individual coverage HRA. |
| 60 | `MCARE_GENDER_IDENTITY_C_NAME` | VARCHAR |  | The gender identity denoted by the subscriber on their Medicare Advantage application. |
| 61 | `MCARE_SEX_ORIENTATION_C_NAME` | VARCHAR |  | The sexual orientation denoted by the subscriber on their Medicare Advantage application. |
| 62 | `MCARE_SPEC_GENDER_IDENTITY` | VARCHAR |  | The term the subscriber specified for their gender identity on their Medicare Advantage application because a value for their gender identity was not present on the application. |
| 63 | `MCARE_SPEC_SEX_ORIENTATION` | VARCHAR |  | The term the subscriber specified for their sexual orientation on their Medicare Advantage application because a value for their sexual orientation was not present on the application. |
| 64 | `MCARE_INDIV_REP_NAME` | VARCHAR |  | The name of the individual representative that helped the subscriber fill out their Medicare Advantage application. |
| 65 | `MCARE_INDIV_REP_REL_C_NAME` | VARCHAR |  | The relationship of the individual representative to the subscriber that they helped fill out the Medicare Advantage application for. |
| 66 | `MCARE_INDIV_REP_NPN` | VARCHAR |  | The National Producer Number of the individual representative that helped the subscriber fill out the Medicare Advantage application, if the individual representative is an agent or a broker. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `SUBSCRIBER_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

