# PB_ACCT_TX_USED_TX_HX

> Table that stores PB payment posting set IDs used in transaction set history.

**Primary key:** `PB_ACT_TX_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_ACT_TX_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the account transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `USED_TX_HX_TRANSACTION_SET_ID` | VARCHAR |  | Stores the Premium Billing transaction set IDs which have used this transaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

