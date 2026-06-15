# ORD_MED_ADMININSTR

> This table is to show administration instruction information for each order. If you want to know order information, you could link this table to ORDER_MED or ORDER_MEDINFO.

**Primary key:** `ORDER_MED_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique ID of the medication order (prescription) record. NOTE: This is an internal unique identifier for order (ORD) master file records in this table and cannot be used to link to CLARITY_MEDICATION. |
| 2 | `LINE` | INTEGER | PK | The line number for each administration instruction line. |
| 3 | `MED_ADMIN_INSTR` | VARCHAR |  | The context for administration instruction converted to plain text. |
| 4 | `ORDERING_DATE` | DATETIME |  | The date the order was placed in calendar format. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

