# IMG_ANNOT_AUDTRAIL

> This displays items for the audit trail of changes to the annotations done to an image.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique ID of the document record. |
| 2 | `LINE` | INTEGER | PK | The Line Count for the IMG per Document - The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IMAGE_ANNOTATION_X` | INTEGER |  | Contains X coordinate of the annotation |
| 4 | `IMAGE_ANNOTATION_Y` | INTEGER |  | Contains the Y coordinate of the annotation |
| 5 | `IMAGE_ANN_TEXT` | VARCHAR |  | This items contains the text of the annotation |
| 6 | `IMAGE_ANN_COMPON_ID` | NUMERIC |  | This item contains the link to measurement component data that is saved to the image as an annotation. |
| 7 | `IMAGE_ANN_COMPON_ID_NAME` | VARCHAR |  | The name of the component. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

