# TASK_COMMENTS

> Task comments converted from rich text to plain text. The rich text comments are stored the Comments (I LTK 52) item.

**Primary key:** `TASK_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TASK_ID` | VARCHAR | PK shared | The unique ID for the task. |
| 2 | `LINE` | INTEGER | PK | The line number of the task's comments. |
| 3 | `COMMENTS` | VARCHAR |  | The task's comments in plain text. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

