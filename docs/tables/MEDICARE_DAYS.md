# MEDICARE_DAYS

> This table stores the number of remaining covered, coinsurance, and reserve days at the beginning of an admission.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MEDCARE_CVG_ID` | NUMERIC |  | Medicare Coverage ID the referral is attached to. |
| 4 | `COVERED_DAYS` | INTEGER |  | Remaining covered days for a particular Medicare visit. |
| 5 | `COINS_DAYS` | INTEGER |  | Remaining co-insurance days for a particular Medicare visit. |
| 6 | `RESERVE_DAYS` | INTEGER |  | Remaining lifetime reserve days for a particular Medicare visit. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

