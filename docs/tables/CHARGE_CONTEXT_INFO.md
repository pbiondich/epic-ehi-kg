# CHARGE_CONTEXT_INFO

> This table contains charge triggering timestamps. Each row contains the timestamp charges were triggered for a specified charge context for an order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHARGE_CONTEXT_C_NAME` | VARCHAR | org | The charging context category ID under which charges were triggered for the order. |
| 4 | `CHARGE_CONTEXT_DTTM` | DATETIME (UTC) |  | Instant a charge was triggered for a given context. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

