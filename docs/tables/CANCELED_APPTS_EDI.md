# CANCELED_APPTS_EDI

> This table contains the list of visit IDs of appointments that used to be linked to an order, but were cancelled due to the order being cancelled. This item is used by the incoming orders-to-cadence interface to rebook appointments if the order is un-cancelled.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CANCEL_APPTS_EDI` | INTEGER |  | List of appointment serial numbers (ASNs) linked to the order. |
| 4 | `CANC_APPT_PREV_STAT` | VARCHAR |  | This item holds the status of the appointments before cancellation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

