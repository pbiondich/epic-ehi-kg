# DOC_EPSD_LIST_INFO_CMPL

> Episodes received from external documents.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EPSD_NAME_CMPL` | VARCHAR |  | The name of this row's received episode. This data is from the most recent contact of this episode in its received document. |
| 4 | `EPSD_CMPL_CMGMT_PROG_CAT_C_NAME` | VARCHAR |  | This item stores the program category value, which defines the type of program supported by a Compass Rose episode type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

