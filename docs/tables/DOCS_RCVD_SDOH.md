# DOCS_RCVD_SDOH

> Contains discrete external social driver of health information from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `SDOH_IDENTIFIER` | VARCHAR |  | This item stores the unique reference ID of a discrete social driver of health documentation. |
| 6 | `SDOH_ENTRY_DATE` | DATETIME |  | This item stores the date a social driver of health was documented for the patient. |
| 7 | `SDOH_CONCERN_LEVEL_C_NAME` | VARCHAR |  | This item stores the Epic-standard concern level for a social driver entry. |
| 8 | `SDOH_INTERPRETATION` | VARCHAR |  | This item stores the free text description of the concern for a social driver entry. |
| 9 | `SDOH_NAME` | VARCHAR |  | This item stores the name of a social driver entry. |
| 10 | `SDOH_DOM_CONFIG_ID_RECORD_NAME` | VARCHAR |  | The name of the social driver domain configuration record. |
| 11 | `SDOH_ASMNT_IDENTIFIER` | VARCHAR |  | This item stores the reference ID of the assessment this social driver entry was created from. |
| 12 | `SDOH_EVENT_IDENT` | VARCHAR |  | This item stores the ID of the event that is associated with an SDOH entry. In cases where there are multiple encounters that link to an SDOH entry, the earliest encounter is represented here. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

