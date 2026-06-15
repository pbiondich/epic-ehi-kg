# CL_ICD_PX

> The CL_ICD_PX table is the master table for ICD procedures.

**Primary key:** `ICD_PX_ID`  
**Columns:** 3  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ICD_PX_ID` | VARCHAR | PK | The unique ID of the ICD procedure record. |
| 2 | `ICD_PX_ID_ICD_PX_NAME` | VARCHAR |  | The name of the ICD procedure record. |
| 3 | `ICD_PX_NAME` | VARCHAR |  | The name of the ICD procedure record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [AP_CLAIM_ICD_PROC](AP_CLAIM_ICD_PROC.md) | `ICD_PX_ID` | high |
| [CASE_ICD_PROC](CASE_ICD_PROC.md) | `ICD_PX_ID` | high |

