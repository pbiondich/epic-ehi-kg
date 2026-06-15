# V_EHI_AUDIT_CVG

> This view contains audit information for coverage records for the purpose of EHI export. This view only contains data that applies to all members on a coverage. If not in the EHI context, AUDIT_ITM_COVERAGE should be used instead.

**Primary key:** `COVERAGE_ID`, `CHANGE_TIME`, `CHANGED_DATA_ELEMENT`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The ID of the coverage record that was changed. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The ID of the patient associated with this coverage. |
| 3 | `CHANGE_TIME` | DATETIME (Local) | PK | The time the information in the record was changed. |
| 4 | `LINE` | INTEGER | PK | A value needed when the item that changed was multiple response. |
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
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

