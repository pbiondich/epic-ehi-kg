# DOCS_RCVD_DEDUP_LNK

> This table contains the logical link between data elements in the de-duplicated Received Documents (DXR) and the composite DXR record. An example of a data element can be an allergy or a reaction.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LOG_LNK_DDUP_REFIDS` | VARCHAR |  | This item stores the unique reference ID for a deduplicated data element. |
| 4 | `LOG_LNK_CMP_REFIDS` | VARCHAR |  | This item stores the unique reference ID for data in the composite external document record. |
| 5 | `LOG_LNK_DATA_TYPE_C_NAME` | VARCHAR |  | This item stores what type of data the reference IDs correspond to. |
| 6 | `LOG_LNK_COMP_CSN` | NUMERIC |  | The source document Contact Serial Number (CSN) for the corresponding data on the composite external document record. |
| 7 | `LOG_LNK_CODE_SRC_YN` | VARCHAR |  | Signifies whether the Contact Serial Number (CSN) stored in I DXR 7110 should be used for code-lookup for this reference ID. |
| 8 | `LOG_LNK_SRC_ORG_ID` | NUMERIC |  | This item stores the organization this line of data originated from. |
| 9 | `LOG_LNK_SRC_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 10 | `LOG_LNK_RCV_INST_LOCAL_DTTM` | DATETIME (Local) |  | The earliest received instant among source documents contributing to this line. |
| 11 | `LOG_LNK_EARLIEST_SRC_CSN` | NUMERIC |  | The source CSN for the earliest received instant |
| 12 | `PRIM_EXT_DATA_INGESTION_CAT_C_NAME` | VARCHAR |  | The data ingestion category ID for the primary data ingestion category of the composite data element associated with this row. The primary data ingestion category for an element is the category that most heavily contributed to the data element, with the nature of that contribution determined by the primary data ingestion category contribution type (PRIM_INGEST_CAT_CONTRIB_TYP_C). This value is only specified in systems that support control of access to external data by data ingestion category. In systems that support ingestion category-based access, if both this column and the contribution type are null for a row, the implicit ingestion category is 1-Provider Data. |
| 13 | `PRIM_INGEST_CAT_CONTRIB_TYP_C_NAME` | VARCHAR |  | The data ingestion category contribution type category ID of the composite data element associated with this row. This represents the nature of the contribution made by the primary data ingestion category (PRIM_EXT_DATA_INGESTION_CAT_C) to the composite data element. This value is only specified in systems that support control of access to external data by ingestion category. In systems that support ingestion category-based access, if both this column and the primary data ingestion category are null for a row, the implicit contribution type is 1-Sole Data Ingestion Category. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

