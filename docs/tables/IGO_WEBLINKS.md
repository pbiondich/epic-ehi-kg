# IGO_WEBLINKS

> This table displays weblinks associated with discrete goal records.

**Primary key:** `GOAL_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GOAL_ID` | VARCHAR | PK FK→ | The unique identifier for the goal record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `WEBLINK_TEXT` | VARCHAR |  | Reference link display text for the address specified by the WEBLINK_ADDRESS column. |
| 4 | `WEBLINK_ADDRESS` | VARCHAR |  | Reference link address for the text specified by the WEBLINK_TEXT column. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GOAL_ID` | [GOAL](GOAL.md) | name_stem | high |

