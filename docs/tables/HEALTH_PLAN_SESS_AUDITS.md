# HEALTH_PLAN_SESS_AUDITS

> This table contains the health plan audit records updated by each coding session linked to a task. The GROUP_LINE column represents the coding session where a contact was created.

**Primary key:** `ACTIVITY_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACTIVITY_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the task record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 5 | `CM_LOG_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| 6 | `CODE_AUDIT_SUMMARY_DATA_ID` | NUMERIC |  | The unique ID of the health plan audit records (RAD) impacted/updated during the coding session recording the changes made. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

