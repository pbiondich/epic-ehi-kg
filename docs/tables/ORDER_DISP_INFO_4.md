# ORDER_DISP_INFO_4

> This table contains dispense information for orders.

**Overflow of:** [ORDER_DISP_INFO](ORDER_DISP_INFO.md)  
**Primary key:** `ORDER_MED_ID`, `CONTACT_DATE_REAL`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `RX_DROPSHIP_QUANTITY` | INTEGER |  | Specifies the quantity of the requested product from the drop shipping vendor. |
| 5 | `RX_DROPSHIP_QUANTITY_UNIT_C_NAME` | VARCHAR |  | Specifies the external unit of measure used when requesting products from the drop shipment vendor. |
| 6 | `RX_DROPSHIP_PACKAGE_COUNT` | INTEGER |  | Represents the number of packages that comprise one request unit (I ORD 48631-RX Drop Shipment Unit) from the drop shipment vendor. For example, if the unit of measure is “Package” and the value is 3, then one “Package” consists of three individual packages. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

