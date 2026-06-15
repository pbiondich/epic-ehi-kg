# AP_CLM_PX_PROCESS_CODE_HX

> History of process/explanation of benefits (EOB) code changes to the claim's service line transaction.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROCESS_CODE_ID_EOB_CODE_NAME` | VARCHAR |  | The name of the processing code. |
| 4 | `ADDED_UTC_DTTM` | DATETIME (UTC) |  | The date and time the code was added in the UTC time zone. |
| 5 | `ADDED_BY_USER_ID` | VARCHAR |  | User who added the service level code |
| 6 | `ADDED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `ADDED_COMMENT` | VARCHAR |  | Comment on why the code was added |
| 8 | `RESOLUTION_C_NAME` | VARCHAR | org | The reason the code was resolved. |
| 9 | `RESOLUTION_UTC_DTTM` | DATETIME (UTC) |  | The date and time the code was resolved in the UTC time zone. |
| 10 | `RESOLUTION_BY_USER_ID` | VARCHAR |  | User who resolved the code. |
| 11 | `RESOLUTION_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `ADDED_DTTM` | DATETIME (Local) |  | The date and time the code was added in the local time zone. |
| 13 | `RESOLUTION_DTTM` | DATETIME (Local) |  | The date and time the code was resolved in the local time's time zone. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

