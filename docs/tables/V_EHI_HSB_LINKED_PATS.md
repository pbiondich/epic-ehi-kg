# V_EHI_HSB_LINKED_PATS

> Placeholder view for HSB EHI data that needs to be marked as both static and dynamic.

**Primary key:** `EPISODE_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique identifier of the episode record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient associated with the episode. |
| 3 | `CM_LOG_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

