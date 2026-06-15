# NEPH_MODALITY_EPISODE

> The NEPH_MODALITY_EPISODE table stores the link between a patient's dialysis modality episode and its associated clinical episode.

**Primary key:** `EPISODE_ID`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique identifier for the episode record. |
| 2 | `CLINICAL_EPISODE_ID` | NUMERIC |  | The clinical episode ID associated with the dialysis modality episode. |
| 3 | `NEPH_TREATMENT_TYPE_C_NAME` | VARCHAR | org | This item is used to store a patient's type of dialysis treatment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

