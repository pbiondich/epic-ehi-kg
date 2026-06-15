# RFL_CVG_DEN_RSN_C

> Related multi table for the Auth-Cert Denials Reason (I RFL 8523) item - coverage level denied days reason.

**Primary key:** `REFERRAL_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `GROUP_LINE` | INTEGER | PK | Line Count |
| 3 | `VALUE_LINE` | INTEGER | PK | Related Multi Item Count |
| 4 | `DENIED_REASON_C_NAME` | VARCHAR | org | Auth-Cert Coverage Level Bed Days - Denial Reason |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

