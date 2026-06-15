# COMP_RX_FMT_HX

> This table contains the history of formatted prescription numbers for each component in an Intelligent Medication Selection (IMS) tab mixture in Long Term Care (including the current active formatted prescription number).

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `COMP_RX_FMT_HX` | VARCHAR |  | The historical list of the formatted prescription numbers for each of the components of an intelligent medication selection (IMS) tab mixture in Long Term Care. An IMS tab mixture is a combination of solid form medications (i.e. tablets, capsules) of varying strengths, chosen to fulfill an order's required strength while using the least amount of tablets. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

