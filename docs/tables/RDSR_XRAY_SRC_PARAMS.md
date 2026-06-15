# RDSR_XRAY_SRC_PARAMS

> Each irradiation event received in a Radiation Dose Structured Reporting (RDSR) message can itself have multiple x-ray sources associated with it. Each row in this table will describe one such x-ray source.

**Primary key:** `IMY_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMY_ID` | NUMERIC | PK shared | The unique identifier of the service-object pair (a particular kind of DICOM message) record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RDSR_ASSOC_IRR_EVNT` | INTEGER |  | The line number of the associated irradiation event. |
| 4 | `RDSR_XRAY_SOURCE` | VARCHAR |  | The X-ray source. |
| 5 | `RDSR_KVP` | NUMERIC |  | The peak kilovoltage (kVp). |
| 6 | `RDSR_MAX_TUBE_CUR` | NUMERIC |  | The maximum X-ray tube current. |
| 7 | `RDSR_TUBE_CUR` | NUMERIC |  | The X-ray tube current. |
| 8 | `RDSR_EXPOSURE_TM` | NUMERIC |  | The exposure time per rotation. |
| 9 | `RDSR_XRAY_FLTR_ALUM` | NUMERIC |  | The X-ray filter aluminum equivalent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

