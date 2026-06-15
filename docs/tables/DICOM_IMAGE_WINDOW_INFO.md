# DICOM_IMAGE_WINDOW_INFO

> This table contains the image's window width and center settings.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `WINDOW_CENTER` | INTEGER |  | This column specifies the window center presets for this image (attribute 0028,1050). |
| 4 | `WINDOW_WIDTH` | INTEGER |  | This column specifies the window width presets for this image (attribute 0028,1051). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

