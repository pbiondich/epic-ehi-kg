# CONSENT_LINKED_SURG_PROCS

> Contains data pertaining to the surgical procedures the consent document covers.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONSENT_PROC_ID` | VARCHAR |  | The procedures attached to consent from the case, networked to the procedures list (ORP). |
| 4 | `CONSENT_PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 5 | `CONSENT_PROC_LATERALITY_LRB_C_NAME` | VARCHAR | org | The procedure lateralities attached to consent from the case. |
| 6 | `CONSENT_PROC_DESCRIPTION` | VARCHAR |  | The procedure descriptions attached to consent from the case. |
| 7 | `CONSENT_PROC_CASE_ID` | VARCHAR |  | The surgical case that the surgical procedure linked to this consent is on. |
| 8 | `CONSENT_PROC_PANEL` | INTEGER |  | The panel to which this procedure on consent belongs. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

