# STMT_CUSTOM_ITEMS

> This table stores information about custom, single-response items on the statement.

**Primary key:** `PRINT_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier for the statement print or detail bill record. |
| 2 | `CUSTOM_ITEM_1` | VARCHAR |  | Custom single response item 1. |
| 3 | `CUSTOM_ITEM_2` | VARCHAR |  | Custom single response item 2. |
| 4 | `CUSTOM_ITEM_3` | VARCHAR |  | Custom single response item 3. |
| 5 | `CUSTOM_ITEM_4` | VARCHAR |  | Custom single response item 4. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

