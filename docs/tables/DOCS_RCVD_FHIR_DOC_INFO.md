# DOCS_RCVD_FHIR_DOC_INFO

> This table stores metadata about FHIR resources received from outside sources.

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
| 5 | `FHIR_DOCUMENT_RESOURCE_TYPE_C_NAME` | VARCHAR |  | The resource type category ID for this FHIR resource |
| 6 | `FHIR_DOCUMENT_RESOURCE_IDENT` | VARCHAR |  | The resource ID for this FHIR resource received from the source organization |
| 7 | `FHIR_DOCUMENT_FILE_NAME` | VARCHAR |  | The file name for this FHIR resource on the BLOB server |
| 8 | `FHIR_DOCUMENT_SUB_RESOURCE_C_NAME` | VARCHAR |  | The sub resource type for this FHIR resource |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

