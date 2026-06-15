# REG_METRIC_CONFIG

> This table contains information about the configuration of a registry metric (MET) record.

**Primary key:** `MET_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MET_ID` | NUMERIC | PK | The unique identifier (.1 item) for the registry metric record. |
| 2 | `MET_ID_RECORD_NAME` | VARCHAR |  | Stores the name of the registry metric record. |
| 3 | `RECORD_NAME` | VARCHAR |  | Stores the name of the registry metric record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [MODEL_FEATURES](MODEL_FEATURES.md) | `MET_ID` | high |

