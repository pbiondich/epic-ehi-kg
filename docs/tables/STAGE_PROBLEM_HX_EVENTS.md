# STAGE_PROBLEM_HX_EVENTS

> This table contains the Diagnosis Stage (STG) items which link a cancer stage to a problem history event.

**Primary key:** `STAGE_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `STAGE_ID` | NUMERIC | PK shared | The unique identifier for the stage record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `PROBLEM_HX_CONTACT_SERIAL_NUM` | NUMERIC |  | This item contains the problem ID (LPL) of the problem history problems associated with the stage. |
| 6 | `PROBLEM_HX_EVENT_LINE` | INTEGER |  | This item contains the line of the event in Problem Event State (I LPL 8100) that the stage is associated with. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

