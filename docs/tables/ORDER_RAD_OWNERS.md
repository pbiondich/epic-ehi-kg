# ORDER_RAD_OWNERS

> ORDER_RAD_OWNERS stores the study owner information for a radiology order performed in radiology

**Primary key:** `ORDER_PROC_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line count for this table as determined by the number of owners for an order. |
| 3 | `OWNER_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `SUP_FOR_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

