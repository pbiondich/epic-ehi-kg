# ORD_PENDING_NOTIF

> Contains users waiting to be notified about an order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RECIPIENT_USER_ID` | VARCHAR |  | EMP ID of a user waiting to be notified about the order. |
| 4 | `RECIPIENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `REQ_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant the user started waiting to be notified. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

