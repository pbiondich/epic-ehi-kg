# BENEFIT_SVC_TYPE

> Each record represents a classification of benefits.

**Primary key:** `SERVICE_TYPE_ID`  
**Columns:** 3  
**Joined by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SERVICE_TYPE_ID` | VARCHAR | PK | The unique identifier for the service type record. |
| 2 | `SERVICE_TYPE_ID_SERVICE_TYPE_NAME` | VARCHAR |  | The name of this benefit service type. |
| 3 | `SERVICE_TYPE_NAME` | VARCHAR |  | The name of this benefit service type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (4)

| From | Column | Confidence |
|------|--------|------------|
| [HSP_CLAIM_PAT_RESP](HSP_CLAIM_PAT_RESP.md) | `SERVICE_TYPE_ID` | high |
| [PR_EST_FAC_FEES](PR_EST_FAC_FEES.md) | `SERVICE_TYPE_ID` | high |
| [PR_EST_PROFEE_CXT](PR_EST_PROFEE_CXT.md) | `SERVICE_TYPE_ID` | high |
| [PR_EST_PX_BEN_ADDL_INFO](PR_EST_PX_BEN_ADDL_INFO.md) | `SERVICE_TYPE_ID` | high |

