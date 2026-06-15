# ENROLL_QUESR_SERIES

> This table contains information about questionnaire series assigned to a patient as part of a research study enrollment.

**Primary key:** `ENROLL_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the enrollment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SERIES_ID` | NUMERIC | FK→ | The unique ID of the questionnaire series assigned for a patient-study association. |
| 4 | `SERIES_ID_SERIES_NAME` | VARCHAR |  | The name for the questionnaire series record. |
| 5 | `SERIES_ANS_ID` | NUMERIC | FK→ | The unique ID of the questionnaire series response for questionnaire series assigned for a patient-study association. |
| 6 | `ASGN_UTC_DTTM` | DATETIME (UTC) |  | The date and time that a questionnaire series was assigned for a patient-study association. |
| 7 | `QUESR_ASGN_MTHD_C_NAME` | VARCHAR |  | The assignment method category ID for the questionnaire series assigned for a patient-study association. |
| 8 | `ASGN_USER_ID` | VARCHAR |  | The unique ID associated with the user that assigned the questionnaire series for a patient-study association. This column is frequently used to link to the CLARITY_EMP table. |
| 9 | `ASGN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `ENROLL_SERIES_STAT_C_NAME` | VARCHAR |  | The status category ID of the questionnaire series assigned for a patient-study association. |
| 11 | `ASGN_FOR_ENROLL_STATUS_C_NAME` | VARCHAR | org | The enrollment status category ID that caused a questionnaire series to be automatically assigned for a patient-study association. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |
| `SERIES_ANS_ID` | [SRS_ASGN_INFO](SRS_ASGN_INFO.md) | sole_pk | high |
| `SERIES_ID` | [SRS_INFO](SRS_INFO.md) | sole_pk | high |

