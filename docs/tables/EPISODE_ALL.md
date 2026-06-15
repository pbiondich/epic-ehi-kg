# EPISODE_ALL

> This table contains all episode records, regardless of the type and is intended for use with Organization Filter functionality. If used for Organization Filtering, users will be able to see an episode if they have authorization for the owning business segment on the episode or the patient associated with the episode.

**Primary key:** `EPISODE_ID`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique identifier of the episode record. |
| 2 | `STATUS_C_NAME` | VARCHAR |  | The status of the episode record. An episode status might be Active, Resolved, or Deleted. |
| 3 | `EPISODE_NAME` | VARCHAR |  | The name of the episode. |
| 4 | `START_DATE` | DATETIME |  | The date the episode was initiated. |
| 5 | `END_DATE` | DATETIME |  | The date the episode was resolved. |
| 6 | `CARE_INTG_ID` | VARCHAR | FK→ | The unique ID of the care plan linked to the episode. |
| 7 | `TREATMENT_CAREPLAN_ID` | VARCHAR |  | Link to the treatment list |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CARE_INTG_ID` | [CAREPLAN_INFO](CAREPLAN_INFO.md) | sole_pk | high |
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

