# V_EHI_AUDIT_TPL_DAY

> Translates DAY_AUDIT_TRAIL.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DAY_AUD_ACTION_C_NAME` | VARCHAR |  | Stores the action taken on the day. |
| 4 | `DAY_AUD_LINE_NUM` | VARCHAR |  | Stores the line number of the day in the treatment plan. |
| 5 | `DAY_AUD_USR_ID` | VARCHAR |  | Stores the user who performed the action. |
| 6 | `DAY_AUD_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `DAY_AUD_UTC_DTTM` | DATETIME (UTC) |  | Stores the UTC instant at which the action was performed. |
| 8 | `DAY_AUD_OLD_TRT_DAY_STATUS_C` | INTEGER |  | Stores the old day status. |
| 9 | `DAY_AUD_NEW_TRT_DAY_STATUS_C` | INTEGER |  | Stores the new day status. |
| 10 | `DAY_AUD_OLD_PLANNED_DATE` | DATETIME |  | Stores the old day planned date. |
| 11 | `DAY_AUD_NEW_PLANNED_DATE` | DATETIME |  | Stores the new day planned date. |
| 12 | `DAY_AUD_OLD_DAY_TYPE_C` | VARCHAR |  | Stores the old day type. |
| 13 | `DAY_AUD_NEW_DAY_TYPE_C` | VARCHAR |  | Stores the new day type. |
| 14 | `DAY_AUD_OLD_LENGTH` | INTEGER |  | Stores the old day length. |
| 15 | `DAY_AUD_NEW_LENGTH` | INTEGER |  | Stores the new day length. |
| 16 | `DAY_AUD_GIVEN_EXTER_RSN_C` | INTEGER |  | Stores the reason for marking a day as given externally. |
| 17 | `DAY_AUD_DEFER_DAY_RSN_C` | INTEGER |  | Stores the reason for deferring a day. |
| 18 | `DAY_AUD_CANCEL_DAY_RSN_C` | INTEGER |  | Stores the reason for canceling a day. |
| 19 | `DAY_AUD_COMMENT` | VARCHAR |  | Stores the comment for performing the action. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

