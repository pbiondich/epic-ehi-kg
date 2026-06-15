# DOCS_RCVD_GEN_IND_REL_ORD

> Stores the orders linked to a genomic indicator.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `REL_PGI_REF_ID` | VARCHAR |  | Stores the reference ID of the patient genomic indicator. |
| 6 | `PGI_REL_ORD_REF_ID` | VARCHAR |  | Reference ID of the order linked to the patient genomic indicator. |
| 7 | `PGI_REL_COMP_REF_ID` | VARCHAR |  | Stores the reference ID to the related component. |
| 8 | `PGI_REL_VAR_STR` | VARCHAR |  | Stores the variant formatted as a string for display. |
| 9 | `PGI_REL_VAR_REF_ID` | VARCHAR |  | Stores the reference ID of the variant linked to the patient genomic indicator. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

