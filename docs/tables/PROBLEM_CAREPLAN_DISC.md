# PROBLEM_CAREPLAN_DISC

> Contains care plan problem discipline priority information.

**Primary key:** `PROBLEM_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_ID` | VARCHAR | PK FK→ | The unique identifier for the problem record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `DISC_TYPE_ID` | VARCHAR | FK→ | The linked discipline record ID. This column is frequently used to link to the DISCIPLINE table. |
| 5 | `DISC_TYPE_ID_DISC_NAME` | VARCHAR |  | The name of the discipline record. |
| 6 | `DISC_PRIORITY_C_NAME` | VARCHAR | org | The category ID of the care plan problem discipline priority. |
| 7 | `DISC_RESOLVED_YN` | VARCHAR |  | Indicates whether the care plan problem for the discipline is resolved. |
| 8 | `DISC_RESOLVED_DTTM` | DATETIME (Local) |  | The instant at which the care plan problem was resolved. |
| 9 | `HH_PROB_DISC_C_NAME` | VARCHAR | org | The Home Health and Hospice disciplines linked to the problem. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DISC_TYPE_ID` | [DISCIPLINE](DISCIPLINE.md) | sole_pk | high |
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |

