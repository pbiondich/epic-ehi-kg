# ORDER_CHG_DXMOD_2

> This table stores modifiers associated with a charge entered at end exam (from the related multiple Charge Modifiers (I ORD 52408) item).

**Primary key:** `ORDER_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record associated with this procedure order. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated charge in this charge modifier record. Together with ORDER_ID, this forms the foreign key to the ORD_PROC_CHG_EAPS table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple charge modifiers that are associated with the charge and the order id from the ORD_PROC_CHG_EAPS table. |
| 4 | `CHARGE_MODIFIERS_ID` | VARCHAR |  | The unique identifier for a modifier applied to a billing charge when ending an exam. |
| 5 | `CHARGE_MODIFIERS_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

