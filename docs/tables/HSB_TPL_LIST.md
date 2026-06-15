# HSB_TPL_LIST

> The linking of an episode ID to a patient ID and a treatment plan ID.

**Primary key:** `EPISODE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The episode ID. |
| 2 | `LINE` | INTEGER | PK | The line number that corresponds to each treatment plan in the episode in this row. |
| 3 | `TPL_ID` | NUMERIC |  | The ID of a treatment plan associated with this episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

