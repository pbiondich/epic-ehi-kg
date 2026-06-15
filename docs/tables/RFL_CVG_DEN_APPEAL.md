# RFL_CVG_DEN_APPEAL

> Table for the related multi Auth-Cert Denials Appealed Flag (I RFL 8524) item indicating whether the denial was appealed.

**Primary key:** `REFERRAL_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated coverage for this referral record. Together with REFERRAL_ID, this forms the foreign key to the REFERRAL_CVG_BED table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple flags indicating if an appeal has been generated for the denied bed day(s) that are associated with the referral and the coverage from the REFERRAL_CVG_BED table. |
| 4 | `DENIED_APPEALED_YN` | VARCHAR |  | Auth-Cert Coverage Level Bed Days - Appealed Flag |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

