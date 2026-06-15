# MANUAL_LINK_ATTACH_ENCS

> This table contains rows for each attachment encounter record that a claim coding record is manually linked to.

**Primary key:** `CODING_RECORD_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CODING_RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the coding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ATTACHMENT_DOCUMENT_ID` | VARCHAR |  | Attachment encounters the claim has been manually linked to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

