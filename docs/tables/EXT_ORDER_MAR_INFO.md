# EXT_ORDER_MAR_INFO

> This table contains administration details for external medication orders.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MAR_TAKEN_INST_UTC_DTTM` | DATETIME (UTC) |  | This item saves the date and time when the administration action was taken on the external medication order. |
| 4 | `MAR_ACTION_C_NAME` | VARCHAR | org | This item saves the administration action for the external medication order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

