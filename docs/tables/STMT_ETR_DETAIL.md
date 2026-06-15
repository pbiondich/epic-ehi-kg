# STMT_ETR_DETAIL

> This table stores information about Professional Billing transactions that are associated with a given statement.

**Primary key:** `PRINT_ID`, `LINE`  
**Columns:** 28  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the statement print or detail bill record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TX_ID` | NUMERIC | shared | The Professional Billing transaction ID. |
| 4 | `PAT_ID` | VARCHAR | FK→ | The patient ID for the transaction. |
| 5 | `COVERAGE_ID` | NUMERIC | FK→ | The coverage ID for the transaction. |
| 6 | `PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 7 | `IS_ASSIGNED_TO_PAYER_YN` | VARCHAR |  | Indicates whether or not the transaction is assigned to a payer. |
| 8 | `POST_DATE` | DATETIME |  | The transaction post date. |
| 9 | `SERVICE_DATE` | DATETIME |  | The transaction service date. |
| 10 | `DESCRIPTION` | VARCHAR |  | The transaction description. |
| 11 | `UNIT` | NUMERIC |  | The transaction units. |
| 12 | `AMT_DUE` | NUMERIC |  | The transaction due amount. |
| 13 | `DEBIT_ORIG_AMT` | NUMERIC |  | The Professional Billing debit original amount. |
| 14 | `CREDIT_ORIG_AMT` | NUMERIC |  | The Professional Billing credit original amount. |
| 15 | `DEBIT_HOLD_AMT` | NUMERIC |  | The Professional Billing debit hold amount. |
| 16 | `CREDIT_HOLD_AMT` | NUMERIC |  | The Professional Billing credit hold amount. |
| 17 | `ADJ_AMT` | NUMERIC |  | The Professional Billing adjustment amount. |
| 18 | `MATCH_TX_INS_PMT_AMT` | NUMERIC |  | The Professional Billing matching transaction insurance payment amount. |
| 19 | `MATCH_TX_PAT_PMT_AMT` | NUMERIC |  | The Professional Billing matching transaction patient payment amount. |
| 20 | `MATCH_TX_ADJ_AMT` | NUMERIC |  | The Professional Billing matching transaction adjustment amount. |
| 21 | `NOTES` | VARCHAR |  | The Professional Billing notes. |
| 22 | `HOLD_STATUS_C_NAME` | VARCHAR | org | The Professional Billing hold status. |
| 23 | `IS_NEW_TX_YN` | VARCHAR |  | Indicates whether or not this is a new transaction. |
| 24 | `INS_AMT` | NUMERIC |  | Insurance balance of a debit transaction. |
| 25 | `PAT_AMT` | NUMERIC |  | Patient amount of a debit transaction. |
| 26 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | The hospital account ID for this professional transaction. |
| 27 | `PURCHASE_SVC_AMT` | NUMERIC |  | The purchased service amount. |
| 28 | `PURCHASE_SVC_POS` | INTEGER |  | The purchased service place of service name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

