# LAB_TASK_FLAGS

> Stores a list of flags placed on a task.

**Primary key:** `SPECIMEN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier for the specimen record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `TASK_FLAGS_C_NAME` | VARCHAR | org | Stores a list of flags placed on a task. |
| 5 | `TASK_FLAGS_CMT` | VARCHAR |  | A free text comment associated with each task flag. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

