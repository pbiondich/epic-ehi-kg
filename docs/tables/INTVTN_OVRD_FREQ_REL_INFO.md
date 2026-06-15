# INTVTN_OVRD_FREQ_REL_INFO

> Contains the related days and times of the override frequency on the intervention.

**Primary key:** `INTERVENTION_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INTERVENTION_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the intervention record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `FREQ_OVRD_REL_DAYS` | INTEGER |  | Contains a list of days, relative to the start date, that are used to override the intervention frequency along with the times in LPI-34656. |
| 6 | `FREQ_OVRD_REL_TM` | DATETIME (Local) |  | Contains a set of times related to the days in LPI-34655 used to override the intervention frequency. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |

