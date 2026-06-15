# FILING_ORDER_HX_TERM_DATE

> This table extracts the related multiple response Effective Date To (I FOH 410) item. Each row of this table corresponds to one member term date on one coverage on one filing order effective date on one contact of one member's filing order history record. This should be joined with the FILING_ORDER_HX table on the record ID, to the record ID, contact date real to contact date real and group line to line. To get the full member effective range do an outer join (to include ranges without a term date) from FILING_ORDER_HX_EFF_DATE on the record ID, contact date real, group line and value line.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the filing order history record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this contact. |
| 4 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple term dates. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `TERM_DATE` | DATETIME |  | Stores the "effective date to" for the member on the coverage. "Member Level Effective Date" (I CVG 330) is stored if present, otherwise "Coverage Effective To Date" (I CVG 410) is used. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

