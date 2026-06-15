# ORDER_IMPRESSION

> This table stores impression information for a procedure.

**Primary key:** `ORDER_PROC_ID`, `ORD_DATE_REAL`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line count for the reading physician's impression. |
| 3 | `IMPRESSION` | VARCHAR |  | The reading physician's impression for this procedure. |
| 4 | `ORD_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date each order was placed in your system. The integer portion of the number specifies the date the order was placed. The digits after the decimal point indicate multiple orders on one day. |
| 5 | `CONTACT_DATE` | DATETIME |  | The calendar date that the order was placed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

