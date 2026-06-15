# CLARITY_ORGANISM

> The CLARITY_ORGANISM table contains basic information about the organisms used in clinical systems.

**Primary key:** `ORGANISM_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORGANISM_ID` | NUMERIC | PK | The unique ID of the organism record. |
| 2 | `ORGANISM_ID_NAME` | VARCHAR |  | The name of the organism. |
| 3 | `NAME` | VARCHAR |  | The name of the organism. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [ORDER_SENSITIVITY](ORDER_SENSITIVITY.md) | `ORGANISM_ID` | high |

