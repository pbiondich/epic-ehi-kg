# AP_BROKER_COMMISSIONS

> This table contains data related to broker commission transactions.

**Primary key:** `TX_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the transaction record. |
| 2 | `AP_CYCLE_STATUS_C_NAME` | VARCHAR |  | The AP Cycle status of transactions for NUR based transactions. |
| 3 | `EFF_DATE` | DATETIME |  | Contains first of month as the date for which the batch containing this transaction is filed. |
| 4 | `TX_STATUS_C_NAME` | VARCHAR |  | The status of the transaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

