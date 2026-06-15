# EPA_NUM_COMPS

> This table holds the conditional comparison information for electronic prior authorization questions.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SING_COMP_OP_C_NAME` | VARCHAR |  | This item holds the comparison operator to use when doing a single comparison for an electronic prior authorization question. |
| 4 | `SING_COMP_VAL` | NUMERIC |  | This item holds the comparison value to use when doing a single comparison for an electronic prior authorization question. |
| 5 | `RNG_COMP_LOW_OP_C_NAME` | VARCHAR |  | This item holds the lower comparison operator to use when doing a range comparison for an electronic prior authorization question. |
| 6 | `RNG_COMP_LOW_VAL` | NUMERIC |  | This item holds the lower comparison value to use when doing a range comparison for an electronic prior authorization question. |
| 7 | `RNG_COMP_UP_OP_C_NAME` | VARCHAR |  | This item holds the upper comparison operator to use when doing a range comparison for an electronic prior authorization question. |
| 8 | `RNG_COMP_UP_VAL` | NUMERIC |  | This item holds the upper comparison value to use when doing a range comparison for an electronic prior authorization question. |
| 9 | `NUM_COMP_NEXT_QUESN` | VARCHAR |  | This item holds the ID of the next question to show after a question meets the conditional logic comparison requirements. |
| 10 | `SING_COMP_DATE` | DATETIME |  | This item holds the comparison operator to use when doing a single date comparison for an electronic prior authorization question. |
| 11 | `SING_COMP_UTC_DTTM` | DATETIME (UTC) |  | This item holds the comparison value to use when doing a single instant comparison for an electronic prior authorization question. |
| 12 | `RNG_COMP_LOW_DATE` | DATETIME |  | This item holds the lower comparison operator to use when doing a date range comparison for an electronic prior authorization question. |
| 13 | `RNG_COMP_LOW_UTC_DTTM` | DATETIME (UTC) |  | This item holds the lower comparison operator to use when doing an instant range comparison for an electronic prior authorization question. |
| 14 | `RNG_COMP_UP_DATE` | DATETIME |  | This item holds the upper comparison operator to use when doing a date range comparison for an electronic prior authorization question. |
| 15 | `RNG_COMP_UP_UTC_DTTM` | DATETIME (UTC) |  | This item holds the upper comparison operator to use when doing an instant range comparison for an electronic prior authorization question. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

