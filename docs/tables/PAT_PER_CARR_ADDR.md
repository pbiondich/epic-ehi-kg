# PAT_PER_CARR_ADDR

> The PAT_PER_CARR_ADDR table contains patient information as specified by the carrier.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 26  
**Org-specific columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting’s encryption utility. |
| 2 | `LINE` | INTEGER | PK | The line number used to identify each line of patient info as specified by the carrier. |
| 3 | `CARR_ADDR_DATE` | DATETIME |  | The effective date of the carrier information. |
| 4 | `CARR_ADDR_CITY` | VARCHAR |  | The city of the patient address as specified by the carrier. |
| 5 | `CARR_ADDR_ZIP` | VARCHAR |  | The ZIP Code of the patient address as specified by the carrier. |
| 6 | `CARR_ADDR_HM_PHONE` | VARCHAR |  | The home phone number of the patient as specified by the carrier. |
| 7 | `CARR_ADDR_WK_PHONE` | VARCHAR |  | The work phone number of the patient as specified by the carrier. |
| 8 | `CARR_ADDR_PAT_NAME` | VARCHAR |  | The name of the patient as specified by the carrier. |
| 9 | `CARR_ADDR_BDATE` | DATETIME |  | The birth date of the patient as specified by the carrier. |
| 10 | `CARR_ADDR_SEX_C_NAME` | VARCHAR | org | The category value of the sex of the patient as specified by the carrier. |
| 11 | `CARRIER_ID` | VARCHAR | FK→ | The unique ID of the carrier for the patient. |
| 12 | `CARRIER_ID_CARRIER_NAME` | VARCHAR |  | The name of the carrier record. |
| 13 | `CARR_ADDR_COUNTY_C_NAME` | VARCHAR | org | The category value corresponding to the county in which the patient lives as specified by the carrier. |
| 14 | `CARR_ADDR_GENDER_IDENTITY_C_NAME` | VARCHAR | org | Stores carrier specific gender identity. |
| 15 | `CARR_ADDR_HOUSE_NUMBER` | VARCHAR |  | Stores the address house number as specified by the carrier. |
| 16 | `CARR_ADDR_DISTRICT_C_NAME` | VARCHAR | org | Stores unique identifier of the address district as specified by the carrier. |
| 17 | `CARR_ADDR_COUNTRY_C_NAME` | VARCHAR | org | Stores unique identifier of the address country as specified by the carrier. |
| 18 | `CARR_ADDR_NAME_RECORD_ID` | VARCHAR |  | The name record of the patient as specified by the carrier. This column is frequently used to link to the NAMES table. |
| 19 | `CARR_ADDR_MBI` | VARCHAR |  | The Medicare Beneficiary Identifier (MBI) of the patient, as specified by the carrier. |
| 20 | `CARR_ADDR_ETHNIC_GROUP_C_NAME` | VARCHAR | org | The external source ethnic group category ID for the patient. |
| 21 | `CARR_ADDR_SEX_ASGN_AT_BIRTH_C_NAME` | VARCHAR | org | Stores sex assigned at birth as specified by an external source. |
| 22 | `CARR_ADDR_SOURCE_NAME` | VARCHAR |  | The source of the patient information as specified by an external source. |
| 23 | `CARR_ADDR_PRONOUN` | VARCHAR |  | The member pronoun information as specified by an external source. |
| 24 | `CARR_ADDR_PREFERRED_LANGUAGE_C_NAME` | VARCHAR | org | Preferred language as specified by an external source |
| 25 | `CARR_ADDR_NEEDS_INTERPRETER_YN` | VARCHAR |  | Whether the patient needs an interpreter as specified by an external source. |
| 26 | `CARR_ADDR_PRONOUN_CMT` | VARCHAR |  | A free-text field for documenting comments or instructions relating to a member's pronouns related to an external source. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CARRIER_ID` | [CLARITY_CARRIER](CLARITY_CARRIER.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

