# DOCS_RCVD_RSLT_SENS

> This table contains result sensitivity information.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `RESULT_SENS_KEY` | INTEGER |  | Key for looking up the order for this sensitivity in the DOCS_RCVD_RSLTS table |
| 5 | `RESULT_SENS_ORGANISM_NAM` | VARCHAR |  | Free text name of the sensitivity organism |
| 6 | `RESULT_SENS_ORGANISM_ID` | NUMERIC |  | The unique ID of the Organism for the received document result sensitivity. |
| 7 | `RESULT_SENS_ORGANISM_ID_NAME` | VARCHAR |  | The name of the organism. |
| 8 | `RESULT_SENS_ANTIBIOTIC_NAM` | VARCHAR |  | Free text name of the antibiotic used |
| 9 | `RESULT_SENS_ANTIBIOTIC_C_NAME` | VARCHAR | org | The antibiotic category ID for the received document result sensitivity. |
| 10 | `RESULT_SENS_SUSCEPT_NAM` | VARCHAR |  | Free text name of the susceptibility result |
| 11 | `RESULT_SENS_SUSCEPT_C_NAME` | VARCHAR | org | The susceptibility category ID of the organism to the given antibiotic for the received document result sensitivity. |
| 12 | `RESULT_SENS_COMMENT` | VARCHAR |  | Free text comment for this sensitivity |
| 13 | `RESULT_SENS_MTHD_NAM` | VARCHAR |  | Free text name of the method used to perform the susceptibility |
| 14 | `RESULT_SENS_MTHD_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

