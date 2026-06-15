# GOAL_TEMPLATES

> This table contains goal template information. It includes columns for the goal template name, goal template record state, display name, goal type, goal template type, description, priority, check point date, goal usage, and duplicate goal action.

**Primary key:** `GOAL_TEMPLATE_ID`  
**Columns:** 3  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GOAL_TEMPLATE_ID` | NUMERIC | PK | The unique identifier for the goal template record. |
| 2 | `GOAL_TEMPLATE_ID_GOAL_TEMPLATE_NAME` | VARCHAR |  | The goal template name. |
| 3 | `GOAL_TEMPLATE_NAME` | VARCHAR |  | The goal template name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [GOAL](GOAL.md) | `GOAL_TEMPLATE_ID` | high |
| [PT_GOALS_INFO](PT_GOALS_INFO.md) | `GOAL_TEMPLATE_ID` | high |

