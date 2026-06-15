# OR_LNLG_ANESTF_TMS

> This table contains the Anesthesia Staff Times information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the Line (ORM) record |
| 2 | `LINE` | INTEGER | PK | The Line Count for a particular Anesthesia staff member. There may be multiple staff assigned to the case. |
| 3 | `ANES_STAFF_ST_CMT` | VARCHAR |  | Anesthesia Staff start time comment |
| 4 | `ANES_STAFF_ET_CMT` | VARCHAR |  | Anesthesia Staff end time comment |
| 5 | `ANES_STAFF_ST_DOCU_ID` | VARCHAR |  | The unique ID of the EMP user who documented this anesthesia staff member's start time. |
| 6 | `ANES_STAFF_ST_DOCU_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `ANES_STAFF_ET_DOCU_ID` | VARCHAR |  | The unique ID of the EMP user who documented this anesthesia staff member's end time. |
| 8 | `ANES_STAFF_ET_DOCU_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `AN_STAFF_TIME_SOURCE_STATUS_C_NAME` | VARCHAR |  | The source and status of the start and end time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

