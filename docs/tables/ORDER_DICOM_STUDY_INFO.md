# ORDER_DICOM_STUDY_INFO

> This tables contains the DICOM study information.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STUDY_UID` | VARCHAR |  | The UID of the study in DICOM. |
| 4 | `SERIES_UID` | VARCHAR |  | The UID of the series in DICOM. |
| 5 | `IMAGE_UID` | VARCHAR |  | The UID of the image in DICOM. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

