# CLARITY_LPP

> The CLARITY_LPP table contains information from the extension master file.

**Primary key:** `LPP_ID`  
**Columns:** 2  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LPP_ID` | NUMERIC | PK | The unique ID of the extension. |
| 2 | `LPP_NAME` | VARCHAR |  | The name of the extension. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [MED_PAUSE_LOG](MED_PAUSE_LOG.md) | `LPP_ID` | high |

