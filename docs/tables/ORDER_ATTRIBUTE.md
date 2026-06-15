# ORDER_ATTRIBUTE

> The ORDER_ATTRIBUTE table enables you to report on attributes for each order. Currently, you could use value 1 to get all order that pyxis override.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique order ID |
| 2 | `LINE` | INTEGER | PK | The line number for the order attributes (I ORD 32). |
| 3 | `ORD_ATTRIBUTE_C_NAME` | VARCHAR |  | The attribute information for the specified order ID and line |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

