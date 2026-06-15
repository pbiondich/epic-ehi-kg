# ORDER_ECONSULT_RECIPIENTS

> This table stores recipient information for e-Consult orders, if manual recipients are selected.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | This column stores the unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ECONSULT_RECIPIENTS` | VARCHAR |  | Stores manually selected recipients in an e-Consult order. If not set, the distribution scheme routes the message. The format for this data is ID^modifier^responsibility If the recipient is a user, ID is the user ID, otherwise, the ID represents the ID based on modifier: P=Pool, C=Class. Responsibility will be 1 if the user has responsibility, 0 or " otherwise. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

