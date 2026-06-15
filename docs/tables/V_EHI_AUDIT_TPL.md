# V_EHI_AUDIT_TPL

> This view contains audit information for document records for the purpose of Electronic Health Information (EHI) export. If not in the EHI context, TPL_AUDIT_TRAIL should be used instead.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`, `AUD_UPDATE_LOCAL_DTTM`, `CHANGED_DATA_ELEMENT`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUD_ITM_NUM` | INTEGER |  | Stores the item number that was updated. |
| 4 | `AUD_ITM_ASSOCIATED_LINE_NUM` | INTEGER |  | If the item in the AUD_ITM_NUM column is related response or multiple response, this column (AUD_ITM_ASSOCIATED_LINE_NUM) stores the line number of the value that was updated. |
| 5 | `AUD_USER_ID` | VARCHAR |  | Stores the user who modified the item. |
| 6 | `AUD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `OLD_VALUE_INTERNAL` | VARCHAR |  | Stores the old value of the item that was changed in internal format. |
| 8 | `NEW_VALUE_INTERNAL` | VARCHAR |  | Stores the new value of the item that was changed in internal format. |
| 9 | `OLD_VALUE_EXTERNAL` | VARCHAR |  | Stores the old value of the item that was changed in external format. |
| 10 | `NEW_VALUE_EXTERNAL` | VARCHAR |  | Stores the new value of the item that was changed in external format. |
| 11 | `CHANGED_DATA_ELEMENT` | VARCHAR | PK | The name of the Clarity table and column corresponding to the changed data. |
| 12 | `AUD_UPDATE_LOCAL_DTTM` | DATETIME (Local) | PK | Stores the instant at which the item was updated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

