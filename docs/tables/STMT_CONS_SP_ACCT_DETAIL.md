# STMT_CONS_SP_ACCT_DETAIL

> This table contains information about insourced hospital accounts that are associated with a given statement.

**Primary key:** `PRINT_ID`, `LINE`  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the stmt/det bill record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONS_SP_HAR_PREV_PAT_BAL` | NUMERIC |  | This stores the patient balance as of the last statement for a received self-pay hospital account. |
| 4 | `CONS_SP_HAR_NEW_CHG_AMT` | NUMERIC |  | Stores the amount of new charges on a received self-pay account for this statement. |
| 5 | `CONS_SP_HAR_NEW_PMT_AMT` | NUMERIC |  | Stores the amount of new payments on a received self-pay account for this statement. |
| 6 | `CONS_SP_HAR_NEW_ADJ_AMT` | NUMERIC |  | Stores the amount of new adjustments on a received self-pay account for this statement. |
| 7 | `CONS_SP_HAR_NEW_INS_PMT_AMT` | NUMERIC |  | Stores the amount of new insurance payments on a received self-pay account for this statement. |
| 8 | `CONS_SP_HAR_NEW_INS_ADJ_AMT` | NUMERIC |  | Stores the amount of new insurance adjustments on a received self-pay account for this statement. |
| 9 | `CONS_SP_HAR_NEW_PAT_PMT_AMT` | NUMERIC |  | Stores the amount of new patient payments on a received self-pay account for this statement. |
| 10 | `CONS_SP_HAR_NEW_PAT_ADJ_AMT` | NUMERIC |  | Stores the amount of new patient adjustments on a received self-pay account for this statement. |
| 11 | `CONS_SP_HAR_TOT_CHG_AMT` | NUMERIC |  | Stores the total charges for a received self-pay account. |
| 12 | `CONS_SP_HAR_TOT_PMT_AMT` | NUMERIC |  | Stores the total payments for a received self-pay account. |
| 13 | `CONS_SP_HAR_TOT_ADJ_AMT` | NUMERIC |  | Stores the total adjustments for a received self-pay account. |
| 14 | `CONS_SP_HAR_TOT_INS_PMT_AMT` | NUMERIC |  | Stores the total insurance payments for a received self-pay account. |
| 15 | `CONS_SP_HAR_TOT_INS_ADJ_AMT` | NUMERIC |  | Stores the total insurance adjustments for a received self-pay account. |
| 16 | `CONS_SP_HAR_TOT_PAT_PMT_AMT` | NUMERIC |  | Stores the total patient payments for a received self-pay account. |
| 17 | `CONS_SP_HAR_TOT_PAT_ADJ_AMT` | NUMERIC |  | Stores the total patient adjustments for a received self-pay account. |
| 18 | `CONS_SP_HAR_CURR_PAT_BAL` | NUMERIC |  | Stores the current balance for a received self-pay account. |
| 19 | `CONS_SP_HAR_CURR_DUE` | NUMERIC |  | Stores the current amount due for a received self-pay account. |
| 20 | `CONS_SP_HAR_PREV_INS_BAL` | NUMERIC |  | This stores the insurance balance as of the last statement for a received self-pay hospital account. |
| 21 | `CONS_SP_HAR_CURR_INS_BAL` | NUMERIC |  | This stores the insurance balance of the current statement for a received self-pay hospital account. |
| 22 | `CONS_SP_HAR_NEW_PAT_DISCNT_ADJ` | NUMERIC |  | This stores the new patient discounts for the current statement for a received self-pay hospital account. |
| 23 | `CONS_SP_HAR_TOT_PAT_DISCNT_ADJ` | NUMERIC |  | This stores the total patient discounts for the current statement for a received self-pay hospital account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

