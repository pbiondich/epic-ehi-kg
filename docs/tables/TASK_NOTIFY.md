# TASK_NOTIFY

> Extracted data about the patient notification of upcoming tasks.

**Primary key:** `ACTIVITY_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACTIVITY_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the task record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SHARE_OUTREACH_DATE` | DATETIME |  | This is the date that the proactive outreach SMS message will be shared with the patient. |
| 4 | `SHARE_LTK_STATUS_C_NAME` | VARCHAR | org | Tracks the internal status of the scheduling for outbound Hello World messages. This status won't be updated after the message is actually sent. The external status can be gathered by looking at the RCH contact referenced from [I LTK 25102] to see if the message was sent. The primary function of this item is for the dual-key index with 25100, the batch job will look over LTK's that haven't been scheduled already. |
| 5 | `SHARE_LTK_CSN` | INTEGER |  | Stores the CSN for the scheduled proactive outreach SMS message. It will be used to determine the current status of the SMS message. It will also be used as a reference point if we need to cancel the SMS message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

