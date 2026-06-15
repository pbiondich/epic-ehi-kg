# MYC_MESG_TASK

> Message tasks are discrete activities that can be attached to a message sent from an system user to a patient. The task contains an action item for the patient to complete, such as filling out a questionnaire or scheduling an appointment. This table stores data regarding tasks that have been attached to Patient Access Message (WMG) records, such as what type of a task it was and when the task was completed by a patient.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The unique ID used to identify a web based chart system message record. |
| 2 | `LINE` | INTEGER | PK | The line number used to identify each row of read data associated with an individual web based chart system message record. |
| 3 | `TASK_TYPE_C_NAME` | VARCHAR |  | A category value corresponding to the type of the current message task. Example types are Appointment and Questionnaire. Link to the ZC_MYC_TASK_TYPE table to get the task names. |
| 4 | `TASK_TYPE_ORD_NUM` | INTEGER |  | This is the message task type ordinal number. It is used in conjunction with TASK_TYPE_C and indicates if a given message task is the first, second, third etc., of a given message type to be attached to the message. For example, if there were three Appointment tasks and two Questionnaire tasks attached to a given web based chart system message, the first Appointment would have a TASK_TYPE_ORD_NUM of 1, the second Appointment would have a TASK_TYPE_ORD_NUM of 2, and the third Appointment would have a TASK_TYPE_ORD_NUM of 3. Similarly, the first Questionnaire task would have a TASK_TYPE_ORD_NUM of 1 and the second Questionnaire task would have a TASK_TYPE_ORD_NUM of 2. |
| 5 | `TASK_DISPLAY_NAME` | VARCHAR |  | This is the display name of the task (what the patient will see in web based chart system). |
| 6 | `TASK_COMP_DATE` | DATETIME (Attached) |  | This stores the instant the message task was completed. If the task has not been completed, this item is blank. |
| 7 | `TASK_COMP_WPR_ID` | VARCHAR |  | The ID of the person who completed the task. |
| 8 | `TASK_SCHED_APPT_REQUEST_ID` | NUMERIC |  | The appointment request order IDs linked to this message as a scheduling task for the patient |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

