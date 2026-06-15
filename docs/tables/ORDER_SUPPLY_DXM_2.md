# ORDER_SUPPLY_DXM_2

> This table stores modifiers associated with a supply (from the related multiple Supply Modifiers (I ORD 52403) item).

**Primary key:** `ORDER_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record associated with this procedure order. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated supply in this supply modifier record. Together with ORDER_ID, this forms the foreign key to the ORDER_SUPPLY table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple supply modifiers that are associated with the supply and the order id from the ORDER_SUPPLY table. |
| 4 | `SUPPLY_MODIFIERS_ID` | VARCHAR |  | The unique ID of the modifiers for a supply charge. |
| 5 | `SUPPLY_MODIFIERS_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

