# AVOIDABLE_DAYS_CMT

> This table contains the avoidable days comment. The primary key for the avoidable days comment table is Referral ID.

**Primary key:** `REFERRAL_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique ID of the referral record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated coverage in this patient's referral record. Together with REFERRAL_ID, this forms the foreign key to the REFERRAL_CVG_BED table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple comments that are associated with the coverage and the referral from the REFERRAL_CVG_BED table. |
| 4 | `PADS_COMMENT` | VARCHAR |  | The coverage level PADS comment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

