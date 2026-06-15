# STAGE_SF_VALUES

> Stores SmartForm data filed to each contact of a cancer stage record.

**Primary key:** `STAGE_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `STAGE_ID` | NUMERIC | PK shared | The unique identifier for the stage record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `STAGE_SF_CUI` | VARCHAR |  | Stores concept unique identifier (CUI) IDs for staging reporting |
| 6 | `STAGE_SF_LINE` | INTEGER |  | Stores the line number within a single concept unique identifier (CUI) for staging SmartForm reporting. |
| 7 | `STAGE_SF_VALUE` | VARCHAR |  | Stores the value of a given concept unique identifier (CUI) and line for staging SmartForm reporting. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

