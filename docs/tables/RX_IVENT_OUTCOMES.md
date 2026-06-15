# RX_IVENT_OUTCOMES

> The intervention outcomes table contains one record for each intervention and the outcome associated with the intervention. The primary key for the intervention type table is INTERVENTION_ID, LINE.

**Primary key:** `INTERVENTION_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INTERVENTION_ID` | NUMERIC | PK FK→ | The unique ID of the intervention. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OUTCOME_C_NAME` | VARCHAR | org | The eventual outcome(s) associated with an intervention, like avoiding an Adverse Drug Effect or a Cost Savings. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |

