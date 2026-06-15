# APP_RECEIPT_STATUS_AUDIT

> This table contains the application receipt status changes and audit information for an order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `APP_RECPT_STATUS_C_NAME` | VARCHAR |  | Application receipt status for order e-messages |
| 4 | `APP_RECPT_USER_ID` | VARCHAR |  | The user associated with the application receipt status update for a given order |
| 5 | `APP_RECPT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `APP_RECPT_STATUS_UTC_DTTM` | DATETIME (UTC) |  | Instant of update for application receipt status of an order |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

