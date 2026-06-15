# IP_WORKLIST_2

> This table contains data associated with task (LTK) records.

**Overflow of:** [IP_WORKLIST](IP_WORKLIST.md)  
**Primary key:** `TASK_ID`  
**Columns:** 42  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TASK_ID` | VARCHAR | PK shared | The unique identifier for the task record. |
| 2 | `DESC_FOR_PAT_OVRIDE` | VARCHAR |  | A descriptive name for instances of this task that is written specifically for a given patient. |
| 3 | `NAME_FOR_PAT_OVRIDE` | VARCHAR |  | A descriptive name for instances of this task at LTK level that is written specifically for patients. |
| 4 | `START_OFFSET_DAYS` | INTEGER |  | Number of days to offset the start date from the task assignment or the anchor event date. |
| 5 | `START_OFFSET_TYPE_C_NAME` | VARCHAR |  | The type of start date offset (e.g., before/after). |
| 6 | `SOURCE_LTT_UTC_DTTM` | DATETIME (Local) |  | Stores the instant the task template (LTT) was assigned which resulted in tasks (LTK) being created. |
| 7 | `CALCULATED_RESUME_UTC_DTTM` | DATETIME (UTC) |  | When resuming a paused task, this will be its start instant if no start date is specified. |
| 8 | `FLO_THRESHOLD_VALUE` | NUMERIC |  | Threshold value for flowsheet based task completion. |
| 9 | `TSK_DISCONTINUE_REASON_C_NAME` | VARCHAR |  | Describe the reason of the discontinued patient-assigned task. |
| 10 | `ENSURE_DELIVERY_C_NAME` | VARCHAR |  | Determines the scheduling behavior of this anchored task when its start date falls in the past. |
| 11 | `EFQ_OVRIDE_CYL_LEN` | INTEGER |  | If there is a frequency override specified, this item will contain the length of a relative specified type cycle. For all other specified types this value will be ignored (and should be empty). |
| 12 | `EFQ_OVRIDE_DAY_TYP` | INTEGER |  | Specifies what the numeric values in the frequency override days columns represent. If it is 1 then the listed days are relative days. If it is 2 then the listed days are weekdays. Any other value has no meaning. |
| 13 | `DURATION` | INTEGER |  | Determines the number of days this recurring task should go on for relative to its start date. |
| 14 | `TASK_NOTE_ID` | VARCHAR |  | The note (HNO) ID that is attached to the task (LTK) record. |
| 15 | `DECISION_TRACKER_ID` | NUMERIC |  | Stores the linked decision, if one exists, for this task |
| 16 | `REQ_DOC_NOT_ATTRIBUTED_RSN_C_NAME` | VARCHAR |  | The did not attribute reason category ID for the required documentation task. This indicates the reason that the task was not attributed to any users. |
| 17 | `USED_FOR_OUTREACH_YN` | VARCHAR |  | Indicates whether a checklist task is used for outreach or not. 'Y' indicates that the checklist task is used for outreach. 'N' or NULL indicates that the checklist task is not used for outreach. |
| 18 | `PAT_ASGN_TASK_PAT_ENC_CSN_ID` | NUMERIC | FK→ | If this task is anchored to an anchor target of type Hospital Discharge, then this item stores the contact serial number associated with the admission. |
| 19 | `SC_SUPPORT_TYPE_C_NAME` | VARCHAR | org | The category value of the support & service type that triggered the generation of this task |
| 20 | `SC_SUPPORT_TYPE_START_DATE` | DATETIME |  | The start date of the support & service type that triggered the generation of this task |
| 21 | `REFERRAL_ID` | NUMERIC | FK→ | The referral that this target is tracking. |
| 22 | `USED_FOR_C_NAME` | VARCHAR |  | The category number which identifies the purpose for which the task is used. |
| 23 | `CREATE_INST_LOCAL_DTTM` | DATETIME (Local) |  | The instant at which the task was created, in local time. This item is the local equivalent of the CREATION_UTC_DTTM column, which is in UTC. |
| 24 | `LINKED_PAT_ID` | VARCHAR | FK→ | This column contains the patient linked directly or indirectly to the task record. This differs from column PAT_ID in table IP_WORKLIST in that this column also contains patients linked indirectly to a task, through a patient CSN (I LTK 215) or an episode (HSB) (I LTK 53100 or I LTK 81110). To find only patients linked directly to a task, use column PAT_ID in table IP_WORKLIST. |
| 25 | `CREATE_USER_ID` | VARCHAR |  | User that created the task. |
| 26 | `CREATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 27 | `OUTREACH_OUTCOME_C_NAME` | VARCHAR | org | Outcome of an outreach task |
| 28 | `CLAIM_ID` | NUMERIC | FK→ | The claim that triggered this task's creation. |
| 29 | `CARE_PLAN_TYPE_C_NAME` | VARCHAR |  | Mark subtype of care plan task. Primarily used to mark if this care plan task instance is a note review task, for the suggested note workflow. |
| 30 | `MEDAC_LTK_STS_C_NAME` | VARCHAR |  | The current status for the task. |
| 31 | `MED_ACCESS_LTK_USER_ID` | VARCHAR |  | The current responsible user for the task. |
| 32 | `MED_ACCESS_LTK_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 33 | `MED_ACCESS_LTK_IB_POOL_ID` | NUMERIC |  | The current responsible pool for the task. |
| 34 | `MED_ACCESS_LTK_IB_POOL_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 35 | `MEDAC_LTK_WAITRSN_C_NAME` | VARCHAR |  | The reason the task's overall status is set to waiting. |
| 36 | `MEDAC_LTK_AUTOMATION_ORDER` | INTEGER |  | This item stores this task's order in the investigation's Automation Order (I HBD 76703) table. Tasks are set to Ready to Start based on the completion of preceding tasks in the investigation's Automation Order table. For example, if the user sets all tasks with an automation order of 1 as either Done or Not Needed, tasks with an automation order of 2 are automatically updated from Not Started to Ready to Start. |
| 37 | `EPISODE_COMPLEXITY_C_NAME` | VARCHAR | org | The category value of the episode complexity that triggered generation of this task |
| 38 | `UNTIMED_HOURS` | NUMERIC |  | This item determines how long untimed occurrences of this task are considered relevant. This item has no effect unless I LTK 382 Show as Untimed is set to 2-For a Number of Hours. |
| 39 | `SHOW_AS_UNTIMED_C_NAME` | VARCHAR |  | This item determines if occurrences of this task will be considered untimed when initially scheduled. Untimed tasks are scheduled for specific instants based on the task's frequency, but are considered relevant and continue to display to clinicians for a range of time starting at the initial scheduled instant and ending at a later instant determined by the value set here. If left blank, the task is not considered untimed. |
| 40 | `RESEARCH_ACTION_TYPE_C_NAME` | VARCHAR |  | The research action type for the task. Used to determine checklist links and autocompletion for research workflows. |
| 41 | `LINKED_DOC_TMPLT_ID_TEMPLT_DISPLAY_NAME` | VARCHAR |  | A name for the template designed for display purposes. |
| 42 | `LINKED_DOCUMENT_ID` | VARCHAR |  | The E-Signature document linked to this task. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |
| `LINKED_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `PAT_ASGN_TASK_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

