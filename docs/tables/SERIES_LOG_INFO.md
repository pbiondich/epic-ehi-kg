# SERIES_LOG_INFO

> Table to store the audit log information for questionnaire series answer records. The audit log contains data such as the last update instant, date, action, questionnaire ID, User (EMP) ID, Patient Access Account (WPR) ID and reason why tickler notification was not queued.

**Primary key:** `SERIES_ANS_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SERIES_ANS_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the series answer record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SRS_ACTION_INS_DTTM` | DATETIME (UTC) |  | This column is used to store the instant when there is a update on this record. |
| 4 | `SRS_ACTION_DATE` | DATETIME |  | This column is used to store the action date for this questionnaire series. |
| 5 | `SRS_ACTION_C_NAME` | VARCHAR | org | This column is used to store the actions taken for this questionnaire series. |
| 6 | `SRS_ACT_QUESR_ID` | VARCHAR |  | This column is used to store the questionnaire ID for the audit action |
| 7 | `SRS_ACT_QUESR_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 8 | `SRS_ACT_USER_ID` | VARCHAR |  | This column is used to store who made this action. |
| 9 | `SRS_ACT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `SRS_ACT_WPR_ID` | VARCHAR |  | This column stores the web portal ID of the user who answered the questionnaire. |
| 11 | `SRS_NOTIF_FAIL_REASON_C_NAME` | VARCHAR |  | Reason why tickler notification could not be queued. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SERIES_ANS_ID` | [SRS_ASGN_INFO](SRS_ASGN_INFO.md) | sole_pk | high |

