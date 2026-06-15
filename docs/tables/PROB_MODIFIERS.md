# PROB_MODIFIERS

> This table contains linked Procedure Modifier (MOD) records to a problem.

**Primary key:** `PROBLEM_LIST_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier for the problem record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROB_MODIFERS_ID` | VARCHAR |  | This item stores modifier records linked to the problem via SmartForms. |
| 4 | `PROB_MODIFERS_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |
| 5 | `MODIFIER_SOURCE_C_NAME` | VARCHAR |  | This item stores the source of modifiers. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

