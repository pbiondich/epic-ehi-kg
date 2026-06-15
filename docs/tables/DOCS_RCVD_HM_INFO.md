# DOCS_RCVD_HM_INFO

> This table stores discrete Health Maintenance information received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `HM_NAME` | VARCHAR |  | This item stores the name of the Health Maintenance topic. |
| 6 | `HM_DUE_DATE` | DATETIME |  | This item stores the due date of the Health Maintenance topic. |
| 7 | `HM_SRC_CSN` | NUMERIC |  | This item stores the Contact Serial Number (CSN) of the source external document record that owns the instance of this Health Maintenance topic. |
| 8 | `HM_LAST_COMP_DT` | DATETIME |  | This item stores the last completion date of the Health Maintenance topic. |
| 9 | `HM_REFERENCE_IDENT` | VARCHAR |  | This item stores the unique reference identifier associated with the Health Maintenance topic. |
| 10 | `HM_COMMENT` | VARCHAR |  | This item stores the comment of the Health Maintenance topic. |
| 11 | `HM_ID` | NUMERIC |  | This item stores the ID of the internal Health Maintenance topic that was mapped to the received info. |
| 12 | `HM_ID_NAME` | VARCHAR |  | The name of the health maintenance topic. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

