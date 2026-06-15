# HH_PROB_INTRVNTN

> This table no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). This table contains Home Health care plan problem intervention information. This information is entered by a user in the Care Plan task on the Home Health Remote Client.

**Primary key:** `PROBLEM_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_ID` | VARCHAR | PK FK→ | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the PROBLEM_ID column in the PROBLEM_INTERVENTION table to report on this item instead. Unique identifier for the care plan problem. |
| 2 | `LINE` | INTEGER | PK | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the LINE column in the PROBLEM_INTERVENTION table to report on this item instead. The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INTERVENTIONS_ID` | VARCHAR |  | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the INTERVENTION_ID column in the PROBLEM_INTERVENTION table to report on this item instead. Care plan problem intervention ID. Links to table INTERVENTION. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |

