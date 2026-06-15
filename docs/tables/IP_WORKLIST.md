# IP_WORKLIST

> This table contains data associated with task (LTK) records.

**Overflow family:** [IP_WORKLIST_2](IP_WORKLIST_2.md)  
**Primary key:** `TASK_ID`  
**Columns:** 57  
**Org-specific columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TASK_ID` | VARCHAR | PK shared | The unique ID for the worklist activity. |
| 2 | `TASK` | VARCHAR |  | The task to be performed. |
| 3 | `WL_PRIORITY_C_NAME` | VARCHAR | org | This notes the priority of the task. |
| 4 | `WORK_UNITS` | FLOAT |  | This is the number of work units required to perform a task. |
| 5 | `SKILLS_NEEDED_C_NAME` | VARCHAR | org | This is the skill set required to perform a task. |
| 6 | `WORKLIST_CAT_C_NAME` | VARCHAR | org | The category associated with this task (i.e. meds, education, vitals). |
| 7 | `LINK_SOURCE` | VARCHAR |  | The master file initials for the record that is the source of this task. This can be LPI, ORD, LGL, FLO, IGL, LDA, SSC, or DM_CSN. If the Source is : Best Practice Alert then LOCATOR_ID has the Alert ID (LGL) |
| 8 | `LINK_RECORD` | VARCHAR |  | The ID of the record that is the source of this task. |
| 9 | `LOCATOR_ID_LOCATOR_NAME` | VARCHAR |  | The name of the Locator record. |
| 10 | `INTERVENTION_ID` | VARCHAR | FK→ | If the task is linked to an intervention (LPI masterfile) the ID of the Care Plan Intervention is stored here. |
| 11 | `ORDER_ID` | NUMERIC | shared | If the task is linked to an Order (ORD masterfile) the ID of the Order is stored here. |
| 12 | `MSTEP_STATUS_C_NAME` | VARCHAR | org | Stores the status of the given multistep order entry task |
| 13 | `TYPE_C_NAME` | VARCHAR |  | The type associated with this task. |
| 14 | `LINK_SOURCE_COMP` | VARCHAR |  | The master file initials for the record that is the source of this task. This can be LPI, ORD, LGL, FLO, IGL, LDA, SSC, or DM_CSN. If the Source is : Best Practice Alert then LOCATOR_ID has the Alert ID (LGL) |
| 15 | `COMMENTS` | VARCHAR |  | This item stores the comments related to the given worklist activity. |
| 16 | `SOURCE_LTR_ID` | NUMERIC |  | This item stores the unique ID of the task record associated with the worklist activity. |
| 17 | `SOURCE_LTR_ID_TASK_NAME` | VARCHAR |  | The name of the task record. |
| 18 | `AUTO_COMPLETE_COND` | VARCHAR |  | This column stores the task auto complete condition, which is copied from the associated task (LTR) record. |
| 19 | `NUM_OCCURRENCES` | INTEGER |  | This column stores the number of occurrences for the associated task. |
| 20 | `PRN_START_INST_DTTM` | DATETIME (Local) |  | This column stores the start instant for a scheduled task. |
| 21 | `DISCONTINUE_DTTM` | DATETIME (Local) |  | This column stores the instant at which a task was discontinued. |
| 22 | `DISCONTINUE_USER_ID` | VARCHAR |  | User who discontinued a task. |
| 23 | `DISCONTINUE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 24 | `EPISODE_ID` | NUMERIC | FK→ | The episode ID with which the task is associated. |
| 25 | `RESPONSIBLE_USER_ID` | VARCHAR |  | The user responsible to complete the task. |
| 26 | `RESPONSIBLE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 27 | `RESPONSIBLE_POOL_ID` | NUMERIC |  | The In Basket Pool responsible for completing the task. |
| 28 | `RESPONSIBLE_POOL_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 29 | `BEDSIDE_USER_ID` | VARCHAR |  | The Initiating Bedside User item holds the ID of the MyChart Bedside User who created an ad hoc task, typically a patient request. |
| 30 | `PAT_COMMENTS` | VARCHAR |  | This item stores the Patient entered comments/additional details for requests they place in MyChartBedside. |
| 31 | `STEP_C_NAME` | VARCHAR | org | The current step of a multi-step task. |
| 32 | `OUTCOME_C_NAME` | VARCHAR | org | The outcome of the task. |
| 33 | `AUTOCOMP_INSTANCE_ID` | NUMERIC |  | The deficiency instance associated with this task. This column will be populate for episode-based tasks that are created from a task record (LTR) with an associated autocompletion template (DEF). |
| 34 | `PARENT_TASK_ID` | VARCHAR |  | The parent task (LTK) that this child task was created from. This column will be populated for episode-based tasks that were created automatically based on the completion of another task on the episode. |
| 35 | `REQUIRED_DOC_TYPE_C_NAME` | VARCHAR |  | Type of required documentation the task corresponds to. |
| 36 | `REQUIRED_DOC_GROUP_C_NAME` | VARCHAR | org | Required documentation group the task corresponds to. |
| 37 | `CONTEXT_C_NAME` | VARCHAR |  | The functional context of a task. |
| 38 | `ASSIGN_TO_PAT_C` | VARCHAR |  | This item determines whether a task is assigned to the patient. |
| 39 | `PERS_STATUS_C_NAME` | VARCHAR | org | Defines the personalization status of the notification times for the task. |
| 40 | `GOAL_ID` | VARCHAR | FK→ | The goal that the task is associated with. |
| 41 | `INTERVENTIONS_ID` | VARCHAR |  | The intervention that the task is associated with. |
| 42 | `LINKED_TREATMENT_DAY_NAME` | VARCHAR |  | The name of the treatment day linked to the task. |
| 43 | `LINKED_TREATMENT_PLAN_ID` | NUMERIC |  | The unique ID of the treatment plan linked to this task. |
| 44 | `LINKED_DAY_LINE` | INTEGER |  | The line in the source record that corresponds to a treatment or timeline day. |
| 45 | `EST_COMPLETION_START_DATE` | DATETIME |  | An estimated start date that the task will be performed based on the lead days of the day in the treatment plan or timeline. |
| 46 | `EST_COMPLETION_END_DATE` | DATETIME |  | An estimated end date that the task will be performed based on the lag days of the day in the treatment plan or timeline. |
| 47 | `ENROLL_ID` | NUMERIC | FK→ | The research study-patient association (LAR) record ID linked to this task. This is only populated by tasks created from a billing timeline. |
| 48 | `SOURCE_LTT_ID` | VARCHAR |  | This contains a link to the source task template (LTT) record if this task was added by a task template. |
| 49 | `SOURCE_LTT_ID_RECORD_NAME` | VARCHAR |  | This column displays the name of the task template record. |
| 50 | `IS_PAUSED_YN` | VARCHAR |  | When a task is assigned to the patient, this item determines whether it's is paused. When a task is paused, it will not have future instances and will not displayed to the patient until resumed. |
| 51 | `SCHEDULE_STATUS_C_NAME` | VARCHAR |  | Determines the scheduling status of a patient-assigned task. When a task is created it may not be scheduled right away. The category table is ZC_TASK_SCHEDULE_STATUS_C. |
| 52 | `RESUME_ON_DISCHARGE_YN` | VARCHAR |  | This item determines if a task paused on hospital admission will be resumed on discharge. |
| 53 | `DAYS_AFTER_DISC_NUM` | INTEGER |  | Indicates the number of days after hospital discharge this reminder will start. Value must be larger than or equal to 0. |
| 54 | `ANCHOR_EVENT_TYPE_C_NAME` | VARCHAR |  | The type of anchor target this task is configured for. |
| 55 | `SURGICAL_OR_CASE_ID` | VARCHAR |  | If this task is anchored to an anchor target of type Surgery, then this item stores the surgical case associated with the surgery. |
| 56 | `PREGNANCY_EPISODE_ID` | NUMERIC |  | If this task is anchored to an anchor target of type Pregnancy, then this item stores the episode associated with the pregnancy. |
| 57 | `APPOINTMENT_SERIAL_NUMBER_ID` | NUMERIC |  | If this task is anchored to an anchor target of type Procedural Appointment, then this item stores the appointment serial number associated with the procedural appointment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |
| `GOAL_ID` | [GOAL](GOAL.md) | name_stem | high |
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |

