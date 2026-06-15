# DOCS_RCVD_PLL_DATA

> This table contains the information about the PLL info received from SFM query.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `PLL_COMMENTS` | VARCHAR |  | This item stores multidose level comment of PLL information. |
| 6 | `PLL_ORDER_DEADLINE_UTC_DTTM` | DATETIME (UTC) |  | This item stores the order deadline instant. |
| 7 | `PLL_FIRST_DOSE_DATE` | DATETIME |  | This item stores the first dosing date for the multidose package. |
| 8 | `PLL_LAST_DOSE_DATE` | DATETIME |  | This item stores the last dosing date in the multidose package. |
| 9 | `PLL_TYPE_C_NAME` | VARCHAR |  | This item stores the multidose package type. |
| 10 | `PLL_DATE_INST_UTC_DTTM` | DATETIME (UTC) |  | This item stores the multidose package info update instant. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

