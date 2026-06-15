# HH_ALERT_TYPE_INFO

> This table stores information about Home Health Alert Types.

**Primary key:** `ALERT_TYPE_ID`  
**Columns:** 2  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALERT_TYPE_ID_ALERT_TYPE_NAME` | VARCHAR |  | The name of the home health alert type. |
| 2 | `ALERT_TYPE_NAME` | VARCHAR |  | The name of the home health alert type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [HH_ALERT_INFO](HH_ALERT_INFO.md) | `ALERT_TYPE_ID` | high |

