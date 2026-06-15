# OUTCOME_EVAL_GOALS

> Contains information about pathway goals for which the evaluation result of this advisory's base locator record (found in ALERT__BPA_LOCATOR_ID) was used to suggest a status of Met or Not Met.

**Primary key:** `ALERT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALERT_ID` | NUMERIC | PK shared | The unique identifier for the med alert record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `GOAL_ID` | VARCHAR | FK→ | Stores the ID of a pathway outcome that used the locator in BPA_LOCATOR_ID in the ALERT table to suggest the status of the outcome as Met or Not Met for this instance of the evaluation of the locator. |
| 6 | `GOAL_CONTACT_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. Can be used along with GOAL_ID to link to a goal information table (e.g., GOAL_CONTACT) to access the related documentation. If null, that means the outcome that used the locator in BPA_LOCATOR_ID in the ALERT table to suggest the status of the outcome as Met or Not Met was not documented on in the workflow in which the suggestion was made. |
| 7 | `ALT_CSN_ID` | NUMERIC | FK→ | A unique serial number for this contact. This number is unique across all alerts in the system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ALT_CSN_ID` | [ALT_HISTORY](ALT_HISTORY.md) | sole_pk | high |
| `GOAL_ID` | [GOAL](GOAL.md) | name_stem | high |

