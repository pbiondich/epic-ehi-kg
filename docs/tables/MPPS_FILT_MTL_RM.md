# MPPS_FILT_MTL_RM

> This table extracts the filter material information from the sequenced Modality Performed Procedure Step (MPPS) data.

**Primary key:** `IMY_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMY_ID` | NUMERIC | PK shared | The unique identifier for the modality data record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the filter material information from the sequenced MPPS data associated with this DICOM instance. Together with IMY_ID, this forms the foreign key to the MPPS_EXPO_DOSE_SEQ table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple filter material values associated with the DICOM instance and item from the MPPS_EXPO_DOSE_SEQ table. |
| 4 | `FILTER_MATERIAL` | VARCHAR |  | The x-ray absorbing material used in the filter. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

