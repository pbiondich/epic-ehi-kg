# ORDER_SESSION_COMMENTS

> This table stores information about the Session Comments for an order. Procedures placed in EpicCare Link can contain display item 186-Session Comments. These comments are shared amongst all the orders containing this item that are placed in the same ordering session.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SESSION_COMMENTS` | VARCHAR |  | Stores comments on the order. These comments are shared among all orders placed at the same time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

