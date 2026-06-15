# PROB_CP_TEMPLATE

> The PROB_CP_TEMPLATE table displays information about careplan templates associated with the given problem record.

**Primary key:** `PROBLEM_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the problem record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CAREPLAN_TEM_ID_TEMPLATE_NAME` | VARCHAR |  | The name of the care plan template record. |
| 4 | `CAREPLAN_TEMP_DAT` | INTEGER |  | This column displays the care plan template contact date (DAT). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |

