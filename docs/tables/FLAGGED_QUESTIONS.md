# FLAGGED_QUESTIONS

> Questions in this answer record that have been flagged, along with reason and linked records, if applicable.

**Primary key:** `ANSWER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ANSWER_ID` | VARCHAR | PK FK→ | The unique identifier for the answer record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FLAGGED_QUESTION_ID_QUEST_NAME` | VARCHAR |  | The name of the question record. |
| 4 | `FLAG_REASON_C_NAME` | VARCHAR |  | Stores the reason the question was flagged. |
| 5 | `FLAG_ALT_CSN_ID` | NUMERIC |  | Stores the unique contact serial number for the alert that caused the question to be flagged. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANSWER_ID` | [CL_QANSWER](CL_QANSWER.md) | sole_pk | high |

