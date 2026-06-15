# VARIANCE_TYPE

> This table contains information on variance types (IGT records).

**Primary key:** `VARIANCE_TYPE_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VARIANCE_TYPE_ID` | VARCHAR | PK | The unique ID for the variance type record. |
| 2 | `VARIANCE_TYPE_ID_VARIANCE_NAME` | VARCHAR |  | The name of the variance type record. |
| 3 | `VARIANCE_NAME` | VARCHAR |  | The name of the variance type record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [VARIANCE](VARIANCE.md) | `VARIANCE_TYPE_ID` | high |

