# DOCS_RCVD_RR_DATA

> This table contains some of the relevant information that is contained in the Reportability Response CDA that is sent as a response to an electronic case report. It columns included this table are whether the case is reportable, the SNOMED code of the case, and the timeframe in which to report.

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
| 5 | `DTRMN_OF_RPT_C_NAME` | VARCHAR |  | Whether or not the case report was determined to be reportable |
| 6 | `REPORTABLE_CONDITION` | VARCHAR |  | The SNOMED code of the condition that the case report was about |
| 7 | `REPORTING_TIMEFRAME` | INTEGER |  | The number of hours from when the Reportability Response was received before which reporting is required. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

