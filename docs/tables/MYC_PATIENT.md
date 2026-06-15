# MYC_PATIENT

> The MYC_PATIENT table contains one row for each web-based chart system account. The data contained in each row consists of basic account information related to logins and passwords, as well as data that the patient has entered and stored in web-based chart system.

**Overflow family:** [MYC_PATIENT_2](MYC_PATIENT_2.md)  
**Primary key:** `MYPT_ID`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MYPT_ID` | VARCHAR | PK shared | The unique ID of the patient's web-based chart system account record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 3 | `SEX_C_NAME` | VARCHAR | org | Contains the sex for non-patient users. Sex for patients should be obtained from column SEX_C in table PATIENT. |
| 4 | `SSN` | VARCHAR |  | Non-patient user's social security number. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

