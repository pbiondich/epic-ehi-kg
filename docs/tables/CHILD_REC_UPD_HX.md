# CHILD_REC_UPD_HX

> Table to extract lines that each represent a deselection of a recommended order. Can be used with other Clarity tables CHI_REC_CMT_HX_RM, CHI_REC_DTTM_HX_RM, CHI_REC_RSN_HX_RM, and CHI_REC_UID_HX_RM to keep track of histories of recommended orders.

**Primary key:** `REGIMEN_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGIMEN_ID` | NUMERIC | PK shared | The unique identifier for the patient order group record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DT` | DATETIME |  | The date of this contact in calendar format. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

