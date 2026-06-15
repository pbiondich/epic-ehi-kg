# EPA_INFO_2

> This table holds information about electronic prior authorization requests.

**Overflow of:** [EPA_INFO](EPA_INFO.md)  
**Primary key:** `REFERRAL_ID`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier for the referral record. |
| 2 | `PREV_AUTH_EXP_DATE` | DATETIME |  | For prior authorization requests that were created because the existing authorization is about to expire, this item holds the date that the existing authorization will expire. |
| 3 | `ELIG_PAT_ENC_CSN_ID` | NUMERIC | FK→ | This item holds the CSN of the encounter to use for pharmacy benefits for a prior authorization request. |
| 4 | `TOTAL_DOC_SECONDS` | INTEGER |  | This item tracks how many total seconds users spent with ePA documentation activities open. |
| 5 | `PA_PRIORITY_SETBY_C_NAME` | VARCHAR |  | The prior authorization priority change source category ID for the source of the priority of medication prior authorization request. |
| 6 | `PA_PRIORITY_C_NAME` | VARCHAR |  | The prior authorization priority category ID for the priority of medication prior authorization request. |
| 7 | `PA_DAYSPLY` | INTEGER |  | This item holds the days' supply value used for ePA requests. |
| 8 | `PA_DAYSPLY_SRC_C_NAME` | VARCHAR | org | Records how ePA days' supply (I RFL 9260) was obtained for printing and auditing. |
| 9 | `ELECTRONIC_APPEAL_USED_YN` | VARCHAR |  | This item tracks whether native Epic Electronic Appeal functionality was used to appeal this Electronic Prior Authorization. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ELIG_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

