# DOCS_RCVD_MEDS_2

> This table stores medications received from outside sources.

**Overflow of:** [DOCS_RCVD_MEDS](DOCS_RCVD_MEDS.md)  
**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 17  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `MED_REFILL_INTERVAL` | INTEGER |  | Stores the medication refill interval in days. |
| 6 | `MED_REFILL_FREE_TXT` | VARCHAR |  | Medication refill free text information. |
| 7 | `MED_QUANTITY_UNIT_C_NAME` | VARCHAR | org | Unit associated with medication quantity (e.g tab, g) |
| 8 | `LAST_FILL_DATE` | DATETIME |  | Date on which the medication was last filled at the pharmacy |
| 9 | `DAYS_SUPPLY` | NUMERIC |  | Number of days for which the medication is going to be dispensed; used by payors during claim adjudication |
| 10 | `BRAND_NECESSARY_YN` | VARCHAR |  | This column stores whether the prescription is intended to be dispensed as written or if a generic substitution may be used for incoming e-prescribing messages. |
| 11 | `DISP_QUANTITY_REMAINING` | NUMERIC |  | Medication dispense quantity remaining. |
| 12 | `DISP_QTY_REMAIN_UNIT_UNMAPPED` | VARCHAR |  | Medication dispense quantity remaining unit that cannot be mapped to ECT-9010. |
| 13 | `QUANTITY_TRANSFERRED` | NUMERIC |  | Medication quantity transferred. This is used in electronic prescription transfers between two pharmacies. |
| 14 | `QTY_TRANSFERRED_DISP_QTYUNIT_C_NAME` | VARCHAR |  | Medication quantity transferred unit. This is used in electronic prescription transfers between two pharmacies. |
| 15 | `QTY_REMAINING_DISP_QTYUNIT_C_NAME` | VARCHAR |  | Medication dispense quantity remaining unit. |
| 16 | `QTY_TRANSFERRED_UNIT_UNMAPPED` | VARCHAR |  | Medication quantity transferred unit that cannot be mapped to ECT-9010. This is used in electronic prescription transfers between two pharmacies. |
| 17 | `MED_INTEND_ACT_C_NAME` | VARCHAR |  | Intended action expected for this medication. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

