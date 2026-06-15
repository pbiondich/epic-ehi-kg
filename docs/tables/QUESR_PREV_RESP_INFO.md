# QUESR_PREV_RESP_INFO

> Table that extracts the information about the questionnaires that were not shown to the patient while branching as the patients previous responses are still valid.

**Primary key:** `ANSWER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ANSWER_ID` | VARCHAR | PK FK→ | This column stores the unique identifier for the answer record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `QUESR_RESP_FORM_ID` | VARCHAR |  | This column stores the form IDs of questionnaires that were not displayed to the patient while branching as their previous responses were valid. Use the QUESR_RESP_CSN_ID column to determine the encounter contact serial number for each throttled questionnaire. |
| 4 | `QUESR_RESP_FORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 5 | `QUESR_RESP_CSN_ID` | NUMERIC |  | This column stores the encounter contact serial number of questionnaires that were not displayed to the patient while branching as their previous responses were valid. use the QUESR_RESP_FORM_ID column to determine the form ID for each throttled questionnaire. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANSWER_ID` | [CL_QANSWER](CL_QANSWER.md) | sole_pk | high |

