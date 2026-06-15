# BLOOD_SPECIAL_REQTS

> This table contains the list of the patient's current blood special requirements.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BLOOD_SPECIAL_REQTS_C_NAME` | VARCHAR | org | The special requirements category ID for a patient who has special requirements for blood transfusions. |
| 4 | `BLOOD_SPECIAL_REQTS_DEGREE_C_NAME` | VARCHAR | org | The category ID of the degree to which a blood special requirement is critical for patient care. |
| 5 | `BLOOD_SPECIAL_REQTS_ADD_INFO` | VARCHAR |  | This item stores additional information to describe a blood special requirement in cases where the name does not adequately describe the requirement. This item can also be used to describe why the requirement is necessary. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

