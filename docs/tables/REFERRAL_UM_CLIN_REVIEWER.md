# REFERRAL_UM_CLIN_REVIEWER

> This table contains information about review of the Clinical Summary navigator section for referrals.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REVIEW_USER_ID` | VARCHAR |  | The unique ID of the user who last reviewed the UM Clinical Summary |
| 4 | `REVIEW_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `CLINICAL_REVIEW_UTC_DTTM` | DATETIME (UTC) |  | The instant that the UM Clinical Summary was marked as reviewed |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

