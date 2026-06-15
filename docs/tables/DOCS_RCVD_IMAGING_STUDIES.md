# DOCS_RCVD_IMAGING_STUDIES

> This table contains metadata about imaging studies retrieved from external sources. Each row represents a discrete imaging study received in this document.

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
| 5 | `STUDY_RESOURCE_IDENT` | VARCHAR |  | The logical ID of the FHIR ImagingStudy resource. |
| 6 | `STUDY_LOCAL_UNIQUE_IDENT` | VARCHAR |  | The locally-assigned unique identifier for the imaging study. |
| 7 | `DICOM_MANIFEST_CSN_ID` | NUMERIC |  | The DICOM Manifest contact corresponding to this ImagingStudy resource. |
| 8 | `STUDY_REMOVED_YN` | VARCHAR |  | Whether the ImagingStudy is no longer in the received imaging list. Default is 0-No. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

