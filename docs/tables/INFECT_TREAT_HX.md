# INFECT_TREAT_HX

> History of treatments for an infection/complication problem.

**Primary key:** `PROBLEM_LIST_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier for the problem record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INFECT_TREAT_HX_C_NAME` | VARCHAR | org | History of changes to the treatments for an infection |
| 4 | `INFECT_TREAT_INST` | DATETIME (Local) |  | Instant the treatments have been changed |
| 5 | `INFECT_TREAT_WHO_ID` | VARCHAR |  | User who changed the infection treatment |
| 6 | `INFECT_TREAT_WHO_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `INFECT_HX_START_DT` | DATETIME |  | Infection treatment start date |
| 8 | `INFECT_HX_END_DT` | DATETIME |  | Infection treatment end date |
| 9 | `INFECT_HX_START_TM` | DATETIME (Local) |  | Infection treatment start time |
| 10 | `INFECT_HX_END_TM` | DATETIME (Local) |  | Infection treatment end time |
| 11 | `INFECT_HX_COMMENTS` | VARCHAR |  | Infection treatment comments |
| 12 | `COMP_HX_UPD_TYPE_C_NAME` | VARCHAR |  | The update type for the complication/infection treatment related group. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

