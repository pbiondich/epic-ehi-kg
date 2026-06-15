# SCRFORM_ANS_INFO

> This table contains information about questionnaire answers for the associated screening form.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the timeout record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SCRFORM_ANSWER_ID` | VARCHAR |  | The unique ID of the questionnaire answers recorded in the screening form. |
| 4 | `SCRFORM_QUESR_ID` | VARCHAR |  | The unique ID of the questionnaire record in the screening form. |
| 5 | `SCRFORM_QUESR_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 6 | `SCRFORM_REVD_INST_UTC_DTTM` | DATETIME (UTC) |  | The last instant the questionnaire answers were reviewed in the screening form. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

