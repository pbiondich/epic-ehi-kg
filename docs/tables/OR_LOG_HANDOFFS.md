# OR_LOG_HANDOFFS

> This table stores information on the patient handoffs associated with a log.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique identifier for the log record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HANDOFF_TYPE_C_NAME` | VARCHAR | org | Documents the type of handoff. |
| 4 | `HNDOFF_FRM_STAFF_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `HANDOFF_TO_STAFF_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `HANDOFF_DATE` | DATETIME |  | Documents the date of the handoff. |
| 7 | `HANDOFF_TIME` | DATETIME (UTC) |  | Documents the time of the handoff. |
| 8 | `HANDOFF_STATUS_C_NAME` | VARCHAR | org | This item stores the handoff status. |
| 9 | `HANDOFF_METHOD_C_NAME` | VARCHAR | org | This item stores the handoff method. |
| 10 | `HANDOFF_COMMENTS` | VARCHAR |  | This item stores any comments related to this handoff. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

