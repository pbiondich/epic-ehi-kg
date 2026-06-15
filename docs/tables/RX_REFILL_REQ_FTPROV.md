# RX_REFILL_REQ_FTPROV

> Stores free-text recipients of Refill Authorization Requests. The information contained in each line is detailed below: Line Info 1 Provider Name 2 Provider DEA Number 3 Provider Phone 4 Provider Fax 5 Provider NPI 6 Whether the provider is an E-Prescribing provider 7 Provider Address: House number 8 Provider Address: Street 9 Provider Address: City 10 Provider Address: State 11 Provider Address: Zip 12 Provider Address: District 13 Provider Address: County 14 Provider Address: Country

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `REFILL_REQ_FREETEXT_PROV` | VARCHAR |  | The free-text provider the refill authorization request was sent to. This column is blank if the request was sent to a provider in the database or an In Basket pool. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

