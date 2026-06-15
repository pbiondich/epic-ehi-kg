# ORD_OLD_TECH_FINDINGS

> This table stores the findings documented by technologists using old drawing tools. This table only exists to support historical data and no new data should be populated into it.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TECH_FINDING_ID` | NUMERIC |  | Stores the findings documented by technologists using old drawing tools. This column exists only to support historical data and no new data should be populated into it. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

