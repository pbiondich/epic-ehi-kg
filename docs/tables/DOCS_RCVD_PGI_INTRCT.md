# DOCS_RCVD_PGI_INTRCT

> This table contains information about drug interactions on genomic indicators on received documents.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `PGI_REF_ID` | VARCHAR |  | The reference ID associated with the patient genomic indicator (PGI) that has interactions. This value can be used to link rows of this table with rows DOCS_RCVD_GENOMIC_IND using PGI_REF_ID. |
| 6 | `INTRCT_SEVERITY_C_NAME` | VARCHAR |  | The severity level of the patient genomic indicator pharmacogenomic interaction. |
| 7 | `INTRCT_TITLE` | VARCHAR |  | The title of the patient genomic indicator pharmacogenomics interaction. |
| 8 | `INTRCT_PROV_DESC_NOTE_ID` | VARCHAR |  | The patient genomic indicator's interaction provider facing description. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

