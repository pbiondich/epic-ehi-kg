# PRE_AR_ANES_EXCL

> Time period to exclude when calculating anesthesia concurrency. The full time range (without exclusion) can be found in the PRE_AR_ANES_TIMES table. Note: temporary accounts receivable (TAR) records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table might be lost if you truncate the table.

**Primary key:** `TAR_ID`, `CHARGE_LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier for the subject record. |
| 2 | `CHARGE_LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ANES_EXCL_START_TM` | DATETIME (Local) |  | The starting time of the period exclusion in anesthesia concurrency calculation. |
| 4 | `ANES_EXCL_START_DT` | DATETIME |  | The starting date of the period exclusion in anesthesia concurrency calculation. |
| 5 | `ANES_EXCL_END_TM` | DATETIME (Local) |  | The ending time of the period exclusion in anesthesia concurrency calculation. |
| 6 | `ANES_EXCL_END_DT` | DATETIME |  | The ending date of the period exclusion in anesthesia concurrency calculation. |
| 7 | `ANES_EXCL_CMT` | VARCHAR |  | The comment of the period exclusion in anesthesia concurrency calculation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

