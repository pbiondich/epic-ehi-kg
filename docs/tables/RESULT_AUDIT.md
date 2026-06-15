# RESULT_AUDIT

> This table is part of a group of tables that extracts audit information related to a finding. Each row specifies an action performed on the finding, along with the new values recorded for the items being audited. This table is very similar in structure to ORDER_RAD_AUDIT, which stores the audit trail of imaging orders. The tables RESULT_AUDIT_ITEMS, RESULT_AUD_PATH_CODES, and RESULT_AUD_MALIG_TYPE contain the rest of the finding audit information not found in this table. Join to these three tables from RESULT_AUDIT using the two primary keys FINDING_ID and LINE.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique ID of the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACTION_PERFORMED_C_NAME` | VARCHAR | org | The action category ID for the action being audited. |
| 4 | `ACTION_DTTM` | DATETIME (UTC) |  | The instant at which the audited action was performed. |
| 5 | `PERFORMING_USER_ID` | VARCHAR |  | The user who performed the audited action. |
| 6 | `PERFORMING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `LESION_CLASS_C_NAME` | VARCHAR | org | The lesion classification category ID, if any, for the action being audited. |
| 8 | `LESION_SIDE_C_NAME` | VARCHAR |  | The pathology finding side category ID, if any, for the action being audited. |
| 9 | `PATH_RESULT_DT` | DATETIME |  | The new value for the pathology finding biopsy date (RES-52340), if any, for the action being audited. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

