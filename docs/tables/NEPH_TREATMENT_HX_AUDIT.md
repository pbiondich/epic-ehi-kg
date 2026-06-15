# NEPH_TREATMENT_HX_AUDIT

> Stores the audit of changes made to the patient's dialysis treatment details.

**Primary key:** `EPISODE_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TREATMENT_TYPE_C_NAME` | VARCHAR | org | Stores the modality of the modified dialysis treatment history entry. |
| 4 | `TREATMENT_SESSIONS_PER_WEEK` | NUMERIC |  | Stores the sessions per week of the modified dialysis treatment history entry. |
| 5 | `TREATMENT_DURATION_MINUTES` | INTEGER |  | Stores the duration in minutes of the modified dialysis treatment history entry. |
| 6 | `TREATMENT_START_DATE` | DATETIME |  | Stores the effective date of the modified dialysis treatment history entry. |
| 7 | `CHANGE_ACTION_C_NAME` | VARCHAR |  | Stores the edit made to the dialysis treatment history entry. |
| 8 | `CHANGE_USER_ID` | VARCHAR |  | Stores the user who edited the dialysis treatment history entry. |
| 9 | `CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `CHANGE_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant the edit was made to the dialysis treatment history entry. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

