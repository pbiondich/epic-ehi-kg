# CLARITY_EPP

> The CLARITY_EPP table contains basic information about your benefit plans.

**Primary key:** `BENEFIT_PLAN_ID`  
**Columns:** 2  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BENEFIT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 2 | `BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [CLARITY_EPP_OT](CLARITY_EPP_OT.md) | `BENEFIT_PLAN_ID` | high |

