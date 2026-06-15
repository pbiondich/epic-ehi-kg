# DOCS_RCVD_ENDO_PROC_INFO

> Contains information about endoscopy procedures extracted from customer systems for use in Cosmos.

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
| 5 | `ENDO_PROC_REF_IDENT` | VARCHAR |  | This item stores the unique reference id associated with the endoscopy procedure. |
| 6 | `ENDO_PROC_ENC` | NUMERIC |  | This item stores the procedures encounter as a link to an EPT CSN. |
| 7 | `ENDO_PROC_SOURCE_ORG_ID` | NUMERIC |  | This item contains the ID of the source organization of the record. |
| 8 | `ENDO_PROC_SOURCE_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 9 | `ENDO_PROC_INST_DTTM` | DATETIME (Attached) |  | Stores the finalizing instant of the procedure in the local timezone. |
| 10 | `ENDO_PROC_BPA_YN` | VARCHAR |  | Stores the bowel prep adequacy metric for colonoscopy procedures. |
| 11 | `ENDO_PROC_CR_YN` | VARCHAR |  | Stores the cecum reached metric for colonoscopy procedures. |
| 12 | `ENDO_PROC_POLYP_YN` | VARCHAR |  | Stores the poylp detected metric for colonoscopy procedures. |
| 13 | `ENDO_PROC_CWT` | NUMERIC |  | Stores the cecal withdrawal time for colonoscopy procedures. |
| 14 | `ENDO_PROC_ADR_YN` | VARCHAR |  | Stores the adenoma detection metric for colonoscopy procedures. |
| 15 | `ENDO_PROC_SCR_COL_YN` | VARCHAR |  | Stores whether or not the colonoscopy procedure was a screening. |
| 16 | `ENDO_PROC_TYPE_C_NAME` | VARCHAR |  | Stores the procedure type category value. |
| 17 | `ENDO_PROC_FND_YN` | VARCHAR |  | Stores whether or not the procedure includes discrete findings data. |
| 18 | `ENDO_PROC_ENC_DEDUP` | VARCHAR |  | This item stores the procedures encounter deduplicated reference ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

