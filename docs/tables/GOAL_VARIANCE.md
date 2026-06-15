# GOAL_VARIANCE

> This table contains data on the variance associated with each goal.

**Primary key:** `GOAL_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GOAL_ID` | VARCHAR | PK FK→ | The unique ID for the goal record. |
| 2 | `LINE` | INTEGER | PK | The line count for the item. |
| 3 | `VARIANCE_ID` | VARCHAR | FK→ | The unique ID for the variances associated with this record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GOAL_ID` | [GOAL](GOAL.md) | name_stem | high |
| `VARIANCE_ID` | [VARIANCE](VARIANCE.md) | sole_pk | high |

