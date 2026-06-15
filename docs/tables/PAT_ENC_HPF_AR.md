# PAT_ENC_HPF_AR

> This patient encounter table contains Professional Billing Hospital Professional Fee encounters. The primary key for the patient encounter table is PAT_ENC_CSN_ID.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. Digits after the decimal point indicate multiple visits on one day. |
| 2 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 3 | `CONTACT_DATE` | DATETIME |  | For Hospital Professional Fee encounters, this is the admit date in calendar format. |
| 4 | `HPF_ENC_STATUS_C_NAME` | VARCHAR | org | The Hospital Professional Fee encounter status category ID for the patient. |
| 5 | `HPF_EM_CODE_REQ_YN` | VARCHAR |  | Indicates whether the Hospital Professional Fee encounter for the patient meets E&M code requirements. |
| 6 | `AR_HPF_ENC_VST_CSN` | NUMERIC |  | This column contains the contact serial number which links the hospital professional fee (HPF) contact with the visit contact. This CSN is the unique contact serial number for the visit contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

