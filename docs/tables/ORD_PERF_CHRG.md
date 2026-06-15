# ORD_PERF_CHRG

> Links to performables (OPE) and chargeables (UCL) for an order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `PERFORMABLE_ID` | NUMERIC |  | Performables for the order. |
| 4 | `CHARGEABLE_ID` | VARCHAR |  | Chargeables for this order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

