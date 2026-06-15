# RFL_ADD_PAYORS

> This table holds information regarding additional payors listed on the referral.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique ID of the referral |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RFL_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 4 | `RFL_PAYOR_AUTH` | VARCHAR |  | The carrier authorization number for this payor |
| 5 | `RFL_PAYOR_PRECERT` | VARCHAR |  | The precertification number for this payor |
| 6 | `RFL_PAYOR_AUTH_CMT` | VARCHAR |  | Authorization comments for this payor |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

