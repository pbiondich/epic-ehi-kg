# DOCS_RCVD_EPSD_PROVS_CMPL

> The compiled list of providers for an external episode.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EPSD_PROV_KEY_CMPL` | VARCHAR |  | Key value to link the provider to the episode. This points to the episode identifier (I DXR 28510).This data is from the most recent contact in I DXR 8600. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

