# CL_QANSWER_AUDIT

> This column stores audit items which detail how patient-entered questionnaire responses were submitted.

**Primary key:** `ANSWER_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ANSWER_ID` | VARCHAR | PK FK→ | The unique identifier for the answer record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ANSWER_METHOD_C_NAME` | VARCHAR |  | This column stores the method/application by which patient-entered questionnaire responses were saved or updated (e.g. MyChart and/or Welcome). |
| 4 | `ANSWER_DTTM_DTTM` | DATETIME (Local) |  | This column stores the instant at which patient-entered questionnaire responses were saved or updated. |
| 5 | `ANSWER_USER_ID` | VARCHAR |  | When applicable, this column stores EpicCare users who saved or updated patient-entered questionnaire responses on behalf of patients. |
| 6 | `ANSWER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `ANSWER_MYPT_ID` | VARCHAR |  | Stores the MyChart user ID who last updated the questionnaire answers. |
| 8 | `ANSWER_PAT_REL_C_NAME` | VARCHAR | org | Stores the relationship to the patient of the user who last updated the questionnaire answers on behalf of the patient. |
| 9 | `ANSWER_BY_KIOSK_PAT_YN` | VARCHAR |  | Indicates whether a questionnaire that was answered in Welcome was answered by the patient or a patient representative. 'Y' indicates that the questionnaire was answered by the patient. 'N' indicates that the questionnaire was answered by a patient representative. NULL indicates that the questionnaire was not answered in Welcome. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANSWER_ID` | [CL_QANSWER](CL_QANSWER.md) | sole_pk | high |

