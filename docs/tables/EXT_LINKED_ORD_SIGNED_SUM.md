# EXT_LINKED_ORD_SIGNED_SUM

> This table contains summary information for external orders that are in linked groups.

**Primary key:** `ORDER_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record representing an external linked group. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the linked order in this external linked group record. Together with ORDER_ID, this forms the foreign key to the EXTERNAL_ORDER_INFO table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of this piece of the external linked order's summary information. |
| 4 | `EXT_LINKED_SUMMARY` | VARCHAR |  | The summary of the linked order. All lines of this order's summary (that is, all lines with the same ORDER_ID and GROUP_LINE) should be concatenated to get the full summary text. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

