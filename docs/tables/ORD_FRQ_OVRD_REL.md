# ORD_FRQ_OVRD_REL

> For frequency overrides that have a different set of times on each day, this table gives the times for each day.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the procedure order record that was reviewed. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EFQ_OVRD_REL_DAYS` | INTEGER |  | Contains the days for a frequency override. Column EFQ_OVRD_REL_TIMES specifies the times for these days. |
| 4 | `EFQ_OVRD_REL_TIME` | DATETIME (Local) |  | Contains the times for a frequency override. Column EFQ_OVRD_REL_DAYS specifies the days for these times. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

