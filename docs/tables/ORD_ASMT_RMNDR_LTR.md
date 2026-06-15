# ORD_ASMT_RMNDR_LTR

> This table contains information about the reminder letters sent for a given mammography assessment.

**Primary key:** `ORDER_PROC_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line count for the reminder letter. |
| 3 | `MAMM_RMD_LTR_DT` | DATETIME |  | Dates on which a reminder letter was sent to have an appointment scheduled for regular mammograms |
| 4 | `MAMMO_LETTER_ID` | VARCHAR |  | The record ID of the mammo reminder letter. This would be commonly used to link to the actual letter text. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

