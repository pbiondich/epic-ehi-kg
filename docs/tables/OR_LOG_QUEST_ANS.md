# OR_LOG_QUEST_ANS

> The OR_LOG_QUEST_ANS table contains questionnaire answers for OR management system surgeries.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the log record. |
| 2 | `LINE` | INTEGER | PK | The line number of the log answer associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ANSWER_ID` | VARCHAR | FK→ | The unique ID of the answer record. |
| 4 | `IS_USER_ADDED_YN` | VARCHAR |  | Indicates whether the questionnaire was added by the user. Y indicates that the questionnaire was added by the user. A null value indicates that the questionnaire was automatically associated with the surgical log. An N will not be populated for this column. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANSWER_ID` | [CL_QANSWER](CL_QANSWER.md) | sole_pk | high |

