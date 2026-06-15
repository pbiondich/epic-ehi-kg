# DISC_SPECIFIC_INFO

> This table contains specific information for disciplines.

**Primary key:** `GOAL_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GOAL_ID` | VARCHAR | PK FK→ | The unique identifier for the goal record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SMARTTEXT_ID` | VARCHAR | FK→ | The unique ID of the SmartText (ETX) used to document on this goal. |
| 4 | `SMARTTEXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 5 | `DISCIPLINES_ID` | VARCHAR |  | The unique ID of the most current Discipline (LDS) for the goal. |
| 6 | `DISCIPLINES_ID_DISC_NAME` | VARCHAR |  | The name of the discipline record. |
| 7 | `HH_GOAL_DISC_C_NAME` | VARCHAR | org | The current Home Health disciplines linked to the goal. |
| 8 | `HH_DISCIPLINE_START_DATE` | DATETIME |  | This item stores the effective date of a Home Health goal discipline which is added after the goal record is created. This column no longer populates data for new HH/HSPC care plans as of Epic May 2024. Use the CONTACT_DATE column in GOAL_DISC table to report on this item instead. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GOAL_ID` | [GOAL](GOAL.md) | name_stem | high |
| `SMARTTEXT_ID` | [SMARTTEXT](SMARTTEXT.md) | sole_pk | high |

