# DOCS_RCVD_DEDUP_LNK_INGST

> This table stores data ingestion category-specific information about the composite data element associated with a row in DOCS_RCVD_DEDUP_LNK. The table only stores data for composite data elements with multiple associated data ingestion categories.

**Primary key:** `DOCUMENT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the link between a composite and deduplicated data element in a deduplicated DXR record. Together with DOCUMENT_ID, this forms the foreign key to the DOCS_RCVD_DEDUP_LNK table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple data ingestion categories associated with a link between a composite and deduplicated data element in a deduplicated DXR record from the DOCS_RCVD_DEDUP_LNK table. |
| 4 | `EXT_DATA_INGESTION_CAT_C` | INTEGER |  | The data ingestion category ID of the specific data ingestion category associated with a composite data element. |
| 5 | `PREF_SRC_DOCUMENT_CSN_ID` | NUMERIC |  | The unique contact serial number of the received document (DXR) contact that is the preferred source contact associated with this data ingestion category for a composite data element. |
| 6 | `EARLIEST_SRC_DOCUMENT_CSN_ID` | NUMERIC |  | The unique contact serial number of the received document (DXR) contact that is the earliest received source contact associated with this data ingestion category for a composite data element. |
| 7 | `EARLIEST_RCV_INST_LOCAL_DTTM` | DATETIME (Local) |  | The document received date and time for the earliest received source document (DXR) contact associated with this data ingestion category for a composite data element. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

