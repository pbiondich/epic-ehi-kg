# ORDER_INSTANTIATED

> This table contains a list of orders that have been instantiated.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record. |
| 2 | `LINE` | INTEGER | PK | The line count for this table as determined by the number of instantiated orders. |
| 3 | `INSTNTD_ORDER_ID` | NUMERIC |  | The ID for the instantiated order, the child. Note: For the case of the grandparent/parent/child scenario (Outpatient Recurring order released into an Inpatient/HOV setting), this column will store the child (i.e. “grandchild”) order and the ORDER_ID column will store the parent order. For the grandparent/parent order relationship, refer to STAND_HOV_INST_ORD.ORDER_ID (“grandparent”) and STAND_HOV_INST_ORD.STAND_INS_IP_ORD_ID (“parent”). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

