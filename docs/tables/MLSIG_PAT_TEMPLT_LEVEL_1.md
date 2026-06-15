# MLSIG_PAT_TEMPLT_LEVEL_1

> This table is for periods/groups of sig lines for multiline sigs.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient order template record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MLSIG_L1_INT_LINK_C_NAME` | VARCHAR |  | For a medication with differing dosage instructions for specified periods of time, the type of linkage (AND, OR, or FOLLOWED BY) to be used between dosage sig lines in one group/period. |
| 4 | `MLSIG_L1_DURATION` | INTEGER |  | For a medication with differing dosage instructions for specified periods of time, the duration in days of the dosage groups/periods. |
| 5 | `MLSIG_L1_CNT_RANGE` | VARCHAR |  | This item stores a ranged value for the count of one period of a multiline sig. It goes along with the ranged count type from OTP 30404, indicating the number of days, weeks, months, or years for which the order will take place. Currently only available in Finland. |
| 6 | `MLSIG_L1_CNT_RANGE_STND_TP_C_NAME` | VARCHAR |  | This ranged count type goes along with the count from OTP-30403 to indicate the number of days, weeks, months, or years for which the order will take place. Currently only available in Finland. |
| 7 | `MLSIG_L1_SUM_FREQ_ID` | VARCHAR |  | This item stores the summary frequency for the multiline sig period. |
| 8 | `MLSIG_L1_SUM_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 9 | `MLSIG_L1_PERIOD_FLAG_C_NAME` | VARCHAR |  | This item stores the status flag for the period. Currently there are two options: 1) Times of day, and 2) Exact times. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

