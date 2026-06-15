# CASE_RFL

> The CASE_RFL table provides the link between case records and referral information.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | NUMERIC | PK shared | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The line number of the referrals associated with this case record. |
| 3 | `REFERRAL_ID` | NUMERIC | FK→ | The unique ID of the referral record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

