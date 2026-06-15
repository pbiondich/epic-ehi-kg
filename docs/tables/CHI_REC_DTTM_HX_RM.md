# CHI_REC_DTTM_HX_RM

> This table extracts the history of timestamps associated with updating comments/reasons for deselecting recommended child order items.

**Primary key:** `REGIMEN_ID`, `CONTACT_DATE_REAL`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGIMEN_ID` | NUMERIC | PK shared | The unique identifier for the patient order group record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `GROUP_LINE` | INTEGER | PK | The line number of the associated instance of deselecting recommended order items in the patient order group record. |
| 4 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple changes made while editing the patient order group record. |
| 5 | `CONTACT_DT` | DATETIME |  | The date of this contact in calendar format. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

