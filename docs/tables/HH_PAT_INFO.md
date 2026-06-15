# HH_PAT_INFO

> Contains Home Health noadd single items in the Patient (EPT) master file.

**Primary key:** `PAT_ID`  
**Columns:** 25  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | Unique identifier for the patient. |
| 2 | `CAREGIVER_1_NAME` | VARCHAR |  | Caregiver 1 name. |
| 3 | `CAREGIVER_1_CITY` | VARCHAR |  | Caregiver 1 city. |
| 4 | `CAREGIVER_1_ZIP` | VARCHAR |  | Caregiver 1 ZIP code. |
| 5 | `CAREGIVER_1_HPHONE` | VARCHAR |  | Caregiver 1 home phone number. |
| 6 | `CAREGIVER_1_WPHONE` | VARCHAR |  | Caregiver 1 work phone number. |
| 7 | `CAREGIVER_1_EMAIL` | VARCHAR |  | Caregiver 1 email address. |
| 8 | `CAREGIVER_2_NAME` | VARCHAR |  | Caregiver 2 name. |
| 9 | `CAREGIVER_2_CITY` | VARCHAR |  | Caregiver 2 city. |
| 10 | `CAREGIVER_2_ZIP` | VARCHAR |  | Caregiver 2 ZIP code. |
| 11 | `CAREGIVER_2_HPHONE` | VARCHAR |  | Caregiver 2 home phone number. |
| 12 | `CAREGIVER_2_WPHONE` | VARCHAR |  | Caregiver 2 work phone number. |
| 13 | `CAREGIVER_2_EMAIL` | VARCHAR |  | Caregiver 2 email address. |
| 14 | `CAREGIVER_1_REL_C_NAME` | VARCHAR | org | Primary caregiver's relationship to the patient |
| 15 | `CAREGIVER_2_REL_C_NAME` | VARCHAR |  | Secondary caregiver's relationship to the patient |
| 16 | `CAREGIVER_1_MPHONE` | VARCHAR |  | The primary caregiver's mobile phone number. |
| 17 | `CAREGIVER_1_PRIM_PHONE_C_NAME` | VARCHAR |  | Tracks which of the caregiver 1 phone numbers is the primary number. |
| 18 | `CAREGIVER_1_LANG_C_NAME` | VARCHAR | org | Tracks the preferred language of the primary caregiver. |
| 19 | `CAREGIVER_2_MPHONE` | VARCHAR |  | Mobile phone number for the secondary caregiver. |
| 20 | `CAREGIVER_2_PRIM_PHONE_C_NAME` | VARCHAR |  | Which of the caregiver 1's phone numbers is the primary number. |
| 21 | `CAREGIVER_2_LANG_C_NAME` | VARCHAR |  | Tracks the secondary caregiver's preferred language. |
| 22 | `CAREGIVER_2_CNTY_C_NAME` | VARCHAR | org | The county portion of the secondary caregiver's address. |
| 23 | `CAREGIVER_2_CNTRY_C_NAME` | VARCHAR | org | The country portion of the secondary caregiver's address. |
| 24 | `CAREGIVER_2_HOU_NUM` | VARCHAR |  | The house number portion of the secondary caregiver's address. |
| 25 | `CAREGIVER_2_DIST_C_NAME` | VARCHAR | org | The district portion of the secondary caregiver's address. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

