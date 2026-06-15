# ENROLL_QUESR

> This table contains information about questionnaires assigned to a patient as part of a research study enrollment.

**Primary key:** `ENROLL_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the enrollment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FORM_ID` | VARCHAR | FK→ | The unique ID of the questionnaire assigned for a patient-study association. |
| 4 | `FORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 5 | `ANSWER_ID` | VARCHAR | FK→ | The unique ID of the questionnaire response for the questionnaire assigned for a patient-study association. |
| 6 | `QUESR_ASGN_MTHD_C_NAME` | VARCHAR |  | The assignment method category ID for the questionnaire assigned for a patient-study association. |
| 7 | `ASGN_USER_ID` | VARCHAR |  | The unique ID associated with the user that assigned the questionnaire for a patient-study association. This column is frequently used to link to the CLARITY_EMP table. |
| 8 | `ASGN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `ASGN_QUESR_STAT_C_NAME` | VARCHAR |  | The status category ID of the questionnaire assigned for a patient-study association. |
| 10 | `ASGN_FOR_ENROLL_STATUS_C_NAME` | VARCHAR | org | The enrollment status category ID that caused a questionnaire to be automatically assigned for a patient-study association. |
| 11 | `ASGN_UTC_DTTM` | DATETIME (UTC) |  | The date and time that a questionnaire was assigned for a patient-study association. |
| 12 | `ASGN_SYSTEM_LOCAL_DTTM` | DATETIME (Local) |  | Instant that a questionnaire was assigned for a patient-study association based on system local time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANSWER_ID` | [CL_QANSWER](CL_QANSWER.md) | sole_pk | high |
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |
| `FORM_ID` | [CL_QFORM1](CL_QFORM1.md) | sole_pk | high |

