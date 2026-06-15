# SRS_ASGN_INFO

> Table that stores series assignment related information as well as information on series answer record status.

**Primary key:** `SERIES_ANS_ID`  
**Columns:** 19  
**Joined by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SERIES_ANS_ID` | NUMERIC | PK | This column stores the unique identifier for the series answer record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | This column stores the status of the series answer record if it is not active. |
| 3 | `SERIES_ID` | NUMERIC | FK→ | This column stores the ID of the series answer record. |
| 4 | `SERIES_ID_SERIES_NAME` | VARCHAR |  | The name for the questionnaire series record. |
| 5 | `SERIES_CSN` | NUMERIC |  | This column stores the contact date (DAT) for the series answer record. |
| 6 | `SERIES_TYPE_C_NAME` | VARCHAR |  | Stores the questionnaire series type. |
| 7 | `SERIES_STATUS_C_NAME` | VARCHAR |  | This column stores the status of the series answer record if it is active. |
| 8 | `ORDERED_BY_USER_ID` | VARCHAR |  | If a series is ordered through Order Entry or through an OurPractice Advisory, this column stores who ordered it for future message routing purposes. |
| 9 | `ORDERED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `SERIES_PAT_ID` | VARCHAR | FK→ | To store ID (EPT id) of the patient who is answering this questionnaire series. |
| 11 | `HQW_CREATION_DT` | DATETIME |  | This column stores the date the series answer record was created. |
| 12 | `INIT_ENC_CSN_ID` | NUMERIC | FK→ | This item stores the contact serial number (CSN) of the encounter where this series is assigned to the user. This item will be empty if the series was assigned from Reporting Workbench. |
| 13 | `PARENT_SRS_ANS_ID` | NUMERIC |  | This column stores the ID of the parent questionnaire series answer record. |
| 14 | `PREV_SRS_ANS_ID` | NUMERIC |  | This column stores the ID of the previous anchor event questionnaire series answer record. |
| 15 | `LINKED_ENC_CSN_ID` | NUMERIC | FK→ | This item stores the encounter this questionnaire series is linked to. If the series is linked to an encounter, then the contact date (DAT) of the encounter will be used for evaluating anchor event rules and extensions. |
| 16 | `LINKED_PROC_PASS_ID` | NUMERIC |  | This item stores the ID of the Procedure Pass linked to this series. This will only be populated if the series is assigned using the Procedure Pass workflow. |
| 17 | `ASSIGNING_ORD_ID` | NUMERIC |  | This item stores the order that assigned this questionnaire series. |
| 18 | `ENROLL_ID` | NUMERIC | FK→ | This item stores the ID of the linked patient-study association if it is linked to an association. |
| 19 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |
| `INIT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `LINKED_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `SERIES_ID` | [SRS_INFO](SRS_INFO.md) | sole_pk | high |
| `SERIES_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

## Joined in — referenced by (9)

| From | Column | Confidence |
|------|--------|------------|
| [ENROLL_QUESR_SERIES](ENROLL_QUESR_SERIES.md) | `SERIES_ANS_ID` | high |
| [HQW_STATUS_HX](HQW_STATUS_HX.md) | `SERIES_ANS_ID` | high |
| [QNR_NEXT_UPD_INFO](QNR_NEXT_UPD_INFO.md) | `SERIES_ANS_ID` | high |
| [SERIES_ANSWERS](SERIES_ANSWERS.md) | `SERIES_ANS_ID` | high |
| [SERIES_ANSWER_ID](SERIES_ANSWER_ID.md) | `SERIES_ANS_ID` | high |
| [SERIES_LOG_INFO](SERIES_LOG_INFO.md) | `SERIES_ANS_ID` | high |
| [SRS_ANCHOR_INFO](SRS_ANCHOR_INFO.md) | `SERIES_ANS_ID` | high |
| [SRS_RESP_OVER_TM](SRS_RESP_OVER_TM.md) | `SERIES_ANS_ID` | high |
| [TASK_PATIENT_ACTIVITY](TASK_PATIENT_ACTIVITY.md) | `SERIES_ANS_ID` | high |

