# DOCS_RCVD_GENOMIC_IND

> This table stores the patient genomic indicators received from external sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `PGI_REF_ID` | VARCHAR |  | The unique reference identifier associated with the PGI. |
| 6 | `PGI_TYPE_C_NAME` | VARCHAR |  | The type of Genomic Indicator. |
| 7 | `PGI_NAME` | VARCHAR |  | The name of the Genomic Indicator. |
| 8 | `PGI_ADDED_DATE` | DATETIME |  | Date the Genomic Indicator was added to the patient. |
| 9 | `PGI_DESC_ID` | VARCHAR |  | Stores the description of the genomic indicator. |
| 10 | `PGI_SHRD_WITH_PAT_YN` | VARCHAR |  | True if the Genomic Indicator has been shared with the patient. |
| 11 | `PGI_OVERVIEW_NOTE_ID` | VARCHAR |  | The overview note associated with the patient genomic indicator. |
| 12 | `PGI_CHECKSUM` | INTEGER |  | The checksum of the patient genomic indicator. |
| 13 | `PGI_LAST_UPD_INST_DTTM` | DATETIME (UTC) |  | Stores the last time the patient genomic indicator has been updated. |
| 14 | `PGI_SRC_DXR_CSN` | NUMERIC |  | The contact serial number of the DXR record that owns the instance of this patient genomic indicator. |
| 15 | `PGI_VISIBLE_TO_ALL_YN` | VARCHAR |  | This item stores if the patient genomic indicator can be viewed by all users. If set to No only users with Genomics View All security can view this inidcator. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

