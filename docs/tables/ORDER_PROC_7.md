# ORDER_PROC_7

> The ORDER_PROC_7 table enables you to report on the procedures ordered in the clinical system. This procedure table has the same basic structure as ORDER_PROC, but was created as a seventh table to prevent ORDER_PROC_6 from getting any larger.

**Overflow of:** [ORDER_PROC](ORDER_PROC.md)  
**Primary key:** `ORDER_ID`  
**Columns:** 16  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `RAD_THERAPY_GOAL_C_NAME` | VARCHAR | org | This item stores the goal for prescribed radiation therapy treatment. |
| 3 | `RT_EPISODE_OPTION_C_NAME` | VARCHAR |  | Indicates if the procedure should generate a new radiation therapy episode, update an existing episode, or have no interaction with an episode. |
| 4 | `ASSOCIATED_RAD_THP_EPISODE_ID` | NUMERIC |  | The existing radiation therapy episode this order should be associated with. The radiation therapy details documented in the order will be added to the episode. |
| 5 | `CLINICAL_SEX_PARAM_C_NAME` | VARCHAR |  | The "Sex Parameter for Clinical Use" (sex categorization that aligns most with the patient in the context of the current order) category ID for the order. |
| 6 | `CLINICAL_SEX_PARAM_COMMENT` | VARCHAR |  | The "Sex Parameter for Clinical Use" (sex categorization that aligns most with the patient in the context of the current order) comments entered in the Order Composer. |
| 7 | `CLINICAL_SEX_PARAM_UTC_DTTM` | DATETIME (UTC) |  | Last update date and time in UTC for Sex Parameter for Clinical Use, the sex categorization that aligns most with the patient in the context of the current order. |
| 8 | `TODAYS_FOCUS_YN` | VARCHAR |  | This items tracks whether the order is today's focus, indicating that a provider is waiting on the order to advance the patient to their next step of care. This item can be set through Patient Availability print group. |
| 9 | `TODAYS_FOCUS_UTC_DTTM` | DATETIME (UTC) |  | Instant that a user marked the order as today's focus, indicating that a provider is waiting on the order to advance the patient to the next step of care. This instant is stored in UTC. |
| 10 | `TODAYS_FOCUS_USER_ID` | VARCHAR |  | User who marked the order as today's focus, indicating that a provider is waiting on the order to advance the patient to the next step of care. |
| 11 | `TODAYS_FOCUS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `HISTORICAL_ORDER_YN` | VARCHAR |  | Whether the order class or procedure was marked as historical at signing. |
| 13 | `LAST_MAMMO_WT_SRC_C_NAME` | VARCHAR |  | Indicates the source of the last mammo weight value. |
| 14 | `EXAM_MAMMO_WT_SRC_C_NAME` | VARCHAR |  | Indicates the source of this exam's mammo weight value. |
| 15 | `PROC_CODE_DESC` | VARCHAR |  | The Procedure Code Description - Stores Additional Information about the Procedure |
| 16 | `ENTRY_START_LOCAL_DTTM` | DATETIME (Local) |  | This table contains the date and time when the user initiates a new session to create orders. This is currently populated only for orders placed from Ancillary Orders and is used to report transcription time for imaging orders that are manually transcribed from scanned documents. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [ORDER_PROC](ORDER_PROC.md).

