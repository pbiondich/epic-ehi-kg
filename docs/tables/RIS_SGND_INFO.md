# RIS_SGND_INFO

> This table contains the physicians/radiologists that signed off on an imaging order and dates/times that the study was signed.

**Primary key:** `ORDER_PROC_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SIGNED_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `SIGNED_DATE` | DATETIME |  | The date when the study is signed by the radiologist. |
| 5 | `SIGNED_TM` | DATETIME (Local) |  | The date & time that the study was signed by the radiologist. |
| 6 | `SIGNED_UTC_DTTM` | DATETIME (UTC) |  | The date and time that an imaging order is signed by a physician/radiologist, and is stored in the Universal Time Coordinated (UTC) format. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

