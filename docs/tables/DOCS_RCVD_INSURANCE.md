# DOCS_RCVD_INSURANCE

> Externally received insurance information.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `INSURANCE_REFERENCE_ID` | VARCHAR |  | Externally received insurance reference ID. |
| 6 | `INSURANCE_SOURCE_OF_PAY_C_NAME` | VARCHAR |  | Stores the financial source of payment for this coverage. |
| 7 | `INSURANCE_DO_NOT_BILL_YN` | VARCHAR |  | Stores whether or not this insurance indicates "Do not bill insurance". |
| 8 | `INSURANCE_CHECKSUM` | INTEGER |  | This column stores the checksum of the externally received insurance information. |
| 9 | `INSURANCE_SOURCE_CSN` | NUMERIC |  | Stores a contact serial number (CSN) pointer to the Document Exchange record where externally received insurance information originated. |
| 10 | `INSURANCE_REF_FIN_CLASS_C_NAME` | VARCHAR |  | Customer mapped reference financial class that coverage is under |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

