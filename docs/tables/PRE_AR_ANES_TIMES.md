# PRE_AR_ANES_TIMES

> This table stores the anesthesia start and end times for each line in a temporary transaction (TAR) record. *Note: TAR records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table may be lost if you truncate the table.

**Primary key:** `TAR_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier for the temporary transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `CE_ANES_START_DTTM` | DATETIME (Local) |  | The start date and time of the anesthesia procedure. |
| 4 | `CE_ANES_END_DTTM` | DATETIME |  | The end date and time of the anesthesia procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

