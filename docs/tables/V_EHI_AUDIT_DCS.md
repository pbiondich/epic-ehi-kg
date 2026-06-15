# V_EHI_AUDIT_DCS

> This view contains audit information for document records for the purpose of Electronic Health Information (EHI) export. If not in the EHI context, DOC_INFO_AUDIT should be used instead.

**Primary key:** `DOC_INFO_ID`, `CHANGE_TIME`, `CHANGED_DATA_ELEMENT`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOC_INFO_ID` | VARCHAR | PK FK→ | The unique ID of the document information record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient associated with the document record. |
| 3 | `CHANGE_TIME` | DATETIME (Local) | PK | The instant when the value was changed. |
| 4 | `LINE` | INTEGER | PK | Audit of the line number that changed |
| 5 | `NEW_VALUE_EXTERNAL` | VARCHAR |  | The value after the audited change in external format. This column shows the translated external value as of when the column was last extracted. |
| 6 | `OLD_VALUE_EXTERNAL` | VARCHAR |  | The value before the audited change in external format. This column shows the translated external value as of when the column was last extracted. |
| 7 | `NEW_VALUE_INTERNAL` | VARCHAR |  | The value of the item after it was changed in internal format. |
| 8 | `OLD_VALUE_INTERNAL` | VARCHAR |  | The value of the item before it was changed in internal format. |
| 9 | `CHANGED_DATA_ELEMENT` | VARCHAR | PK | The name of the Clarity table and column corresponding to the changed data. |
| 10 | `USER_ID` | VARCHAR | FK→ | The ID of the employee who changed the item. |
| 11 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DOC_INFO_ID` | [DOC_INFORMATION](DOC_INFORMATION.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

