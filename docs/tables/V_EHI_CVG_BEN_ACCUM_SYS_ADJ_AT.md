# V_EHI_CVG_BEN_ACCUM_SYS_ADJ_AT

> This table is used to track system adjustments that were applied to account-level benefit accumulation buckets.

**Primary key:** `COVERAGE_ID`, `BUCKET_ID`, `ROLL_PERIOD_KEY`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier of the coverage record. |
| 2 | `BUCKET_ID` | NUMERIC | PK shared | The unique ID of the benefit bucket this row corresponds to. |
| 3 | `BUCKET_ID_BUCKET_NAME` | VARCHAR |  | The name of the bucket. |
| 4 | `ROLL_PERIOD_KEY` | VARCHAR | PK | This column is only used as part of the primary key and is not useful for reporting purposes. |
| 5 | `ROLL_PRD_START` | NUMERIC |  | This column contains a numeric representation of the roll period start date for the bucket. A bucket's roll period start value is dependent on the roll period type. For buckets with a roll type of Calendar Year, this column contains the 4-digit year of the roll period. For buckets with a roll type of Number of Days, this column contains a numeric representation (a DAT value) of the date of the first service. For buckets with a roll type of No Roll, this column contains 99999. For buckets with a roll type of Contract Year, this column contains the 4-digit year of the contract. For buckets with a roll type of Admission, this column contains a numeric representation (a DTE value) of the admission date. For buckets with a roll type of Calendar Week, this column contains a numeric representation (a DAT value) of the first day of the weekly roll period. For buckets with a roll type of Calendar Month, this column contains a numeric representation (a DAT value) of the first day of the monthly roll period. |
| 6 | `ROLL_PRD_END` | NUMERIC |  | Contains the roll period end date for the bucket. Only populated for admission roll period buckets. |
| 7 | `BUCKET_ROLL_PERIOD_C_NAME` | VARCHAR |  | The type of roll period the bucket uses. |
| 8 | `CALC_ROLL_PRD_START_DATE` | DATETIME |  | Except for the cases described next, this column stores the roll period start date of the bucket. For no roll buckets (BUCKET_ROLL_PERIOD_C = 3), 12/31/1840 is stored since there is technically no roll period. For contract year buckets (BUCKET_ROLL_PERIOD_C = 4), NULL is stored since the roll period depends on employer group build that can change overtime. |
| 9 | `CALC_ROLL_PRD_END_DATE` | DATETIME |  | Except for the cases described next, this column stores the roll period end date of the bucket. For no roll buckets (BUCKET_ROLL_PERIOD_C = 3), 09/27/2173 is stored since there is technically no roll period. For contract year buckets (BUCKET_ROLL_PERIOD_C = 4), NULL is stored since the roll period depends on employer group build that can change overtime. |
| 10 | `ROLL_PRD_START_YEAR` | INTEGER |  | For all bucket types, stores the start year of the roll period. For no roll buckets, 1840 is stored since there is technically no roll period. This column is most useful for calculating the roll period of contract year buckets. |
| 11 | `SYS_ADJ_BEN_AMOUNT` | NUMERIC |  | This is the system adjusted total amount of the bucket. Negative adjustments are stored as positive values. For example, if the bucket amount is -100, this column will store 100. |
| 12 | `TX_TOTAL_KEY` | VARCHAR |  | Uniquely identifies the coverage, bucket, and roll period this transaction applies to. This value simplifies joins to BEN_ACCUMULATION_HX_ACCT, although the COVERAGE_ID column must still be included in the join. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

