# ORD_SCHED_INSTR

> Appointments can be scheduled from an order. This table contains scheduling instructions for an appointment created from an order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique system identifier of the order record (ORD dot one) |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORDER_SCHED_INSTR` | VARCHAR |  | This column contains scheduling instructions for appointments scheduled from the associated order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

