# GOAL_TYPE

> This table contains information on goal types (INO records).

**Primary key:** `GOAL_TYPE_ID`  
**Columns:** 3  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GOAL_TYPE_ID` | VARCHAR | PK | The unique ID for the goal type record. |
| 2 | `GOAL_TYPE_ID_GOAL_NAME` | VARCHAR |  | The name of the goal type record. |
| 3 | `GOAL_NAME` | VARCHAR |  | The name of the goal type record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [GOAL](GOAL.md) | `GOAL_TYPE_ID` | high |
| [VARIANCE](VARIANCE.md) | `GOAL_TYPE_ID` | high |

