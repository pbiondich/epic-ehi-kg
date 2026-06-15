# STMT_HSP_ACCT_DETAIL

> This table contains information about hospital accounts that are associated with a given statement.

**Primary key:** `PRINT_ID`, `LINE`  
**Columns:** 95

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the statement print or detail bill record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | The hospital account ID. |
| 4 | `HB_PREV_PAT_BAL` | NUMERIC |  | The hospital account previous patient balance. |
| 5 | `HB_NEW_CHG_AMT` | NUMERIC |  | The hospital account new charge amount. |
| 6 | `HB_NEW_PMT_AMT` | NUMERIC |  | The hospital account new payment amount. |
| 7 | `HB_NEW_ADJ_AMT` | NUMERIC |  | The hospital account new adjustment amount. |
| 8 | `HB_TOT_CHG_AMT` | NUMERIC |  | The hospital account total charge amount. |
| 9 | `HB_TOT_PMT_AMT` | NUMERIC |  | The hospital account total payment amount. |
| 10 | `HB_TOT_ADJ_AMT` | NUMERIC |  | The hospital account total adjustment amount. |
| 11 | `HB_CURR_PAT_BAL` | NUMERIC |  | Stores the Hospital Billing outstanding self-pay balance for the hospital account. |
| 12 | `HB_CURR_AMT_DUE` | NUMERIC |  | Stores the Hospital Billing amount due for the hospital account. It is usually the self-pay outstanding balance, but will be zero for accounts on a payment plan (since the payment plan amount due is really at the guarantor level unless sending hospital account level statements). |
| 13 | `HB_PAT_LIAB_SPLIT_UP` | VARCHAR |  | The hospital account patient liability split-up. |
| 14 | `HB_ADMIT_DATE` | DATETIME |  | The hospital account admit date. |
| 15 | `HB_DISCHARGE_DATE` | DATETIME |  | The hospital account discharge date. |
| 16 | `HB_PRIM_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 17 | `HB_SP_STATUS_C_NAME` | VARCHAR |  | The hospital account self-pay status. |
| 18 | `HB_FIRST_STMT_DATE` | DATETIME |  | The hospital account first statement date. |
| 19 | `HB_PREV_STMT_DATE` | DATETIME |  | The hospital account previous statement date. |
| 20 | `HB_SENT_STMT_CNT` | INTEGER |  | The number of statements sent for a hospital account. |
| 21 | `HB_IS_INFORMATIONAL_YN` | VARCHAR |  | The hospital account-level storage of whether this particular hospital account had a patient balance. |
| 22 | `HB_PREV_INS_BAL` | NUMERIC |  | The hospital account-level previous insurance balance. |
| 23 | `HB_NEW_INS_CHG_AMT` | NUMERIC |  | The new insurance charges at the hospital account level. |
| 24 | `HB_NEW_INS_PMT_AMT` | NUMERIC |  | The new insurance payments for this hospital account. |
| 25 | `HB_NEW_INS_ADJ_AMT` | NUMERIC |  | The new insurance adjustments on this hospital account. |
| 26 | `HB_CURR_INS_BAL` | NUMERIC |  | The current insurance balance on this hospital account. |
| 27 | `PB_PREV_PAT_BAL` | NUMERIC |  | Previous professional patient balance on the hospital account. |
| 28 | `PB_NEW_CHG_AMT` | NUMERIC |  | New professional charges on the hospital account. |
| 29 | `PB_NEW_PMT_AMT` | NUMERIC |  | New professional payments on the hospital account. |
| 30 | `PB_NEW_ADJ_AMT` | NUMERIC |  | New professional adjustments on the hospital account. |
| 31 | `PB_TOT_CHG_AMT` | NUMERIC |  | Total professional charges on the hospital account. |
| 32 | `PB_TOT_PMT_AMT` | NUMERIC |  | Total professional payments on the hospital account. |
| 33 | `PB_TOT_ADJ_AMT` | NUMERIC |  | Total professional adjustments on the hospital account. |
| 34 | `PB_CURR_PAT_BAL` | NUMERIC |  | Stores the Professional Billing outstanding self-pay balance for the hospital account. |
| 35 | `PB_CURR_AMT_DUE` | NUMERIC |  | Stores the Professional Billing amount due for the hospital account. It is usually the self-pay outstanding balance, but will be zero for accounts on a payment plan (since the payment plan amount due is really at the guarantor level unless sending hospital account level statements). |
| 36 | `PB_PREV_INS_BAL` | NUMERIC |  | Previous professional insurance balance on the hospital account. |
| 37 | `PB_NEW_INS_CHG_AMT` | NUMERIC |  | The new professional charges for which an insurance payment is expected. |
| 38 | `PB_NEW_INS_PMT_AMT` | NUMERIC |  | The new professional payments that have been applied to the insurance portion of charges and debit adjustments. |
| 39 | `PB_NEW_INS_ADJ_AMT` | NUMERIC |  | The amount of new adjustment applied to the insurance portion of the hospital account. |
| 40 | `PB_CURR_INS_BAL` | NUMERIC |  | The current professional insurance balance. |
| 41 | `PB_TOT_PAT_PMT_AMT` | NUMERIC |  | Stores the total Professional Billing patient payments for a hospital account. |
| 42 | `PB_TOT_PAT_ADJ_AMT` | NUMERIC |  | Stores the total Professional Billing patient adjustments for a hospital account. |
| 43 | `PB_TOT_INS_PMT_AMT` | NUMERIC |  | Stores the total Professional Billing insurance payments for a hospital account. |
| 44 | `PB_TOT_INS_ADJ_AMT` | NUMERIC |  | Stores the total Professional Billing insurance adjustments for a hospital account. |
| 45 | `HB_NEW_PAT_CHG_AMT` | NUMERIC |  | Stores the new patient charges for a hospital account. |
| 46 | `HB_NEW_PAT_PMT_AMT` | NUMERIC |  | Stores the new patient payments for a hospital account. |
| 47 | `HB_NEW_PAT_ADJ_AMT` | NUMERIC |  | Stores the new patient adjustments for a hospital account. |
| 48 | `HB_PMT_PLAN_INIT_BAL` | NUMERIC |  | Stores the Hospital Billing hospital account-level initial payment plan balance. |
| 49 | `HB_PMT_PLAN_REMAIN_BAL` | NUMERIC |  | Stores the Hospital Billing hospital account-level remaining payment plan balance. |
| 50 | `HB_COLLECTION_STATUS_C_NAME` | VARCHAR |  | Stores the hospital account's collection status. |
| 51 | `HB_COLL_AGENCY_ID` | NUMERIC |  | Stores the outsource agency for the hospital account. |
| 52 | `HB_COLL_AGENCY_ID_COLL_AGENCY_NAME` | VARCHAR |  | The name of the collection agency. |
| 53 | `HB_IS_OUTSOURCED_YN` | VARCHAR |  | Stores if the hospital account has been outsourced. |
| 54 | `HB_FOLLOW_UP_CYCLE_LEVEL` | INTEGER |  | Follow-up cycle level for this hospital account. |
| 55 | `HB_SP_FOLLOW_UP_LEVEL_C_NAME` | VARCHAR |  | Stores the hospital account self-pay follow-up level. |
| 56 | `HB_PMT_PLAN_DUE` | NUMERIC |  | Stores the Hospital Billing hospital account-level payment plan due. |
| 57 | `HB_PMT_PLAN_MONTHLY_AMT` | NUMERIC |  | Stores the Hospital Billing hospital account-level payment plan monthly amount. |
| 58 | `HB_STATEMENT_TYPE_C_NAME` | VARCHAR |  | The Hospital Billing hospital account statement type. |
| 59 | `HB_SP_AGING_DATE` | DATETIME |  | This item stores the date for aging the self-pay balances. |
| 60 | `HB_PREV_STMT_END_BATCH_DATE` | DATETIME |  | Stores the end system batch date of the last statement generated for the hospital account. |
| 61 | `HB_PREV_STMT_PRINT_ID` | NUMERIC |  | Stores the previous statement generated for the hospital account. |
| 62 | `HB_TOT_PAT_PMT_AMT` | NUMERIC |  | Stores the total Hospital Billing patient payments for a hospital account. |
| 63 | `HB_TOT_PAT_ADJ_AMT` | NUMERIC |  | Stores the total Hospital Billing patient adjustments for a hospital account. |
| 64 | `HB_TOT_INS_PMT_AMT` | NUMERIC |  | Stores the total Hospital Billing insurance payments for a hospital account. |
| 65 | `HB_TOT_INS_ADJ_AMT` | NUMERIC |  | Stores the total Hospital Billing insurance adjustments for a hospital account. |
| 66 | `HB_PMT_PLAN_OVERDUE_AMT` | NUMERIC |  | Stores the hospital account-level payment plan overdue amount. |
| 67 | `HB_PMT_PLAN_PAID_AHEAD_AMT` | NUMERIC |  | Stores the hospital account-level payment plan paid ahead amount. |
| 68 | `HB_ADVBILL_ESTIMATE_ID` | NUMERIC |  | Stores the advance bill estimate on the hospital account. |
| 69 | `HB_NEW_CONTESTED_CHG_AMT` | NUMERIC |  | Sum of new contested Hospital Billing charges for the hospital account. |
| 70 | `HB_NEW_CONTESTED_PMT_AMT` | NUMERIC |  | Sum of new contested Hospital Billing payments for the hospital account. |
| 71 | `HB_NEW_CONTESTED_ADJ_AMT` | NUMERIC |  | Sum of new contested Hospital Billing adjustments for the hospital account. |
| 72 | `HB_NEW_CONTESTED_INS_PMT_AMT` | NUMERIC |  | Sum of new contested Hospital Billing insurance payments for the hospital account. |
| 73 | `HB_NEW_CONTESTED_INS_ADJ_AMT` | NUMERIC |  | Sum of new contested Hospital Billing insurance adjustments for the hospital account. |
| 74 | `HB_CONTESTED_CHG_AMT` | NUMERIC |  | Sum of all contested Hospital Billing charges for the hospital account. |
| 75 | `HB_CONTESTED_PMT_AMT` | NUMERIC |  | Sum of all contested Hospital Billing payments for the hospital account. |
| 76 | `HB_CONTESTED_ADJ_AMT` | NUMERIC |  | Sum of all contested Hospital Billing adjustments for the hospital account. |
| 77 | `HB_CONTESTED_INS_PMT_AMT` | NUMERIC |  | Sum of all contested Hospital Billing insurance payments for the hospital account. |
| 78 | `HB_CONTESTED_INS_ADJ_AMT` | NUMERIC |  | Sum of all contested Hospital Billing insurance adjustments for the hospital account. |
| 79 | `HB_CONTESTED_BAL` | NUMERIC |  | Total contested balance for the hospital account. |
| 80 | `HB_NEW_PAT_DISCNT_CHARITY_ADJ` | NUMERIC |  | Stores the new HB patient discounts for this specific HAR that occurred since the last statement. |
| 81 | `HB_TOT_PAT_DISCNT_CHARITY_ADJ` | NUMERIC |  | Stores the total HB patient discount amount for this particular HAR on the current statement. |
| 82 | `HB_NEW_PAT_RFND` | NUMERIC |  | Stores the new HB patient refund amount for this specific HAR that occurred since the last statement. |
| 83 | `HB_TOT_PAT_RFND` | NUMERIC |  | Stores the total HB patient refund amount for this particular HAR on the current statement. |
| 84 | `HB_NEW_PAT_OTHER_ADJ` | NUMERIC |  | Stores the new HB patient other adjustment amount for this specific HAR that occurred since the last statement. Patient other adjustments are any patient adjustments that are not refunds or discounts. |
| 85 | `HB_TOT_PAT_OTHER_ADJ` | NUMERIC |  | Stores the total HB patient other adjustment amount for this specific HAR on the current statement. Patient other adjustments are any patient adjustments that are not refunds or discounts. |
| 86 | `PB_NEW_PAT_RFND` | NUMERIC |  | Stores the new PB patient refund amount for this specific HAR that occurred since the last statement. |
| 87 | `PB_TOT_PAT_RFND` | NUMERIC |  | Stores the total PB patient refund amount for this particular HAR on the current statement. |
| 88 | `PB_NEW_PAT_DISCNT_CHARITY_ADJ` | NUMERIC |  | Stores the new PB patient discount amount for this specific HAR that occurred since the last statement. |
| 89 | `PB_TOT_PAT_DISCNT_CHARITY_ADJ` | NUMERIC |  | Stores the total PB patient discount amount for this particular HAR on the current statement. |
| 90 | `PB_NEW_PAT_OTHER_ADJ` | NUMERIC |  | Stores the new PB patient other adjustment amount for this specific HAR that occurred since the last statement. Patient other adjustments are any patient adjustments that are not refunds or discounts. |
| 91 | `PB_TOT_PAT_OTHER_ADJ` | NUMERIC |  | Stores the total PB patient other adjustment amount for this specific HAR on the current statement. Patient other adjustments are any patient adjustments that are not refunds or discounts. |
| 92 | `DISCOUNT_OFFER_AMT` | NUMERIC |  | The proposed discount amount for this specific HAR. |
| 93 | `PAY_NOW_AMT` | NUMERIC |  | The due amount for this HAR including the proposed discount. |
| 94 | `DISCOUNT_OFFER_PCT` | NUMERIC |  | The percent discount proposed for this HAR. |
| 95 | `PB_HAR_EXPRESS_CLAIM_YN` | VARCHAR |  | Indicates if the visit HAR qualifies as an Express Claim visit. For a visit HAR to qualify as an Express Claim visit, the following conditions must be true: - All active charges on the HAR should have been sent on an outbound express claim and received a "payment expected" response from the insurance payer. - An actual payment transaction has not yet been received from the insurance payer. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

