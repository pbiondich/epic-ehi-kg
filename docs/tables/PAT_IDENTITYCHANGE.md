# PAT_IDENTITYCHANGE

> This table contains information regarding the identity (demographic) changes that are made to the patient. The identity changes include changes to a patient's name, sex, Social Security number and/or date of birth. Whenever a user tries to change the above identity information in the graphical user interface (GUI) this table logs the action.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 16  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this row. Multiple pieces of information can be associated with this row. |
| 3 | `ID_CHANGE_INSTANT` | DATETIME (Local) |  | The instant when someone edited this patient's identity. |
| 4 | `ID_CHANGE_USER_ID` | VARCHAR |  | User that changed patient demographics and triggered a potential overlay. |
| 5 | `ID_CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `ID_CHANGE_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 7 | `ID_CHANGE_REASON_C_NAME` | VARCHAR | org | Reason selected by user to indicate why the patient's identity is changed. |
| 8 | `ID_CHG_OLD_NAME` | VARCHAR |  | Name before the change. |
| 9 | `ID_CHG_OLD_SSN` | VARCHAR |  | Social security number before change. |
| 10 | `ID_CHANGE_OLD_SEX_C_NAME` | VARCHAR | org | The category ID of the patient's sex before the change. |
| 11 | `ID_CHG_OLD_DOB_DT` | DATETIME |  | Birth date before change. |
| 12 | `ID_CHANGE_NEW_NAME` | VARCHAR |  | The patient's name after the change. |
| 13 | `ID_CHANGE_NEW_SSN` | VARCHAR |  | Social security number after change. |
| 14 | `ID_CHANGE_NEW_SEX_C_NAME` | VARCHAR |  | The category ID of the patient's sex after the change. |
| 15 | `ID_CHG_NEW_DOB_DT` | DATETIME |  | Birth date after change. |
| 16 | `ID_CHANGE_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

