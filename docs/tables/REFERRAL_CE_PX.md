# REFERRAL_CE_PX

> This audit table stores the Care Everywhere Procedures.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_PX_MODIFIERS` | VARCHAR |  | Stores a comma delimited list of procedure modifiers. This item is used to audit data from incoming Care Everywhere referrals. |
| 4 | `AUDIT_PX_REVENUE_CODE` | VARCHAR |  | Stores the revenue code associated for a procedure associated with the referral. This item is used to audit data from incoming Care Everywhere referrals. |
| 5 | `AUDIT_PX_REQUESTED_UNITS` | INTEGER |  | Stores the requested number of units for a procedure associated with the referral. This item is used to audit data from incoming Care Everywhere referrals. |
| 6 | `AUDIT_PX_APPROVED_UNITS` | INTEGER |  | Stores the approved number of units for a procedure associated with the referral. This item is used to audit data from incoming Care Everywhere referrals. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

