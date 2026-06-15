# PROBLEM_EVENTS_AUD

> This table contains an audit trail of changes made to a problem's history, stored in the PROBLEM_EVENTS table.

**Primary key:** `PROBLEM_LIST_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier for the problem record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `AUDIT_USER_ID` | VARCHAR |  | Stores the user that edited an event |
| 6 | `AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `AUDIT_INST_DTTM` | DATETIME (UTC) |  | Stores the UTC instant that an event was edited |
| 8 | `AUDIT_LINE` | INTEGER |  | Stores the line number of the edited event |
| 9 | `AUDIT_ACTION_C_NAME` | VARCHAR |  | Stores the action taken on this event |
| 10 | `AUDIT_VALUE` | VARCHAR |  | Stores the value associated with the audit action |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

