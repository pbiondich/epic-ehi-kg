# RX_ADJUD_INFO_HX

> This table contains the historical adjudication contacts for each dispense or administration of medications for Long Term Care and Home Infusion.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `ADJUD_HX_ORDER_ID` | NUMERIC |  | This item saves previously linked adjudication order IDs. This item is set when orders stored in ORD 47411 are cleared. The last row in this table should correspond to the most recently unlinked adjudication order and contact. |
| 6 | `ADJUD_HX_DATE_REAL` | FLOAT |  | This item saves previously linked adjudication order contact dates in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. This item is set when order contacts stored in ORD 47412 are cleared. The last row in this table should correspond to the most recently unlinked adjudication order and contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

