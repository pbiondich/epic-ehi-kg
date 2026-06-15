# RFL_CVG_BED_REFNUM

> Related multi table for the Auth-Cert Approved Days Reference Number (I RFL 8513) item.

**Primary key:** `REFERRAL_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated Auth/Cert Approved Days reference number for a particular coverage (payor) in this referral record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple Auth/Cert Approved Days reference numbers that are associated with the referral and the particular coverage (payor) in the Auth/Cert bed days related table. |
| 4 | `APPROVED_DAY_REFNUM` | VARCHAR |  | Reference number associated with the approved bed days range for a particular coverage (payor). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

