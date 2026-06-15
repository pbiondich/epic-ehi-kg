# DOCS_RCVD_PCCNOTE

> This table stores discrete information for patient care coordination notes received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `PCCNOTE_REF_ID` | VARCHAR |  | This item stores the unique reference identifier associated with the care coordination note. |
| 6 | `PCCNOTE_SIGNED_INST_DTTM` | DATETIME (Local) |  | This item stores the instant when the patient care coordination note was signed. |
| 7 | `PCCNOTE_AUTHOR` | VARCHAR |  | This item stores the author's name of the patient care coordination note. |
| 8 | `PCCNOTE_ID` | VARCHAR |  | This item stores the identifier of the Notes (HNO) record that stores the patient care coordination note. |
| 9 | `PCCNOTE_SRC_CSN` | NUMERIC |  | This item stores the contact serial number (CSN) of the Document Received record that owns the instance of this patient care coordination note. |
| 10 | `PCC_LST_UPD_INST_DTTM` | DATETIME (UTC) |  | Stores the last update instant of a Patient Care Coordination note in UTC. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

