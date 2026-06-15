# KEYSTONE_DEPENDENCIES

> This table contains information about the dependency orders linked to a related keystone order. Keystone dependency orders are suggested for discontinuation when a clinician tries to discontinue a keystone order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `KSTONE_DEPENDENCIES_ID` | NUMERIC |  | The unique identifier of any orders that are considered a dependency of the order record for this row. Discontinuing the current order will prompt the user to consider discontinuing the other orders in this list. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

