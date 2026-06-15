# DOCS_RCVD_RSLTS_ADDENDUM

> This table stores discrete result addendum information received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `RSLT_ADDEND_REFID` | VARCHAR |  | This item stores the reference ID of the result that this addendum belongs to. |
| 6 | `RSLT_ADDEND_NOTE_ID` | VARCHAR |  | This item stores the ID of the note record (HNO) that contains the text of the addendum. |
| 7 | `RSLT_ADDEND_INS_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant when this addendum is documented. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

