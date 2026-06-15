# ORDER_NARRATIVE

> This table stores the narrative information resulting from a procedure.

**Primary key:** `ORDER_PROC_ID`, `ORD_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record |
| 3 | `NARRATIVE` | VARCHAR |  | Stores the narrative information for this order. |
| 4 | `ORD_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date each order was placed in your system. The integer portion of the number specifies the date the order was placed. The digits after the decimal point indicate multiple orders on one day. |
| 5 | `CONTACT_DATE` | DATETIME |  | The calendar date that the order was placed. |
| 6 | `IS_ARCHIVED_YN` | VARCHAR |  | Indicates whether the order narrative is archived. Y’ indicates that the order narrative is archived. N’ or NULL indicate that the order narrative is not archived. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

