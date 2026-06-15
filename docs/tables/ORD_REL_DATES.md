# ORD_REL_DATES

> This table contains information on when instances of this order are to be released to the lab to be performed.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID number of the order |
| 2 | `LINE` | INTEGER | PK | The line count for this table as determined by the number of users who reviewed this order. |
| 3 | `RELEASE_ORD_DATE` | DATETIME |  | The dates on which instances of this order are to be released to the lab to be performed |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

