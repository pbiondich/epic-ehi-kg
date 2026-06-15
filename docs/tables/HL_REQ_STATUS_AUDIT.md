# HL_REQ_STATUS_AUDIT

> Hospital Logistics Request Status Audit.

**Primary key:** `HLR_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLR_ID` | NUMERIC | PK shared | The unique identifier for the request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EVENT_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant when a status change event occurred for this Logistics Request. |
| 4 | `STATUS_C_NAME` | VARCHAR |  | The status audit trail for this Logistics Request's status (I HLR 160). |
| 5 | `CANCEL_RSN_C_NAME` | VARCHAR | org | The status audit trail for this Logistics Request's cancel or Job's skip reason (I HLR 175). |
| 6 | `EVENT_LOCAL_DTTM` | DATETIME (Local) |  | The local instant when a status change event occurred for this Logistics request. For UTC, use HL_REQ_STATUS_AUDIT.EVENT_UTC_DTTM. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

