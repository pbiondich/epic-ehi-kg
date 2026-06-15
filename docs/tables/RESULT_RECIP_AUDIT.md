# RESULT_RECIP_AUDIT

> Audit information about the recipients of In Basket results messages for an order.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID associated with the order record for this row. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `RESULT_REC_NOTIF_ID` | NUMERIC |  | Stores link to push notification sent during results routing |
| 5 | `RESULT_REC_SMT_RECORD_ID` | NUMERIC |  | The unique ID of the submitter record for this row. |
| 6 | `RESULT_REC_SMT_RECORD_ID_RECORD_NAME` | VARCHAR |  | The name of the submitter record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

