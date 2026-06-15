# DOC_EXTERNAL_INFO

> This contains information related to external information associated with this document.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique identifier for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DOC_MAP_DATA_TYPE_C_NAME` | VARCHAR |  | If the document contains data received for the patient's chart, this column stores the type of data referenced in a received document record. |
| 4 | `DOC_MAP_DATA_REF_ID` | VARCHAR |  | If the document contains data received for the patient's chart, this column stores the reference ID for a particular piece of information about the data stored in a received document record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

