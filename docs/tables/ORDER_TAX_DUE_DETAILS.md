# ORDER_TAX_DUE_DETAILS

> This table contains tax charge components associated with the total tax due for an order.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `TAX_CSN` | NUMERIC |  | This column contains the contact serial number (CSN) of the tax definition record that was applied to the product or service within a business transaction. |
| 6 | `TAX_CLASS_C_NAME` | VARCHAR | org | The tax classification category ID that determines which tax rate to use in the corresponding tax definition record for the order. |
| 7 | `DUE_AMOUNT` | NUMERIC |  | This column contains the amount due in taxes, without rounding, for a tax definition. |
| 8 | `EXEMPTED_AMOUNT` | NUMERIC |  | This column contains the amount of tax exempted, without rounding, for a tax authority. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

