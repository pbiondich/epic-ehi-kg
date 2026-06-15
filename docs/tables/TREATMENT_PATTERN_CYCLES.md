# TREATMENT_PATTERN_CYCLES

> Pattern cycles in a treatment plan.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PATTERN_CYCLE_SORT_VALUE` | INTEGER |  | Stores the Id to identify a cycle in a pattern. Note that multiple cycles can have the same Id if they are part of different patterns. |
| 4 | `PATTERN_CYCLE_PATTERN_LINE` | INTEGER |  | Stores the line in SI TPL 11000 for the pattern this cycle is part of. |
| 5 | `PATTERN_CYCLE_NAME` | VARCHAR |  | An override cycle name that is set on a pattern cycle. This will be set in the cycle created from that pattern cycle. |
| 6 | `PATTERN_CYCLE_STATUS_C_NAME` | VARCHAR |  | The status of a pattern cycle in the plan. |
| 7 | `PATTERN_CYCLE_LENGTH` | INTEGER |  | The length of the pattern cycle in days. |
| 8 | `PATTERN_CYCLE_SRC_TYPE_C_NAME` | VARCHAR |  | The type of cycle this pattern cycle was created from. |
| 9 | `PATTERN_CYCLE_SOURCE_LINE` | INTEGER |  | The line in the source where this cycle was created from. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

