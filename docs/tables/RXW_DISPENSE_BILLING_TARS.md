# RXW_DISPENSE_BILLING_TARS

> This table extracts the list of payment TAR records associated with an ambulatory pharmacy point of sale payment. These will be set only if professional billing integration is enabled for ambulatory pharmacy.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the work request record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this contact. |
| 4 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this contact. |
| 5 | `PAYMENT_TAR_ID` | NUMERIC |  | The temporary payment record IDs associated with this payment. Multiple entries indicate the payment was split into several payment records for distribution among multiple guarantor accounts associated with this sale. This item is populated only when integration between ambulatory pharmacy and professional billing is enabled. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

