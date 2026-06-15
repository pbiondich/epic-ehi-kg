# STMT_EB_DETAIL

> This table contains Enterprise Billing information about your statement print and detail bill records.

**Primary key:** `PRINT_ID`  
**Columns:** 60

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the statement print or detail bill record. |
| 2 | `PREV_PAT_BAL` | NUMERIC |  | The enterprise billing outstanding self-pay balance for the guarantor from the previous statement. |
| 3 | `PREV_AMT_DUE` | NUMERIC |  | The enterprise billing amount due for the guarantor from the previous statement. It is a combination of the payment plan amount due plus any outstanding balances not on a payment plan. |
| 4 | `NEW_CHG_AMT` | NUMERIC |  | The enterprise billing new charge amount. |
| 5 | `NEW_PMT_AMT` | NUMERIC |  | The enterprise billing new payment amount. |
| 6 | `NEW_ADJ_AMT` | NUMERIC |  | The enterprise billing new adjustment amount. |
| 7 | `TOT_CHG_AMT` | NUMERIC |  | The enterprise billing total charge amount. |
| 8 | `TOT_PMT_AMT` | NUMERIC |  | The enterprise billing total payment amount. |
| 9 | `TOT_ADJ_AMT` | NUMERIC |  | The enterprise billing total adjustment amount. |
| 10 | `CURR_PAT_BAL` | NUMERIC |  | The enterprise billing outstanding self-pay balance for the guarantor. |
| 11 | `CURR_AMT_DUE` | NUMERIC |  | The enterprise billing amount due for the guarantor. It is a combination of the payment plan amount due plus any outstanding balances not on a payment plan. |
| 12 | `FOLLOW_UP_CYCLE_LEVEL` | INTEGER |  | The enterprise billing follow-up cycle level for this statement. |
| 13 | `IS_INFORMATIONAL_YN` | VARCHAR |  | Indicates whether or not this is informational (meaning the amount due is zero). |
| 14 | `PREV_INS_BAL` | NUMERIC |  | The enterprise billing previous insurance balance. |
| 15 | `NEW_INS_CHGS` | NUMERIC |  | The enterprise billing new insurance charge amount. |
| 16 | `NEW_INS_PMTS` | NUMERIC |  | The enterprise billing new insurance payment amount. |
| 17 | `NEW_INS_ADJS` | NUMERIC |  | The enterprise billing new insurance adjustment amount. |
| 18 | `CURR_INS_BAL` | NUMERIC |  | The enterprise billing current insurance balance. |
| 19 | `NEW_PAT_CHGS` | NUMERIC |  | The enterprise billing new patient charge amount. |
| 20 | `NEW_PAT_PMTS` | NUMERIC |  | The enterprise billing new patient payment amount. |
| 21 | `NEW_PAT_ADJS` | NUMERIC |  | The enterprise billing new patient adjustment amount. |
| 22 | `PMT_PLAN_TOT` | NUMERIC |  | Total amount of payment plan. |
| 23 | `PMT_PLAN_BAL` | NUMERIC |  | Total amount of enterprise payment plan balance. |
| 24 | `PMT_PLAN_DUE` | NUMERIC |  | Amount due per period of the payment plan. |
| 25 | `SP_FOLLOW_UP_LEVEL_C_NAME` | VARCHAR |  | The guarantor self-pay follow-up level. |
| 26 | `PMT_PLAN_MONTH_AMT` | NUMERIC |  | The monthly amount of enterprise payment plan. |
| 27 | `TOT_PAT_PMT_AMT` | NUMERIC |  | The total patient payments for a guarantor. |
| 28 | `TOT_PAT_ADJ_AMT` | NUMERIC |  | The total patient adjustments for a guarantor. |
| 29 | `TOT_INS_PMT_ADJ` | NUMERIC |  | The total insurance payments for a guarantor. |
| 30 | `TOT_INS_ADJ_AMT` | NUMERIC |  | The total insurance adjustments for a guarantor. |
| 31 | `PMT_PLAN_OVERDUE_AMT` | NUMERIC |  | The overdue amount on the payment plan. |
| 32 | `AUTOPAY_CARD_ID` | NUMERIC |  | The payment method that is used for guarantor's Auto Pay. |
| 33 | `AUTOPAY_DATE` | DATETIME |  | Date to charge the payment method for this specific statement if its guarantor is on Auto Pay. |
| 34 | `AUTOPAY_NXT_PMT_AMT` | NUMERIC |  | The amount that the system calculates as the next payment amount. This amount is based on the current scheduled payment plus the next monthly due amount. It also takes into account the system definition settings regarding whether auto pay should collect overdue amounts or be reduced by other patient payments. This amount will be charged to the payment method for this specific statement if its guarantor is on Auto Pay. |
| 35 | `PMT_PLAN_PAID_AHEAD_AMT` | NUMERIC |  | The paid ahead amount on the payment plan. |
| 36 | `TOT_CONTESTED_BAL` | NUMERIC |  | The total contested balance for the guarantor. |
| 37 | `PROP_PMT_PLAN_MONTH_AMT` | NUMERIC |  | If the guarantor can sign up for a payment plan, then this is the proposed monthly amount that will be shown if they were to sign up in MyChart. |
| 38 | `PROP_PMT_PLAN_NUM_PMTS` | INTEGER |  | If the guarantor can sign up for a payment plan, then this is the proposed number of payments that will be shown if they were to sign up in MyChart. |
| 39 | `TOT_SCHED_PMTS` | NUMERIC |  | The total scheduled payments on the statement. |
| 40 | `PAY_NOW_AMT` | NUMERIC |  | The amount the patient should pay now. This is calculated by subtracting scheduled payments from the statement due amount. |
| 41 | `PMT_PLAN_LN` | INTEGER |  | The payment plan line on the guarantor. This gives additional details about the payment plan. |
| 42 | `IS_AUTOPAY_SUSPENDED_YN` | VARCHAR |  | Indicates whether or not the Auto Pay is currently suspended for the payment plan. |
| 43 | `AUTOPAY_DECLINE_DATE` | DATETIME |  | The date Auto Pay was suspended because of a declined payment. |
| 44 | `STMT_DUE_DATE` | DATETIME |  | The due date of the statement. |
| 45 | `PMT_PLAN_TRACKER_SCHED_PMT_ID` | NUMERIC |  | The unique ID of the payment plan expected payment tracker record when the statement was generated. |
| 46 | `PMT_PLAN_DEFER_MONTHS` | INTEGER |  | The number of months that the payment plan was deferred when the statement was generated. |
| 47 | `PMT_PLAN_HARS_BAL_NOT_ON_PLAN` | NUMERIC |  | The total balance not on a payment plan for the hospital accounts that are on the payment plan that generated this statement. |
| 48 | `PMT_PLAN_INITIAL_EST_BAL` | NUMERIC |  | The initial balance of all the pre-service estimates on the payment plan that generated this statement. |
| 49 | `PMT_PLAN_REMAINING_EST_BAL` | NUMERIC |  | The remaining balance of all the pre-service estimates on the payment plan that generated this statement. |
| 50 | `PMT_PLAN_PMT_NOT_APPLY_AMT` | NUMERIC |  | Total of payment plan payments not yet applied to charges. |
| 51 | `NEW_PAT_DISC_ADJ` | NUMERIC |  | Stores the new patient discount amount that occurred since the last statement. |
| 52 | `TOT_PAT_DISC_ADJ` | NUMERIC |  | Stores the total patient discount amount on the current statement. |
| 53 | `NEW_PAT_REF` | NUMERIC |  | Stores the new patient refund amount that occurred since the last statement. |
| 54 | `TOT_PAT_REF` | NUMERIC |  | Stores the total patient refund amount on the current statement. |
| 55 | `NEW_PAT_OTH_ADJ` | NUMERIC |  | Stores the new patient other adjustment amount that occurred since the last statement. Patient other adjustments are any patient adjustments that are not refunds or discounts. |
| 56 | `TOTAL_PAT_OTH_ADJ` | NUMERIC |  | Stores the total patient other adjustment amount on the current statement. Patient other adjustments are any patient adjustments that are not refunds or discounts. |
| 57 | `DISCOUNT_OFFER_AMT` | NUMERIC |  | Stores the proposed discount amount for the statement. |
| 58 | `PAY_NOW_BEFORE_DISCOUNT_AMT` | NUMERIC |  | The amount a guarantor would pay for a statement that includes the proposed discount. |
| 59 | `DISCOUNT_OFFER_END_DATE` | DATETIME |  | This is the date by which a guarantor must pay the balance by to receive the proposed discount for their payment. |
| 60 | `DISCOUNT_OFFER_PCT` | NUMERIC |  | The discount percentage that is used for display for proposed payment discounts. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

