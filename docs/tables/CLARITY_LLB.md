# CLARITY_LLB

> Interface laboratory general information.

**Primary key:** `RESULTING_LAB_ID`  
**Columns:** 3  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULTING_LAB_ID` | NUMERIC | PK | The unique ID of the interface laboratory record. |
| 2 | `RESULTING_LAB_ID_LLB_NAME` | VARCHAR |  | Interface laboratory name. |
| 3 | `LLB_NAME` | VARCHAR |  | Interface laboratory name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [ORDER_RESULTS](ORDER_RESULTS.md) | `RESULTING_LAB_ID` | high |
| [ORDER_SENSITIVITY](ORDER_SENSITIVITY.md) | `RESULTING_LAB_ID` | high |
| [ORDER_STATUS](ORDER_STATUS.md) | `RESULTING_LAB_ID` | high |

