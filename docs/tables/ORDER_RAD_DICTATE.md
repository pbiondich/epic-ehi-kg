# ORDER_RAD_DICTATE

> This table stores the dictation radiologist & dictating date information for orders performed in radiology.

**Primary key:** `ORDER_PROC_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line count for this table as determined by the number of dictating radiologists for an order. |
| 3 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `DICTATING_DT` | DATETIME |  | The date that the radiologist sent the dictation to the transcriptionist. |
| 5 | `DICTATED_UTC_DTTM` | DATETIME (UTC) |  | This item captures the date and time in the Universal Time Coordinated (UTC) format that the provider listed in the Dictated Physicians (I ORD 52205) item dictated the study. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

