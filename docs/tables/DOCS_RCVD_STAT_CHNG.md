# DOCS_RCVD_STAT_CHNG

> Status change notes.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `STAT_CHNG_USER_ID` | VARCHAR |  | The unique ID associated with the user who changed the status of this document to Pend. This column is frequently used to link to the CLARITY_EMP table. |
| 6 | `STAT_CHNG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `STAT_CHNG_INST_DTTM` | DATETIME (UTC) |  | The instant of the document status change event. |
| 8 | `STAT_CHNG_HNO_ID` | VARCHAR |  | The record ID of the Clinical Note used to store notes entered by the user during a document status change event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

