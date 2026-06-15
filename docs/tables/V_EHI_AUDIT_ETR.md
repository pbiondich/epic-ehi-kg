# V_EHI_AUDIT_ETR

> This view contains one row for each audited item changed on a transaction record that corresponds to a column that is configured for EHI export.

**Primary key:** `TX_ID`, `LINE`, `CHANGED_DATA_ELEMENT`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHANGE_USER_ID` | VARCHAR |  | Stores the user ID of the person who performed edit operations. |
| 4 | `CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `CHANGE_UTC_DTTM` | DATETIME (UTC) |  | Instant of change for the transaction history. |
| 6 | `ITEM_CHANGE_LINE` | NUMERIC |  | The transaction line that was changed from transaction edit. |
| 7 | `OLD_VALUE_INTERNAL` | VARCHAR |  | The edited items previous value. |
| 8 | `OLD_VALUE_EXTERNAL` | VARCHAR |  | The edited items previous value, in an external format. This column shows the translated external value as of when the column was last extracted. |
| 9 | `NEW_VALUE_INTERNAL` | VARCHAR |  | The edited items new value. |
| 10 | `NEW_VALUE_EXTERNAL` | VARCHAR |  | The edited items new value, in an external format. This column shows the translated external value as of when the column was last extracted. |
| 11 | `CHANGED_DATA_ELEMENT` | VARCHAR | PK | The column descriptor that contains the metadata to be associated with data stored in columns OLD_VALUE_INTERNAL and NEW_VALUE_INTERNAL. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

