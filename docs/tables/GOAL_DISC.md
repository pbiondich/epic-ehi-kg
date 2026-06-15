# GOAL_DISC

> This table contains data on the disciplines associated with the goals.

**Primary key:** `GOAL_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GOAL_ID` | VARCHAR | PK FK→ | The unique ID for the goal record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | The DTE contact date for the goal record. |
| 3 | `LINE` | INTEGER | PK | The line count for the record. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `DISC_TYPE_ID` | VARCHAR | FK→ | The unique ID for the discipline to be responsible for this goal. |
| 6 | `DISC_TYPE_ID_DISC_NAME` | VARCHAR |  | The name of the discipline record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DISC_TYPE_ID` | [DISCIPLINE](DISCIPLINE.md) | sole_pk | high |
| `GOAL_ID` | [GOAL](GOAL.md) | name_stem | high |

