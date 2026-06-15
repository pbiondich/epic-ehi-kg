# ST_QUES_VERIFICATION_INFO

> This table extracts information related to the question answers extracted by the LLM process for self-triage chat workflows and the verification status of those answers.

**Primary key:** `ANSWER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ANSWER_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the answer record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ST_CHAT_QUESTION_ID_QUEST_NAME` | VARCHAR |  | The name of the question record. |
| 4 | `UNVERIFIED_ANSWER_UNFORMATTED` | VARCHAR |  | This item stores the answer extracted by the LLM from the patient's response that must be verified. |
| 5 | `ST_ANS_VERIF_STATUS_C_NAME` | VARCHAR |  | This item stores the verification status of the potential answer to the question. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANSWER_ID` | [CL_QANSWER](CL_QANSWER.md) | sole_pk | high |

