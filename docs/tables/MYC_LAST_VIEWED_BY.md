# MYC_LAST_VIEWED_BY

> Once an order result has been displayed in web based chart system, both the time it was reviewed and the patient who reviewed it are stored in this table.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the procedure order record that was reviewed. |
| 2 | `LINE` | INTEGER | PK | The line number identifying appropriate contact for a given ORDER_ID item. |
| 3 | `MYC_VIEWED_BY_ID` | VARCHAR |  | The unique ID of the patient viewing the record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

