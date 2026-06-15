# ION_AMOUNTS

> Clarity table to store the ordered ion amounts.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ION_C_NAME` | VARCHAR |  | The category ID for the name of an ion selected as part of this order record. |
| 4 | `ION_ORDERED_AMTS` | NUMERIC |  | This amount of an ion that was ordered by a clinician in this order record. |
| 5 | `ION_ORDERED_UNITS_C_NAME` | VARCHAR | org | This unit of an ion amount that was ordered by a clinician in this order record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

