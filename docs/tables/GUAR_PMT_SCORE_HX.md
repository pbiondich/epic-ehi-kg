# GUAR_PMT_SCORE_HX

> Contains information on the guarantor Payment History Score. Each line contains factors that contributed to the score for one billing system for one guarantor.

**Primary key:** `ACCOUNT_ID`, `LINE`  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the guarantor record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LAST_CALCULATED_UTC_DTTM` | DATETIME (UTC) |  | The last instant at which this payment history score was updated. |
| 4 | `BILLING_SYSTEM_C_NAME` | VARCHAR |  | The billing system of the payment history score in this line. |
| 5 | `SCORE` | INTEGER |  | The payment history score for a guarantor based on their self-pay history (PB, HB or EB score). |
| 6 | `NUM_ACCTS` | INTEGER |  | Number of accounts used to calculate the guarantor's payment history score. |
| 7 | `NUM_BAD_DEBT_ACCTS` | INTEGER |  | The number of accounts sent to bad debt in the history range for the guarantor's payment history score. |
| 8 | `BAD_DEBT_BALANCE` | NUMERIC |  | The total balance sent to bad debt for this guarantor in the payment history score's history window. |
| 9 | `NUM_UNCOLL_ACCTS` | INTEGER |  | Number of accounts with uncollectable balance for the guarantor in the payment history score history window. |
| 10 | `UNCOLL_BALANCE` | NUMERIC |  | The total uncollectable balance for this guarantor in the payment history score history window. |
| 11 | `AVG_SP_LEVEL_C_NAME` | VARCHAR |  | The guarantor's average self-pay level in the PB payment history score history window. |
| 12 | `MAX_SP_LEVEL_C_NAME` | VARCHAR |  | The highest self-pay level at account close (or bad debt outsource) for the guarantor in the payment history score history window. |
| 13 | `NUM_MISSED_PAYMENTS` | INTEGER |  | The number of missed payments by the guarantor in the payment history score history range. |
| 14 | `NUM_MISSED_PP_PAYMENTS` | INTEGER |  | The number of missed payment plan payments by the guarantor in the payment history score history window. |
| 15 | `HAS_PAID_ONLINE_YN` | VARCHAR |  | Whether the guarantor has paid online to this billing system in the payment history score history window. |
| 16 | `LAST_CALCULATED_LOCAL_DTTM` | DATETIME (Local) |  | The last instant at which this payment history score was updated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |

