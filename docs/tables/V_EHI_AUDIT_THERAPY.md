# V_EHI_AUDIT_THERAPY

> Translates THERAPY_AUDIT.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 22  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PLAN_OTP_ID` | NUMERIC |  | The unique ID of the parent order template record that is affected by the change in this row. |
| 4 | `INTERVAL_C_NAME` | VARCHAR |  | The category number for the interval. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 5 | `REQ_TOTAL_COUNT` | INTEGER |  | The count of treatments requested for the affected order template. |
| 6 | `START_DATE` | DATETIME |  | The initial date on which the affected order template may be shown to be due. |
| 7 | `ORDER_CAT_HX_C_NAME` | VARCHAR | org | The category number for order category associated with the order template in this row. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 8 | `CHANGE_DTTM_DTTM` | DATETIME (Local) |  | The date and time when the change audited in this row was made. |
| 9 | `CHANGE_USER_ID` | VARCHAR |  | The unique ID associated with the user record for this row. This identifies the user making the change audited in this row. This column is frequently used to link to the CLARITY_EMP table. |
| 10 | `CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `CHANGE_TYPE_C_NAME` | VARCHAR |  | The category number for the type of change audited in this row. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 12 | `CONTEXT_OTP_ID` | NUMERIC |  | The unique ID of the child order template affected by the change in this row. This value will only be present for certain types of changes. |
| 13 | `MIN_TREAT_SEP_HX` | INTEGER |  | Historical record of changes to the minimum treatment separation value for an order. |
| 14 | `TREAT_DIST_HX_C_NAME` | VARCHAR |  | Category item, stores the changes to the treatment distribution type. Changes stored for reporting purposes. |
| 15 | `INTER_DET_DESC_HX` | VARCHAR |  | Stores the changes to the interval details description item. Changes stored for reporting purposes. |
| 16 | `NEXT_DUE_DATE` | DATETIME |  | Stores the history of next due date of the linked order. |
| 17 | `END_DATE` | DATETIME |  | This item stores the history of end date for an order after which the order should be completed. |
| 18 | `NUMBER_OF_RELEASES` | INTEGER |  | Stores the number of times the linked order has been released when calculating due dates. |
| 19 | `MANUAL_DUE_DATE` | DATETIME |  | Stores the manual due date of the linked order. |
| 20 | `NEXT_DUE_TREATMENT` | INTEGER |  | Stores the next treatment the linked order is due on. |
| 21 | `PLAN_OTP_NAME` | VARCHAR |  | The display name of the plan order template. |
| 22 | `CONTEXT_OTP_NAME` | VARCHAR |  | The display name of the context order template. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

