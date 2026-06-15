# TXP_HEART_STATUS_AUD

> The audit trail for the heart status of the patient.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HR_STATUS_AUDIT_C_NAME` | VARCHAR | org | Audit trail item for heart status. |
| 4 | `HR_ST_DATE_AUDIT_DT` | DATETIME |  | Audit trail item for heart status date. |
| 5 | `HR_ST_RSN_OTH_AUD` | VARCHAR |  | Audit item for the free text reason for the heart status. |
| 6 | `HR_ST_UPDATE_USR_ID` | VARCHAR |  | The user who made the corresponding update to the heart status. |
| 7 | `HR_ST_UPDATE_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `HR_ST_UPDATE_INST_DTTM` | DATETIME (UTC) |  | The instant the corresponding change to the heart status was made. |
| 9 | `HR_ST_CHANGE_TYPE_C_NAME` | VARCHAR |  | The type of audit event that occurred. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

