# IMG_COMP_STUDIES

> This table holds comparison study information for orders.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record for this row. This column is frequently used to link to the ORDER_PROC table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMP_STUDIES_ID` | NUMERIC |  | The unique order ID for studies marked as comparison studies for the current order record. This column is frequently used to link to the ORDER_PROC table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

