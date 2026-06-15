# ORDER_EXCLUDE_FROM_CDS

> This table reports items that indicate an order should be excluded from decision support.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `EXCLUDE_FROM_CDS_REASON_C_NAME` | VARCHAR |  | The exclude from decision support reason category ID for an order record. 1 indicates an order that was not successfully completed. 2 indicates that the order's result information was documented on the wrong patient. |
| 6 | `EXCLUDE_FROM_CDS_SOURCE_C_NAME` | VARCHAR |  | The source of the Exclude From Decision Support reason for the order. |
| 7 | `EXCLUDE_FROM_CDS_UTC_DTTM` | DATETIME (UTC) |  | The date and time in UTC when an order record was excluded from decision support. |
| 8 | `EXCLUDE_FROM_CDS_USER_ID` | VARCHAR |  | The unique ID of the user associated with the change to the Exclude From Decision Support reason for the order. |
| 9 | `EXCLUDE_FROM_CDS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `EXCLUDE_FROM_CDS_DTTM` | DATETIME (Local) |  | The date and time when an order record was excluded from decision support. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

