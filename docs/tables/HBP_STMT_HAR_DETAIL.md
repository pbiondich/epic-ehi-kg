# HBP_STMT_HAR_DETAIL

> This table stores the hospital accounts that are associated with a given Hospital Billing statement print record.

**Primary key:** `HBP_PRINT_ID`, `LINE`  
**Columns:** 39

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HBP_PRINT_ID` | NUMERIC | PK FK→ | The unique identifier for the bill print record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | The hospital account ID. |
| 4 | `ADMIT_DATE` | DATETIME |  | The admit date. |
| 5 | `DISCH_DATE` | DATETIME |  | The discharge date. |
| 6 | `FIRST_STMT_DATE` | DATETIME |  | The first statement date. |
| 7 | `NUM_PREV_STMTS_SENT` | INTEGER |  | The number of previous statements sent. |
| 8 | `PRIM_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 9 | `PREV_STMT_DATE` | DATETIME |  | The previous statement balance. |
| 10 | `PREV_BAL` | NUMERIC |  | The previous balance. |
| 11 | `PREV_INS_BAL` | NUMERIC |  | The previous insurance balance. |
| 12 | `TOT_CHG_AMT` | NUMERIC |  | The total charge amount. |
| 13 | `NEW_CHG_AMT` | NUMERIC |  | The new charge amount since the last statement. |
| 14 | `NEW_PAT_CHG_AMT` | NUMERIC |  | The new patient charge amount. |
| 15 | `NEW_INS_CHG_AMT` | NUMERIC |  | The new insurance charge amount. |
| 16 | `TOT_PMT_AMT` | NUMERIC |  | The total payment amount. |
| 17 | `NEW_PMT_AMT` | NUMERIC |  | The new payment amount since the last statement. |
| 18 | `NEW_PAT_PMT_AMT` | NUMERIC |  | The new patient payment amount. |
| 19 | `NEW_INS_PMT_AMT` | NUMERIC |  | The new insurance payment amount. |
| 20 | `TOT_ADJ_AMT` | NUMERIC |  | The total adjustment amount. |
| 21 | `NEW_ADJ_AMT` | NUMERIC |  | The new adjustment amount since the last statement. |
| 22 | `NEW_PAT_ADJ_AMT` | NUMERIC |  | The new patient adjustment amount. |
| 23 | `NEW_INS_ADJ_AMT` | NUMERIC |  | The new insurance adjustment amount. |
| 24 | `CURR_INS_BAL` | NUMERIC |  | The current insurance balance. |
| 25 | `CURR_BAL` | NUMERIC |  | The current balance on the hospital account. |
| 26 | `CURR_PAT_LIABILITY_AMT` | NUMERIC |  | The current patient liability amount. |
| 27 | `PAT_LIAB_SPLIT_UP` | VARCHAR |  | The patient liability split-up. |
| 28 | `PMT_PLAN_INIT_BAL` | NUMERIC |  | The initial balance on the payment plan. |
| 29 | `PMT_PLAN_REMAINING_BAL` | NUMERIC |  | The remaining balance on the payment plan. |
| 30 | `BUCKET_ID` | NUMERIC | shared | The liability bucket ID. |
| 31 | `IS_INFORMATIONAL_YN` | VARCHAR |  | Indicates whether or not the hospital account is on an informational statement. |
| 32 | `CLAIM_PRINT_ID` | NUMERIC | shared | The claim print ID. |
| 33 | `SELFPAY_STATUS_C_NAME` | VARCHAR |  | The self-pay status. |
| 34 | `SP_LEVEL_C_NAME` | VARCHAR |  | The self-pay follow-up level. |
| 35 | `FOLLOW_UP_LEVEL` | INTEGER |  | The follow-up level. |
| 36 | `COLLECTION_STATUS_C_NAME` | VARCHAR |  | The collection status. |
| 37 | `COLL_AGENCY_ID` | NUMERIC |  | The collection agency. |
| 38 | `COLL_AGENCY_ID_COLL_AGENCY_NAME` | VARCHAR |  | The name of the collection agency. |
| 39 | `IS_OUTSOURCED_YN` | VARCHAR |  | Indicates whether or not the hospital account has been outsourced. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HBP_PRINT_ID` | [HBP_STMT_PRINT](HBP_STMT_PRINT.md) | sole_pk | high |
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

