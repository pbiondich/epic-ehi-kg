# RFL_PROC_QUESTIONS

> Procedure Questions answered during the referral workflows.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RFL_PROC_QUESTION_ID_QUEST_NAME` | VARCHAR |  | The name of the question record. |
| 4 | `PROC_QUESN_DT` | NUMERIC |  | This item holds the specific contact for the procedure question (LQL) answered. |
| 5 | `PROC_QUESN_RESPONSE` | VARCHAR |  | This item holds the responses for procedure questions. |
| 6 | `PROC_QUESN_COMMENT` | VARCHAR |  | Additional comment added when a procedure question is answered. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

