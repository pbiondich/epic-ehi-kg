# TXP_INTESTINE_STATUS_AUD

> The audit trail for the intestine status of the patient.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IN_STATUS_AUDIT_C_NAME` | VARCHAR | org | Stores the audit trail information for the intestine status for the transplant episode. |
| 4 | `IN_ST_AUDIT_DT` | DATETIME |  | Audit trail item for intestine status date. |
| 5 | `IN_ST_RSN_OTH_AUD` | VARCHAR |  | Stores the audit trail information for the free-text reason for the intestine status for the transplant episode. |
| 6 | `IN_ST_UPDATE_USR_ID` | VARCHAR |  | Stores the user responsible for the corresponding update to the intestine status for the transplant episode. |
| 7 | `IN_ST_UPDATE_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `IN_ST_UPDATE_INST_DTTM` | DATETIME (UTC) |  | Stores the instant on which the corresponding update to the intestine status was changed for the transplant episode. |
| 9 | `IN_ST_CHANGE_TYPE_C_NAME` | VARCHAR |  | The type of audit event that occurred to the intestine status |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

