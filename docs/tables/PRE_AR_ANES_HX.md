# PRE_AR_ANES_HX

> Contains history of activities performed on Anesthesia charge. Information about the activity, time at which the activity is performed, user performing the activity and comment are stored. Note: temporary accounts receivable (TAR) records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table might be lost if you truncate the table.

**Primary key:** `TAR_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier for the temporary transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ANES_HX_ACTIVITY_C_NAME` | VARCHAR |  | The activity category ID performed on an Anesthesia temporary transaction. |
| 4 | `ANES_HX_TIMES_DTTM` | DATETIME (Local) |  | Contains the time when the activity is performed on Anesthesia charge. |
| 5 | `ANES_HX_USER_ID` | VARCHAR |  | User who performed the activity on Anesthesia charge. |
| 6 | `ANES_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `ANES_HX_COMMENT` | VARCHAR |  | Comment for the activity performed on Anesthesia charge. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

