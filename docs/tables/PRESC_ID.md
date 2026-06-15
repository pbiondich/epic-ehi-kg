# PRESC_ID

> This table contains the prescription ID of an order that is populated by an interface.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID for the Order record for the prescription. |
| 2 | `LINE` | INTEGER | PK | The line number for the prescription ID. Multiple pieces of information can be associated with this contact. |
| 3 | `PRESC_ID` | VARCHAR |  | The prescription ID of the order populated by an interface. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

