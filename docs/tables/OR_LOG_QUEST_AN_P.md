# OR_LOG_QUEST_AN_P

> The OR_LOG_QUEST_AN_P table contains questionnaire answers for OR management systems surgeries.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the log record. |
| 2 | `LINE` | INTEGER | PK | The line number of the procedure answer associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROC_ID` | VARCHAR | FK→ | The unique ID of the procedure record for which there is an answer. |
| 4 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 5 | `PANEL` | INTEGER |  | The panel number in which the questionnaire is found. |
| 6 | `ANSWER_ID` | VARCHAR | FK→ | The unique ID of the answer record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANSWER_ID` | [CL_QANSWER](CL_QANSWER.md) | sole_pk | high |
| `PROC_ID` | [CLARITY_EAP](CLARITY_EAP.md) | sole_pk | high |

