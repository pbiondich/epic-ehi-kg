# NEPH_TREATMENT_HISTORY

> This table stores the historical details of patients' dialysis treatments.

**Primary key:** `EPISODE_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TREATMENT_TYPE_C_NAME` | VARCHAR | org | This item stores the type of modality for a prescribed dialysis treatment. |
| 4 | `TREATMENT_SESSIONS_PER_WEEK` | NUMERIC |  | This item stores the number of sessions per each week for a prescribed dialysis treatment. |
| 5 | `TREATMENT_DURATION_MINUTES` | INTEGER |  | This item stores the duration in minutes for a prescribed dialysis treatment. |
| 6 | `TREATMENT_START_DATE` | DATETIME |  | This item stores the date a prescribed dialysis treatment started. |
| 7 | `LAST_EDIT_USER_ID` | VARCHAR |  | This item stores the user who last modified details for a prescribed dialysis treatment. |
| 8 | `LAST_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `LAST_EDIT_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | This item stores the last instant that the treatment details for a prescribed dialysis treatment were modified. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

