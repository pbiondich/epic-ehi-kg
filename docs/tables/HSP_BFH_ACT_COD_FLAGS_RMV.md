# HSP_BFH_ACT_COD_FLAGS_RMV

> This table extracts the coding flags that are listed as removed in the Billing History. It should be used in conjunction with table HSP_BFH_ACTIVITY.

**Primary key:** `BFH_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BFH_ID` | NUMERIC | PK FK→ | The unique identifier for the activity history record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `ACTION_FLAGS_RMV_C_NAME` | VARCHAR | org | Contains the coding flags that were removed via the Modify Coding Flags account action. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BFH_ID` | [HSP_BFH_ACTIVITY](HSP_BFH_ACTIVITY.md) | sole_pk | high |

