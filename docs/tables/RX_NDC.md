# RX_NDC

> This table contains the National Drug Code (NDC) information.

**Primary key:** `NDC_ID`  
**Columns:** 3  
**Joined by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NDC_ID` | VARCHAR | PK | The unique ID for the NDC (National Drug Code) |
| 2 | `NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 3 | `NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (5)

| From | Column | Confidence |
|------|--------|------------|
| [AP_CLM_RX_DTL](AP_CLM_RX_DTL.md) | `NDC_ID` | high |
| [AUTH_UM_STATUS_HX](AUTH_UM_STATUS_HX.md) | `NDC_ID` | high |
| [HSP_PRE_AR_TX](HSP_PRE_AR_TX.md) | `NDC_ID` | high |
| [HSP_TRANSACTIONS](HSP_TRANSACTIONS.md) | `NDC_ID` | high |
| [INV_NDC_INFO](INV_NDC_INFO.md) | `NDC_ID` | high |

