# DOC_REL_MEMBERS

> This table contains patient (EPT) IDs associated with a document (DCS). For example, if a document is scanned for a referral, the patient on the referral will be stored in this table.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique ID for this document. |
| 2 | `LINE` | INTEGER | PK | The line number for the member associated with this document. Multiple members can be associated with a single document. |
| 3 | `DOC_REL_MEM_ID` | VARCHAR |  | The patient (EPT) ID related to the scan. For example, if a document (DCS) is attached to a referral, this is the patient associated with the referral. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

