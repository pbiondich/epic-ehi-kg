# CONSENT_LNK_ETX

> The CONSENT_LNK_ETX table contains information about content selections applied to surgical and non-surgical consent documents.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ASSOCIATED_SMARTTEXT_ID` | VARCHAR |  | This column stores the ETX content selected for a DCS record. |
| 4 | `ASSOCIATED_SMARTTEXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

