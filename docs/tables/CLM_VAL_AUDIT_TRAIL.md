# CLM_VAL_AUDIT_TRAIL

> This table contains a list of the changes made by the user directly to the claim. Changes that occur because of changes to source data or configuration are not listed here. For multiple and related items, line numbers are included. For related multi items, the value position number within the line is included.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim value record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_LINK` | INTEGER |  | A line number that can be used to link the audit details in this table to a user action in VALUE_EDIT_HISTORY. |
| 4 | `AUDIT_EVENT_C_NAME` | VARCHAR |  | The event category ID for the type of change the user made to the claim. |
| 5 | `AUDIT_ITEM_C_NAME` | VARCHAR | org | The category ID of the item the user changed. |
| 6 | `AUDIT_OLD_LINE` | INTEGER |  | The previous line number for the item in AUDIT_ITEM_C that was changed. It will only be populated when the item is multiple response or part of a related group. |
| 7 | `AUDIT_OLD_POS` | INTEGER |  | The previous value position number for the item in AUDIT_ITEM_C that was changed. It will only be populated for related multi items. |
| 8 | `AUDIT_OLD_VAL` | VARCHAR |  | The value before the user's change. |
| 9 | `AUDIT_NEW_LINE` | INTEGER |  | The new line number for the item in AUDIT_ITEM_C that was changed. It will only be populated when the item is multiple response or part of a related group. |
| 10 | `AUDIT_NEW_POS` | INTEGER |  | The new value position number for the item in AUDIT_ITEM_C that was changed. It will only be populated for related multi items. |
| 11 | `AUDIT_NEW_VAL` | VARCHAR |  | The value after the user's change. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

