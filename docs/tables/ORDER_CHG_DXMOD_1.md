# ORDER_CHG_DXMOD_1

> This table stores billing diagnoses associated with a charge entered at end exam (from the related multiple Charge Billing Diagnoses (I ORD 52407) item).

**Primary key:** `ORDER_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record associated with this procedure order. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated charge in this billing diagnosis record. Together with ORDER_ID, this forms the foreign key to the ORD_PROC_CHG_EAPS table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple billing diagnoses that are associated with the charge and the order id from the ORD_PROC_CHG_EAPS table. |
| 4 | `CHARGE_DIAGNOSES_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

