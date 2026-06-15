# PATIENT_CONF_ADDR

> This table contains the patient's confidential address information.

**Primary key:** `PAT_ID`  
**Columns:** 12  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID for the patient record. |
| 2 | `CONF_CITY` | VARCHAR |  | The city associated with the patient's confidential address. |
| 3 | `CONF_STATE_C_NAME` | VARCHAR | org | The category value corresponding to the state that is associated with the patient's confidential address. |
| 4 | `CONF_COUNTRY_C_NAME` | VARCHAR | org | The category value corresponding to the country that is associated with the patient's confidential address. |
| 5 | `CONF_ZIP_CODE` | VARCHAR |  | The Zip Code that is associated with the patient's confidential address. |
| 6 | `CONF_CONTACT_PERSON` | VARCHAR |  | The name of the person who should be contacted at the patient's confidential address. |
| 7 | `CONF_EMAIL_ADDRESS` | VARCHAR |  | The patient’s confidential e-mail address. |
| 8 | `CONF_START_DATE` | DATETIME |  | The date in which the patient's confidential address should take effect for the patient. |
| 9 | `CONF_END_DATE` | DATETIME |  | The date in which the patient's confidential address should expire for the patient. |
| 10 | `CONF_COUNTY_C_NAME` | VARCHAR | org | The category value corresponding to the county that is associated with the patient's confidential address. |
| 11 | `CONF_HOUSE_NUM` | VARCHAR |  | The house number associated with the patient's confidential address. |
| 12 | `CONF_DISTRICT_C_NAME` | VARCHAR | org | The category value corresponding to the district that is associated with the patient's confidential address. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

