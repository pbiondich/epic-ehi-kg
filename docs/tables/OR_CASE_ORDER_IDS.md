# OR_CASE_ORDER_IDS

> This table contains the IDs of the orders which were used to create a case.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique ID of the procedural case record. |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `ORDER_ID` | NUMERIC | shared | Order Record ID for the case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

