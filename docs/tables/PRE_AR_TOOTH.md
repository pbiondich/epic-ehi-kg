# PRE_AR_TOOTH

> This table contains tooth information for a single temporary accounts receivable (TAR) line. This data is coming from the Dental-Tooth Numbers (I TAR 508) item. Note: TAR records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table might be lost if you truncate the table.

**Primary key:** `TAR_ID`, `CHARGE_LINE`, `TOOTH_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier for the subject record. |
| 2 | `CHARGE_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `TOOTH_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `TOOTH_NUM_C_NAME` | VARCHAR |  | The tooth number category ID for the temporary transaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

