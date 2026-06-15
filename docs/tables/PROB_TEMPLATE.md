# PROB_TEMPLATE

> The PROB_TEMPLATE table displays information about the template associated with the careplan problem.

**Primary key:** `PROBLEM_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_ID` | VARCHAR | PK FK→ | The unique identifier for the problem record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROBLEM_TEMPLATE_ID` | NUMERIC |  | This column displays the problem template ID |
| 4 | `PROBLEM_TEMPLATE_ID_TEMPLATE_PROB_NAME` | VARCHAR |  | This column displays the template problem name. |
| 5 | `CP_PROB_TEMP_DAT` | INTEGER |  | This column displays the care plan problem template contact date (DAT). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |

