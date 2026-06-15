# CLARITY_HM_TOPIC

> The CLARITY_HM_TOPIC table contains the names and IDs of your health maintenance topic records. These records include tests and procedures that form the basis for Health Maintenance plans in clinical system.

**Primary key:** `HM_TOPIC_ID`  
**Columns:** 2  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HM_TOPIC_ID` | NUMERIC | PK | The unique ID of the health maintenance topic record. |
| 2 | `NAME` | VARCHAR |  | The name of the health maintenance topic. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [ALERT](ALERT.md) | `HM_TOPIC_ID` | high |
| [HM_HISTORICAL_STATUS](HM_HISTORICAL_STATUS.md) | `HM_TOPIC_ID` | high |

