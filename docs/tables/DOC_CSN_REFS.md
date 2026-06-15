# DOC_CSN_REFS

> This table contains references to the document from patient contacts, by contact serial number. It is populated by the Consents navigator section.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique identifier for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CSN_REFERENCE` | NUMERIC |  | This item contains the patient contacts (by contact serial number) that reference this document. A reference here does not imply the document was created during any of these contacts and is different from the encounter storage level for documents (provided by I DCS 280); it is simply an indicator of relevance. If this item is populated, a document should not be allowed to move between patients. The user must remove all of these references manually before a patient change can occur. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

