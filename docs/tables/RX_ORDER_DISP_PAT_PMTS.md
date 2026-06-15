# RX_ORDER_DISP_PAT_PMTS

> A list of patient payment Temporary Accounts Receivable (TAR) records for an individual prescription fill.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `RX_TAR_ID` | NUMERIC |  | The unique identifier of the attending provider for the charge session (TAR) for the corresponding patient payment when payments are processed in Willow Ambulatory. |
| 6 | `RX_PAYMENT_AMOUNT` | NUMERIC |  | When a patient payment is made in Willow Ambulatory, this stores the amount of the payment that applies to this order, in the case that the payment was made for multiple orders. If this is not set, the system assumes that the payment applies in its entirety to this order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

