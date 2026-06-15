# EPA_QUESTIONS

> This table holds the questions for an electronic prior authorization interaction.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `QUESN_ID` | VARCHAR |  | This item holds the ID of the electronic prior authorization question. |
| 4 | `QUESN_SEQUENCE_NUM` | NUMERIC |  | The item holds the sequence number for the electronic prior authorization question. |
| 5 | `QUESN_LEVEL` | VARCHAR |  | This item holds the question level for the electronic prior authorization question. |
| 6 | `DFLT_NEXT_QUESN` | VARCHAR |  | This item holds the ID of the default next question to show after this question. |
| 7 | `QUESN_TYPE_C_NAME` | VARCHAR |  | This item holds the type of question for electronic prior authorization. |
| 8 | `SEL_QUES_START_LINE` | INTEGER |  | This item holds the line number of the first select question detail line associated with this electronic prior authorization question. The actual select question details are stored in referral file (RFL) related group 9350. |
| 9 | `SEL_QUESN_END_LINE` | INTEGER |  | This item holds the line number of the last select question detail line associated with this electronic prior authorization question. The actual select question details are stored in referral file (RFL) related group 9350. |
| 10 | `DT_QUESN_REQ_TM_YN` | VARCHAR |  | This item indicates if a time is required for an electronic prior authorization date question. |
| 11 | `NUM_CMP_START_LINE` | INTEGER |  | This item holds the line number of the first conditional comparison detail line associated with this electronic prior authorization question. The actual conditional comparison details are stored in RFL related group 9340. |
| 12 | `NUM_CMP_END_LINE` | INTEGER |  | This item holds the line number of the last conditional comparison detail line associated with this electronic prior authorization question. The actual conditional comparison details are stored in RFL related group 9340. |
| 13 | `CODE_REF_START_LINE` | INTEGER |  | This item holds the line number of the first coded reference detail line associated with this electronic prior authorization question. The actual coded reference details are stored in referral file (RFL) related group 9390. |
| 14 | `CODE_REF_END_LINE` | INTEGER |  | This item holds the line number of the last coded reference detail line associated with this electronic prior authorization question. The actual coded reference details are stored in referral file (RFL) related group 9390. |
| 15 | `SEL_QUES_MULT_YN` | VARCHAR |  | This item holds whether multiple answers can be selected for selection questions. |
| 16 | `NONE_CHOICE_IDENT` | VARCHAR |  | This item holds the ID of the electronic prior authorization question choice that represents a "None Of The Above" answer. The ID stored here will correspond to an ID in I RFL 9350. |
| 17 | `SIMPLE_SUGGESTION_STAT_C_NAME` | NUMERIC |  | This item tracks whether a Simple Suggestion was made available and how it was used for a particular Electronic Prior Authorization Question. |
| 18 | `COPY_SUGGESTION_STAT_C_NAME` | NUMERIC |  | This item tracks whether a Copy Forward Suggestion was made available and how it was used for a particular Electronic Prior Authorization Question. |
| 19 | `AI_SUGGESTION_STAT_C_NAME` | NUMERIC |  | This item tracks whether an AI generated Suggestion was made available and how it was used for a particular Electronic Prior Authorization Question. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

