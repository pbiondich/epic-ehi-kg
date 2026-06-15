# HSP_BFH_BILL_RANGE_END

> Stores the billing end date for a billing activity.

**Primary key:** `BFH_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BFH_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the billing activity history record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `ACT_BILL_END_DATE` | DATETIME |  | Holds the end date for a billing date range |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BFH_ID` | [HSP_BFH_ACTIVITY](HSP_BFH_ACTIVITY.md) | sole_pk | high |

