# V_EHI_PAX_PB_ACCT_TX

> This view filters out premium billing transaction data that is not appropriate for member level EHI exports when group billing is used.

**Primary key:** `PB_ACT_TX_ID`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_ACT_TX_ID` | VARCHAR | PK shared | The unique ID of the premium billing account transaction. |
| 2 | `TX_AMT` | NUMERIC |  | Amount of the premium billing account transaction. |
| 3 | `PREV_BAL` | NUMERIC |  | Indicates the previous balance for the premium billing account before the transaction. |
| 4 | `NEW_BAL` | NUMERIC |  | Indicates the new balance for the premium billing account after the transaction. |
| 5 | `OUTSTND_AMT` | NUMERIC |  | Specifies the outstanding amount for the transaction. |
| 6 | `DIST_AMT` | NUMERIC |  | Total distributed amount for the transaction. |
| 7 | `UNDIST_AMT` | NUMERIC |  | Total undistributed amount for the transaction. |
| 8 | `CURRENT_BILLING_AMOUNT` | NUMERIC |  | The amount billed for the current period for a billing transaction. |
| 9 | `RETRO_BILLING_AMOUNT` | NUMERIC |  | The amount billed for prior periods due to retroactivity for a billing transaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

