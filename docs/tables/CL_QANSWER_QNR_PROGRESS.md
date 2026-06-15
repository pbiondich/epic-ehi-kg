# CL_QANSWER_QNR_PROGRESS

> The CL_QANSWER_QNR_PROGRESS table contains information about the steps a user took while navigating a questionnaire as they provided answers. This information includes the questionnaires they've seen and the pages they've visited.

**Primary key:** `ANSWER_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ANSWER_ID` | VARCHAR | PK FK→ | This column stores the unique identifier for the answer record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FORM_CSN_ID` | NUMERIC |  | Stores what questionnaire form was shown to the patient at this point in their audit history. |
| 4 | `FORM_PAGE` | INTEGER |  | Stores what page of the corresponding questionnaire was shown to the patient at this point in their audit history. |
| 5 | `IN_PROGRESS_FORM_ID` | VARCHAR |  | Stores the record ID for the questionnaire that was shown to the patient at this point in their audit history. |
| 6 | `IN_PROGRESS_FORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 7 | `IN_PROGRESS_CONTACT_DATE_REAL` | NUMERIC |  | Stores the contact date (DAT) for the questionnaire that was shown to the patient at this point in their audit history. |
| 8 | `FORM_ANSWER_ID` | VARCHAR |  | Stores the answer corresponding to the questionnaire that was shown to the patient at this point in their audit history. |
| 9 | `COMPLD_FORM_LOCALE` | VARCHAR |  | Stores the locale subscript of the compiled questionnaire record that was shown to the patient at this point in their audit history. This only applies if a language override was triggered. |
| 10 | `FORM_SUBPAGE` | INTEGER |  | Stores the last subpage shown to the patient for a given page in their audit history. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANSWER_ID` | [CL_QANSWER](CL_QANSWER.md) | sole_pk | high |

