# PB_TX_SET

> The PB_TX_SET table contains the premium billing payment transaction sets.

**Primary key:** `PB_TXSET_ID`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_TXSET_ID` | VARCHAR | PK shared | The unique ID of the premium billing transaction set. |
| 2 | `PB_ACCT_ID` | VARCHAR | FK→ | The unique ID of the premium billing account associated with the transaction set. |
| 3 | `PB_PMT_ID` | VARCHAR |  | The unique ID of the premium billing payment associated with the transaction set. |
| 4 | `CANCEL_PB_PMT_ID` | VARCHAR |  | The unique ID of the cancelled premium billing payment associated with the transaction set. |
| 5 | `PERIOD_FROM_DATE` | DATETIME |  | Beginning date of period for the transaction set. |
| 6 | `PERIOD_TO_DATE` | DATETIME |  | Ending date of the period for the transaction set. |
| 7 | `PMT_METH_C_NAME` | VARCHAR |  | Payment method of the transaction set (balance forward or exception). |
| 8 | `CUST_PAIDBY_PTS_C_NAME` | VARCHAR |  | Describes portion of the invoice that this transaction set was targeted towards (entire invoice, custom portion, remaining invoice, or custom advice). |
| 9 | `CUST_PTS_CMT` | VARCHAR |  | Comment associated with a customized transaction set. |
| 10 | `LATEST_PB_INVC_ID` | VARCHAR |  | The unique ID of the latest premium billing invoice record on the premium billing account when this payment was committed. |
| 11 | `INC_EFF_FR_DT` | DATETIME |  | Effective from date for transactions included in the custom transaction set. |
| 12 | `EXC_EFF_FR_DT` | DATETIME |  | Effective from date for transactions excluded from the custom transaction set. |
| 13 | `EXC_EFF_TO_DT` | DATETIME |  | Effective to date for transactions excluded from the custom transaction set. |
| 14 | `UPDATE_DATE` | DATETIME (Local) |  | The extract date and time of the record for this table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_ACCT_ID` | [PB_ACCT](PB_ACCT.md) | name_stem | high |

