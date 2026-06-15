# PROB_USER_EDITS

> Care plan-related table which stores patient contact serial number (CSN), ID of user who added the problem, and time the problem was added (related to Bring Forward functionality).

**Primary key:** `PROBLEM_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_ID` | VARCHAR | PK FK→ | The unique ID for the care integrator problem. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IP_CP_PROB_EPT_CSN` | NUMERIC |  | The patient contact serial numbers for the encounters where a care plan problem was addressed. |
| 4 | `IP_CP_PROB_EMP_ID` | VARCHAR |  | The ID of the user who added a care plan problem to an encounter. |
| 5 | `IP_CP_PROB_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `IP_CP_PROB_ADD_INST` | DATETIME (Local) |  | The instant a care plan problem was added to an encounter. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |

