# REQ_CHANGE_SMT

> Contains the auditing information for when a requisition's submitter is updated.

**Primary key:** `REQUISITION_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REQUISITION_ID` | NUMERIC | PK shared | The unique identifier for the requisition record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHANGE_REASON_C_NAME` | VARCHAR | org | The change reason category ID for the requisition submitter change. |
| 4 | `CHANGING_USER_ID` | VARCHAR |  | The unique ID associated with the user record for this requisition submitter change. This column is frequently used to link to the CLARITY_EMP table. |
| 5 | `CHANGING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `CHANGE_INSTANT_DTTM` | DATETIME (UTC) |  | The instant when the requisition's submitter was changed. |
| 7 | `PREV_SUBMITTER_ID` | NUMERIC |  | The unique ID of the submitter that was associated with the requisition prior to the submitter being updated. |
| 8 | `PREV_SUBMITTER_ID_RECORD_NAME` | VARCHAR |  | The name of the submitter record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

