# OPE_INFO

> This table stores order performable information.

**Primary key:** `OPE_ID`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OPE_ID` | NUMERIC | PK shared | The unique identifier for the performable order record. |
| 2 | `PERFORMABLE_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 3 | `ACCT_ID` | NUMERIC | shared | The unique identifier of the account record. |
| 4 | `LOGIN_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 5 | `PAT_LINK_ID` | VARCHAR |  | The unique ID of the patient record associated with the orders performed record for this row. |
| 6 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The hidden or visible status of the record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

