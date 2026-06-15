# INTERVENTIONS_HISTORY

> History of interventions if they are re-ordered.

**Primary key:** `PROBLEM_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the problem record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `TREATMENT_CLASS_ID` | NUMERIC | FK→ | The list of treatment classes. |
| 6 | `TREATMENT_CLASS_ID_DISPLAY_NAME` | VARCHAR |  | The name of the treatment class that is displayed to end users. |
| 7 | `INTERVENTION_ID` | VARCHAR | FK→ | Interventions list with reordering history. |
| 8 | `FUTURE_ADDED_BY_SYSTEM_YN` | VARCHAR |  | Indicates whether the treatment class was a future class dynamically added by the system for this contact on the treatment list. 'Y' indicates that the treatment class was a future class dynamically added by the system. "N' or NULL indicate that the treatment class not a future class added dynamically. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |
| `TREATMENT_CLASS_ID` | [TREATMENT_CLASS](TREATMENT_CLASS.md) | sole_pk | high |

