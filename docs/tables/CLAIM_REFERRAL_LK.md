# CLAIM_REFERRAL_LK

> This table contains the referrals linked to AP claims.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The ID number of the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number indicating the order of referrals associated with this claim. |
| 3 | `REFERRAL_ID` | NUMERIC | FK→ | The ID number of the referral associated with the claim. |
| 4 | `RFL_NOT_USED` | VARCHAR |  | Stores 1 if the referral was not used during adjudication and is blank otherwise. |
| 5 | `PROC_LINES_ALLOWED` | VARCHAR |  | Stores a list of service lines allowed to count against this referral as a comma-delimited list. The lines correspond to the values in AP_CLAIM_PROC_IDS.LINE for the claim. |
| 6 | `RFL_ATTACH_SOURCE_C_NAME` | VARCHAR |  | The referral attachment source category ID for the AP claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

