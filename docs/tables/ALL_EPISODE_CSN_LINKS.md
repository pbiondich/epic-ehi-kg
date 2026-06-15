# ALL_EPISODE_CSN_LINKS

> The ALL_EPISODE_CSN_LINKS table contains one row for each master file link added to an episode. Each row contains information associated with the master file stored in the EPISODE_LINK_INI column. It can be used with other episode tables to report on episode data whether the episode is linked to an encounter or not.

**Primary key:** `EPISODE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique ID of the episode of care record for this row. |
| 2 | `LINE` | INTEGER | PK | This identifies the link master file. |
| 3 | `TREATMENT_PLAN_ID` | NUMERIC | shared | The unique ID of the transplant record for this row. |
| 4 | `TREATMENT_PLAN_CSN_ID` | NUMERIC |  | The unique serial number for this transplant record. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

