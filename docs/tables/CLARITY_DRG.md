# CLARITY_DRG

> This table contains information for the DRG (Diagnosis Related Groups) master file.

**Primary key:** `DRG_ID`  
**Columns:** 3  
**Joined by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DRG_ID` | VARCHAR | PK | The unique identifier of the Diagnoses Related Group record. This is not the DRG code. |
| 2 | `DRG_ID_DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |
| 3 | `DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (8)

| From | Column | Confidence |
|------|--------|------------|
| [ACCUM_CONTEXTUAL_DATA](ACCUM_CONTEXTUAL_DATA.md) | `DRG_ID` | high |
| [AP_CLAIM](AP_CLAIM.md) | `DRG_ID` | high |
| [AP_CLAIM_PROC](AP_CLAIM_PROC.md) | `DRG_ID` | high |
| [CASE_DRG_ID](CASE_DRG_ID.md) | `DRG_ID` | high |
| [CLM_ADJUD_INFO](CLM_ADJUD_INFO.md) | `DRG_ID` | high |
| [HSP_CLAIM_DETAIL1](HSP_CLAIM_DETAIL1.md) | `DRG_ID` | high |
| [HSP_CLM_EXP_ALLOW](HSP_CLM_EXP_ALLOW.md) | `DRG_ID` | high |
| [PR_EST_AP_CLAIM_PROC](PR_EST_AP_CLAIM_PROC.md) | `DRG_ID` | high |

