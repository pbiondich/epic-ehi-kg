# CAREPLAN_PT_TASK_INFO

> This table contains information about patient-assigned tasks in the care plan.

**Primary key:** `CAREPLAN_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CAREPLAN_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the care plan record. |
| 2 | `TOTAL_PT_INST_CNT` | INTEGER |  | The total number of patient-assigned task instances in the care plan which are no longer actionable or have been acted upon. |
| 3 | `COMP_PT_INST_CNT` | INTEGER |  | The total number of completed patient-assigned task instances in the care plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

