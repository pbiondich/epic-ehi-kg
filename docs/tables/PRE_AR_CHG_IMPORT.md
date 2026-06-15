# PRE_AR_CHG_IMPORT

> This table contains information about imported charges such as raw data and description. Note: temporary accounts receivable (TAR) records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table might be lost if you truncate the table.

**Primary key:** `TAR_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier for the temporary transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHG_IMPORT` | NUMERIC |  | Information about imported charges. |
| 4 | `CHG_IMPORT_TAR` | NUMERIC |  | Transaction import temporary transaction item. |
| 5 | `CHG_IMPORT_RAWDATA` | VARCHAR |  | Raw data of imported charge. |
| 6 | `CHG_IMPORT_DESC` | VARCHAR |  | Description of imported charge. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

