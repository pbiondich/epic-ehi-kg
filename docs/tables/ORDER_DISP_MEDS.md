# ORDER_DISP_MEDS

> This table contains information about the dispensed medications for orders.

**Primary key:** `ORDER_MED_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique ID of the order to which these component actions belong. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can often be associated with this record. |
| 4 | `OVR_COMP_CHARGE` | NUMERIC |  | The override charge of the component. |
| 5 | `RX_INTENDED_QTY` | NUMERIC |  | The intended dispense amount for partial fills in Ambulatory Rx. |
| 6 | `RX_INTEND_QTYUNT_C_NAME` | VARCHAR | org | The intended quantity unit for partial fills in Rx Adjudication |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

