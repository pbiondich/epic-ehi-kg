# REFERRAL_CVG_BED

> Auth/Cert Coverage Level Bed Days

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique ID of the referral. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUTH_CERT_BDCVG_ID` | NUMERIC |  | Coverage ID for Bed Days at the Coverage (CVG) Level |
| 4 | `AUTH_TOTAL_NUM_DAYS` | INTEGER |  | Bed Days Coverage Level Total Authorized Days |
| 5 | `AUTH_NEXT_REVIEW_DT` | DATETIME |  | Coverage Level Bed Days Next Review Date |
| 6 | `CVG_EARLIEST_DATE` | DATETIME |  | Earliest Start Date for Coverage Level Bed Days |
| 7 | `CVG_LATEST_DATE` | DATETIME |  | Coverage Level Latest Bed Days End Date |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

