# V_EHI_PTS_PB_TX_SET

> This view filters out premium billing payment data that is not appropriate for member level EHI exports when group billing is used.

**Primary key:** `PB_TXSET_ID`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_TXSET_ID` | VARCHAR | PK shared | The unique ID of the premium billing transaction set. |
| 2 | `PMT_AMT` | NUMERIC |  | Amount of the payment. |
| 3 | `TX_SET_TOTAL` | NUMERIC |  | Total amount of outstanding transactions to be closed in the transaction set. |
| 4 | `TOTAL_CREDIT` | NUMERIC |  | Total credits for the transaction set. |
| 5 | `NET_EXCEPT` | NUMERIC |  | Amount for net exceptions from the transaction set. |
| 6 | `NET_DIFF` | NUMERIC |  | Net difference for the transaction set. This represents the amount that still needs to be balanced in the transaction set. |
| 7 | `BAL_FWD_AMT` | NUMERIC |  | Balance forward amount for the transaction set. |
| 8 | `ADJ_AMOUNT` | NUMERIC |  | This field stores the total adjustment amount for this transaction set. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

