# TASK_PEF_ROW

> This table contains patient-entered flowsheet-related setup for patient-assigned flowsheet tasks.

**Primary key:** `ACTIVITY_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACTIVITY_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the task record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PEF_FLO_MEAS_ID` | VARCHAR |  | This item stores the flowsheet row (FLO) records associated with the patient-assigned flowsheet task. |
| 4 | `PEF_FLO_MEAS_ID_DISP_NAME` | VARCHAR |  | The display name given to the flowsheet group/row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

