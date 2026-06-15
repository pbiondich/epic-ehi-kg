# PLAN_HOLD_HISTORY

> The history of all the instances when a treatment plan was put on hold.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 16  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_HOLD_INST_UTC_DTTM` | DATETIME (UTC) |  | A history of when this plan was put on hold. This is the UTC instant when it was put on hold. |
| 4 | `HX_HOLD_USER_ID` | VARCHAR |  | A history of when this plan was put on hold. This is the user who put the plan on hold. |
| 5 | `HX_HOLD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `HX_HOLD_REASON_C_NAME` | VARCHAR | org | A history of when this plan was put on hold. This is the reason for putting the plan on hold. |
| 7 | `HX_HOLD_COMMENT` | VARCHAR |  | A history of when this plan was put on hold. This is the comment for putting the plan on hold. |
| 8 | `HX_RELEASE_INST_UTC_DTTM` | DATETIME (UTC) |  | A history of when this plan was put on hold. This is the UTC instant when the hold on the plan was released. |
| 9 | `HX_RELEASE_USER_ID` | VARCHAR |  | A history of when this plan was put on hold. This is the user who released the plan from hold. |
| 10 | `HX_RELEASE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `HX_RELEASE_REASON_C_NAME` | VARCHAR | org | A history of when this plan was put on hold. This is the reason for releasing the hold from the plan. |
| 12 | `HX_RELEASE_COMMENT` | VARCHAR |  | A history of when this plan was put on hold. This is the comment given for releasing the hold from the plan. |
| 13 | `HX_HOLD_ADT_ID` | NUMERIC |  | If this plan was put on hold because of an ADT event, this will be the ID of that ADT event. |
| 14 | `HX_HOLD_IS_UNDO_YN` | VARCHAR |  | Whether this hold action was the result of undoing an ADT event. |
| 15 | `HX_RELEASE_ADT_ID` | NUMERIC |  | If this plan was released from hold because of an ADT event, this will be the ID of that ADT event. |
| 16 | `HX_RELEASE_IS_UNDO_YN` | VARCHAR |  | Whether this release from hold action was the result of undoing an ADT event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

