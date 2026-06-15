# PR_EST_SRC_TREAT_OPTION

> This table stores the source treatment options for an estimate. When clinical information is updated on the estimate, then these treatment options will be included in the updated estimate. Treatments that don't have a source option will pull information from its selected option.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the patient estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TREATMENT_PLAN_ID` | NUMERIC | shared | The list of source treatment option records that estimates should be updated with. When estimates are updated, information from these options will be used rather than the selected options of treatments. If additional treatments are included in the estimates, then the selected option of those treatments will be used. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

