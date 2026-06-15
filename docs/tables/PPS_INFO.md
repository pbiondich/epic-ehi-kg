# PPS_INFO

> New table for the Hospital Accounts Receivable (HAR) to specify what assessed HIPPS code and reimbursement amount is versus the charge-based HIPPS code and reimbursement amount.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the hospital account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PPS_TYPE_C_NAME` | VARCHAR |  | This category holds the data that indicates what type of data is on the row. A row can represent the pricing from the assessment or the pricing from the charges (what really happened). |
| 4 | `HIPPS_CODE` | VARCHAR |  | Stores the calculated HIPPS code. Item HAR 680 stores if it is assessment based or charge based. |
| 5 | `EXP_PAYMENT` | NUMERIC |  | Expected payment for the associated HIPPS code. Multiple responses are permitted (one per line). |
| 6 | `NRS_AMOUNT` | NUMERIC |  | Non routine supply amount for the associated HIPPS code. Multiple responses are permitted (one per line). |
| 7 | `EPISODE_RATE` | NUMERIC |  | The episode rate for the associated HIPPS code. |
| 8 | `PAYMENT_CASE_C_NAME` | VARCHAR |  | Payment case for the associated HIPPS code. |
| 9 | `ADD_ON_LUPA` | NUMERIC |  | This item stores the Low Utilization Payment Adjustment (LUPA) add on amount. |
| 10 | `ADD_ON_RURAL` | NUMERIC |  | This item stores the rural add on amount. |
| 11 | `ADD_ON_OUTLIER` | NUMERIC |  | This item stores the outlier add on amount. |
| 12 | `LOCALE_ID` | NUMERIC | FK→ | The unique identifier for the locale record for this row. |
| 13 | `LOCALE_ID_LOCALE_NAME` | VARCHAR |  | The name of the locale record. |
| 14 | `EPISODE_TIMING_C_NAME` | VARCHAR |  | The episode timing for this Home Health PDGM account. |
| 15 | `ADMIT_SOURCE_C_NAME` | VARCHAR |  | The admission source for this Home Health PDGM account. |
| 16 | `CLINICAL_GROUP_C_NAME` | VARCHAR |  | The clinical group for this Home Health PDGM account. |
| 17 | `FUNCTIONAL_LEVEL_C_NAME` | VARCHAR |  | The functional impairment level for this Home Health PDGM account. |
| 18 | `COMORBIDITY_ADJUSTMENT_C_NAME` | VARCHAR |  | The comorbidity adjustment for this Home Health PDGM account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `LOCALE_ID` | [LOCALE](LOCALE.md) | sole_pk | high |

