# V_EHI_AUDIT_EPT

> This view contains audit information for patient records for the purpose of Electronic Health Information (EHI) export. This view contains patient-level patient data. If not in the EHI context, AUDIT_ITM_PATIENT should be used instead.

**Primary key:** `PAT_ID`, `CHANGE_TIME`, `CHANGED_DATA_ELEMENT`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The ID of the patient record that was changed. |
| 2 | `CHANGE_TIME` | DATETIME (Local) | PK | The time the information in the record was changed. |
| 3 | `LINE` | INTEGER | PK | A value needed when the item that changed was multiple response. |
| 4 | `NEW_VALUE_EXTERNAL` | VARCHAR |  | The value after the change, in external format. This column shows the translated external value as of when the column was last extracted. |
| 5 | `OLD_VALUE_EXTERNAL` | VARCHAR |  | The value before the change, in external format. This column shows the translated external value as of when the column was last extracted. |
| 6 | `NEW_VALUE_INTERNAL` | VARCHAR |  | The value after the change, in internal format. |
| 7 | `OLD_VALUE_INTERNAL` | VARCHAR |  | The value before the change, in internal format. |
| 8 | `CHANGED_DATA_ELEMENT` | VARCHAR | PK | The name of the Clarity table and column corresponding to the changed data. |
| 9 | `USER_ID` | VARCHAR | FK→ | The ID of the user that made the change. |
| 10 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

