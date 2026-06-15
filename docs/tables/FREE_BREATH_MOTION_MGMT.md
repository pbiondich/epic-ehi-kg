# FREE_BREATH_MOTION_MGMT

> This table contains the techniques used for motion management with free breathing.

**Primary key:** `RT_SUMMARY_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RT_SUMMARY_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the radiotherapy summary record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `FREE_BREATH_MOT_MGT_TECH_TEXT` | VARCHAR |  | Stores a free text representation of the technique for free-breathing motion management when no coded value is stored in I ERT 665. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

