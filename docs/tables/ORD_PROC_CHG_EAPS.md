# ORD_PROC_CHG_EAPS

> This table is to extract the associated procedure charges for imaging procedures.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line count for this table as determined by the number of linked chargeables associated with this order. |
| 3 | `CHARGEABLE_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `CHARGEABLE_PROC_QUA` | NUMERIC |  | Quantity of the chargeable procedure involved in an exam. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

