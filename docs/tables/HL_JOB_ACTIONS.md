# HL_JOB_ACTIONS

> Hospital Logistics Requests Actions.

**Primary key:** `HLR_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLR_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HL_ACTION_HL_REQ_STATUS_C_NAME` | VARCHAR |  | The status that triggered the corresponding action. |
| 4 | `HL_ACTION_C_NAME` | VARCHAR |  | The action that was triggered when this Request reached the corresponding status. |
| 5 | `HL_ACTION_RESULT_C_NAME` | VARCHAR |  | The result of the corresponding action. If the action failed, this will include the reason for failure. |
| 6 | `HL_ACTION_SOURCE_HLR_ID` | NUMERIC |  | The Logistics Request or Job (HLR) that was the source of this action. For single-stage Requests, this will always be this Job. For multi-stage Requests, this will either be this Job or this Job's parent Request. If a Job has the same Task as its parent Request, only actions sourced from the parent request will be triggered by that Job; the Job's actions will be ignored. |
| 7 | `HL_ACTION_HL_REQ_STATUS_MOD_C_NAME` | VARCHAR |  | The status modifier that triggered the corresponding action. |
| 8 | `HL_ACTION_HL_REQ_HOLD_TYPE_C_NAME` | VARCHAR |  | The hold type that triggered the corresponding action when Job Action Status Modifier (I HLR 276) equals 2 - Hold. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

