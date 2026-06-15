# DOCS_RCVD_MEDS_3

> This table stores medications received from outside sources.

**Overflow of:** [DOCS_RCVD_MEDS](DOCS_RCVD_MEDS.md)  
**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `MED_FREQ_IS_PRN_YN` | VARCHAR |  | Whether a medication frequency is "as needed". This data is currently populated only in ambient recording workflows. |
| 6 | `MED_FREQ_TIME_UNIT` | VARCHAR |  | This item stores the time unit associated with a medication's frequency. This data is currently populated only in ambient recording workflows, where it should be a UCUM unit. |
| 7 | `MED_FREQ_TIME_QTY` | INTEGER |  | Time quantity for a medication frequency. For example, for a frequency of "twice per eight hours", this value would be 8. This data is currently populated only in ambient recording workflows. |
| 8 | `MED_FREQ_PER_INTER` | INTEGER |  | Number of times per interval for a medication frequency. For example, for a frequency of "twice per eight hours", this value would be 2. This data is currently populated only in ambient recording workflows. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

