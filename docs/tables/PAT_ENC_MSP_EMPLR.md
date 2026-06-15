# PAT_ENC_MSP_EMPLR

> This table contains the Employer Information part of the Medicare Secondary Payor Information from the Patient (EPT) master file.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 27  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `CONTACT_DATE` | DATETIME |  | The date (calendar format) on which the encounter took place. |
| 3 | `PAT_EMPLYD_YN` | VARCHAR |  | Indicates whether the patient is currently employed for the purposes of the MSPQ. Y indicates that the patient is currently employed. N indicates that the patient is not currently employed or has never been employed. A null value indicates this item was not filled out. |
| 4 | `EMPLOYER_NAME` | VARCHAR |  | Name of the patient's employer. |
| 5 | `EMPLOYER_SIZE_C_NAME` | VARCHAR | org | The size range category ID of the patient's employer. |
| 6 | `EMPLOYER_PHONE` | VARCHAR |  | Phone number of the patient's employer. |
| 7 | `EMPLOYER_ADR_1` | VARCHAR |  | Line 1 of the patient's employer's address. |
| 8 | `EMPLOYER_ADR_2` | VARCHAR |  | Line 2 of the patient's employer's address. |
| 9 | `EMPLOYER_CITY` | VARCHAR |  | City of the patient's employer. |
| 10 | `EMPLOYER_ZIP` | VARCHAR |  | Zip code of the patient's employer. |
| 11 | `OTHER_EMPLYD_YN` | VARCHAR |  | Indicates whether the spouse or other family member is currently employed for the purposes of the MSPQ. Y indicates that the spouse or other family member is currently employed. N indicates that the spouse or other family member is not currently employed or has never been employed. A null value indicates this item was not filled out. |
| 12 | `OTHR_FAM_MEM_NAME` | VARCHAR |  | Name of other family members who are employed. |
| 13 | `OTHR_FAM_REL_C_NAME` | VARCHAR | org | Employed family member's relationship to the patient. |
| 14 | `OTHR_EMPLR_NAME` | VARCHAR |  | Employed family member employer's name. |
| 15 | `OTHR_EMPLR_SIZE_C_NAME` | VARCHAR |  | Size of the employer of the other employed family member. |
| 16 | `OTHR_EMPLR_PHONE` | VARCHAR |  | Phone number of the employer of the other employed family member. |
| 17 | `OTHR_EMPLR_ADR_1` | VARCHAR |  | Line 1 of the employer's address of the other employed family member. |
| 18 | `OTHR_EMPLR_ADR_2` | VARCHAR |  | Line 2 of the employer's address of the other employed family member. |
| 19 | `OTHR_EMPLR_CITY` | VARCHAR |  | City of the employer of the other employed family member. |
| 20 | `OTHR_EMPLR_STATE_C_NAME` | VARCHAR | org | State of the employer of the other employed family member. |
| 21 | `OTHR_EMPLR_ZIP` | VARCHAR |  | Zip of the employer of the other employed family member. |
| 22 | `FAMILY_EMPLR_NAME` | VARCHAR |  | Name of the family member's employer. In some questionnaires, this information is instead stored as part of the spouse / other family member employer information, OTHR_EMPLR_*. |
| 23 | `FAMILY_EMPLR_ADR_1` | VARCHAR |  | First line of the family member's employer's address. In some questionnaires, this information is instead stored as part of the spouse / other family member employer information, OTHR_EMPLR_*. |
| 24 | `FAMILY_EMPLR_ADR_2` | VARCHAR |  | Second line of the family member's employer's address. In some questionnaires, this information is instead stored as part of the spouse / other family member employer information, OTHR_EMPLR_*. |
| 25 | `FAMILY_EMPLR_CITY` | VARCHAR |  | The City part of the family member's employer's address. |
| 26 | `FAMILY_EMPLR_ZIP` | VARCHAR |  | The ZIP part of the family member's employer's address. |
| 27 | `FAMILY_EMPLR_PHONE` | VARCHAR |  | Family member's employer's phone number. In some questionnaires, this information is instead stored as part of the spouse / other family member employer information, OTHR_EMPLR_*. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

