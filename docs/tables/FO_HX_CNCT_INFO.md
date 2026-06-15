# FO_HX_CNCT_INFO

> This table stores the contact information for each filing order history record.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the Filing Order History record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The contact serial number (CSN) of the contact. |
| 5 | `CONTACT_NUM` | INTEGER |  | Stores contact number |
| 6 | `INSTANT_OF_ENTRY_DTTM` | DATETIME (Attached) |  | Stores the instant of entry when a record is edited |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

