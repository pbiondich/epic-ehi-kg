# TPL_SCHED_VST_DEP

> This is the related-multi table for the 'Visit Department' item in the treatment plan scheduling group of tables. To be used with tables: TPL_SCHED_SELECTED TPL_SCHED_VST_KND TPL_SCHED_VST_LEN TPL_SCHED_VST_PROV TPL_SCHED_VST_TYP

**Primary key:** `TREATMENT_PLAN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique ID of the treatment plan. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The Value Count. |
| 4 | `SCHEDULE_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

