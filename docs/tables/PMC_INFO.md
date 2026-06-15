# PMC_INFO

> This table displays promotion information.

**Primary key:** `PROMOTION_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROMOTION_ID` | NUMERIC | PK | The unique identifier for the promotion record. |
| 2 | `PROMOTION_ID_PROMOTION_NAME` | VARCHAR |  | The promotion record name. |
| 3 | `PROMOTION_NAME` | VARCHAR |  | The promotion record name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [PR_EST_PROMOTION_INFO](PR_EST_PROMOTION_INFO.md) | `PROMOTION_ID` | high |

