# REFERRAL_EOB_CODES

> This table holds the Claim Alert Explanation of Benefits (EOB) Codes attached to a referral.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number of the change to the referral. For example, if the referral is changed twice, the first change will have a line value of 1, while the second change will have a line value of 2. |
| 3 | `EOB_CODE_ID_EOB_CODE_NAME` | VARCHAR |  | The name of the processing code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

