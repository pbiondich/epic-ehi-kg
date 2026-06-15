# SPEC_WORKFLOW_STEP_HX

> This table contains information about the workflow step history of a specimen.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 4 | `TEST_ID_TEST_NAME` | VARCHAR |  | The name of the test record. |
| 5 | `WORKFLOW_STEP_RECORD_ID` | NUMERIC |  | The unique ID of the workflow step. |
| 6 | `WORKFLOW_STEP_RECORD_ID_RECORD_NAME` | VARCHAR |  | The name of the node record. |
| 7 | `WORKFLOW_STEP_TYPE_RECORD_ID` | VARCHAR |  | The unique ID of the event type corresponding to the workflow step. |
| 8 | `WORKFLOW_STEP_TYPE_RECORD_ID_RECORD_NAME` | VARCHAR |  | The name of the event template. |
| 9 | `COMPLETE_UTC_DTTM` | DATETIME (UTC) |  | The date and time at which the workflow step action occurred. |
| 10 | `COMPLETE_USER_ID` | VARCHAR |  | The unique ID of the user responsible for the workflow step action. |
| 11 | `COMPLETE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `WORKFLOW_STEP_RESULT_ID` | VARCHAR |  | The unique ID of the result snapshot taken when the user completed the workflow step. |
| 13 | `WORKFLOW_STEP_ACTION_C_NAME` | VARCHAR |  | Stores the workflow step action |
| 14 | `WORKFLOW_STEP_EVENT_RECORD_ID` | VARCHAR |  | Stores the event associated with the workflow step action |
| 15 | `WORKFLOW_STEP_EVENT_RECORD_ID_RECORD_NAME` | VARCHAR |  | The name of the event template. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

