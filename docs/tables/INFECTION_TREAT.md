# INFECTION_TREAT

> Treatments for an infection problem.

**Primary key:** `PROBLEM_LIST_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier for the problem record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INFECT_TREAT_C_NAME` | VARCHAR | org | List of treatments for an infection problem |
| 4 | `INFECT_TX_START_DT` | DATETIME |  | Infection treatment start date |
| 5 | `INFECT_TX_END_DT` | DATETIME |  | Infection treatment end date |
| 6 | `INFECT_TX_START_TM` | DATETIME (Local) |  | Infection treatment start time |
| 7 | `INFECT_TX_END_TM` | DATETIME (Local) |  | Infection treatment end time |
| 8 | `INFECTION_COMMENTS` | VARCHAR |  | Comments about infection treatments |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

