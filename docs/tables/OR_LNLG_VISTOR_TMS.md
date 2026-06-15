# OR_LNLG_VISTOR_TMS

> The OR_LNLG_VISTOR_TMS table stores the in/out time information of the visitors who visited the surgery.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the record that contains the information about a single visitor who visited the surgery. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. Each line contains in/out time for the visitor. A visitor may have multiple in/out times if he/she entered and exited the surgery multiple times. Each in/out time pair is stored as a separate line. |
| 3 | `VISITOR_ST_CMT` | VARCHAR |  | Visitor start time comment |
| 4 | `VISITOR_ET_CMT` | VARCHAR |  | Visitor end time comment |
| 5 | `VISITOR_ST_DOCU_ID` | VARCHAR |  | The unique ID of the EMP user who documented this visitor's start time. |
| 6 | `VISITOR_ST_DOCU_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `VISITOR_ET_DOCU_ID` | VARCHAR |  | The unique ID of the EMP user who documented this visitor's end time. |
| 8 | `VISITOR_ET_DOCU_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

