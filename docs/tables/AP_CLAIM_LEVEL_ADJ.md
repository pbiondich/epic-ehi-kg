# AP_CLAIM_LEVEL_ADJ

> This table contains information about a claim's claim-level adjustments. These adjustments are on top of service line amounts, so they don't factor into patient portion / benefits but are subject to interest and penalties. These amounts affect the total payment of the claim.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLAIM_ADJ_AMT` | NUMERIC |  | The monetary claim-level adjustment amount for a claim. |
| 4 | `CLAIM_ADJ_RSN_C_NAME` | VARCHAR | org | The Claim Level Adjustment Reason category ID for the claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

