# TPL_STATUS

> This table contains overtime single response treatment plan information.

**Primary key:** `TREATMENT_PLAN_ID`, `CONTACT_DATE_REAL`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the plan record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `TREATMENT_PLAN_CSN_ID` | NUMERIC |  | The contact serial number (CSN) of the contact. |
| 5 | `CONTACT_NUM` | VARCHAR |  | The contact number of the TPL record. |
| 6 | `INSTANT_OF_ENTRY_DTTM` | DATETIME (Local) |  | The instant data was entered. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

