# ORD_LAB_LINKED_ORD

> Contains a list of orders a (lab) order is linked to.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LAB_LINKED_ORD_ID` | NUMERIC |  | The unique identifier of the order record for this row this order is linked to. |
| 4 | `LINK_TYPE_C_NAME` | VARCHAR | org | The link type category number for this linked order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

