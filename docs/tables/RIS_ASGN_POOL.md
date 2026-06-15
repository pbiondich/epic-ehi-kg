# RIS_ASGN_POOL

> This table contains the assigned pools for an imaging order.

**Primary key:** `ORDER_PROC_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line count for the assigned radiology pools for an order. |
| 3 | `RAD_ASGN_PLS_ID` | VARCHAR |  | The unique ID of the assigned pools for an order. |
| 4 | `RAD_ASGN_PLS_ID_POOL_NAME` | VARCHAR |  | The name of the scheduling pool used when searching for available providers for an appointment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

