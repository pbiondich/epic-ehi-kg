# V_EHI_ORD_ITM_AUDIT_TRL

> This view contains an audit history of several Orders items, along with human-readable versions of the old and new values and references to Clarity columns that extract those items.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OLD_VALUE_INTERNAL` | VARCHAR |  | Contains the old value for the item that was changed. |
| 4 | `NEW_VALUE_INTERNAL` | VARCHAR |  | Contains the new value for the item that was changed. |
| 5 | `OLD_VALUE_EXTERNAL` | VARCHAR |  | Contains the old value for the item that was changed, in external format. This column shows the translated external value as of when the column was last extracted. |
| 6 | `NEW_VALUE_EXTERNAL` | VARCHAR |  | Contains the new value for the item that was changed, in external format. This column shows the translated external value as of when the column was last extracted. |
| 7 | `ITEM_CHNG_USER_ID` | VARCHAR |  | Contains the ID of the user who changed the item. |
| 8 | `ITEM_CHNG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `ITEM_CHANGE_DTTM` | DATETIME (Local) |  | Contains the instant the item was changed. |
| 10 | `CHANGED_DATA_ELEMENT` | VARCHAR |  | The table and column descriptor associated with the item in the ITEM column. |
| 11 | `ITEM` | VARCHAR |  | The item number for the item that was changed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

