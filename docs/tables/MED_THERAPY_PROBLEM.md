# MED_THERAPY_PROBLEM

> Table for medication therapy recommendation information stored in Tasks Database (LTK) records.

**Primary key:** `ACTIVITY_ID`  
**Columns:** 13  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACTIVITY_ID` | VARCHAR | PK shared | The unique identifier for the task record. |
| 2 | `MTP_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 3 | `MTP_MED_ID` | NUMERIC |  | This column displays the medication order identifier which corresponds to a Medication Therapy Problem. |
| 4 | `MTP_RATIONALE_C_NAME` | VARCHAR | org | This column displays the rationale associated with a Medication Therapy Problem. |
| 5 | `MTP_PROBLEM_C_NAME` | VARCHAR | org | This column displays the problem category of a Medication Therapy Problem. |
| 6 | `MTP_TOPIC_C_NAME` | VARCHAR | org | This column displays the topic of a Medication Therapy Problem. |
| 7 | `MTP_RECOMMEND_C_NAME` | VARCHAR | org | This column displays the recommended action which corresponds to a Medication Therapy Problem. |
| 8 | `MTP_RECOMMEND_MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 9 | `MTP_RECOMMEND_ORDER` | VARCHAR |  | This column displays the recommended order associated with a Medication Therapy Problem. |
| 10 | `MTP_ACTION_TAKEN_C_NAME` | VARCHAR | org | This column displays the action taken for a Medication Therapy Problem. |
| 11 | `MTP_OUTCOME_C_NAME` | VARCHAR | org | This column displays the outcome of a Medication Therapy Problem. |
| 12 | `MTP_START_DATE` | DATETIME |  | This column displays the start date of a Medication Therapy Problem. |
| 13 | `MTP_END_DATE` | DATETIME |  | This column displays the end date of a Medication Therapy Problem. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

