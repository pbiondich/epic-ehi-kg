# DISCIPLINE

> This table contains information on defined disciplines (LDS records).

**Primary key:** `DISC_TYPE_ID`  
**Columns:** 3  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DISC_TYPE_ID` | VARCHAR | PK | The unique ID of the discipline record. |
| 2 | `DISC_TYPE_ID_DISC_NAME` | VARCHAR |  | The name of the discipline record. |
| 3 | `DISC_NAME` | VARCHAR |  | The name of the discipline record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [GOAL_DISC](GOAL_DISC.md) | `DISC_TYPE_ID` | high |
| [PROBLEM_CAREPLAN_DISC](PROBLEM_CAREPLAN_DISC.md) | `DISC_TYPE_ID` | high |

