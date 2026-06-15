# RXW_AUDIT_USER

> This contains the audit trail user and instant portion for Willow Ambulatory work requests.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the work request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_EMP_USER_ID` | VARCHAR |  | ID of the user who took the action that triggered an update to the audit trail. |
| 4 | `AUDIT_EMP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `AUDIT_UPDATE_INST_DTTM` | DATETIME (UTC) |  | Instant of the action that triggered an update to the audit trail. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

