# STMT_CUSTOM_ITEM_2_LIST

> The table stores statement information about the custom multiple-response 2 item.

**Primary key:** `PRINT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier for the statement print or detail bill record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CUSTOM_ITEM` | VARCHAR |  | Custom multiple response item 2. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

