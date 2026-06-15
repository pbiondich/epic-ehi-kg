# PR_EST_AP_CLAIM_PROC

> This table stores service line information for managed care estimates.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 22  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the patient estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONTEXT_LINE` | INTEGER |  | The LINE in the PR_EST_AP_CLAIM table that stores the claim information that this service line is associated with. |
| 4 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 5 | `PROC_MODS` | VARCHAR |  | The modifiers associated with the service line. |
| 6 | `PROC_QTY` | INTEGER |  | The procedure quantity associated with the service line. |
| 7 | `CHG_AMT` | NUMERIC |  | The billed amount associated with the service line. |
| 8 | `SYS_CHG_AMT` | NUMERIC |  | The system-calculated billed amount associated with the service line detail. |
| 9 | `ALLOW_AMT` | NUMERIC |  | The allowed amount associated with the service line. |
| 10 | `SYS_ALLOW_AMT` | NUMERIC |  | The system-calculated allowed amount associated with the service line detail. |
| 11 | `SELF_PAY_AMT` | NUMERIC |  | The self-pay amount associated with the service line. |
| 12 | `SYS_SELF_PAY_AMT` | NUMERIC |  | The system-calculated self-pay amount associated with the service line detail. |
| 13 | `MC_ADDL_LINE` | INTEGER |  | The LINE in the PR_EST_ADDL_INFO table that stores additional information about the service line. |
| 14 | `TX_ID` | NUMERIC | shared | The AP Claims transaction (ETR) ID associated with this estimate procedure line. |
| 15 | `AUTH_REQUIRED_YN` | VARCHAR |  | Identifies if an authorization is required for the procedure line to be covered. |
| 16 | `DRG_ID` | VARCHAR | FK→ | The Diagnosis Related Group (DRG) associated with the service line detail. |
| 17 | `DRG_ID_DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |
| 18 | `MC_NETWORK_LEVELS_C_NAME` | VARCHAR | org | Indicates if the service is priced to be In or Out of network. |
| 19 | `MC_CLICKED_ON_YN` | VARCHAR |  | Signals if the line was clicked on by the member |
| 20 | `MC_IS_ANCHOR_YN` | VARCHAR |  | This indicates whether the associated procedure is what the member searched for in Cost Calc (Aka. Anchor) |
| 21 | `REV_CODE_ID` | NUMERIC |  | The revenue code associated with the service line detail. |
| 22 | `REV_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DRG_ID` | [CLARITY_DRG](CLARITY_DRG.md) | sole_pk | high |

