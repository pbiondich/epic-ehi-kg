# ORD_CALC_IONS

> Clarity table to store the calculated ion amounts for an ion based TPN order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CALC_ION_C_NAME` | VARCHAR |  | This column contains the name of the ion from the TPN order that the calculated amount and unit from columns CALC_ION_AMOUNT and CALC_ION_UNIT_C from the same line apply to. |
| 4 | `CALC_ION_AMOUNT` | NUMERIC |  | This column contains the unrounded calculated amount of ion for a total parenteral nutrition (TPN) order. |
| 5 | `CALC_ION_UNIT_C_NAME` | VARCHAR | org | This column contains the unit for the calculated amount of ion for a total parenteral nutrition (TPN) order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

