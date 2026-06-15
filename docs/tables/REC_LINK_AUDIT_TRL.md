# REC_LINK_AUDIT_TRL

> This table stores an audit trail of changes made to a recommendation's linking.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique ID of the recommendation record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_DATETIME` | DATETIME (Local) |  | The date and time when the recommendation link change was made. |
| 4 | `AUDIT_USER_ID` | VARCHAR |  | The unique ID of the user that made the change to the recommendation link. |
| 5 | `AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `AUDIT_WORKFLOW_C_NAME` | VARCHAR |  | The category number for the workflow that triggered the link changes. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

