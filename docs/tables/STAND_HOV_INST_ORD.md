# STAND_HOV_INST_ORD

> The records in this table contain child order IDs of standing orders released in an HOV encounter.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record. This is the “grandparent” order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `STAND_INS_IP_ORD_ID` | NUMERIC |  | The unique ID of the instantiated hospital outpatient visit child orders (i.e. the “parent” order in the grandparent/parent/child structure). Note that the order in this column may also be found in ORDER_INSTANTIATED.ORDER_ID (assuming that child orders have been released from this order). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

