# V_EHI_PAX_PB_ACCT_TX_PMT_TX

> This view filters out premium billing transaction data that is not appropriate for member level EHI exports when group billing is used.

**Primary key:** `PB_ACT_TX_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_ACT_TX_ID` | VARCHAR | PK shared | The unique ID of the premium account transaction. |
| 2 | `LINE` | INTEGER | PK | Line counter of the payment on the transaction. |
| 3 | `HIST_PB_ACT_TX_ID` | VARCHAR |  | The unique ID of the premium account transaction used as a payment against this premium account transaction. |
| 4 | `PMT_AMT` | NUMERIC |  | Amount of the payment transaction applied towards this premium account transaction. |
| 5 | `REMAINING_AMT` | NUMERIC |  | Amount remaining on the premium account transaction after the payment has been applied. |
| 6 | `PAYMENT_REV_LINE` | INTEGER |  | Specifies the payment history reversed line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

