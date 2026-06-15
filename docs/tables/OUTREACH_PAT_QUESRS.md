# OUTREACH_PAT_QUESRS

> This table stores patient questionnaire tasks linked to an outreach tasks, and the answers to the questionnaires.

**Primary key:** `ACTIVITY_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACTIVITY_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the task record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_QUESTIONNAIRE_FORM_ID` | VARCHAR |  | For outreach tasks, this item stores any patient questionnaires linked to this outreach. |
| 4 | `PAT_QUESTIONNAIRE_FORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 5 | `PAT_QUESTIONNAIRE_ANSWER_ID` | VARCHAR |  | The patient's answers to the questionnaire sent in the linked task. This may be an in progress response if the linked task is not completed. |
| 6 | `PAT_QUESTIONNAIRE_ORDER_ID` | NUMERIC |  | The order record related to the questionnaire, if any. |
| 7 | `PAT_QUESTIONNAIRE_START_DATE` | DATETIME |  | The date the questionnaire is to be available to be answered by the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

