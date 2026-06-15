# IP_ORD_UNACK_CANCEL_HOLD

> This table displays orders with unacknowledged Cancel Hold order actions.

**Primary key:** `INPATIENT_DATA_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique identifier for the inpatient data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORD_UNACK_CANCEL_HOLD_ORDER_ID` | NUMERIC |  | The unique identifier of an order record that has not been acknowledged for the Cancel Hold action. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

