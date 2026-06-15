# PAT_CUR_TRT_EPSD

> The current treatment plan episodes for a patient.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The patient ID. |
| 2 | `LINE` | INTEGER | PK | The line number that corresponds to each treatment plan episode (HSB) for the patient in this row. |
| 3 | `CUR_TRT_PLAN_TYP_ID_EPISODE_DEF_NAME` | VARCHAR |  | This column displays the name of the episode / block definition record. |
| 4 | `CUR_TRT_EPISODE_ID` | NUMERIC |  | The episode (HSB) record ID of a treatment plan episode for the patient in this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

