# RXHI_FILL_PLAN

> Items related to the plan of administration for a home infusion medication fill.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `START_DATE` | DATETIME |  | List of start dates for administrations in a home infusion fill |
| 6 | `DAYS` | INTEGER |  | Number of days of service covered by this entry in the fill plan table |
| 7 | `FILL_PLAN_DOSE` | INTEGER |  | Related dose number in shipment |
| 8 | `DISPENSE_CONTACT_DATE_REAL` | VARCHAR |  | Pointer to the dispense DAT related to this item in the fill plan, once it exists. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

