# CHG_REVIEW_ACT_AUD

> Professional billing charge review activity auditing. Note: temporary accounts receivable (TAR) records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table might be lost if you truncate the table.

**Primary key:** `TAR_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier for the temporary transaction record on which the charge review activity is performed. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACT_LINE_REF` | NUMERIC |  | The line number of the Charge Review History group on which the related activity is performed. Other items on the line have the information regarding which data field is changed by the activity, the old value, and the new value. |
| 4 | `DATA_FIELD` | NUMERIC |  | The temporary transaction item number for the field whose data is changed by the activity. |
| 5 | `OLD_VALUE` | VARCHAR |  | The value of the item before changing |
| 6 | `NEW_VALUE` | VARCHAR |  | The item value after changing |
| 7 | `DATA_FIELD_LINE` | NUMERIC |  | The line number for multiple response or related group data field. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

