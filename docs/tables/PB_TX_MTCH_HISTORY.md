# PB_TX_MTCH_HISTORY

> Table containing the matching history for the transaction.

**Primary key:** `TRANSACTION_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TRANSACTION_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the detail transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MTCH_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The instant the transaction was matched on. |
| 4 | `MTCH_TRANSACTION_ID` | VARCHAR |  | The transaction ID that was matched to. Will never be cleared. |
| 5 | `MTCH_USER_ID` | VARCHAR |  | The user that caused the transaction to match. |
| 6 | `MTCH_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `MTCH_WORKFLOW_C_NAME` | VARCHAR |  | The workflow that caused the transaction to match |
| 8 | `UNMTCH_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The instant the transaction was unmatched with the matched transaction. |
| 9 | `UNMTCH_USER_ID` | VARCHAR |  | The user that caused the transaction to unmatch |
| 10 | `UNMTCH_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `UNMTCH_WORKFLOW_C_NAME` | VARCHAR |  | The workflow that caused the transaction to unmatch. |
| 12 | `MTCH_CURRENT_TRANSACTION_ID` | VARCHAR |  | The transaction that is currently matched. This is only populated if the transaction has not been unmatched. It is to quickly keep track of and find the transactions that are linked. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `TRANSACTION_ID` | [CAP_DTL_TX](CAP_DTL_TX.md) | sole_pk | high |

