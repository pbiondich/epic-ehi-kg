# TXP_PHASE_HX_AUDIT

> This table contains the audit trail for transplant phase, including changes from phase history as well as editing in transplant info section.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PHASE_HX_AUDIT_C_NAME` | VARCHAR |  | Stores the audit trail for transplant episode phase updates. |
| 4 | `DATE_HX_AUDIT_DT` | DATETIME |  | Stores the audit trail for transplant episode status date updates. |
| 5 | `STATUS_HX_AUDIT_C_NAME` | VARCHAR | org | Stores the audit trail for transplant episode status updates. |
| 6 | `UPDATE_USER_AUDIT_ID` | VARCHAR |  | This item stores the audit trail for the users who update the phase history in both Phase History activity and Transplant Information section. |
| 7 | `UPDATE_USER_AUDIT_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `UPDATE_INST_AUD_DTTM` | DATETIME (Local) |  | This item stores the audit trail for the instant when the transplant phase history is updated in both Phase History activity and Transplant Information section. |
| 9 | `REASON_HX_AUDIT_C_NAME` | VARCHAR | org | Stores the audit trail of the reasons the transplant episode status was updated. |
| 10 | `PHASE_AUD_EVENT_C_NAME` | VARCHAR |  | Stores the audit trail for if data was added, edited, or removed from the transplant episode's phase, status, reason, and/or date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

