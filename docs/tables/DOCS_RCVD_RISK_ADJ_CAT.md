# DOCS_RCVD_RISK_ADJ_CAT

> This table stores risk adjustment categories received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `RAD_REF_IDENT` | VARCHAR |  | The unique reference identifier associated with the risk adjustment category. |
| 6 | `RAD_CALC_DATE` | DATETIME |  | The date of the last time the external system generated the report for the risk adjustment category. |
| 7 | `RAD_START_DATE` | DATETIME |  | The start date of the clinical evaluation period during which the risk adjustment category is documented. |
| 8 | `RAD_END_DATE` | DATETIME |  | The end date of the clinical evaluation period during which the risk adjustment category is documented. |
| 9 | `RAD_CAT_NAME` | VARCHAR |  | The name of the risk adjustment category representing the risk adjustment data. |
| 10 | `RAD_DESCRIPTOR` | VARCHAR |  | The descriptor of the risk adjustment data, which includes the model abbreviation, version abbreviation, and the category identifier. |
| 11 | `RAD_STATUS_C_NAME` | VARCHAR |  | The status of the risk adjustment category to indicate if this category is historic or suspected. |
| 12 | `RAD_EVIDENCE_NOTE_ID` | VARCHAR |  | A note (HNO) about the evidence for the risk adjustment category. |
| 13 | `RAD_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 14 | `RAD_EXT_DATA_FILTER_REASON_C_NAME` | VARCHAR |  | Stores the reason why an external risk adjustment category should be filtered from the composite record. |
| 15 | `RAD_SRC_DOCUMENT_CSN_ID` | NUMERIC |  | The contact serial number of the DXR record that owns the instance of this risk adjustment category. |
| 16 | `RAD_BULK_STAT_C_NAME` | VARCHAR |  | The status of this risk adjustment data element within DINE. |
| 17 | `RAD_LAST_UPD_UTC_DTTM` | DATETIME (UTC) |  | This item stores the date and time when the risk adjustment data was last updated by the external system. |
| 18 | `RAD_CODING_STATUS_C_NAME` | NUMERIC |  | The coding status of the risk adjustment category to indicate if this category is open or closed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

