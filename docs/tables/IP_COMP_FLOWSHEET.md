# IP_COMP_FLOWSHEET

> This table displays completed flowsheet row information for Inpatient (INP) records.

**Primary key:** `INPATIENT_DATA_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique identifier for the inpatient record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMPLETE_FLOW_ROWS` | VARCHAR |  | The flowsheet ID of completed rows is stored here. If the row is of duplicable type, it stores the flowsheet ID and line number. |
| 4 | `ROW_STATUS_C_NAME` | VARCHAR |  | The status of the row specified by COMPLETE_FLOW_ROWS. |
| 5 | `UPDATE_INSTANT_TM` | DATETIME (Local) |  | The instant the row was updated. |
| 6 | `UPDATE_USER_ID` | VARCHAR |  | Stores the unpadded User ID of the user that updated the row status. |
| 7 | `UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `UPDATE_REASON_C_NAME` | VARCHAR | org | Stores the reason for updating the row status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

