# BND_EPSD_TERMS

> This table contains information about your bundled episode terms (BPC) records, which define various reimbursement related attributes related to a bundled episode (HSB).

**Primary key:** `BPC_ID`  
**Columns:** 3  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BPC_ID` | NUMERIC | PK | This column stores the unique identifier for the bundled episode terms record. |
| 2 | `BPC_ID_BPC_NAME` | VARCHAR |  | The name of the bundled episode terms record. |
| 3 | `BPC_NAME` | VARCHAR |  | The name of the bundled episode terms record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [BND_EPSD_INFO](BND_EPSD_INFO.md) | `BPC_ID` | high |
| [EPISODE_2](EPISODE_2.md) | `BPC_ID` | high |

