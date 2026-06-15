# PATIENT_ALG_UPD_HX

> The PATIENT_ALG_UPD_HX table contains one record for each update of a patient's allergy information.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID assigned to the patient record. |
| 2 | `LINE` | INTEGER | PK | The line number of a specific allergy update in the patient's allergy update history. This is the second column in the primary key and, in addition to the patient ID, uniquely identifies a patient allergy update. |
| 3 | `ALRG_UPDT_DATE` | DATETIME |  | The date on which the patient's allergy history was updated. |
| 4 | `ALRG_UPDT_USER_ID` | VARCHAR |  | The user who last updated the patient's allergy history. |
| 5 | `ALRG_UPDT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `ALRG_UPDT_TIME` | DATETIME |  | The time at which the patient's allergy history was updated. |
| 7 | `ALRG_HX_REV_STAT_C_NAME` | VARCHAR | org | This item stores the history of the status of the review of allergies. |
| 8 | `ALRG_HX_REV_REAS_C_NAME` | VARCHAR | org | This item stores the history of the review reason of allergies. |
| 9 | `ALRG_UPDT_DTTM` | DATETIME |  | The date and time at which the patient's allergy history was updated. |
| 10 | `ALRG_HX_REV_EPT_CSN` | NUMERIC |  | This column contains historical entries for the source encounter where allergies were reviewed. If allergies were reviewed outside the context of an encounter, the value is null. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

