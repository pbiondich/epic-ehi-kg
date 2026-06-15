# ACCT_EB_STMT_HIST

> This table contains enterprise statement history information.

**Primary key:** `ACCOUNT_ID`, `LINE`  
**Columns:** 67

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the guarantor record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACCEPT_DT` | DATETIME |  | Enterprise statement acceptance date. |
| 4 | `END_BATCH_DT` | DATETIME |  | End batch date for the enterprise statement. |
| 5 | `PRINT_RECORD_ID` | NUMERIC |  | This column stores the unique identifier for the Statement Print record. |
| 6 | `IS_DEMAND_STMT_YN` | VARCHAR |  | Whether the statement was a demand statement. |
| 7 | `FOLLOW_UP_CYC_LVL` | NUMERIC |  | Enterprise guarantor follow up cycle level. This is used for looking up follow up cycle level message to be printed on statement. |
| 8 | `PREV_BALANCE_AMT` | NUMERIC |  | Previous non-demand statement balance. |
| 9 | `PREV_DUE_AMT` | NUMERIC |  | Previous non-demand statement amount due. |
| 10 | `NEW_CHARGES_AMT` | NUMERIC |  | New charges since last non-demand statement. |
| 11 | `NEW_PAYMENTS_AMT` | NUMERIC |  | New payments since last non-demand statement. |
| 12 | `NEW_ADJS_AMT` | NUMERIC |  | New adjustments since last non-demand statement. |
| 13 | `TOTAL_CHARGES_AMT` | NUMERIC |  | Total charges amount on the statement. |
| 14 | `TOTAL_PAYMENTS_AMT` | NUMERIC |  | Total payments amount on the statement. |
| 15 | `TOTAL_ADJS_AMT` | NUMERIC |  | Total adjustments amount on the statement. |
| 16 | `CUR_BALANCE_AMT` | NUMERIC |  | Current statement balance. |
| 17 | `CUR_DUE_AMT` | NUMERIC |  | Current statement amount due |
| 18 | `PROC_PROF_YN` | VARCHAR |  | Whether this statement contains balance from billing system Professional Billing. This will be YES if billing system Professional Billing is using enterprise statement in the guarantor's service area. |
| 19 | `PROC_HOSP_YN` | VARCHAR |  | Whether this statement contains balance from billing system Hospital Billing. This will be YES if billing system Hospital Billing is using enterprise statement in the guarantor's service area. |
| 20 | `INVOICE_NUMBER` | VARCHAR |  | Invoice number for the statement. |
| 21 | `HB_PREV_BAL_AMT` | NUMERIC |  | Hospital portion of the previous statement amount due. |
| 22 | `HB_PREV_DUE_AMT` | NUMERIC |  | This column stores the hospital portion of the previous statement amount due. |
| 23 | `HB_NEW_CHARGES_AMT` | NUMERIC |  | Hospital portion of the new charges. |
| 24 | `HB_NEW_PAYMENT_AMT` | NUMERIC |  | Hospital portion of the new payments. |
| 25 | `HB_NEW_ADJS_AMT` | NUMERIC |  | Hospital portion of the new adjustments. |
| 26 | `HB_TOT_CHARGES_AMT` | NUMERIC |  | Hospital portion of the total charges. |
| 27 | `HB_TOT_PAYMENT_AMT` | NUMERIC |  | Hospital portion of the total payments. |
| 28 | `HB_TOT_ADJS_AMT` | NUMERIC |  | Hospital portion of the total adjustments. |
| 29 | `HB_CUR_BALANCE_AMT` | NUMERIC |  | Hospital portion of the current balance. |
| 30 | `HB_CUR_DUE_AMT` | NUMERIC |  | Hospital portion of the current amount due. |
| 31 | `HB_PMTPLAN_TOT_AMT` | NUMERIC |  | Hospital billing payment plan original balance. |
| 32 | `HB_PMTPLAN_BAL_AMT` | NUMERIC |  | Hospital billing payment plan current balance. |
| 33 | `HB_PMTPLAN_DUE_AMT` | NUMERIC |  | Hospital billing payment plan current amount due. |
| 34 | `HB_PRORATION_AMT` | NUMERIC |  | This is the prorated self-pay balance contributed to the hospital portion of current balance. |
| 35 | `PREV_INS_BAL` | NUMERIC |  | This column stores the previous insurance balance that was shown on the statement. |
| 36 | `CUR_INS_BAL` | NUMERIC |  | This column stores the current insurance balance from the statement. |
| 37 | `IS_INFO_STMT_YN` | VARCHAR |  | Indicates whether the statement is informational. This item is "1" if the statement was informational, and "0" or " if not. A statement is informational if no self-pay balance was due for the guarantor. |
| 38 | `PB_PREV_INS_BAL` | NUMERIC |  | This column stores the previous insurance balance for professional billing. |
| 39 | `PB_CUR_INS_BAL` | NUMERIC |  | This column stores the current insurance balance for professional billing. |
| 40 | `HB_PREV_INS_BAL` | NUMERIC |  | This column stores the previous insurance balance for hospital billing. |
| 41 | `HB_CUR_INS_BAL` | NUMERIC |  | This column stores the current insurance balance for hospital billing. |
| 42 | `STMT_SP_LEVEL_C_NAME` | VARCHAR |  | The guarantor self-pay follow-up level for the statement. |
| 43 | `STMT_DVRY_MTD_C_NAME` | VARCHAR |  | Stores how the statement was delivered. |
| 44 | `STMT_FST_VW_DTTM` | DATETIME (UTC) |  | This column stores the instant the statement was first viewed in MyChart. The date and time for this column is stored in Coordinated Universal Time (UTC) and can be converted to local time by using the EFN_UTC_TO_LOCAL Clarity database function. |
| 45 | `STMT_LST_VW_DTTM` | DATETIME (UTC) |  | This column stores the instant the statement was last viewed in MyChart. The date and time for this column is stored in Coordinated Universal Time (UTC) and can be converted to local time by using the EFN_UTC_TO_LOCAL Clarity database function. |
| 46 | `STMT_PAPER_RSN_C_NAME` | VARCHAR |  | Stores the reason why the statement was sent via paper. |
| 47 | `EB_PMT_PLAN_TOT_AMT` | NUMERIC |  | Enterprise payment plan total. This is the total amount this payment was created to capture. |
| 48 | `EB_PMT_PLAN_BAL_AMT` | NUMERIC |  | Enterprise payment plan balance. This is how much remains to be paid for this payment plan. |
| 49 | `EB_PMT_PLAN_DUE_AMT` | NUMERIC |  | Enterprise payment plan due. This is how much was due for the next payment under this plan for each line in the history. |
| 50 | `PB_HELD_AMT` | NUMERIC |  | Professional billing held amount. This is the amount that is held from the patient statement due to some or all of the charges being with insurance at the time the statement is sent. |
| 51 | `PB_VOID_TRANS_AMT` | NUMERIC |  | Professional billing void/transfer amount. This is the amount of the balance that was voided or transferred since the previous statement. |
| 52 | `STMT_HIST_IS_MYC_NOTIF_YN` | VARCHAR |  | Stores if the statement/detail bill notification was sent via MyChart. |
| 53 | `STMT_HX_CNTST_BAL` | NUMERIC |  | Stores the contested balance on the statement. |
| 54 | `STMT_HX_TOT_SCH_PMT` | NUMERIC |  | The total amount of all scheduled payments on the statement. |
| 55 | `STMT_HX_PAY_NOW` | NUMERIC |  | The pay now amount on the statement. This is the amount due subtracted by the total scheduled payment amount. |
| 56 | `PB_CUR_DUE_AMT` | NUMERIC |  | The professional portion of the current statement amount due. |
| 57 | `PB_CUR_BALANCE_AMT` | NUMERIC |  | The professional portion of the current statement balance. |
| 58 | `PB_NEW_ADJS_AMT` | NUMERIC |  | The total new professional adjustment amount posted since last statement. |
| 59 | `PB_NEW_CHARGES_AMT` | NUMERIC |  | The total new professional charge amount posted since last statement. |
| 60 | `PB_NEW_PAYMENT_AMT` | NUMERIC |  | The total new professional payment amount posted since last statement. |
| 61 | `PB_PMTPLAN_BAL_AMT` | NUMERIC |  | The professional payment plan balance. |
| 62 | `PB_PMTPLAN_DUE_AMT` | NUMERIC |  | The professional payment plan amount due. |
| 63 | `PB_PMTPLAN_TOT_AMT` | NUMERIC |  | The professional payment plan total amount. |
| 64 | `PB_PREV_DUE_AMT` | NUMERIC |  | The previous professional portion statement amount due. |
| 65 | `PB_TOT_ADJS_AMT` | NUMERIC |  | The total professional adjustment amount. |
| 66 | `PB_TOT_CHARGES_AMT` | NUMERIC |  | The total professional charge amount. |
| 67 | `PB_TOT_PAYMENT_AMT` | NUMERIC |  | The total professional payment amount. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |

