# DOCS_RCVD_GENERIC_ORDERS

> Stores generic order data received.

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
| 5 | `GENERIC_ORDER_IDENT` | VARCHAR |  | Stores unique identifier for the generic order we received. |
| 6 | `GENERIC_ORDER_NAME` | VARCHAR |  | This item stores the generic order name. |
| 7 | `GENERIC_INTEND_ACT_C_NAME` | VARCHAR |  | Intended action expected for this generic order. |
| 8 | `GENERIC_ORDER_FMT_NAME` | VARCHAR |  | This item stores the formatted generic order name. |
| 9 | `GEN_INTEND_TYP_C_NAME` | NUMERIC |  | Intended procedure order type for this generic order |
| 10 | `GEN_ORDER_SYNONYMS` | VARCHAR |  | This item stores the synonyms for the generic order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

