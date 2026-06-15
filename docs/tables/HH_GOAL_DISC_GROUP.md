# HH_GOAL_DISC_GROUP

> The table for overtime related multi discipline group info.

**Primary key:** `GOAL_ID`, `CONTACT_DATE_REAL`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GOAL_ID` | VARCHAR | PK FK→ | The unique identifier for the goal record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this contact. |
| 4 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this contact. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `OT_DISC_GROUP_ID` | VARCHAR |  | This item stores the unique identifier of the discipline record and links to the table DISCIPLINE. |
| 7 | `OT_DISC_GROUP_ID_DISC_NAME` | VARCHAR |  | The name of the discipline record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GOAL_ID` | [GOAL](GOAL.md) | name_stem | high |

