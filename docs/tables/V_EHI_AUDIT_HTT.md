# V_EHI_AUDIT_HTT

> This view contains one row for each audited item changed on a transaction record that corresponds to a column that is configured for EHI export.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHANGE_USER_ID` | VARCHAR |  | This column stores the user who changed the items on the record. |
| 4 | `CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `CHANGE_UTC_DTTM` | DATETIME (UTC) |  | This column stores the date and time of data change on the record. |
| 6 | `TRANSACTION_LINE` | INTEGER |  | This column stores on which line the data change happened. It will be blank if the change is not specific to a line. |
| 7 | `ITEM_CHANGE_LN` | INTEGER |  | This column stores on which item line the record's item changes. It is only set for multiple response item value changes. |
| 8 | `OLD_VALUE_INTERNAL` | VARCHAR |  | Stores the old data value that was changed on the temporary transaction. If you use IntraConnect, this is the CID of the old stored value. |
| 9 | `OLD_VALUE_EXTERNAL` | VARCHAR |  | This column stores the previous value, in an external format, of the changed item in the record's audit history. This column shows the translated external value as of when the column was last extracted. |
| 10 | `NEW_VALUE_INTERNAL` | VARCHAR |  | Stores the new data value that was added to the temporary transaction. If you use IntraConnect, this is the CID of the new stored value. |
| 11 | `NEW_VALUE_EXTERNAL` | VARCHAR |  | This column stores the new value, in an external format, of the changed item in the record's audit history. This column shows the translated external value as of when the column was last extracted. |
| 12 | `CHANGED_DATA_ELEMENT` | VARCHAR |  | The column descriptor that contains the metadata to be associated with data stored in columns OLD_VALUE_INTERNAL and NEW_VALUE_INTERNAL. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

