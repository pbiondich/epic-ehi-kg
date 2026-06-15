# RFL_CVG_DEN_NTF_DT

> Related multi table for the Auth-Cert Denials Date Notified (I RFL 8522) item - coverage level denied days notification date.

**Primary key:** `REFERRAL_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `GROUP_LINE` | INTEGER | PK | Line Count |
| 3 | `VALUE_LINE` | INTEGER | PK | Related Multi Item Count |
| 4 | `DENIED_NOTIF_DATE` | DATETIME |  | Auth/Cert Coverage Level - Denials Date Notified |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

