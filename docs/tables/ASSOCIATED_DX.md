# ASSOCIATED_DX

> Diagnoses associated with treatment plans.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `SPECIFIC_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 5 | `PROBLEM_LIST_ID` | NUMERIC | FK→ | This column is used to track problems currently or previously linked to the plan (via episodes of care). |
| 6 | `PROBLEM_LINKED_TO_PLAN_YN` | VARCHAR |  | This column is used to store whether the problem and diagnoses on this line are linked to the plan. This column is updated for plans of active and future statuses. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

