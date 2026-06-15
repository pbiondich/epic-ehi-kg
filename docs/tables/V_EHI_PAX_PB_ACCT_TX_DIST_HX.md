# V_EHI_PAX_PB_ACCT_TX_DIST_HX

> This view filters out premium billing transaction data that is not appropriate for member level EHI exports when group billing is used.

**Primary key:** `PB_ACT_TX_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_ACT_TX_ID` | VARCHAR | PK shared | The unique ID of the premium account transaction. |
| 2 | `LINE` | INTEGER | PK | Line counter for the transaction distribution history item. |
| 3 | `DIST_DATE` | DATETIME |  | Date that the payment distribution took place in the system. |
| 4 | `HIST_PB_INVOICE_ID` | VARCHAR |  | The unique ID of the premium billing invoice associated with the distribution. |
| 5 | `HIST_PB_ACT_TX_ID` | VARCHAR |  | The unique ID of the account transaction associated with the distribution. |
| 6 | `HIST_DIST_AMT` | NUMERIC |  | Amount of the distribution. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

