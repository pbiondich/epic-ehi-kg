# CAL_COMM_HX_REF_TASK

> Stores the history of tasks referenced by a communication (i.e. the history of CAL_REFERENCE_TASK). Each GROUP_LINE corresponds to a line in CAL_COMM_HX for a COMM_ID.

**Primary key:** `COMM_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | VARCHAR | PK shared | The unique identifier for the communication record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `REF_TASK_ID` | VARCHAR |  | Stores the unique identifier of a task referenced by this communication. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

