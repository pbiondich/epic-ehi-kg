# BND_EPSD_INFO_TRANSFORM

> This table contains information on how the episode was transformed from one bundled episode term to a different term.

**Primary key:** `EPISODE_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the bundled episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORIG_BPC_CSN` | NUMERIC |  | This column stores the original bundled episode terms' contact serial number before the transform occurred. |
| 4 | `TARGET_BPC_CSN` | NUMERIC |  | Holds the new bundled episode term's contact serial number for the episode after the transform occurred. |
| 5 | `TRANSFORM_TRIGGER_DATE` | DATETIME |  | Holds the date on the episode on which the bundled episode transform was triggered. Transforms on episodes are always based on the earliest non-anchor event that qualifies for the transform criteria. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

