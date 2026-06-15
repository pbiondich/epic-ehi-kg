# MPPS_NONSEQ_DATA

> This table contains non-sequenced radiation exposure data from modality performed procedure step (MPPS) messages.

**Primary key:** `IMY_ID`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMY_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the modality data record. |
| 2 | `FLUORO_TIME` | NUMERIC |  | Total duration of X-Ray exposure during fluoroscopy in seconds (pedal time) during this Performed Procedure Step. |
| 3 | `NUM_EXPOSURES` | INTEGER |  | Total number of exposures made during this Performed Procedure Step. The number includes non-digital and digital exposures. |
| 4 | `DETECTOR_DISTANCE` | NUMERIC |  | Distance in mm from the source to detector center. |
| 5 | `ENTRANCE_DISTANCE` | NUMERIC |  | Distance in mm from the source to the surface of the patient closest to the source during this Performed Procedure Step. |
| 6 | `DAP_TOTAL` | NUMERIC |  | Total area-dose-product to which the patient was exposed, accumulated over the complete Performed Procedure Step and measured in dGy*cm*cm, including fluoroscopy. |
| 7 | `SUMMARY_COMMENTS` | VARCHAR |  | User-defined comments on any special conditions related to radiation dose encountered during this Performed Procedure Step. |
| 8 | `ENTRANCE_DOSE_MGY` | NUMERIC |  | Average entrance dose value measured in mGy at the surface of the patient during this Performed Procedure Step. |
| 9 | `TOTAL_DLP` | NUMERIC |  | Total dose length product (DLP) for the Performed Procedure Step. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

