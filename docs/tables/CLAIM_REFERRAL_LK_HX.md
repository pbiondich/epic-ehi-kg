# CLAIM_REFERRAL_LK_HX

> This table contains the history of referrals linked to AP claims. Amounts and counts calculated during adjudication when these referrals were attached to the AP claim are also included.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REFERRAL_ID` | NUMERIC | FK→ | The unique identifier of the referral previously associated with this claim. |
| 4 | `VISIT_COUNT` | INTEGER |  | The visit count for this referral when it was linked to the AP claim. |
| 5 | `ADJUD_AMT` | NUMERIC |  | The adjudicated dollar amount for this referral when it was linked to the AP claim. |
| 6 | `PAID_AMT` | NUMERIC |  | The paid dollar amount for this referral when it was linked to the AP claim. |
| 7 | `RFL_ATTACH_SOURCE_C_NAME` | VARCHAR |  | The historical referral attachment source category ID for the AP claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

