# REFERRAL_REASONS

> Contains the reasons for each referral.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique ID of the referral. |
| 2 | `LINE` | INTEGER | PK | The line number of the referral reason. |
| 3 | `REFERRAL_REASON_C_NAME` | VARCHAR | org | The reason category value. |
| 4 | `REFERRAL_REASON_OTHER` | VARCHAR |  | The comment entered when the user chooses "Other" as the reason for referral. If the comment surpasses 60 characters, it will be truncated to 60. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

