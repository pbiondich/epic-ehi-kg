# CLARITY_EPP_OT

> The CLARITY_EPP_OT table contains overtime information from the benefit plan master file.

**Primary key:** `BENEFIT_PLAN_ID`, `CONTACT_DATE_REAL`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BENEFIT_PLAN_ID` | NUMERIC | PK FK→ | The unique ID of the benefit plan. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | The contact date of the benefit plan in decimal format. |
| 3 | `HOME_INFUSION_ENABLE_BFD_YN` | VARCHAR |  | Indicates whether bill for denial is enabled for this plan in Home Infusion workflows. 'Y' indicates bill for denial is enabled. 'N' indicates it is not enabled. If NULL, then the payer-level setting is used by the system instead. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BENEFIT_PLAN_ID` | [CLARITY_EPP](CLARITY_EPP.md) | sole_pk | high |

