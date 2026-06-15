# SURVEILLANCE_ABSTRACTION

> This table contains basic information from surveillance abstractions.

**Primary key:** `SURV_ABSTN_REGISTRY_DATA_ID`  
**Columns:** 2  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SURV_ABSTN_REGISTRY_DATA_ID` | NUMERIC | PK | The unique identifier (.1 item) for the registry data record. |
| 2 | `ASSOC_RPT_HOSP_REGULATORY_ID_CMS_MU_NAME` | VARCHAR |  | The name of the CMS Meaningful Use record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [INFECTION_ABSTNS](INFECTION_ABSTNS.md) | `SURV_ABSTN_REGISTRY_DATA_ID` | high |

