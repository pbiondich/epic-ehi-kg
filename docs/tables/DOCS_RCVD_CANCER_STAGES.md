# DOCS_RCVD_CANCER_STAGES

> This table stores cancer stages received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `HISTOPATHOLOGIC_TYPE_C_NAME` | VARCHAR | org | This column stores the histopathologic type associated with the cancer stage. |
| 5 | `HISTOPATHOLOGIC_TYPE_NAME` | VARCHAR |  | This column stores the name of the histopathologic type associated with the cancer stage. |
| 6 | `CANCER_TYPE_NAME` | VARCHAR |  | This column stores the name of the cancer site or type associated with the cancer stage. |
| 7 | `STAGE_SNGL_SRC_ORG_ID` | NUMERIC |  | Source organization for cancer stages with a single source. |
| 8 | `STAGE_SNGL_SRC_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

