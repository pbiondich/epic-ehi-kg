# DOCS_RCVD_RSLT_TEXTS

> This table stores discrete textual information about results from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `RESULT_TEXT_KEY` | VARCHAR |  | Key for looking up the order for this impression line |
| 6 | `RESULT_TEXT` | VARCHAR |  | Data line for the impression text |
| 7 | `RESULT_TEXT_C_NAME` | VARCHAR |  | Type of result text |
| 8 | `RSLT_TXT_INSTANCE_N` | INTEGER |  | Key when a text blob type occurs more than once in a result. |
| 9 | `PERFORMING_SITE_REF` | VARCHAR |  | This item stores the lab reference ID for a Narrative or an Impression of a result. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

