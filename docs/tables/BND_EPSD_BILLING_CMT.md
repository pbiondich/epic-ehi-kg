# BND_EPSD_BILLING_CMT

> This table contains information about the comments associated with bundled episodes.

**Primary key:** `EPISODE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the bundled episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Longer billing comments can be broken up into multiple lines of information. |
| 3 | `BILLING_COMMENT` | VARCHAR |  | Stores the billing comments for the bundled episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

