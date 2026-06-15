# STMT_PB_DETAIL

> This table contains Professional Billing information about your statement print and detail bill records.

**Primary key:** `PRINT_ID`  
**Columns:** 54

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the statement print or detail bill record. |
| 2 | `PREV_PAT_BAL` | NUMERIC |  | The Professional Billing outstanding self-pay balance for the guarantor from the previous statement. |
| 3 | `PREV_AMT_DUE` | NUMERIC |  | The Professional Billing amount due for the guarantor from the previous statement. It only includes outstanding self-pay balances not on a payment plan. |
| 4 | `NEW_CHG_AMT` | NUMERIC |  | The Professional Billing new charge amount. |
| 5 | `NEW_PMT_AMT` | NUMERIC |  | The Professional Billing new payment amount. |
| 6 | `NEW_ADJ_AMT` | NUMERIC |  | The Professional Billing new adjustment amount. |
| 7 | `TOT_CHG_AMT` | NUMERIC |  | The Professional Billing total charge amount. |
| 8 | `TOT_PMT_AMT` | NUMERIC |  | The Professional Billing total payment amount. |
| 9 | `TOT_ADJ_AMT` | NUMERIC |  | The Professional Billing total adjustment amount. |
| 10 | `CURR_PAT_BAL` | NUMERIC |  | The Professional Billing outstanding self-pay balance for the guarantor. |
| 11 | `CURR_AMT_DUE` | NUMERIC |  | The Professional Billing amount due for the guarantor. It only includes outstanding self-pay balances not on a payment plan. |
| 12 | `PMT_PLAN_TOT` | NUMERIC |  | The Professional Billing payment plan total amount. |
| 13 | `PMT_PLAN_BAL` | NUMERIC |  | The Professional Billing payment plan balance. |
| 14 | `PMT_PLAN_DUE` | NUMERIC |  | The Professional Billing payment plan due amount. |
| 15 | `FOLLOW_UP_CYCLE_AGING_DATE` | DATETIME |  | The Professional Billing follow-up cycle aging date. |
| 16 | `IS_INFORMATIONAL_YN` | VARCHAR |  | Indicates whether or not this is informational (meaning the amount due is zero). |
| 17 | `PREV_INS_BAL` | NUMERIC |  | The previous Professional Billing insurance balance. |
| 18 | `NEW_INS_CHG_AMT` | NUMERIC |  | The new Professional Billing insurance charge amount. |
| 19 | `NEW_INS_PMT_AMT` | NUMERIC |  | The new Professional Billing insurance payment amount. |
| 20 | `NEW_INS_ADJ_AMT` | NUMERIC |  | The new Professional Billing insurance adjustment amount. |
| 21 | `CURR_INS_BAL` | NUMERIC |  | The current Professional Billing insurance balance. |
| 22 | `NEW_PAT_CHG_AMT` | NUMERIC |  | The new Professional Billing patient charge amount. |
| 23 | `NEW_PAT_PMT_AMT` | NUMERIC |  | The new patient payment amount. |
| 24 | `NEW_PAT_ADJ_AMT` | NUMERIC |  | The new patient adjustment amount. |
| 25 | `PREV_UNDIST_AMT` | NUMERIC |  | Stores the total undistributed amount from previous statement. |
| 26 | `AUTOPAY_CARD_ID` | NUMERIC |  | The credit card used for the Professional Billing automatic payment plan. |
| 27 | `AUTOPAY_DATE` | DATETIME |  | The next date that the credit card will be charged for the Professional Billing automatic payment plan. |
| 28 | `AUTOPAY_AMT_DUE` | NUMERIC |  | Stores the amount that the credit card will be charged for the Professional Billing automatic payment plan. |
| 29 | `TOT_DEBIT_AMT` | NUMERIC |  | The total debit amount. |
| 30 | `TOT_DEBIT_ADJ_AMT` | NUMERIC |  | The total debit adjustment amount. |
| 31 | `TOT_CREDIT_AMT` | NUMERIC |  | The total credit amount. |
| 32 | `TOT_CREDIT_ADJ_AMT` | NUMERIC |  | The total credit adjustment amount. |
| 33 | `TOT_MATCH_INS_PMT_AMT` | NUMERIC |  | The total matched insurance payment amount. |
| 34 | `TOT_MATCH_PAT_PMT_AMT` | NUMERIC |  | The total matched patient payment amount. |
| 35 | `TOT_MATCH_ADJ_AMT` | NUMERIC |  | The total matched adjustment amount. |
| 36 | `TOT_UNDIST_AMT` | NUMERIC |  | The total undistributed amount. |
| 37 | `PAT_UNDIST_AMT` | NUMERIC |  | The patient undistributed amount. |
| 38 | `INS_UNDIST_AMT` | NUMERIC |  | The insurance undistributed amount. |
| 39 | `TOT_VOIDED_CHG_AMT` | NUMERIC |  | The total voided charge amount. |
| 40 | `TOT_VOIDED_DEBIT_ADJ_AMT` | NUMERIC |  | The total voided debit adjustment amount. |
| 41 | `TOT_VOIDED_PMT_AMT` | NUMERIC |  | The total voided payment amount. |
| 42 | `TOT_VOIDED_CREDIT_ADJ_AMT` | NUMERIC |  | The total voided credit adjustment amount. |
| 43 | `CURR_ACCT_BAL` | NUMERIC |  | The current account balance. |
| 44 | `NEW_SKIPPED_CHG_TOT` | NUMERIC |  | Sum of the original amount of charges that are skipped this statement and shown on the previous statement. |
| 45 | `NEW_UNSKIPPED_CHG_TOT` | NUMERIC |  | Sum of the original amount of charges that are shown on this statement and skipped on the previous statement. |
| 46 | `NEW_VOIDED_TX_TOT` | NUMERIC |  | Sum of the original amount of void debits that are shown on previous statement. |
| 47 | `NEW_ADJ_TX_TOT` | NUMERIC |  | Sum of new adjustments matched amount. |
| 48 | `NEW_PMT_ADJ_TOT` | NUMERIC |  | Sum of the difference of the payment's outstanding amount between current statement and previous statement. |
| 49 | `NEW_PAT_DISCNT_CHARITY_ADJ` | NUMERIC |  | Stores the new PB patient discount amount that occurred since the last statement. |
| 50 | `TOT_PAT_DISCNT_CHARITY_ADJ` | NUMERIC |  | Stores the total PB patient discount amount on the current statement. |
| 51 | `NEW_PAT_RFND` | NUMERIC |  | Stores the new PB patient refund amount that occurred since the last statement. |
| 52 | `TOT_PAT_RFND` | NUMERIC |  | Stores the total PB patient refund amount on the current statement. |
| 53 | `NEW_PAT_OTHER_ADJ` | NUMERIC |  | Stores the new PB patient other adjustment amount that occurred since the last statement. Patient other adjustments are any patient adjustments that are not refunds or discounts. |
| 54 | `TOT_PAT_OTHER_ADJ` | NUMERIC |  | Stores the total PB patient other adjustment amount on the current statement. Patient other adjustments are any patient adjustments that are not refunds or discounts. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

