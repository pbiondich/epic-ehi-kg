# SCHEDULER_HX

> Inpatient scheduler history table.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SCH_EXTRA_ACTION_C_NAME` | VARCHAR |  | This item stores what special scheduler action, if any, was performed on scheduling. |
| 4 | `SCH_SKIPPED_DTTM` | DATETIME (Local) |  | The instant an occurrence was skipped by the scheduler because an off schedule occurrence was too close to a standard time. |
| 5 | `SCHEDULE_EXTRA_DTTM` | DATETIME (Local) |  | Time that an extra occurrence was scheduled since a standard specified time was just missed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

