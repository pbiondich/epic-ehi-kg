# IMAGE_DRAW_AUDIT_TRAIL

> Contains the drawing data for an image.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IMAGE_DRAWING_LINE_NUM` | INTEGER |  | Contains the line number for image drawing data. |
| 4 | `IMAGE_DRAWING_DATA` | VARCHAR |  | Contains the drawing data for an image. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

