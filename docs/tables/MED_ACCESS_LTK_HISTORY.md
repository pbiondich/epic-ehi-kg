# MED_ACCESS_LTK_HISTORY

> History of med access tasks.

**Primary key:** `ACTIVITY_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACTIVITY_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the task record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MEDAC_LTK_STS_C_NAME` | VARCHAR |  | A list of statuses the task has gone through. |
| 4 | `MA_HX_LTK_USER_ID` | VARCHAR |  | The new responsible user at the time the change was made. |
| 5 | `MA_HX_LTK_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `MA_HX_LTK_IB_POOL_ID` | NUMERIC |  | The new responsible pool at the time the change was made. |
| 7 | `MA_HX_LTK_IB_POOL_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 8 | `MA_HX_LTK_INST_UTC_DTTM` | DATETIME (UTC) |  | A timestamp for when the change was made. |
| 9 | `MA_HX_LTK_EDIT_USER_ID` | VARCHAR |  | The user who made the change. |
| 10 | `MA_HX_LTK_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `MA_HX_MEDAC_LTK_WAITRSN_C_NAME` | VARCHAR |  | The reason the task's status was set to waiting. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

