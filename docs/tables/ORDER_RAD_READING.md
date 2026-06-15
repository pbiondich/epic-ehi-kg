# ORDER_RAD_READING

> This table stores reading physician information for imaging procedures.

**Primary key:** `ORDER_PROC_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line count for this table as determined by the number of reading radiologists for an order. |
| 3 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `READING_DT` | DATETIME |  | The date that the study was read by the reading radiologist (PROV_ID) -- i.e., the date that the radiologist performed any action on the study. |
| 5 | `READ_PHYS_SPEC_C_NAME` | VARCHAR | org | The reading physician roles category ID for the order. |
| 6 | `READING_RESIDENT_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 7 | `READ_UTC_DTTM` | DATETIME (UTC) |  | The date and time in UTC format when the reading physician made a change to the study. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

