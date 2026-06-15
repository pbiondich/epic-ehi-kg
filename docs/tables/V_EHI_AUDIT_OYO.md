# V_EHI_AUDIT_OYO

> This view contains audit information for communication preferences records for the purpose of Electronic Health Information (EHI) export. If not in the EHI context, AUDIT_ITM_COMM_PREF should be used instead.

**Primary key:** `PREFERENCES_ID`, `CHANGE_TIME`, `CHANGED_DATA_ELEMENT`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PREFERENCES_ID` | NUMERIC | PK FK→ | The ID of the communication preference record that was changed. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The ID of the patient associated with this communication preference record. |
| 3 | `CHANGE_TIME` | DATETIME (Local) | PK | The time the information in the record was changed. |
| 4 | `LINE` | INTEGER | PK | Indicates which line of the item this row holds. This is used for items which can have multiple responses. |
| 5 | `NEW_VALUE_EXTERNAL` | VARCHAR |  | The value after the change, in external format. This column shows the translated external value as of when the column was last extracted. |
| 6 | `OLD_VALUE_EXTERNAL` | VARCHAR |  | The value before the change, in external format. This column shows the translated external value as of when the column was last extracted. |
| 7 | `NEW_VALUE_INTERNAL` | VARCHAR |  | The value after the change, in internal format. |
| 8 | `OLD_VALUE_INTERNAL` | VARCHAR |  | The value before the change, in internal format. |
| 9 | `CHANGED_DATA_ELEMENT` | VARCHAR | PK | The name of the Clarity table and column corresponding to the changed data. |
| 10 | `USER_ID` | VARCHAR | FK→ | The ID of the user that made the change. |
| 11 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `PREFERENCES_ID` | [COMM_PREF_ADDL_ITEMS](COMM_PREF_ADDL_ITEMS.md) | sole_pk | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

