# RAD_THERAPY_EPISODE_INFO

> This table stores information related to a radiation-therapy episode, such as the goal and treatment technique. This is a no-add table.

**Primary key:** `SUMMARY_BLOCK_ID`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID of the episode of care record. |
| 2 | `RAD_THERAPY_TREAT_TECHNIQUE_C_NAME` | VARCHAR |  | The treatment technique for radiation therapy. |
| 3 | `RAD_THERAPY_TREATMENT_GOAL_C_NAME` | VARCHAR | org | The radiation therapy treatment goal. |
| 4 | `RAD_THERAPY_PLANNED_START_DATE` | DATETIME |  | The planned start date for radiation therapy. |
| 5 | `RAD_THERAPY_EPISODE_NOTE_ID` | VARCHAR |  | The episode note ID |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

