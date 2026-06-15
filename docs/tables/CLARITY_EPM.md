# CLARITY_EPM

> The CLARITY_EPM table contains information about payer records.

**Primary key:** `PAYOR_ID`  
**Columns:** 2  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 2 | `PAYOR_NAME` | VARCHAR |  | The name of the payor. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [CLARITY_EPM_OT](CLARITY_EPM_OT.md) | `PAYOR_ID` | high |
| [RXA_ADJUD_MESSAGE](RXA_ADJUD_MESSAGE.md) | `PAYOR_ID` | high |

