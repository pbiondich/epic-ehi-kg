# RES_VLD_AUDIT

> Result audit information for verification and unverification (result correction).

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RES_SPECIMEN_ID` | VARCHAR |  | Internal specimen identifier associated with result |
| 4 | `RES_VLD_STATUS_C_NAME` | VARCHAR |  | The result validation status category number for the audit trail validation status. |
| 5 | `RES_UNVLD_RSN_C_NAME` | VARCHAR | org | The result correction reason category number for the result correction. |
| 6 | `RES_VLD_USER` | VARCHAR |  | The unique ID associated with the user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| 7 | `RES_VLD_USER_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `RES_VLD_INSTANT` | DATETIME (Local) |  | The instant when the result is validated. |
| 9 | `RES_UNVLD_RSN_COM` | VARCHAR |  | Unvalidation reason comment |
| 10 | `RES_UNVLD_RESULT_ID` | VARCHAR |  | The unique identifier of the validation audit result record that is associated with this result record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

