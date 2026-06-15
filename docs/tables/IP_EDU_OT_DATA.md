# IP_EDU_OT_DATA

> This table contains generic contact specific data for the title/topic/point.

**Primary key:** `TEACHING_TTP_ID`, `CONTACT_DATE_REAL`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TEACHING_TTP_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `DISPLAY_NAME` | VARCHAR |  | The display name of the title/topic/point. |
| 4 | `PAT_FRIENDLY_NAME` | VARCHAR |  | The name of the title/topic/point that is used when displayed to a patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

