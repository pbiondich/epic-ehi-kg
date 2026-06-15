# ORD_SPEC_COLL

> This table contains the IDs of the specimens (HSC records) that were collected with this order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with an order record. Multiple specimens can be associated with one order record. |
| 3 | `SPEC_COLL_ID` | NUMERIC |  | The IDs of specimens (HSC) collected for an order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

