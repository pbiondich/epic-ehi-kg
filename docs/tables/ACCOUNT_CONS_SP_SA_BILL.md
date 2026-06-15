# ACCOUNT_CONS_SP_SA_BILL

> Applies only if you have enabled the consolidated balances functionality. Contains information about the guarantors and their balances that are sent to a different service area for billing to the guarantor.

**Primary key:** `ACCT_ID`  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the account record. |
| 2 | `PB_CONS_SP_TOT_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total PB balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 3 | `PB_CONS_SP_PAT_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total PB self-pay balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 4 | `PB_CONS_SP_INS_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total PB insurance balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 5 | `PB_CONS_SP_CONTEST_PAT_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total PB contested self-pay balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 6 | `PB_CONS_SP_EXT_BD_PAT_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total PB external AR bad debt self-pay balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 7 | `PB_CONS_SP_EXT_BD_INS_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total PB external AR bad debt insurance balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 8 | `PB_CONS_SP_CONT_EXT_AR_PAT_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total PB contested external AR balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 9 | `PB_CONS_SP_EXT_AR_PAT_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total PB external AR self-pay balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 10 | `PB_CONS_SP_EXT_AR_INS_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total PB external AR insurance balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 11 | `PB_CONS_SP_UNDIST_INS_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total PB undistributed insurance credits sent to a different service area for billing to the guarantor. |
| 12 | `PB_CONS_SP_UNDIST_PAT_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total PB undistributed self-pay credits sent to a different service area for billing to the guarantor. |
| 13 | `CONS_SP_ACCT_ID` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The target guarantor in the target service area to whom the balances are sent for billing. |
| 14 | `HB_CONS_SP_TOT_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total HB balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 15 | `HB_CONS_SP_PREBILL_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total HB prebilled balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 16 | `HB_CONS_SP_INS_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total HB insurance balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 17 | `HB_CONS_SP_PAT_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total HB self-pay balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 18 | `HB_CONS_SP_UNDIST_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total HB undistributed balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 19 | `HB_CONS_SP_BAD_DEBT_PAT_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total HB bad debt self-pay balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 20 | `HB_CONS_SP_BAD_DEBT_INS_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total HB bad debt insurance balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 21 | `HB_CONS_SP_BAD_DEBT_UNDIST_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total HB bad debt undistributed balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 22 | `HB_CONS_SP_EXT_AR_INS_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total HB external AR insurance balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 23 | `HB_CONS_SP_EXT_AR_PAT_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total HB external AR self-pay balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 24 | `HB_CONS_SP_EXT_AR_UNDIST_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The total HB external AR undistributed balance of the hospital accounts sent to a different service area for billing to the guarantor. |
| 25 | `HB_CONS_SP_IN_PROG_PAT_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The HB self-pay balance of in progress accounts for the guarantor that are sent to a different service area, excluding hospital accounts in external AR or bad debt. In progress accounts are those that have not yet been billed to self-pay. |
| 26 | `HB_CONS_SP_IN_PROG_BD_PAT_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The HB self-pay balance of in progress bad debt accounts for the guarantor that are sent to a different service area. In progress accounts are those that have not yet been billed to self-pay. |
| 27 | `HB_CONS_SP_INPROG_EXTAR_PATBAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The HB self-pay balance of in progress external AR accounts for the guarantor that are sent to a different service area. In progress accounts are those that have not yet been billed to self-pay. |
| 28 | `HB_CONS_SP_CONTEST_PAT_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The HB self-pay balance of contested accounts for the guarantor that are sent to a different service area, excluding hospital accounts in external AR or bad debt. |
| 29 | `HB_CONS_SP_CONTEST_BD_PAT_BAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The HB bad debt self-pay balance of contested accounts for the guarantor that are sent to a different service area. |
| 30 | `HB_CONS_SP_CONTST_EXTAR_PATBAL` | NUMERIC |  | Applies only if you have enabled the consolidated balances functionality. The HB External AR self-pay balance of contested accounts for the guarantor that are sent to a different service area. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

