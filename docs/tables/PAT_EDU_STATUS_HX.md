# PAT_EDU_STATUS_HX

> This table stores information to track the record status changes made to patient education records. Since a record's status may change multiple times, a record's status-change information may occupy multiple rows in the table.

**Primary key:** `EDUCATION_RECORD_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EDUCATION_RECORD_ID` | NUMERIC | PK | The unique identifier for the education record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SDFL_EDIT_DTTM` | DATETIME (Attached) |  | The date and time when the record's status was changed. |
| 4 | `SDFL_EDIT_USER_ID` | VARCHAR |  | The unique ID of the user who changed the record's status. |
| 5 | `SDFL_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `SDFL_EDIT_ACTION_C_NAME` | VARCHAR |  | The edit action category number that indicates how the record's status was changed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

