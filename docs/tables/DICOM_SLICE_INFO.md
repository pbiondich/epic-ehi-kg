# DICOM_SLICE_INFO

> This table contains metadata information for cross sectional images.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INSTANCE_UID` | VARCHAR |  | This is the DICOM image instance UID (attribute 0008,0018) for a cross-sectional image. A cross-sectional image is also known as a slice. |
| 4 | `INSTANCE_NUM` | INTEGER |  | This is the instance number (attribute 0020,0013) for a cross-sectional image. A cross-sectional image is also known as a slice. |
| 5 | `SLICE_WINDOW_WIDTH` | INTEGER |  | Instance (slice) specific window width setting. |
| 6 | `SLICE_WINDOW_CENTER` | INTEGER |  | Slice specific window center setting. |
| 7 | `SLICE_PS_SERIES_UID` | VARCHAR |  | The presentation state series UID for this cross sectional image. |
| 8 | `SLICE_PS_INST_UID` | VARCHAR |  | The presentation state instance UID for this cross sectional image. |
| 9 | `IMG_SLCT_TYPE_C_NAME` | VARCHAR |  | The category ID indicating how the slice associated with the record was selected, including if it was computer selected or marked as a key image. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

