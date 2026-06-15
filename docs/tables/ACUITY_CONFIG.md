# ACUITY_CONFIG

> This table contains the configuration information for the acuity systems.

**Primary key:** `ACUITY_SYSTEM_ID`  
**Columns:** 2  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACUITY_SYSTEM_ID` | NUMERIC | PK | The unique identifier (.1 item) for the acuity system record. |
| 2 | `ACUITY_SYSTEM_NAME` | VARCHAR |  | The name of this HDA record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [QM_GEN_INFO](QM_GEN_INFO.md) | `ACUITY_SYSTEM_ID` | high |

