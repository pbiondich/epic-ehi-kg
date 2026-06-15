# TREATMENT_PATTERNS

> Treatment patterns in a treatment plan.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PATTERN_SORT_VALUE` | INTEGER |  | An Id to identify a cycle pattern in this treatment plan. It is also used to determine the sequence the patterns should be displayed to the user. |
| 4 | `PATTERN_STATUS_C_NAME` | VARCHAR |  | The status of a pattern in a treatment plan. |
| 5 | `PATTERN_SOURCE_TYPE_C_NAME` | VARCHAR |  | An item to describe where this pattern was created from. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

