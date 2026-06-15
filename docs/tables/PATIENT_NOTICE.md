# PATIENT_NOTICE

> The PATIENT_NOTICE table contains information on inpatient security alerts.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The ID of the patient with this notice. |
| 2 | `LINE` | INTEGER | PK | The line number of the notice for the patient. |
| 3 | `NOTICE_TYPE_C_NAME` | VARCHAR | org | The category value corresponding to the notice type for the patient. |
| 4 | `NOTICE_COMMENT` | VARCHAR |  | Free text comment concerning this notice. |
| 5 | `USER_ID` | VARCHAR | FK→ | The unique ID of the employee who entered this notice. |
| 6 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `UPDATE_TIME` | DATETIME (Local) |  | The date when this notice was last updated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

