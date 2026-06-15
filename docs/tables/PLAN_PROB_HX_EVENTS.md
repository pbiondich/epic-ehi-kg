# PLAN_PROB_HX_EVENTS

> This table contains problem history contact serial numbers (CSNs) and lines to link problem history events to treatment plans that generated them. Problem history events are stored in the PROBLEM_EVENTS table.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROBLEM_HX_CSN` | NUMERIC |  | This item contains the problem history contact serial number (CSN) that this treatment plan is linked to. |
| 4 | `PROB_HX_EVENT_LINE` | INTEGER |  | This item contains the line from the Problem Event State (I LPL 8100) that this treatment plan is associated with. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

