# RFL_CVG_BED_NUM

> Table for the related multi Auth-Cert Bed Days Total (I RFL 8504) item - approved number of days for day type.

**Primary key:** `REFERRAL_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated coverage in this referral record. Together with REFERRAL_ID, this forms the foreign key to the REFERRAL_CVG_BED. |
| 3 | `VALUE_LINE` | INTEGER | PK | Related Multi Count (Value Count) |
| 4 | `AUTH_TOD_NUM_DAYS` | INTEGER |  | Coverage Level Bed Days Total |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

