# ORD_SCHED_TIMES

> Contains the scheduled times for procedure orders.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SCHEDULED_INST_DTTM` | DATETIME (Local) |  | Stores the scheduled times of this order |
| 4 | `SCHEDULE_STATUS_C_NAME` | VARCHAR |  | The schedule status category ID for each scheduled time of the order record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

