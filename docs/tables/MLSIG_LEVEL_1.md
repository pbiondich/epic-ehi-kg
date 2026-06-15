# MLSIG_LEVEL_1

> This table is for periods/groups of sig lines for multiline sigs.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MLSIG_L1_INTERIOR_LINKAGE_C_NAME` | VARCHAR |  | The linkage type category ID for the order record which describes the relationship between multiple sets of medication instructions for specified periods of time. |
| 4 | `MLSIG_L1_DURATION` | INTEGER |  | Duration in days of one period for a medication with differing dosage instructions for specified periods of time. |
| 5 | `MLSIG_L1_END_DTTM` | DATETIME (Local) |  | End instant of one period for a medication with differing dosage instructions for specified periods of time. |
| 6 | `MLSIG_L1_CNT_RANGE` | VARCHAR |  | This item stores a ranged value for the count of one period of a multiline sig. It goes along with the ranged count type from ORD 30404, indicating the number of days, weeks, months, or years for which the order will take place. Currently only available in Finland. |
| 7 | `MLSIG_L1_CNT_RANGE_STND_TP_C_NAME` | VARCHAR |  | This ranged count type goes along with the count from ORD-30403 to indicate the number of days, weeks, months, or years for which the order will take place. Currently only available in Finland. |
| 8 | `MLSIG_L1_SUM_FREQ_ID` | VARCHAR |  | This item stores the summary frequency for the period. |
| 9 | `MLSIG_L1_SUM_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 10 | `MLSIG_L1_PERIOD_FLAG_C_NAME` | VARCHAR |  | This item stores the status flag for the period. Currently there are two options: 1) Times of day, and 2) Exact times. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

