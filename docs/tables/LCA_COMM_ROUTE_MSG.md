# LCA_COMM_ROUTE_MSG

> Table for LCA routing that contains information applicable to the routing message. Essentially no add multiple response items.

**Primary key:** `COMMUNICATION_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMMUNICATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the routing record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMM_ROUTING_MSG` | VARCHAR |  | This stores the routing message entered by the user when routing a report or letter from Chart Review or routing any report from InBasket using route button. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

