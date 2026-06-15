# STMT_HB_DETAIL

> This table contains Hospital Billing information about your statement print and detail bill records.

**Primary key:** `PRINT_ID`  
**Columns:** 36

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the statement print or detail bill record. |
| 2 | `PREV_PAT_BAL` | NUMERIC |  | The Hospital Billing outstanding self-pay balance for the guarantor from the previous statement. |
| 3 | `PREV_AMT_DUE` | NUMERIC |  | The Hospital Billing amount due for the guarantor from the previous statement. It only includes outstanding self-pay balances not on a payment plan. |
| 4 | `NEW_CHG_AMT` | NUMERIC |  | The Hospital Billing new charge amount. |
| 5 | `NEW_PMT_AMT` | NUMERIC |  | The Hospital Billing new payment amount. |
| 6 | `NEW_ADJ_AMT` | NUMERIC |  | The Hospital Billing new adjustment amount. |
| 7 | `TOT_CHG_AMT` | NUMERIC |  | The Hospital Billing total charge amount. |
| 8 | `TOT_PMT_AMT` | NUMERIC |  | The Hospital Billing total payment amount. |
| 9 | `TOT_ADJ_AMT` | NUMERIC |  | The Hospital Billing total adjustment amount. |
| 10 | `CURR_PAT_BAL` | NUMERIC |  | The Hospital Billing outstanding self-pay balance for the guarantor. |
| 11 | `CURR_AMT_DUE` | NUMERIC |  | The Hospital Billing amount due for the guarantor. It only includes outstanding self-pay balances not on a payment plan. |
| 12 | `PMT_PLAN_TOT` | NUMERIC |  | The Hospital Billing payment plan total amount. |
| 13 | `PMT_PLAN_BAL` | NUMERIC |  | The Hospital Billing payment plan balance. |
| 14 | `PMT_PLAN_DUE` | NUMERIC |  | The Hospital Billing payment plan due amount. |
| 15 | `INS_PORTION_AMT` | NUMERIC |  | The Hospital Billing insurance portion amount. |
| 16 | `PAT_PORTION_AMT` | NUMERIC |  | The Hospital Billing patient portion amount. |
| 17 | `FOLLOW_UP_CYCLE_AGING_DATE` | DATETIME |  | The Hospital Billing follow-up cycle aging date. |
| 18 | `IS_INFORMATIONAL_YN` | VARCHAR |  | Indicates whether or not this is informational (meaning the amount due is zero). |
| 19 | `PREV_INS_BAL` | NUMERIC |  | The Hospital Billing previous insurance balance. |
| 20 | `NEW_INS_CHG_AMT` | NUMERIC |  | The Hospital Billing new insurance charge amount. |
| 21 | `NEW_INS_PMT_AMT` | NUMERIC |  | The Hospital Billing new insurance payment amount. |
| 22 | `NEW_INS_ADJ_AMT` | NUMERIC |  | The Hospital Billing new insurance adjustment amount. |
| 23 | `CURR_INS_BAL` | NUMERIC |  | The Hospital Billing current insurance balance. |
| 24 | `NEW_PAT_CHG_AMT` | NUMERIC |  | The Hospital Billing new patient charge amount. |
| 25 | `NEW_PAT_PMT_AMT` | NUMERIC |  | The Hospital Billing new patient payment amount. |
| 26 | `NEW_PAT_ADJ_AMT` | NUMERIC |  | The Hospital Billing new patient adjustment amount. |
| 27 | `PMT_PLAN_MONTH_AMT` | NUMERIC |  | The Hospital Billing payment plan monthly amount. |
| 28 | `AUTOPAY_CARD_ID` | NUMERIC |  | The payment method that is used for the guarantor's Auto Pay. |
| 29 | `AUTOPAY_DATE` | DATETIME |  | Date to charge the payment method for this specific statement if its guarantor is on Auto Pay. |
| 30 | `AUTOPAY_AMT_DUE` | NUMERIC |  | The amount to be charged to the payment method for this specific statement if its guarantor is on Auto Pay. |
| 31 | `NEW_PAT_DISC_ADJ` | NUMERIC |  | Stores the new HB patient discount amount that occurred since the last statement. |
| 32 | `TOT_PAT_DISC_ADJ` | NUMERIC |  | Stores the total HB patient discount amount on the current statement. |
| 33 | `NEW_PAT_REF` | NUMERIC |  | Stores the new HB patient refund amount that occurred since the last statement. |
| 34 | `TOT_PAT_REF` | NUMERIC |  | Stores the total HB patient refund amount on the current statement. |
| 35 | `NEW_PAT_OTH_ADJ` | NUMERIC |  | Stores the new HB patient other adjustment amount that occurred since the last statement. Patient other adjustments are any patient adjustments that are not refunds or discounts. |
| 36 | `TOT_PAT_OTH_ADJ` | NUMERIC |  | Stores the total HB patient other adjustment amount on the current statement. Patient other adjustments are any patient adjustments that are not refunds or discounts. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

