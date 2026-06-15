# HSP_BKT_SPLIT_EOB_INFO

> This table contains information about payment split EOBs.

**Primary key:** `BUCKET_ID`, `LINE`  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BUCKET_ID` | NUMERIC | PK shared | The hospital billing bucket ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EOB_PMT_TX_ID` | NUMERIC |  | The payment split EOB payment ID. |
| 4 | `POST_DATE` | DATETIME |  | The payment split EOB post date. |
| 5 | `DEPOSIT_DATE` | DATETIME |  | The payment split EOB deposit date. |
| 6 | `ORIG_BUCKET_ID` | NUMERIC |  | The payment split EOB original hospital billing bucket ID. |
| 7 | `PMT_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 8 | `BUCKET_PAYER_ID` | NUMERIC |  | The payment split EOB hospital billing bucket payer ID. |
| 9 | `COVERAGE_ID` | NUMERIC | FK→ | The payment split EOB coverage ID. |
| 10 | `INVOICE_NUMBER` | VARCHAR |  | The payment split EOB invoice number. |
| 11 | `IMAGE_ID` | VARCHAR | shared | The payment split EOB image database ID. |
| 12 | `ICN` | VARCHAR |  | The payment split EOB internal control number (ICN). |
| 13 | `PMT_AMT` | NUMERIC |  | The payment split EOB payment amount. |
| 14 | `ALLOWED_AMT` | NUMERIC |  | The payment split EOB allowed amount. |
| 15 | `NOT_ALLOWED_AMT` | NUMERIC |  | The payment split EOB not allowed amount. |
| 16 | `DEDUCTIBLE_AMT` | NUMERIC |  | The payment split EOB deductible amount. |
| 17 | `COINS_AMT` | NUMERIC |  | The payment split EOB coinsurance amount. |
| 18 | `COPAY_AMT` | NUMERIC |  | The payment split EOB copay amount. |
| 19 | `COB_AMT` | NUMERIC |  | The payment split EOB COB amount. |
| 20 | `ADJ_AMT` | NUMERIC |  | The payment split EOB adjustment amount. |
| 21 | `NON_COVERED_AMT` | NUMERIC |  | The payment split EOB non-covered amount. |
| 22 | `INCLUDE_ADJ_AMT` | NUMERIC |  | The payment split EOB include adjustment amount. |
| 23 | `EXCLUDE_ADJ_AMT` | NUMERIC |  | The payment split EOB exclude adjustment amount. |
| 24 | `IGNORE_ADJ_AMT` | NUMERIC |  | The payment split EOB ignore adjustment amount. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

