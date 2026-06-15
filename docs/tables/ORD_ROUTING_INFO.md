# ORD_ROUTING_INFO

> This table contains the PLF (patient location facility) record and/or department type used to get the routing information for the order record. It will only contain rows that have at least one value in either the ROUTING_DEPT_PLF_ID column or the ROUTING_DEPT_TYPE_C column.

**Primary key:** `ORDER_ID`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `ROUTING_DEPT_PLF_ID_RECORD_NAME` | VARCHAR |  | The name of the PLF record. |
| 3 | `ROUTING_DEPT_TYPE_C_NAME` | VARCHAR | org | The phase of care category ID for an order record, used as a routing department to route the order when a specific department is known. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

