# TPL_TXDAYS

> This table contains the treatment days in a treatment plan record or the steps in a pathway record.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 43  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The treatment plan ID. |
| 2 | `LINE` | INTEGER | PK | The line number that corresponds to each treatment day in the treatment plan in this row. |
| 3 | `TREATMENT_DAY_ID` | NUMERIC |  | The treatment day row ID of a treatment day in the treatment plan. |
| 4 | `TX_DAY_TYPE_C_NAME` | VARCHAR |  | The treatment day type (outpatient or inpatient) of a treatment day in the treatment plan. |
| 5 | `TREATMENT_DAY_DAT` | VARCHAR |  | The contact date (DAT) of a treatment day record in the treatment plan. |
| 6 | `TREATMENT_DAY_NAME` | VARCHAR |  | The treatment day name of a treatment day in the treatment plan. |
| 7 | `TRT_CYCLE` | VARCHAR |  | The cycle containing a treatment day in the treatment plan. |
| 8 | `TREATMENT_DATE` | DATETIME |  | The planned date in external format when a treatment day in the treatment plan is expected to occur. |
| 9 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The contact serial number (CSN) of the first patient encounter in which an order from this treatment day was released. |
| 10 | `TRT_DAY_STATUS_C_NAME` | VARCHAR |  | The status of a treatment day in the treatment plan. For example, Planned, Scheduled, Deferred, Canceled, Completed, or Deleted. |
| 11 | `TRT_DAY_WAIT_AFTER` | NUMERIC |  | The number of days to wait after a treatment day in the treatment plan. |
| 12 | `TRT_DAY_MAX_LEAD` | NUMERIC |  | The max lead of a treatment day in the treatment plan. |
| 13 | `TRT_DAY_MAX_LAG` | NUMERIC |  | The max lag of a treatment day in the treatment plan. |
| 14 | `TRT_DAY_UNIQ_ID` | VARCHAR |  | A cycle-level unique ID of a treatment day in the treatment plan. |
| 15 | `TRT_DAY_NUM` | INTEGER |  | The treatment day number for this treatment day. |
| 16 | `STEP_START_DTTM` | DATETIME (Local) |  | The start date and time of the step. |
| 17 | `MANUAL_STRT_STP_YN` | VARCHAR |  | This flag indicates whether the step should be manually started. Y indicates that the step should be started manually. A null value or N indicates that the step doesn't need to be started manually. |
| 18 | `MANUAL_STRT_USER_ID` | VARCHAR |  | The user who manually started the step. |
| 19 | `MANUAL_STRT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 20 | `MANUAL_STRT_DTTM` | DATETIME (Local) |  | The date and time when the step was manually started. |
| 21 | `STEP_DURATION_SECS` | NUMERIC |  | This item stores the duration of the step in seconds. This value can be added to the start date and time to get the end date and time of the step. |
| 22 | `TX_STAT_CHG_USER_ID` | VARCHAR |  | This item stores the ID of the user who changed the status of this treatment day. |
| 23 | `TX_STAT_CHG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 24 | `DAY_LENGTH` | INTEGER |  | The number of calendar days that are represented by the treatment day. |
| 25 | `TX_STATUS_CHG_DTTM` | DATETIME (Local) |  | Stores the instant at which the day status changed. |
| 26 | `DAY_CREATED_BY_ID` | VARCHAR |  | Stores the ID of the user who created the treatment day. |
| 27 | `DAY_CREATED_BY_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 28 | `DAY_CREATE_DTTM` | DATETIME (Local) |  | Instant when the treatment day was created. |
| 29 | `DAY_CREATE_COMMENT` | VARCHAR |  | Additional comment entered by user when creating the treatment day. |
| 30 | `DAY_SOURCE_UID` | VARCHAR |  | Stores the unique ID of the day from which it was created. |
| 31 | `TX_PLANNED_DT` | DATETIME |  | Stores the planned date for the treatment day. |
| 32 | `TX_STARTED_DTTM` | DATETIME (UTC) |  | Stores the instant at which the day was started. |
| 33 | `DAY_SOURCE_CSN` | NUMERIC |  | When the treatment plan day is created from a protocol (PRL), the source treatment day (OSQ)'s contact serial number will be set in this item. If the treatment plan day is copied or deferred, this item will be copied into the new day. |
| 34 | `AUTO_COMP_STATUS_C_NAME` | VARCHAR |  | The status of the "Status" item of the day. Used in the cases where the system changes the status of the day (mainly auto-completes a day) so that we can determine if we need to let the user know about it the next time they open the plan. |
| 35 | `TREAT_DAY_CONTACT_DATE_REAL` | FLOAT |  | The contact date real of the treatment day (TRG) record which is held in this row. The contact date real is a unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 36 | `DEFERRED_FROM_LN` | INTEGER |  | If this treatment day was created by deferring another treatment day, this item will contain the line number of that deferred treatment day. |
| 37 | `CONVERSION_TARGET` | INTEGER |  | If this day was replaced for conversion, this will be the day (given by line in SI TPl 5000) that replaced it. |
| 38 | `DAY_SOURCE_INSTANCE_NUM` | INTEGER |  | For the clinical protocol treatment day contact indicated by the contact serial number in the DAY_SOURCE_CSN column, this column stores the instance number (or repetition number) represented by this day in the treatment plan. |
| 39 | `TX_SCHED_DATE` | DATETIME |  | Stores the date for which the treatment day is scheduled. |
| 40 | `TX_SCHED_CONFLICT_C_NAME` | VARCHAR | org | Stores whether the scheduled date of the treatment day is outside tolerance range or if multiple appointments are scheduled for the same treatment day. |
| 41 | `DAY_PATTERN_SOURCE_LINE` | INTEGER |  | For this day, if it was created from a pattern day, this item will store the source line in SI TPL 13000 it was created from. |
| 42 | `DAY_NOTE_ID` | VARCHAR |  | The unique ID of the note record that contains the notes for a given day in the treatment plan. |
| 43 | `DAY_CREATION_METHOD_C_NAME` | VARCHAR |  | If this day was created from a repeating cycle, this column specifies whether it was created manually or automatically. This item will be blank if the day was not created from a repeating cycle, or if it was created by copying and pasting a repeating day. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

