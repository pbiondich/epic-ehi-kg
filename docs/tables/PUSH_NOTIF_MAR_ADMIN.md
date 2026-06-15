# PUSH_NOTIF_MAR_ADMIN

> This table contains information about the linkage between push notifications and MAR administrations.

**Primary key:** `NOTIF_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTIF_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the notification record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MAR_ORDER_ID` | NUMERIC |  | MAR admin order record linked to the notification |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

