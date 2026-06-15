# DOCS_RCVD_EVENT_PROVS

> The providers for an external event.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `EVENT_PROV_KEY` | VARCHAR |  | Key value to link the provider to the event |
| 6 | `EVENT_PROV_TYPE_C_NAME` | VARCHAR | org | Type of the event provider |
| 7 | `EVENT_PROV_EFFECT_DTTM` | DATETIME (Local) |  | The start or effective date of the event provider. |
| 8 | `EVENT_PROV_TERM_DTTM` | DATETIME (Local) |  | The end or termination date of the event provider. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

