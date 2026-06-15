# STMT_CONS_SP_DETAIL

> This table contains information about insourced balances on your statement print and detail bill records.

**Primary key:** `PRINT_ID`  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the stmt/det bill record. |
| 2 | `CONS_SP_PREV_PAT_BAL` | NUMERIC |  | Stores the total previous patient balance for all received self-pay accounts on the statement. |
| 3 | `CONS_SP_PREV_AMT_DUE` | NUMERIC |  | Stores the total previous amount due for all received self-pay accounts on the statement. |
| 4 | `CONS_SP_NEW_CHG_AMT` | NUMERIC |  | Stores the total new charges for all received self-pay accounts on the statement. |
| 5 | `CONS_SP_NEW_PMT_AMT` | NUMERIC |  | Stores the total new payments for all received self-pay accounts on the statement. |
| 6 | `CONS_SP_NEW_ADJ_AMT` | NUMERIC |  | Stores the total new adjustments for all received self-pay accounts on the statement. |
| 7 | `CONS_SP_NEW_INS_PMTS` | NUMERIC |  | Stores the new insurance payments for all received self-pay accounts on the statement. |
| 8 | `CONS_SP_NEW_INS_ADJS` | NUMERIC |  | Stores the new insurance adjustments for all received self-pay accounts on the statement. |
| 9 | `CONS_SP_NEW_PAT_PMTS` | NUMERIC |  | Stores the new patient payments for all received self-pay accounts on the statement. |
| 10 | `CONS_SP_NEW_PAT_ADJS` | NUMERIC |  | Stores the new patient adjustments for all received self-pay accounts on the statement. |
| 11 | `CONS_SP_TOT_CHG_AMT` | NUMERIC |  | Stores the total charges for all received self-pay accounts on the statement. |
| 12 | `CONS_SP_TOT_PMT_AMT` | NUMERIC |  | Stores the total payments for all received self-pay accounts on the statement. |
| 13 | `CONS_SP_TOT_ADJ_AMT` | NUMERIC |  | Stores the total adjustments for all received self-pay accounts on the statement. |
| 14 | `CONS_SP_CURR_PAT_BAL` | NUMERIC |  | Stores the current patient balance for all received self-pay accounts on the statement. |
| 15 | `CONS_SP_CURR_DUE_AMT` | NUMERIC |  | Stores the current amount due for all received self-pay accounts on the statement. |
| 16 | `CONS_SP_PREV_INS_BAL` | NUMERIC |  | Stores the previous insurance balance for all received self-pay accounts on the statement. |
| 17 | `CONS_SP_CURR_INS_BAL` | NUMERIC |  | Stores the current insurance balance for all received self-pay accounts on the statement. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

