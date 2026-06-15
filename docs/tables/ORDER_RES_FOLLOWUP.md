# ORDER_RES_FOLLOWUP

> Table for lab follow-up tasks.

**Primary key:** `FINDING_ID`  
**Columns:** 32  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique ID of the Result Finding record. |
| 2 | `LAB_STATUS_C_NAME` | VARCHAR |  | The status category number for the lab follow-up task. |
| 3 | `LAB_ASSIGNED_EMP_ID` | VARCHAR |  | The unique ID of the user who is assigned responsibility for the follow-up task. |
| 4 | `LAB_ASSIGNED_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `LAB_SPECIMEN_ID` | VARCHAR |  | The unique ID of the specimen that is associated with this follow-up task. |
| 6 | `LAB_TEST_ID_TEST_NAME` | VARCHAR |  | The name of the test record. |
| 7 | `LAB_ORDER_ID` | NUMERIC |  | The unique ID of the order that is associated with the comm log follow-up task. |
| 8 | `LAB_ADD_INSTANT` | DATETIME (Local) |  | The instant when the follow-up task was added or reopened. |
| 9 | `LAB_REQUISITION_ID` | NUMERIC |  | The unique ID of the requisition that is associated with this follow-up task. |
| 10 | `LAB_TYPE_REQ_FOLL_C_NAME` | VARCHAR | org | The follow-up type category number for the lab requisition follow-up task. |
| 11 | `LAB_ADDING_EMP_ID` | VARCHAR |  | The unique ID of the user who is responsible for adding the follow-up task to the list. |
| 12 | `LAB_ADDING_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `LAB_REMOVE_EMP_ID` | VARCHAR |  | The unique ID of the user who is responsible for removing the follow-up task from the list. |
| 14 | `LAB_REMOVE_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `LAB_REQ_MISSING_ITM` | VARCHAR |  | List of missing required requisition items. |
| 16 | `LAB_REC_MISSING_ITM` | VARCHAR |  | List of missing recommended requisition items. |
| 17 | `RESULT_TYPE_C_NAME` | VARCHAR |  | The result type category number for the lab follow-up task. |
| 18 | `LAB_DUE_TM` | DATETIME (Local) |  | The current due time for this lab follow-up task. |
| 19 | `LAB_START_TM` | DATETIME (Local) |  | The current start time for this lab follow-up task. |
| 20 | `LAB_REQ_GRP_ID` | NUMERIC |  | The unique ID of the requisition grouper that is associated with this follow-up task. |
| 21 | `LAB_REMOVE_TM` | DATETIME (Local) |  | The time the follow-up task was removed from the work list. |
| 22 | `LAB_ACTION_DT` | DATETIME |  | The date the next action will be executed for this follow-up record. |
| 23 | `LAB_ACTION_ID` | NUMERIC |  | The unique ID of the follow-up action record that will be triggered at the next action date. |
| 24 | `LAB_ACTION_ID_RECORD_NAME` | VARCHAR |  | The name of the node record. |
| 25 | `ASSOC_LABORATORY_ID_LAB_NAME` | VARCHAR |  | The name of the lab record. |
| 26 | `LAB_FU_SUBM_ID` | NUMERIC |  | The unique ID of the submitter that is associated with this follow-up task record. |
| 27 | `LAB_FU_SUBM_ID_RECORD_NAME` | VARCHAR |  | The name of the submitter record. |
| 28 | `LAB_RMV_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | Indicates the UTC instant a task was removed from the work list. |
| 29 | `LAB_DUE_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | Lab follow-up task due instant in UTC |
| 30 | `LAB_START_INST_UTC_DTTM` | DATETIME (UTC) |  | Lab follow-up task start instant in UTC |
| 31 | `LAB_ADD_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | Indicates the UTC instant a task was added to the work list, either initially or when a previously closed task was re-opened. |
| 32 | `TEST_LINE` | INTEGER |  | The test line on the specimen that the follow-up is associated with. This column can be used with the LAB_SPECIMEN_ID column to join to the SPEC_TEST_REL table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

