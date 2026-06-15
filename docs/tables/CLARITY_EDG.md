# CLARITY_EDG

> The CLARITY_EDG table contains basic information about diagnoses.

**Primary key:** `DX_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 2 | `DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 3 | `PAT_FRIENDLY_TEXT` | VARCHAR |  | A description of the diagnosis that is easy for patients to understand. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [PRE_AR_CHG_2](PRE_AR_CHG_2.md) | `DX_ID` | high |

