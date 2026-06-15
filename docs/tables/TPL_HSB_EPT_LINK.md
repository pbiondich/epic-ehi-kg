# TPL_HSB_EPT_LINK

> Information linking a treatment plan to an episode and a patient.

**Primary key:** `TREATMENT_PLAN_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The treatment plan ID. |
| 2 | `EPISODE_ID` | NUMERIC | FK→ | The episode that contains the treatment plan in this row. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The ID of the patient on the treatment plan in this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

