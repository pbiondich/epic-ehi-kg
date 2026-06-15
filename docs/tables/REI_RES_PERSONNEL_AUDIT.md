# REI_RES_PERSONNEL_AUDIT

> This table contains audit events that tracks changes made to an embryology result's personnel documentation.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EMB_PRS_AUDIT_EVENT_C_NAME` | VARCHAR |  | An audit event for changes to personnel for this embryology result. |
| 4 | `REI_EMB_RESPONSIBILITY_C_NAME` | VARCHAR | org | The embryology procedure responsibility for the associated personnel audit event. |
| 5 | `PERSONNEL_AUDIT_USER_ID` | VARCHAR |  | The user personnel that is being modified in the associated personnel audit event. |
| 6 | `PERSONNEL_AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `PERSONNEL_AUDIT_TEXT_PREVIOUS` | VARCHAR |  | The previous value of the free text personnel being modified in the associated personnel audit event. |
| 8 | `PERSONNEL_AUDIT_TEXT_NEW` | VARCHAR |  | The new value of the free text personnel being modified in the associated personnel audit event. |
| 9 | `PERSONNEL_AUDIT_EDIT_USER_ID` | VARCHAR |  | The user that made an edit to this embryology result's personnel to trigger the associated personnel audit event. |
| 10 | `PERSONNEL_AUDIT_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `PERSONNEL_AUDIT_EDIT_UTC_DTTM` | DATETIME (UTC) |  | The instant for the associated personnel audit event. |
| 12 | `AUDIT_RESP_REQ_OVRIDE_REASON_C_NAME` | VARCHAR | org | The requirement override reason for the associated personnel audit event. |
| 13 | `PERS_AUDIT_OVRD_CMT` | VARCHAR |  | The requirement override comment for the associated personnel audit event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

