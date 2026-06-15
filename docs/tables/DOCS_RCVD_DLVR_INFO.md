# DOCS_RCVD_DLVR_INFO

> This table contains delivery information in the SFM query.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `DLVR_RSPTID` | VARCHAR |  | This item stores the resptid of the prescription included in the delivery package. |
| 6 | `DLVR_DISPID` | VARCHAR |  | This item stores the dispense id of the prescription in the eMultidose package. |
| 7 | `DLVR_REPACK_C_NAME` | VARCHAR |  | This item stores the repack info for the prescription in the eMultidose package. |
| 8 | `DLVR_FIRST_DATE` | DATETIME |  | This item stores the first dosing date of the prescription in the eMultidose package. |
| 9 | `DLVR_LAST_DATE` | DATETIME |  | This item stores the last dosing date of the prescription in the eMultidose package. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

