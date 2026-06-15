# TASK_MED_PRBLM_LIST

> This table stores information about the medication problem lists that are linked to a task record.

**Primary key:** `ACTIVITY_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACTIVITY_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the task record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORDER_ID` | NUMERIC | shared | The order that triggered the related medication problem list to be linked to the task. |
| 4 | `ORDER_DAT` | VARCHAR |  | A fill request is a contact on the order record documenting a dispense of that order to the patient. This field specifies which fill request (or contact) on the order triggered the related medication problem list to be linked to the task. |
| 5 | `LINKED_MED_METH_C_NAME` | VARCHAR |  | Method used to link medication to the task |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

