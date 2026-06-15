# TPL_HSB_PREMERGE

> The source episode (HSB) for a treatment plan.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The treatment plan ID. |
| 2 | `LINE` | INTEGER | PK | The line number that corresponds to each episode record (HSB ID) in the treatment plan in this row. |
| 3 | `BEFOREMERGE_HSB_ID` | NUMERIC |  | A source episode (HSB) before a treatment plan merge took place for the treatment plan in this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

