# CL_ORD_FST_LST_SCH

> This table stores an order's first and last scheduled date and time, along with the type of review notice for the expire items (i.e. let expire or review).

**Primary key:** `ORDER_ID`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record associated with this order. |
| 2 | `DATE_FIRST_ORDEREN` | DATETIME |  | Date of the first schedule. |
| 3 | `TIME_FIRST_ORDEREN` | DATETIME (Local) |  | Time of the first schedule. |
| 4 | `DATE_LAST_ORDERENT` | DATETIME |  | Date of the last schedule. |
| 5 | `TIME_LAST_ORDERENT` | DATETIME (Local) |  | Time of the last schedule. |
| 6 | `LET_EXPIRE_TYPE_C_NAME` | VARCHAR |  | Determines the type of review notice for the former "let expire" items |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

