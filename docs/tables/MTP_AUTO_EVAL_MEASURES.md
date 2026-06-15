# MTP_AUTO_EVAL_MEASURES

> The quality measure outcome information obtained from the Medication Therapy Opportunities Engine.

**Primary key:** `PROBLEM_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the med therapy problem record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REGISTRY_DATA_ID` | NUMERIC | shared | The RDI outcome records associated with the quality measures identified by the medication therapy opportunities engine evaluation. |
| 4 | `MEASURE_OUTCOME_KEY` | INTEGER |  | The unique outcome key that is calculated using a combination of the measure, measure version, measurement period pattern, benefit plan, line of business, and product line that are related to a specific measure outcome. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |

