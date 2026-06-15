# LCA_PDF_DOC_INFO

> This table stores the DCS IDs of generated PDFs.

**Primary key:** `COMMUNICATION_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMMUNICATION_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the routing record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LCA_PDF_DOC_INFO_ID` | VARCHAR |  | This item stores the Document (DCS) IDs of the PDFs generated from an LCA-based patient level communication. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

