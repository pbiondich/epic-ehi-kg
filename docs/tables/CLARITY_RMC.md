# CLARITY_RMC

> This table contains basic information about the remittance codes that can accompany electronic payments and claim denials.

**Primary key:** `REMIT_CODE_ID`  
**Columns:** 3  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REMIT_CODE_ID` | VARCHAR | PK | This column stores the unique identifier for the remittance code record. |
| 2 | `REMIT_CODE_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 3 | `REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [BDC_INFO](BDC_INFO.md) | `REMIT_CODE_ID` | high |
| [INV_CLM_LN_ADDL](INV_CLM_LN_ADDL.md) | `REMIT_CODE_ID` | high |
| [PR_EST_SVC_LN_RMT_INFO](PR_EST_SVC_LN_RMT_INFO.md) | `REMIT_CODE_ID` | high |

