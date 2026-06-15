# POC_RECORD_STS_HX

> This table contains record status information for the Plan of Care (POC) master file.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the plan of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SDFL_EDIT_INST_DTTM` | DATETIME (Local) |  | This item stores the instant that the record status was changed. |
| 4 | `SDFL_EDIT_USER_ID` | VARCHAR |  | This item stores the user who changed the record status. |
| 5 | `SDFL_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `SDFL_EDIT_ACTION_C_NAME` | VARCHAR |  | This item stores the action that was applied to the record status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

