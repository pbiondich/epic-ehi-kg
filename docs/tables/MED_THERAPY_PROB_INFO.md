# MED_THERAPY_PROB_INFO

> This table contains basic information about a medication therapy problem.

**Primary key:** `PROBLEM_ID`  
**Columns:** 14  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the medication therapy problem record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 3 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for the patient encounter where this medication therapy problem was created. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 4 | `CREATION_USER_ID` | VARCHAR |  | The unique ID associated with the user who created this medication therapy problem. This column is frequently used to link to the CLARITY_EMP table. |
| 5 | `CREATION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 7 | `EPISODE_ID` | NUMERIC | FK→ | The unique ID associated with the episode that this medication therapy problem is linked to. |
| 8 | `MTP_CONTEXT_C_NAME` | VARCHAR | org | The context category ID for the medication therapy problem. |
| 9 | `RESPONSIBLE_USER_ID` | VARCHAR |  | The unique ID associated with the user responsible for the resolution of this medication therapy problem. |
| 10 | `RESPONSIBLE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `COMMENTS_NOTE_ID` | VARCHAR |  | The unique ID of the note that contains additional information documented for this medication therapy problem. |
| 12 | `SOURCE_TASK_ID` | VARCHAR |  | The unique ID of the task record that this medication therapy problem was created from. |
| 13 | `CURRENT_MTP_STATUS_C_NAME` | VARCHAR |  | The current status of the medication therapy problem. |
| 14 | `CURRENT_MTP_RATIONALE_C_NAME` | VARCHAR | org | The rationale behind why this is a medication therapy problem. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |

