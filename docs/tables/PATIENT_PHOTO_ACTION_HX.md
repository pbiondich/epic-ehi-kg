# PATIENT_PHOTO_ACTION_HX

> History of actions taken on the Patient Photo checklist section.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PATIENT_PHOTO_ACTION_TAKEN_C_NAME` | VARCHAR |  | The action taken on the Patient Photo checklist section |
| 4 | `PATIENT_PHOTO_USER_ID` | VARCHAR |  | User who took the action on the Patient Photo checklist section |
| 5 | `PATIENT_PHOTO_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `PHOTO_TIMESTAMP_UTC_DTTM` | DATETIME (UTC) |  | Date and time the action was taken on the Patient Photo checklist section |
| 7 | `PHOTO_LOGIN_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 8 | `PHOTO_ENC_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 9 | `PHOTO_ENC_DEPARTMENT_DTTM` | DATETIME (Local) |  | Date and time the action was taken on the Patient Photo checklist section in the timezone of the encounter department |
| 10 | `PHOTO_LOGIN_DEPARTMENT_DTTM` | DATETIME (Local) |  | Date and time the action was taken on the Patient Photo checklist section in the timezone of the login department |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

