# V_EHI_AUDIT_HTR

> This view contains one row for each audited item changed on a transaction record that corresponds to a column that is configured for EHI export.

**Primary key:** `TX_ID`, `LINE`, `CHANGED_DATA_ELEMENT`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHANGE_USER_ID` | VARCHAR |  | This item stores the user who changed the hospital temporary transaction items while the hospital billing transaction is in its temporary state. It is part of the hospital billing transaction audit history. |
| 4 | `CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `CHANGE_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant of data change on a hospital temporary transaction when a hospital billing transaction is in its temporary state. |
| 6 | `ITEM_CHANGE_LINE` | INTEGER |  | This item stores on which item line a hospital temporary transaction item changes. It is only set for multiple response item value changes. It is part of the hospital billing transaction audit history. |
| 7 | `OLD_VALUE_INTERNAL` | VARCHAR |  | This item stores the previous value of the changed hospital temporary transaction item when the hospital billing transaction is in its temporary state. It is part of the hospital billing transaction audit history. |
| 8 | `OLD_VALUE_EXTERNAL` | VARCHAR |  | This item stores the previous value, in an external format, of the changed hospital temporary transaction item when the hospital billing transaction is in its temporary state. It is part of the hospital billing transaction audit history. |
| 9 | `NEW_VALUE_INTERNAL` | VARCHAR |  | This item stores the new value of the changed hospital temporary transaction item when a hospital billing transaction is in its temporary state. It is part of the hospital billing transaction audit history. |
| 10 | `NEW_VALUE_EXTERNAL` | VARCHAR |  | This item stores the new value, in an external format, of the changed hospital temporary transaction item when the hospital billing transaction is in its temporary state. It is part of the hospital billing transaction audit history. |
| 11 | `CHANGED_DATA_ELEMENT` | VARCHAR | PK | The column descriptor that contains the metadata to be associated with data stored in columns OLD_VALUE_INTERNAL and NEW_VALUE_INTERNAL. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

