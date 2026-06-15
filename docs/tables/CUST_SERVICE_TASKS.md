# CUST_SERVICE_TASKS

> This table extracts task information associated with a customer service record.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique ID of the customer service communication record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TASK_CRM_OWNER_YN` | VARCHAR |  | Indicates if the task is assigned to the customer service communication's owner. |
| 4 | `TASK_MANUAL_ADD_YN` | VARCHAR |  | Stores whether the task was manually added |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

