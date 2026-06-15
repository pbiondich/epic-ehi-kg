# HSP_BFH_SELECTED_HAR

> Stores which hospital accounts were selected for a guarantor action.

**Primary key:** `BFH_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BFH_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the billing activity history record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HOSP_ACCOUNT_ID` | NUMERIC |  | This column stores the history of hospital accounts that were selected for a guarantor action. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BFH_ID` | [HSP_BFH_ACTIVITY](HSP_BFH_ACTIVITY.md) | sole_pk | high |

