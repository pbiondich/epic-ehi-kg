# PUMP_PROGRAMMING

> This table contains compliance information about infusion pumps. The records included in this table are Alerts (ALT) records that track information about pump programming attempts.

**Primary key:** `ALERT_ID`, `LINE`  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALERT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the med alert record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INF_ACTION_TAKEN_C_NAME` | VARCHAR |  | The category ID of the action taken by the user after getting the message from the pump. |
| 4 | `INF_ERROR_TITLE` | VARCHAR |  | The title of the message from the pump that is displayed to the user. |
| 5 | `INF_ERROR_TEXT` | VARCHAR |  | The message text from the pump that is displayed to the user. |
| 6 | `INF_INT_STAT_C_NAME` | VARCHAR |  | The category ID of the status of the message from the pump. |
| 7 | `INF_SEND_INST_DTTM` | DATETIME (UTC) |  | The instant when the pump program was sent to the infusion pump. |
| 8 | `INF_RESPONSE_I_DTTM` | DATETIME (UTC) |  | The instant when the response was received from the infusion pump. |
| 9 | `INF_MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 10 | `INF_ORDER_ID` | NUMERIC |  | The unique ID of the order that is associated with this message from the pump. |
| 11 | `INF_USER_ID` | VARCHAR |  | The unique ID of the user that is associated with this message from the pump. This column is frequently used to link to the CLARITY_EMP table. |
| 12 | `INF_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `INF_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 14 | `INF_DEVICE_ID` | VARCHAR |  | The unique ID of the device that is associated with this message from the pump. |
| 15 | `INF_DEVICE_ID_DEVICE_NAME` | VARCHAR |  | The name for this device. |
| 16 | `INF_LINE_NUMBER` | INTEGER |  | The line number for the most recent prior message sent to the pump for the same order for the same patient encounter. |
| 17 | `VOLUME_TO_INFUSE_IN_ML` | NUMERIC |  | The volume to infuse in mL that was sent to the pump. |
| 18 | `INF_ATTEMPT_UTC_DTTM` | DATETIME (UTC) |  | Tracks the instant the user attempted to program the pump |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

