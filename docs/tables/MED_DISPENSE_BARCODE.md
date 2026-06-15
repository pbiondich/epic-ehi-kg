# MED_DISPENSE_BARCODE

> This table contains external barcodes received as part of prescription fills from a third party interface if the fill is not accepted automatically.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `GROUP_LINE` | INTEGER | PK | The line number of a single medication/ingredient in the overall dispense. Together with DOCUMENT_ID and CONTACT_DATE_REAL, this forms the foreign key to the MED_DISPENSE table. |
| 4 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple external barcode IDs associated with the overall dispense and the single medication/ingredient from the MED_DISPENSE table. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `DISP_BARCODE_IDENT` | VARCHAR |  | This item records the medication barcode IDs received as part of an external dispense. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

