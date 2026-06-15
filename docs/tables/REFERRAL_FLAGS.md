# REFERRAL_FLAGS

> The REFERRAL_FLAGS table holds the referral flag information associated with the referral records stored in the REFERRAL table. Each referral record can have any number of flags assigned to it. This table stores every flag associated with each referral record.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The internal ID of the referral that this row of information corresponds to. |
| 2 | `LINE` | INTEGER | PK | The line number of the referral flag that this row of information corresponds to. For instance, if the referral has two flags, the first flag will have a Line value of 1 while the second will have a Line value of 2 |
| 3 | `FLAG_C_NAME` | VARCHAR | org | The category number associated with the flag assigned to the referral |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

