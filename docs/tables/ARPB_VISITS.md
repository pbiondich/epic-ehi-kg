# ARPB_VISITS

> This table contains Professional Billing visit information stored in the Hospital Accounts Receivable (HAR) master file. It only includes PB HAR records created in classic PB self-pay service areas.

**Primary key:** `PB_VISIT_ID`  
**Columns:** 29  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_VISIT_ID` | NUMERIC | PK | The unique identifier for the Professional Billing visit. |
| 2 | `PB_BILLING_STATUS_C_NAME` | VARCHAR |  | This column stores the Professional Billing status category ID for the visit. |
| 3 | `PB_FO_OVRRD_ST_C_NAME` | VARCHAR |  | This column indicates whether the Professional Billing filing order has been overridden by a user. |
| 4 | `PB_FO_MSPQ_STATE_C_NAME` | VARCHAR |  | This column indicates whether the filing order for the Professional Billing visit has been verified by Medicare Secondary Payer Questionnaire logic. |
| 5 | `PB_VISIT_NUM` | VARCHAR |  | This column stores the PB visit number. |
| 6 | `PRIM_ENC_CSN_ID` | NUMERIC | FK→ | The contact serial number associated with the primary patient contact on the Professional Billing visit. |
| 7 | `GUARANTOR_ID` | NUMERIC |  | Stores the guarantor ID associated with the Professional Billing visit. |
| 8 | `COVERAGE_ID` | NUMERIC | FK→ | The primary coverage on the Professional Billing visit. |
| 9 | `SELF_PAY_YN` | VARCHAR |  | Indicates whether the Professional Billing visit is self-pay. |
| 10 | `DO_NOT_BILL_INS_YN` | VARCHAR |  | Indicates whether the Professional Billing visit has the Do Not Bill Insurance flag set. |
| 11 | `ACCT_FIN_CLASS_C_NAME` | VARCHAR | org | The financial class category ID for the Professional Billing visit. |
| 12 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 13 | `REVENUE_LOCATION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 14 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 15 | `PB_TOTAL_BALANCE` | NUMERIC |  | Contains the combined total balance of transactions on the PB visit. |
| 16 | `PB_TOTAL_CHARGES` | NUMERIC |  | The total charges on the PB visit. |
| 17 | `PB_TOTAL_PAYMENTS` | NUMERIC |  | The total payments on the PB visit. |
| 18 | `PB_TOTAL_ADJ` | NUMERIC |  | Contains total adjustments on the PB visit. |
| 19 | `PB_INS_BALANCE` | NUMERIC |  | Contains insurance balance on the PB visit. |
| 20 | `PB_UND_BALANCE` | NUMERIC |  | Contains undistributed balances on the PB visit. |
| 21 | `PB_SELFPAY_BALANCE` | NUMERIC |  | Contains the self-pay balance on the Professional Billing visit. |
| 22 | `PB_BAD_DEBT_BALANCE` | NUMERIC |  | Contains the bad debt balance on the Professional Billing visit. |
| 23 | `REC_CREATE_USER_ID` | VARCHAR |  | The user who created the Professional Billing visit record. |
| 24 | `REC_CREATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 25 | `FIRST_PB_CHG_TX_ID` | NUMERIC |  | Contains the first valid Professional Billing charge on the Professional Billing visit. |
| 26 | `BAL_FULL_SELF_PAY_YN` | VARCHAR |  | This item shows whether the balances for this hospital account are in full self-pay. |
| 27 | `PRIMARY_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 28 | `PRIMARY_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 29 | `CHANGE_EAR_FLAG_YN_NAME` | VARCHAR |  | Indicates whether the HAR’s coverage list originated from a source guarantor as a result of change guarantor. When set, retro processes will bypass the HAR. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PRIM_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

