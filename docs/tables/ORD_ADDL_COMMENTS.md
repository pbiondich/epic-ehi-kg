# ORD_ADDL_COMMENTS

> The ORD_ADDL_COMMENT table allows you to report on additional comments for non-medication orders.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORD_ADDL_COMMENTS` | VARCHAR |  | Field to capture additional comments about an order. When populated for a referral order, these comments can be pulled into the referral as a referral note. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

