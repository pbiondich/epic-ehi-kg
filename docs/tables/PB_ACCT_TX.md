# PB_ACCT_TX

> The PB_ACCT_TX table contains the transactions associated with premium billing accounts.

**Primary key:** `PB_ACT_TX_ID`  
**Columns:** 29  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_ACT_TX_ID` | VARCHAR | PK shared | The unique ID of the premium billing account transaction. |
| 2 | `PB_ACT_TX_TYPE_C_NAME` | VARCHAR |  | Specifies the type of premium billing account transaction (i.e. premium billing, payment, ad hoc adjustment, balance forward, etc.) |
| 3 | `PB_ACT_TX_SENSE_C_NAME` | VARCHAR |  | Indicates whether the premium billing account transaction is a credit or charge. |
| 4 | `CYCLE_DATE` | DATETIME |  | Cycle date for the premium billing account transaction. |
| 5 | `PERIOD_DATE` | DATETIME |  | Indicates the time period for which the account transaction applies |
| 6 | `POST_DATE` | DATETIME |  | Indicates the date the transaction was posted. |
| 7 | `PB_ACCT_ID` | VARCHAR | FK→ | The unique ID of the premium billing account associated with the transaction. |
| 8 | `CANC_PB_ACT_TX_ID` | VARCHAR |  | This column is populated if this transaction reverses another transaction. The unique ID listed is that of the transaction that was reversed. |
| 9 | `NOT_OUTSTND_DATE` | DATETIME |  | Specifies the date on which the premium billing account transaction is no longer outstanding. |
| 10 | `FIRST_AR_DATE` | DATETIME |  | Specifies the first date on which payment is received for the transaction. |
| 11 | `PB_BAT_ID` | VARCHAR |  | Specifies the unique ID of the premium billing batch that generated the transaction. |
| 12 | `ADJ_RSN_C_NAME` | VARCHAR | org | Adjustment reason assigned to the account transaction. |
| 13 | `IDX_PB_ACCT_ID` | VARCHAR |  | Selective account index for the account transaction. |
| 14 | `OUTSTND_PB_INVC_ID` | VARCHAR |  | The unique ID of invoice on which the transaction is outstanding. |
| 15 | `CLOSE_REASON_C_NAME` | VARCHAR |  | Indicates the reason the transaction has been closed. |
| 16 | `SINCE_PB_ACCT_ID` | VARCHAR |  | The unique ID of the premium billing invoice. |
| 17 | `PB_TXSET_ID` | VARCHAR | shared | The unique ID of the transaction set. |
| 18 | `USEDIN_PB_TXSET_ID` | VARCHAR |  | The unique ID of the transaction set. |
| 19 | `PTMT_TOTAL` | NUMERIC |  | Total payment amount for the transaction. |
| 20 | `ATTACH_PP_BAT` | VARCHAR |  | The unique ID of payment posting batch to which the transaction is attached. |
| 21 | `CNCLD_PB_ACT_TX_ID` | VARCHAR |  | This column is populated if the transaction was reversed. The unique ID listed is that of the transaction that included the reversal. |
| 22 | `AP_CHECK_ID` | NUMERIC |  | The unique ID of the AP check issued from this premium billing account based on this premium billing transaction. |
| 23 | `REV_PB_PMT_ID` | VARCHAR |  | If this transaction is a payment reversal, then this field lists the unique ID of the premium billing payment being reversed. |
| 24 | `UPDATE_DATE` | DATETIME (Local) |  | The extract date and time of the record for this table. |
| 25 | `PMNT_REV_BY_PAX_ID` | VARCHAR |  | The unique reversed by payment ID for the transaction. This refers to the PB account transactions being reversed as original PB account transactions. |
| 26 | `BAL_FWD_MIRROR_PB_ACT_TX_ID` | VARCHAR |  | Keeps track of the link between the charge and credit premium billing amount by each storing the unique ID of the other amount. |
| 27 | `WRITE_OFF_DECISION_C_NAME` | VARCHAR | org | Stores the decision for a write off. |
| 28 | `PB_REFUND_STATUS_C_NAME` | VARCHAR |  | This item is used to track how far along through the refunding process a certain transaction is. Approved - the refund has been created in Epic but has not been distributed to the member. Ready for Check - a check for this refund is being written manually. Refund Sent - the refund has either been processed automatically or an end user has confirmed that the refund has been sent to the member via check. Canceled - the refund was approved and has since been canceled and reversed (before being set to Refund Sent). |
| 29 | `PAYMENT_ID` | VARCHAR |  | The payment id of a payment tranasction. This is only populated when the new payment workflow is being used. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_ACCT_ID` | [PB_ACCT](PB_ACCT.md) | name_stem | high |

