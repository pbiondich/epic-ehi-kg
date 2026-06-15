# CL_QANSWER_QA

> This table contains the questions and answers for questionnaire answer records. It also includes audit information such as when the question was answered and by whom.

**Primary key:** `ANSWER_ID`, `LINE`  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ANSWER_ID` | VARCHAR | PK FK→ | The unique ID of the questionnaire answer record. |
| 2 | `LINE` | INTEGER | PK | Line count of the answers in the questionnaire record. |
| 3 | `QUEST_LINE_NUM` | INTEGER |  | The line number for the question for this record. |
| 4 | `QUEST_EDIT_USER_ID` | VARCHAR |  | The unique ID of the user associated with this record. |
| 5 | `QUEST_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `QUESTION_INSTANT` | DATETIME (Local) |  | Stores the instant a question was answered. |
| 7 | `VARCHAR_ANSWER` | VARCHAR |  | For questions of networked or category response types where the linked INI and item is string (aka varchar) based, this column will hold either a record ID or category ID. These are useful for linking directly to other tables such as CLARITY_SER for provider-linked questions, or ZC tables for category response types. If you are unsure what types of records these IDs hold, consult CL_QQUEST_OVTM for the question ID in the QUEST_ID column and use the RESP_INI and RESP_ITEM columns. |
| 8 | `NUMERIC_ANSWER` | INTEGER |  | For questions of networked or category response types where the linked INI and item is numeric (integer) based, this column holds either a record ID or category ID. |
| 9 | `FLOAT_ANSWER` | FLOAT |  | The answer to the question for this record converted into a floating point value. |
| 10 | `IS_NULL` | INTEGER |  | Specifies if there was no response to a question (set to 1 - Yes). |
| 11 | `QUESTION_SDI` | VARCHAR |  | The SmartData identifier of the SmartData element that this patient-entered custom history question uses. |
| 12 | `QUESN_SDI_FILED_YN` | VARCHAR |  | Whether the response to this custom history question has been filed to the patient's history. |
| 13 | `DATETIME_ANSWER` | DATETIME (Local) |  | Stores questionnaire answer data in a datetime format that includes hours and seconds. |
| 14 | `TIME_ANSWER` | VARCHAR |  | The answer to the question for this record, formatted as a time value. This is the preferred column for reporting on answers to questions with the response type (LQL 110) of 3-Time. Source: HQA 120 |
| 15 | `SCORE_STD_ERR` | NUMERIC |  | The standard error on the score calculated by the computerized adaptive testing (CAT) algorithm |
| 16 | `DOC_INFO_ID` | VARCHAR | FK→ | The unique identifier of a document uploaded for a question. |
| 17 | `FOL_UP_PAR_QUEST_ID_QUEST_NAME` | VARCHAR |  | The name of the question record. |
| 18 | `PAT_LOC_DOC_ID` | VARCHAR |  | Stores the ID of the drawing record (DCS) submitted by the patient in the locale in which he answered the question if the locale is different from the base locale. |
| 19 | `ANSWER_SEVERITY_C_NAME` | VARCHAR |  | The severity level of an answer. Calculated using the thresholds defined for the question that was answered. |
| 20 | `QUEST_INITIAL_ANSWER` | VARCHAR |  | Contains the pre-populated answer for the question if one is available. |
| 21 | `DYNAMIC_QUESTION_PROMPT` | VARCHAR |  | Prompt shown to the patient for a generated question |
| 22 | `QUESTION_ATTACH_ROI_ID` | VARCHAR |  | The release of information (ROI) uploaded for a question. |
| 23 | `QUESTION_COVER_LET_NOTE_ID` | VARCHAR |  | The cover letter (HNO) uploaded for an attachment. |
| 24 | `QUESTION_ATTACH_OVRIDE_ROI_ID` | VARCHAR |  | The override release of information (ROI) uploaded for a question. Consists of the base ROI in I HQA 127 combined with the cover letter in I HQA 128. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANSWER_ID` | [CL_QANSWER](CL_QANSWER.md) | sole_pk | high |
| `DOC_INFO_ID` | [DOC_INFORMATION](DOC_INFORMATION.md) | sole_pk | high |

