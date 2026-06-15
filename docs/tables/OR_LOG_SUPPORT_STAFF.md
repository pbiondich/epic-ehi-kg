# OR_LOG_SUPPORT_STAFF

> This table contains information about support staff.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique identifier for the log record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SUPPORT_STAFF_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `SUPPORT_STAFF_PHASE_C_NAME` | VARCHAR | org | This category ID for the support staff phase. |
| 5 | `SUPPORT_STAFF_START_TM` | DATETIME (Local) |  | This column stores the start time for the support staff. |
| 6 | `SUPPORT_STAFF_END_TM` | DATETIME (Local) |  | This column stores the end time for the support staff. |
| 7 | `SUPPORT_STAFF_COMMENTS_FT` | VARCHAR |  | This column stores free-text information about the support staff. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

