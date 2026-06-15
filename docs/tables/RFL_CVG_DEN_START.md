# RFL_CVG_DEN_START

> Related multi table for the Auth-Cert Denials Start Date (I RFL 8520) item - coverage level denied days start date.

**Primary key:** `REFERRAL_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated coverage for this referral record. Together with REFERRAL_ID, this forms the foreign key to the REFERRAL_CVG_BED table. |
| 3 | `VALUE_LINE` | INTEGER | PK | Related Multi Item Count |
| 4 | `DENIED_START_DATE` | DATETIME |  | The start date for the denial(s) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

