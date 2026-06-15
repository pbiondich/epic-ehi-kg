# EXTERNAL_ORDER_INFO

> This table contains data about medication orders in external encounters that was received but could not be stored discretely.

**Primary key:** `ORDER_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record for this row. |
| 2 | `DISPLAY_NAME` | VARCHAR |  | The display name for the external order. |
| 3 | `FREQUENCY` | VARCHAR |  | A description of the external order's frequency. |
| 4 | `LINK_GROUP_IDENTIFIER` | VARCHAR |  | If the external order was part of a linked group, this contains a unique identifier for that group. This is not the ID of any other record in the system. |
| 5 | `LINK_TYPE_C_NAME` | VARCHAR |  | If the external order was part of a linked group, this contains the link type of that group. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

