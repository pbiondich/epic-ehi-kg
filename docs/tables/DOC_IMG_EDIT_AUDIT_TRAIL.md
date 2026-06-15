# DOC_IMG_EDIT_AUDIT_TRAIL

> Contains the audit trail for image editing.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IMAGE_EDIT_INST_DTTM` | DATETIME (UTC) |  | The instant of the image edit. |
| 4 | `IMAGE_EDIT_USER_ID` | VARCHAR |  | The user who edited the image. |
| 5 | `IMAGE_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `IMAGE_EDIT_COMMENT` | VARCHAR |  | The comment associated with the image edit. |
| 7 | `IMAGE_EDIT_PREV_BLOB_KEY` | VARCHAR |  | The previous BLOB key that holds the image prior to the edit. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

