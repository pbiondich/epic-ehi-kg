# DOCS_RCVD_INGESTION_CATS

> This table contains the data ingestion categories associated with a received document.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ASSOC_DATA_INGESTION_CAT_C_NAME` | VARCHAR |  | Identifiers for the data ingestion categories associated with this record. This item, in combination with other system configuration, is used to control user and automated workflow access to this document and discrete data compiled from it. DXR records on provider systems are expected to have at least one data ingestion category populated, if data ingestion category filing is enabled. Historical records may have neither populated. Those records are associated with the Provider Data ingestion category. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

