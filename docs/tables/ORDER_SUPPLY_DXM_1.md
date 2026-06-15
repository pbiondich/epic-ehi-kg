# ORDER_SUPPLY_DXM_1

> This is the table for billing diagnoses associated with a supply (from the related multiple Supply Diagnoses (I ORD 52402) item).

**Primary key:** `ORDER_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record associated with this procedure order. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated supply in this billing diagnosis record. Together with ORDER_ID, this forms the foreign key to the ORDER_SUPPLY table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple billing diagnoses that are associated with the supply and the order id from the ORDER_SUPPLY table. |
| 4 | `SUPPLY_DIAGNOSES_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

