# HBP_STMT_PRINT

> This table stores information about Hospital Billing statement print records.

**Primary key:** `HBP_PRINT_ID`  
**Columns:** 38  
**Org-specific columns:** 1  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HBP_PRINT_ID` | NUMERIC | PK | The HB print record ID. |
| 2 | `BILL_RUN_TYPE_C_NAME` | VARCHAR | org | The type of bill print record. |
| 3 | `IS_DEMAND_BILL_YN` | VARCHAR |  | Indicates whether or not this is a demand bill. |
| 4 | `CURR_AMOUNT_DUE` | NUMERIC |  | The current amount due. |
| 5 | `BILLED_DATE` | DATETIME |  | The billed date. |
| 6 | `STMT_DATE` | DATETIME |  | The statement date. |
| 7 | `ACCT_ID` | NUMERIC | shared | The guarantor account ID. |
| 8 | `RESP_PARTY` | VARCHAR |  | The responsible party. |
| 9 | `BILL_CITY` | VARCHAR |  | The billing city of the guarantor. |
| 10 | `BILL_STATE_C` | VARCHAR |  | The billing state of the guarantor. |
| 11 | `BILL_ZIP` | VARCHAR |  | The billing zip of the guarantor. |
| 12 | `PREV_BAL` | NUMERIC |  | The previous balance. |
| 13 | `PREV_AMT_DUE` | NUMERIC |  | The previous amount due. |
| 14 | `PREV_INS_BAL` | NUMERIC |  | The previous insurance balance. |
| 15 | `CURR_BAL` | NUMERIC |  | The current balance. |
| 16 | `GUAR_INS_DUE` | NUMERIC |  | The insurance due amount on the guarantor. |
| 17 | `PMT_PLAN_MONTHLY_AMT` | NUMERIC |  | The monthly amount on the payment plan. |
| 18 | `PMT_PLAN_TOT` | NUMERIC |  | The total amount on the payment plan. |
| 19 | `PMT_PLAN_BAL` | NUMERIC |  | The payment plan balance. |
| 20 | `TOT_CHG_AMT` | NUMERIC |  | The total charge amount. |
| 21 | `GUAR_PMT_PLAN_AMT_DUE` | NUMERIC |  | The amount due on the guarantor's payment plan. |
| 22 | `GUAR_PMT_PLAN_TOT` | NUMERIC |  | The total amount on the guarantor's payment plan. |
| 23 | `GUAR_PMT_PLAN_BAL` | NUMERIC |  | The balance on the guarantor's payment plan. |
| 24 | `GUAR_PMT_PLAN_PAT_PORTION` | NUMERIC |  | The patient portion on the guarantor's payment plan. |
| 25 | `NEW_CHG_AMT` | NUMERIC |  | The new charge amount. |
| 26 | `NEW_PAT_CHG_AMT` | NUMERIC |  | The new patient charge amount. |
| 27 | `NEW_INS_CHG_AMT` | NUMERIC |  | The new insurance charge amount. |
| 28 | `TOT_PMT_AMT` | NUMERIC |  | The total payment amount. |
| 29 | `NEW_PMT_AMT` | NUMERIC |  | The new payment amount. |
| 30 | `NEW_PAT_PMT_AMT` | NUMERIC |  | The new patient payment amount. |
| 31 | `NEW_INS_PMT_AMT` | NUMERIC |  | The new insurance payment amount. |
| 32 | `TOT_ADJ_AMT` | NUMERIC |  | The total adjustment amount. |
| 33 | `NEW_ADJ_AMT` | NUMERIC |  | The new adjustment amount. |
| 34 | `NEW_PAT_ADJ_AMT` | NUMERIC |  | The new patient adjustment amount. |
| 35 | `NEW_INS_ADJ_AMT` | NUMERIC |  | The new insurance adjustment amount. |
| 36 | `IS_INFORMATIONAL_YN` | VARCHAR |  | Indicates whether or not this is an informational statement. |
| 37 | `REC_CREATE_DATE` | DATETIME |  | The creation date for this record. |
| 38 | `PMT_PLAN_AMT_OVERDUE` | NUMERIC |  | The amount overdue on the payment plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [HBP_STMT_HAR_DETAIL](HBP_STMT_HAR_DETAIL.md) | `HBP_PRINT_ID` | high |
| [HBP_STMT_PRINT_ADDR](HBP_STMT_PRINT_ADDR.md) | `HBP_PRINT_ID` | high |
| [HSP_ACCT_DETAIL_BILL_HX](HSP_ACCT_DETAIL_BILL_HX.md) | `HBP_PRINT_ID` | high |

