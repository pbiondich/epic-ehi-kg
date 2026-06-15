# V_EHI_PAX_PB_ACCT_TX_GRP_PMT

> This view filters out premium billing transaction data that is not appropriate for member level EHI exports when group billing is used.

**Primary key:** `PB_ACT_TX_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_ACT_TX_ID` | VARCHAR | PK shared | The unique ID of the premium account transaction. |
| 2 | `LINE` | INTEGER | PK | Line counter for the group payment on the transaction. |
| 3 | `GP_PAY_PAX_ID` | VARCHAR |  | The unique ID of the account transaction associated with the group payment. |
| 4 | `GP_PAY_PLAN_GRP_ID` | VARCHAR |  | The unique ID of the employer group associated with the payment. |
| 5 | `GP_PAY_PLAN_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |
| 6 | `GP_PAY_AMT` | NUMERIC |  | Amount of the payment towards the employer group |
| 7 | `GP_PAY_REMAIN_AMT` | NUMERIC |  | Amount remaining on the transaction for the employer group after payment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

