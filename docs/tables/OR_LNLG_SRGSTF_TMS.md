# OR_LNLG_SRGSTF_TMS

> This table contains the Surgical Staff Times information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the Line (ORM) record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STAFF_ST_CMT` | VARCHAR |  | Staff start time comment |
| 4 | `STAFF_ET_CMT` | VARCHAR |  | Staff end time comment |
| 5 | `STAFF_ST_DOCU_ID` | VARCHAR |  | The unique ID of the EMP user who documented this staff member's start time. |
| 6 | `STAFF_ST_DOCU_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `STAFF_ET_DOCU_ID` | VARCHAR |  | The unique ID of the EMP user who documented this staff member's start time. |
| 8 | `STAFF_ET_DOCU_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `STAFF_TIME_SOURCE_STATUS_C_NAME` | VARCHAR |  | The source and status of the start and end time for the provider. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

