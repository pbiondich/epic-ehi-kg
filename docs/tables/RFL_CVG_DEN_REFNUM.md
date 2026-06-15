# RFL_CVG_DEN_REFNUM

> Related multi table for the Auth-Cert Denied Days Reference Number (I RFL 8527) item.

**Primary key:** `REFERRAL_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated coverage in this referral record. Together with REFERRAL_ID, this forms the foreign key to the REFERRAL_CVG_BED table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple denied days reference numbers that are associated with the referral and the coverage from the REFERRAL_CVG_BED table. |
| 4 | `DENIED_DAYS_REFNUM` | VARCHAR |  | Reference number associated with the denied bed days range for a particular coverage (payor). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

