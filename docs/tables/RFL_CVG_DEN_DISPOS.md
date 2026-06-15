# RFL_CVG_DEN_DISPOS

> Table for the related multi Auth-Cert Denials Dispositions (I RFL 8525) item - denied days disposition.

**Primary key:** `REFERRAL_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated coverage for this referral record. Together with REFERRAL_ID, this forms the foreign key to the REVERRAL_CVG_BED table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple denial dispositions that are associated with the referral and the coverage from the REFERRAL_CVG table. |
| 4 | `DENIED_DISPOSTN_C_NAME` | VARCHAR | org | Auth-Cert Coverage Level - Denials Disposition |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

