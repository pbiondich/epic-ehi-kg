# PB_DTL_TX_AR_STAT_HX

> The Status History table contains a history of each time the transaction's status has changed.

**Primary key:** `TRANSACTION_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TRANSACTION_ID` | VARCHAR | PK FK→ | The unique identifier for the detail transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AR_STATUS_CHANGE_UTC_DTTM` | DATETIME (UTC) |  | The instant of the status change. |
| 4 | `AR_SYSTEM_UPDATED_STATUS_YN` | VARCHAR |  | Whether the status change occurred automatically by the system (yes or no). |
| 5 | `AR_TX_STATUS_C_NAME` | VARCHAR |  | The status that the transaction was changed to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `TRANSACTION_ID` | [CAP_DTL_TX](CAP_DTL_TX.md) | sole_pk | high |

