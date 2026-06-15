# BEN_ACCUMULATION

> This table is used to track accumulations to benefit buckets. To calculate the current benefit bucket amount, join this table to BEN_ACCUMULATION_SYS_ADJ using all three primary key columns and subtracting BEN_ACCUMULATION_SYS_ADJ.SYS_ADJ_BEN_AMOUNT from BEN_ACCUMULATION.BEN_AMOUNT.

**Primary key:** `COVERAGE_ID`, `PAT_BUCKET_COMBO`, `BEN_ACCUM_UNIQ_KEY`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | This column stores the ID of the coverage record. |
| 2 | `PAT_BUCKET_COMBO` | VARCHAR | PK | This item is only used as part of the primary key and is not useful for reporting purposes. Its purpose is to make PAT_ID part of the primary key, but still allow PAT_ID to be null. PAT_ID is null for account level buckets. The format of this column is "PAT_ID;CMB_ID" |
| 3 | `ROLL_PRD_START` | NUMERIC |  | This column contains a numeric representation of the roll period start date for the bucket. A bucket's roll period start value is dependent on the roll period type. For buckets with a roll type of Calendar Year, this column contains the 4-digit year of the roll period. For buckets with a roll type of Number of Days, this column contains a numeric representation (a DAT value) of the date of the first service. For buckets with a roll type of No Roll, this column contains 99999. For buckets with a roll type of Contract Year, this column contains the 4-digit year of the contract. For buckets with a roll type of Admission, this column contains a numeric representation (a DTE value) of the admission date. For buckets with a roll type of Calendar Week, this column contains a numeric representation (a DAT value) of the first day of the weekly roll period. For buckets with a roll type of Calendar Month, this column contains a numeric representation (a DAT value) of the first day of the monthly roll period. |
| 4 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the member this row corresponds to, or null if this is an account bucket. |
| 5 | `BUCKET_ID` | NUMERIC | shared | This is the bucket ID this row corresponds to. |
| 6 | `BUCKET_ID_BUCKET_NAME` | VARCHAR |  | The name of the bucket. |
| 7 | `BEN_AMOUNT` | NUMERIC |  | This is the total amount currently in the bucket for this row (i.e. this coverage, patient, bucket, and roll period combination). |
| 8 | `ROLL_PRD_END` | NUMERIC |  | Contains the roll period end date for the bucket. It is only populated for admission roll period buckets. |
| 9 | `BEN_ACCUM_UNIQ_KEY` | VARCHAR | PK | This column stores a unique key that is used to identify the data row. |
| 10 | `BUCKET_ROLL_PERIOD_C_NAME` | VARCHAR |  | The type of roll period the bucket uses. |
| 11 | `CALC_ROLL_PRD_START_DATE` | DATETIME |  | Except for the cases described next, this column stores the roll period start date of the bucket. For no roll buckets (BUCKET_ROLL_PERIOD_C = 3), 12/31/1840 is stored since there is technically no roll period. For contract year buckets (BUCKET_ROLL_PERIOD_C = 4), NULL is stored since the roll period depends on employer group build that can change overtime. |
| 12 | `CALC_ROLL_PRD_END_DATE` | DATETIME |  | Except for the cases described next, this column stores the roll period end date of the bucket. For no roll buckets (BUCKET_ROLL_PERIOD_C = 3), 09/27/2173 is stored since there is technically no roll period. For contract year buckets (BUCKET_ROLL_PERIOD_C = 4), NULL is stored since the roll period depends on employer group build that can change overtime. |
| 13 | `ROLL_PRD_START_YEAR` | INTEGER |  | For all bucket types, stores the start year of the roll period. For no roll buckets, 1840 is stored since there is technically no roll period. This column is most useful for calculating the roll period of contract year buckets. |
| 14 | `PAT_BKT_TX_TOTAL_KEY` | VARCHAR |  | Stores a string that uniquely identifies the coverage, patient, bucket, and roll period this transaction applies to. It is only populated for patient-level buckets and simplifies joins to BEN_ACCUMULATION_HX_PAT. COVERAGE_ID must still be included in the join. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

