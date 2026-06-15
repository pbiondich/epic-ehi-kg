# ORDER_RAD_REPEATS

> This table stores information about film repeats for an imaging order.

**Primary key:** `ORDER_PROC_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line count for this table as determined by the number of repeat/repeat reason combinations associated with an order. |
| 3 | `NUMBER_REPEATS` | INTEGER |  | The number of repeats for a particular repeat reason for the associated order record. |
| 4 | `REPEAT_RSN_C_NAME` | VARCHAR | org | The repeat reason category ID for a particular number of repeats (NUMBER_REPEATS). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

