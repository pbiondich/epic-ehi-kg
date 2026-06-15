# DOCUMENT_STAMPS

> This table contains information about stamps added to scanned documents.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STAMP_TEXT` | VARCHAR |  | Contains stamps that have been added to this document. |
| 4 | `STAMP_TYPE_C_NAME` | VARCHAR | org | Contains types of stamps that have been added to this document. |
| 5 | `STAMP_ADD_USER_ID` | VARCHAR |  | The user who added a stamp to the document. |
| 6 | `STAMP_ADD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `STAMP_ADDED_UTC_DTTM` | DATETIME (UTC) |  | The instant a stamp was added to the document. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

