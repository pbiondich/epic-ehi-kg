# AP_CLAIM_PX_RFLS_USED

> This table contains the list of referrals that are used during AP claims adjudication to satisfy authorization requirements for this service.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REFERRAL_ID` | NUMERIC | FK→ | Tracks the referrals used to satisfy authorization requirements during AP claims adjudication. |
| 4 | `USED_COUNT` | INTEGER |  | Tracks the used count for each referral used during AP claims adjudication. |
| 5 | `COUNTS_SHARED_C_NAME` | VARCHAR |  | Whether the referral count used is shared with a previously-adjudicated claim or service. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

