# EPA_SELECT_CHOICES

> This table holds the select choices for electronic prior authorization questions.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SEL_CHOICE_ID` | VARCHAR |  | This item holds the ID of the multiple choice option for electronic prior authorization. |
| 4 | `SEL_CHOICE_SEQUENCE` | NUMERIC |  | This item holds the sequence for the multiple choice option. |
| 5 | `ALLOW_FREE_TEXT_C_NAME` | VARCHAR |  | Indicates whether a free text comment was allowed for the multiple choice option. If set to No, free text comments will not be allowed. If set to Yes-Required, a free text comment will be required. If set to Yes-Optional, a free text comment will be allowed, but optional. |
| 6 | `SEL_QUESN_NEXT_ID` | VARCHAR |  | This item holds the ID of the next question if this answer choice is selected. |
| 7 | `SEL_CODE_REF_START` | INTEGER |  | This item holds the line number of the first coded reference detail line associated with this electronic prior authorization multiple choice option. The actual coded reference details are stored in referral file (RFL) related group 9390. |
| 8 | `SEL_CODE_REF_END` | INTEGER |  | This item holds the line number of the last coded reference detail line associated with this electronic prior authorization multiple choice option. The actual coded reference details are stored in referral file (RFL) related group 9390. |
| 9 | `SEL_CHOICE_VALUE_YN` | VARCHAR |  | This item holds whether this selection option was chosen. If it is set to 1-Yes, it indicates that the answer was selected. If it is set to null or 0-No, it indicates that the answer was not selected. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

