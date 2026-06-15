# HH_VO_DEFICIENCY

> This table contains the deficiencies associated with the home care order.

**Primary key:** `VERBAL_ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VERBAL_ORDER_ID` | VARCHAR | PK FK→ | Unique identifier for the verbal order. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DFI_ID` | NUMERIC |  | The deficency ID associated with the home care order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VERBAL_ORDER_ID` | [HH_VO_INFO](HH_VO_INFO.md) | sole_pk | high |

