# ORDER_TPN_CALCINFO

> This table holds calculated Total Parenteral Nutrition (TPN) data for components and mixture compatibility calculations, including component, amount, and unit.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TPN_DATA_COMP_C_NAME` | VARCHAR |  | The component or mixture compatibility calculation category ID for the order. |
| 4 | `TPN_DATA_UNIT_C_NAME` | VARCHAR | org | Unit of amount for the component or compatibility check |
| 5 | `TPN_DATA_AMT` | NUMERIC |  | Amount for corresponding component or compatibility check |
| 6 | `TPN_DATA_AMT_MAX` | NUMERIC |  | If the component has a ranged value, this will be the upper bound. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

