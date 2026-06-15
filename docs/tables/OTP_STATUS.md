# OTP_STATUS

> This table contains overtime single response order template information.

**Primary key:** `OTP_ID`, `CONTACT_DATE_REAL`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the patient order template record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CONTACT_NUM` | VARCHAR |  | The contact number of the OTP record. |
| 5 | `INSTANT_OF_ENTRY_DTTM` | DATETIME (Local) |  | The instant data was entered. |
| 6 | `INSTANT_OF_EDIT_DTTM` | DATETIME (Local) |  | The instant data was edited. |
| 7 | `ITEMS_EDITED` | VARCHAR |  | The item edited in the record |
| 8 | `DATA_ENTRY_PERSON` | VARCHAR |  | The user who created/edited this contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

