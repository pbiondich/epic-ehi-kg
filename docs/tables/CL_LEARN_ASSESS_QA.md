# CL_LEARN_ASSESS_QA

> Enterprise reporting table for learning assessment questions per contact.

**Primary key:** `LEARNING_ASSMT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LEARNING_ASSMT_ID` | NUMERIC | PK FK→ | The unique ID for the patient learning assessment record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | Line count for the patient learning assessment Questions. |
| 4 | `CONTACT_DATE` | DATETIME |  | The contact date in external format. |
| 5 | `TEMPLATE` | VARCHAR |  | The template for the patient learning assessment contact. |
| 6 | `TOPIC` | VARCHAR |  | Patient learning assessment topic. |
| 7 | `LA_QUESTION_ID_QUEST_NAME` | VARCHAR |  | The name of the question record. |
| 8 | `LA_QUESTION_DAT` | VARCHAR |  | Contact date for patient learning assessment question. Stored in internal format. |
| 9 | `LA_ANSWER` | VARCHAR |  | Answer to the patient learning assessment question. Related to the learning assessment question ID. |
| 10 | `LA_COMMENT` | VARCHAR |  | Comment to the learning assessment question. Related to the learning assessment question ID. |
| 11 | `QUESTION_USER_ID` | VARCHAR |  | User ID of the person asking the learning assessment question. Related to the learning assessment question ID. |
| 12 | `QUESTION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `QUESTION_INSTANT` | DATETIME (Local) |  | Date/Time stamp for the instance when the question was asked. Related to the learning assessment question ID. |
| 14 | `ADD_REPORT_YN` | VARCHAR |  | Response to whether this learning assessment question should be added to the report or not. |
| 15 | `TEMPLATE_ID_ILA_RECORD_NAME` | VARCHAR |  | The name for this Learning Assessment Template/Topic record. |
| 16 | `TOPIC_ID_ILA_RECORD_NAME` | VARCHAR |  | The name for this Learning Assessment Template/Topic record. |
| 17 | `END_CONT_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of the last encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `LEARNING_ASSMT_ID` | [CL_LEARN_ASSESS_NS](CL_LEARN_ASSESS_NS.md) | sole_pk | high |

