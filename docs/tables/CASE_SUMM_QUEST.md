# CASE_SUMM_QUEST

> The CASE_SUMM_QUEST table allows you to report on questionnaires (not contact-specific) in Tapestry's Chronic Disease Case Management module.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | NUMERIC | PK shared | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The line count of the summary questionnaire information for the case record. |
| 3 | `QUEST_FORM_ID` | VARCHAR |  | The unique ID of the summary questionnaire form. |
| 4 | `QUEST_FORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 5 | `QUEST_ANSWER_ID` | VARCHAR |  | The unique ID of the summary questionnaire answer. |
| 6 | `QUEST_TIME` | DATETIME (Local) |  | The time of the summary questionnaire. |
| 7 | `QUEST_USER_ID` | VARCHAR |  | The unique ID of the user associated with the summary questionnaire. |
| 8 | `QUEST_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `QUEST_COMMENT` | VARCHAR |  | The comment of the summary questionnaire. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

