# HH_PROB_INFO

> This table no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Contains Home Health care plan problems noadd single items information.

**Primary key:** `PROBLEM_ID`  
**Columns:** 12  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_ID` | VARCHAR | PK FK→ | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the PROBLEM_ID column in the PROBLEM table to report on this item instead. Unique identifier for the care plan problem. |
| 2 | `PROBLEM_TYPE_ID_NAME` | VARCHAR |  | The name of the multidisciplinary diagnoses. |
| 3 | `CREATE_DATE` | DATETIME |  | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the CREATED_DATE column in the PROBLEM table to report on this item instead. Date on which care plan problem was created. |
| 4 | `DELETE_DATE` | DATETIME |  | This column no longer populates data for new HH/HSPC as of the Epic 2018 release (8.4). Use the DELETED_DATE column in the PROBLEM table to report on this item instead. Date on which care plan problem was deleted. |
| 5 | `REASON_FOR_DEL_C_NAME` | VARCHAR | org | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the DEL_REASON_C column in the PROBLEM table to report on this item instead. Reason for deleting problem. Links to category table ZC_DEL_REASON. |
| 6 | `DISCIPLINE_C_NAME` | VARCHAR | org | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the DISCIPLINE_C column in the PROBLEM table to report on this item instead. Care plan problem discipline. Links to category table ZC_DISCIPLINE. |
| 7 | `IP_DISCIPLINE_ID` | VARCHAR |  | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the IP_DISC_TYPE_ID column in the PROBLEM table to report on this item instead. Care plan problem inpatient discipline. Links to table DISCIPLINE. |
| 8 | `IP_DISCIPLINE_ID_DISC_NAME` | VARCHAR |  | The name of the discipline record. |
| 9 | `PROB_DESCR_ID` | VARCHAR |  | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Use the PROBLEM_DESCRIPTION_HNO_ID column in the PROBLEM table to report on this item instead. Care plan problem description ID. |
| 10 | `GOAL_DESCR_ID` | VARCHAR |  | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Care plan problem goal description ID. |
| 11 | `INTERV_DESC_ID` | VARCHAR |  | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Care plan problem intervention description ID. |
| 12 | `OUTCOMES_DESC_ID` | VARCHAR |  | This column no longer populates data for new HH/HSPC problems as of the Epic 2018 release (8.4). Care plan problem outcomes description ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |

