# ASSIGN_CRIT_TYPE

> Stores whether the criteria, used by the Workload Balancer, of the current line of the related multi item is a matching criteria or sorting criteria. 1 - Yes indicates that the criteria is a matching criteria while 0 - No indicates that the criteria is a sorting criteria.

**Primary key:** `SUMMARY_BLOCK_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `ASSIGN_CRIT_TYPE_YN` | VARCHAR |  | This item will be set when providers are assigned to this episode using a Workload Balancer. Stores whether the criteria, used by the Workload Balancer, of the current line of the related multi item is a matching criteria or sorting criteria. 1 - Yes indicates that the criteria is a matching criteria while 0 - No indicates that the criteria is a sorting criteria. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

