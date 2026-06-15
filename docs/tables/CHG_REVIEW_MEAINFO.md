# CHG_REVIEW_MEAINFO

> The table stores the measurement information (MEA segment information) entered in a charge session. Each row in the table is one line of measurement for one procedure, including MEA reference ID code, MEA qualifier, MEA value, and MEA date. Note: temporary accounts receivable (TAR) records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table might be lost if you truncate the table.

**Primary key:** `TAR_ID`, `LINE`, `MEA_LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier of the temporary transaction record on which the charge review activity is performed. |
| 2 | `LINE` | INTEGER | PK | The line count for the item. This represents a single charge procedure on the temporary transaction record. |
| 3 | `MEA_LINE` | INTEGER | PK | The line count for the measurement information entered for a procedure. |
| 4 | `MEA_REF_ID_C` | INTEGER |  | The measurement reference ID code for a procedure. |
| 5 | `MEA_QUALIFIER_C` | VARCHAR |  | The measurement qualifier for a procedure. |
| 6 | `MEA_VALUE` | FLOAT |  | The measurement value for a procedure. |
| 7 | `MEA_DATE` | DATETIME |  | The date the measurement was collected for a procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

