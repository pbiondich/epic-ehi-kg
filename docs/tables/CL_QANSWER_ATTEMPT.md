# CL_QANSWER_ATTEMPT

> This table contains attempts at answering a patient-entered questionnaire.

**Primary key:** `ANSWER_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ANSWER_ID` | VARCHAR | PK FK→ | The unique identifier for the questionnaire answer record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ATTEMPT_START_DTTM` | DATETIME (Local) |  | The instant at which the patient-entered questionnaire attempt started. An attempt begins when the questionnaire is started, resumed, or traversed to from another questionnaire. This includes navigating forwards, backwards, and jumping to a question from the review page. |
| 4 | `ATTEMPT_END_DTTM` | DATETIME (Local) |  | The instant at which the patient-entered questionnaire attempt ended. The end of the attempt is updated when the user takes an action during the attempt. For branched questionnaires, the end instant does not include actions taken on its parent. |
| 5 | `ATTEMPT_STATUS_C_NAME` | VARCHAR |  | The status of the patient-entered questionnaire attempt. This column can be joined to the ZC_ST_WKFL_STATUS table. |
| 6 | `ATTEMPT_ANSWER_METHOD_C_NAME` | VARCHAR |  | The method used when attempting to answer the patient-entered questionnaire. |
| 7 | `ATTEMPT_USER_ID` | VARCHAR |  | The user who updated the patient-entered questionnaire answers on behalf of the patient if answering from Hyperspace. |
| 8 | `ATTEMPT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `ATTEMPT_MYPT_ID` | VARCHAR |  | The MyChart user who updated the patient-entered questionnaire answers. |
| 10 | `ATTEMPT_SESSION_NUM` | NUMERIC |  | The session number for a MyChart user for the MyChart user access audit trail. |
| 11 | `ATTEMPT_FURTHEST_QUESTION_ID_QUEST_NAME` | VARCHAR |  | The name of the question record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANSWER_ID` | [CL_QANSWER](CL_QANSWER.md) | sole_pk | high |

