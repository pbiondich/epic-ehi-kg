# V_EHI_AUDIT_RT_HSB_ITEMS

> This view contains audit information for document records for the purpose of Electronic Health Information (EHI) export. If not in the EHI context, RAD_THERAPY_AUDIT_INFO should be used instead.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`, `RAD_THERAPY_AUD_INST_UTC_DTTM`, `CHANGED_DATA_ELEMENT`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID of the episode of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RAD_THERAPY_AUDIT_ITEM_NUM` | VARCHAR |  | Stores the updated item. |
| 4 | `RAD_THERAPY_AUD_ITEM_LINE_NUM` | VARCHAR |  | This item stores the item line that was updated. |
| 5 | `RAD_THERAPY_AUDIT_USER_ID` | VARCHAR |  | Stores the user responsible for item update. |
| 6 | `RAD_THERAPY_AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `OLD_VALUE_INTERNAL` | VARCHAR |  | Contains the old value of the item in internal chronicles format. |
| 8 | `NEW_VALUE_INTERNAL` | VARCHAR |  | Contains the new value of the item in internal chronicles format. |
| 9 | `OLD_VALUE_EXTERNAL` | VARCHAR |  | Contains the old value of the item in external format. |
| 10 | `NEW_VALUE_EXTERNAL` | VARCHAR |  | Contains the new value of the item in external format. |
| 11 | `CHANGED_DATA_ELEMENT` | VARCHAR | PK | The table and column descriptor associated with the item in the ITEM_NUMBER column. |
| 12 | `RAD_THERAPY_AUD_INST_UTC_DTTM` | DATETIME (UTC) | PK | Stores the instant at which the item was updated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

