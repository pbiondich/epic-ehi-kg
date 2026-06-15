# MED_AUTH_DETAILS

> This table holds details about a medication prior authorization.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PA_PHARM_TYPE_C_NAME` | VARCHAR |  | This item holds the pharmacy type that the medication was authorized for. |
| 4 | `PA_QUANTITY_UNIT_C_NAME` | VARCHAR | org | This item holds the unit of the medication quantity that was authorized. |
| 5 | `PA_DAYS_SUPPLY` | NUMERIC |  | This item holds the days supply authorized for the medication. |
| 6 | `PA_DISPENSE_CYCLES` | NUMERIC |  | This item holds the number of dispense cycles authorized for the medication. |
| 7 | `PA_REFILLS` | NUMERIC |  | This item holds the number of refills authorized for the medication. |
| 8 | `PA_QUANTITY` | NUMERIC |  | This item holds the medication quantity that was authorized. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

