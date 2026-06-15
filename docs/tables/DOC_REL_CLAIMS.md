# DOC_REL_CLAIMS

> This table contains claim (CLM) IDs associated with a document (DCS). For example, if a document is a Periodic Explanation of Benefits, the claims in the Periodic Explanation of Benefits will be stored in this table.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DOC_REL_CLM_ID` | NUMERIC |  | Stores the Claim IDs related to the document |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

