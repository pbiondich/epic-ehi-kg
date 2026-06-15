# RFL_CROSS_ORG_FAIL_REASON

> This table contains reasons for why CERM, 360X, or Electronic ToC referral failed to send.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CROSS_ORG_FAIL_REASON_C_NAME` | VARCHAR |  | This item records the reasons a Care Everywhere Referral (CERM, 360X, or ToC) fails to send. Item is in RFL instead of DXS because if the referral fails to send due to not have Care Everywhere Patient Authorization, a DXS record will not be created. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

