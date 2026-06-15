# CASE_CONT_QUEST

> The CASE_CONT_QUEST table allows you to report on questionnaires for each contact in the Chronic Disease Case Management module.

**Primary key:** `CASE_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | NUMERIC | PK shared | The unique ID for the case record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | The contact date in decimal format. |
| 3 | `LINE` | INTEGER | PK | The line count of questionnaire information for the case record. |
| 4 | `CONTACT_DATE` | DATETIME |  | The contact date in datetime format. |
| 5 | `QUEST_FORM_ID` | VARCHAR |  | The unique ID of the questionnaire form. |
| 6 | `QUEST_FORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 7 | `QUEST_ANSWER_ID` | VARCHAR |  | The unique ID of the questionnaire answer. |
| 8 | `QUEST_TIME` | DATETIME (Local) |  | The date and time of the questionnaire. |
| 9 | `QUEST_USER_ID` | VARCHAR |  | The unique ID of the user associated with the questionnaire. |
| 10 | `QUEST_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `QUEST_COMMENT` | VARCHAR |  | The comment of the questionnaire. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

