# RX_SHIPMENT_TRACKING_INFO

> This contains the shipment tracking information for a prescription fill.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `RX_SHP_TRK_SRC_C_NAME` | VARCHAR | org | The authority/source assigning/delegating source category ID of the tracking number for the shipment containing the prescription fill. |
| 6 | `RX_SHP_TRK_UTC_DTTM` | DATETIME (UTC) |  | This is the instant when the tracking number was assigned to the fill. |
| 7 | `RX_SHP_TRK_NUM` | VARCHAR |  | This is the actual tracking number assigned by the associated tracking source for the prescription fill. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

