# V_EHI_AUDIT_CLP

> This view contains one row for each audited item changed on a claim print record that corresponds to a column that is configured for EHI export.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the claim print record. |
| 2 | `LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 3 | `CHANGE_USER_ID` | VARCHAR |  | Stores the user ID of the person who performed edit operations. |
| 4 | `CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `CHANGE_UTC_DTTM` | DATETIME (Local) |  | Stores the date/time instance when the claim was edited. |
| 6 | `ITEM_CHANGE_CUR_LN` | INTEGER |  | Stores the current line number. |
| 7 | `ITEM_CHANGE_PREV_LN` | INTEGER |  | Stores the previous line number. |
| 8 | `OLD_VALUE_INTERNAL` | VARCHAR |  | Stores the old data value that was edited. |
| 9 | `OLD_VALUE_EXTERNAL` | VARCHAR |  | Stores the old data value, in an external format, that was edited. |
| 10 | `NEW_VALUE_INTERNAL` | VARCHAR |  | Stores the new data value that was added to the claim. |
| 11 | `NEW_VALUE_EXTERNAL` | VARCHAR |  | Stores the new data value, in an external format, that was edited. |
| 12 | `CHANGED_DATA_ELEMENT` | VARCHAR |  | The column descriptor that contains the metadata to be associated with data stored in columns OLD_VALUE_INTERNAL and NEW_VALUE_INTERNAL. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

