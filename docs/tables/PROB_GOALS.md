# PROB_GOALS

> This table contains data on the discrete goal (IGO) records associated with each problem.

**Primary key:** `PROBLEM_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_ID` | VARCHAR | PK FK→ | The unique ID for the care integrator problem. |
| 2 | `LINE` | INTEGER | PK | The line count for the item. |
| 3 | `GOAL_ID` | VARCHAR | FK→ | The unique ID for the goal associated with this problem. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GOAL_ID` | [GOAL](GOAL.md) | name_stem | high |
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |

