# ORDER_DEFER_USERS

> This table contains information about users who have clicked the Defer Order button in Verification. The records included in this table are ORD records, and each line contains a user ID and instant.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RX_DEFERRAL_USER_ID` | VARCHAR |  | Users who have deferred this order to a pharmacist for review. Will record each user who clicks the "Defer Order" button in Verification. Only relevant if Manual Defer in Verification is enabled (RXD 1270). |
| 4 | `RX_DEFERRAL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `RX_DEFER_INST_DTTM` | DATETIME (Local) |  | Instants at which this order was deferred to a pharmacist for review. New values will be added each time a user clicks the "Defer Order" button in Verification. Only relevant if Manual Defer in Verification is enabled (RXD 1270). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

