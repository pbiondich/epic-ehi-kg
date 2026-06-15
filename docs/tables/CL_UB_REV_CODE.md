# CL_UB_REV_CODE

> The CL_UB_REV_CODE table contains information on UB revenue codes.

**Primary key:** `UB_REV_CODE_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `UB_REV_CODE_ID` | NUMERIC | PK | This column stores the unique identifier for the revenue code record. |
| 2 | `UB_REV_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 3 | `REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [HSP_TRANSACTIONS](HSP_TRANSACTIONS.md) | `UB_REV_CODE_ID` | high |

