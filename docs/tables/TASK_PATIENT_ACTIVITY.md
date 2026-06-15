# TASK_PATIENT_ACTIVITY

> This table contains data about patient tasks assigned by MyChart Care Companion.

**Primary key:** `ACTIVITY_ID`  
**Columns:** 62  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACTIVITY_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the task record. |
| 2 | `TASK_TYPE_C_NAME` | VARCHAR |  | The task type. |
| 3 | `TASK_CONTEXT_C_NAME` | VARCHAR |  | The functional context of a task. |
| 4 | `DOCMNT_TYPE_C_NAME` | VARCHAR |  | The documentation type for this task. |
| 5 | `TASK_SCHEDULE_STATUS_C_NAME` | VARCHAR |  | The scheduling status of a patient-assigned task. When a task is created it may not be scheduled right away. |
| 6 | `IS_PAUSED_YN` | VARCHAR |  | Whether a task is assigned to the patient is paused. When a task is paused, it will not have future instances and will not displayed to the patient until resumed. |
| 7 | `GOAL_ID` | VARCHAR | FK→ | The goal that the task is associated with. |
| 8 | `FREQ_ID` | VARCHAR | FK→ | If you would like this activity to be performed at a different frequency than the ordering frequency, enter it here. |
| 9 | `FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 10 | `CASE_ID` | VARCHAR | shared | If this task is anchored to an anchor target of type Surgery, then this item stores the surgical case associated with the surgery. |
| 11 | `CARE_INTG_ID` | VARCHAR | FK→ | The patient's care plan associated with the task |
| 12 | `PROBLEM_ID` | VARCHAR | FK→ | The problem associated with the task. |
| 13 | `PREGNANCY_EPISODE_ID` | NUMERIC |  | If this task is anchored to an anchor target of type Pregnancy, then this item stores the episode associated with the pregnancy. |
| 14 | `ESCALATE_YN` | VARCHAR |  | Whether or not the task should be escalated if not completed. |
| 15 | `ESCL_ELAPSE_TIME_NUM` | NUMERIC |  | The amount of time before the task will be escalated, if escalation is enabled. |
| 16 | `START_INST_DTTM` | DATETIME (Local) |  | Start instant for a PRN task |
| 17 | `END_DATE` | DATETIME |  | The end date from the scheduler. |
| 18 | `DISCONTINUE_DTTM` | DATETIME (Local) |  | Instant a task was discontinued |
| 19 | `TASK_START_TIME_C_NAME` | VARCHAR |  | The start time of the task. |
| 20 | `AUTO_COMPLETE_COND` | VARCHAR |  | Task Auto Complete Condition copied from LTR |
| 21 | `NUM_OCCURRENCES` | INTEGER |  | The number of times this task will occur. |
| 22 | `PERSONALIZABLE_STATUS_C_NAME` | VARCHAR | org | Defines the personalization status of the notification times for the task. |
| 23 | `ANCHOR_EVENT_TYPE_C_NAME` | VARCHAR |  | The type of anchor target this task is configured for. |
| 24 | `ANCHOR_EVENT_NAME` | VARCHAR |  | The display name of the anchor target this task is configured for. This display name appears within the details of this task in the Patient To Do List activity. |
| 25 | `RESUME_ON_DISCHARGE_YN` | VARCHAR |  | Whether a task paused on hospital admission or added during hospital admission will start after discharge. |
| 26 | `DAYS_AFTER_DISCHARGE_NUM` | INTEGER |  | Indicates the number of days after hospital discharge this reminder will start. Value must be larger than or equal to 0. |
| 27 | `ENSURE_DELIVERY_C_NAME` | VARCHAR |  | Determines the scheduling behavior of this anchored task when its start date falls in the past. |
| 28 | `APPT_SERIAL_NUM` | NUMERIC |  | If this task is anchored to an anchor target of type Procedural Appointment, then this item stores the appointment serial number associated with the procedural appointment. |
| 29 | `ADMISSION_ENC_CSN_ID` | NUMERIC | FK→ | If this task is anchored to an anchor target of type Hospital Discharge, then this item stores the contact serial number associated with the admission. |
| 30 | `PERSISTENT_QUESR_SERIE_C_NAME` | VARCHAR |  | Indicates that the questionnaire series associated with this task is persistent and what type of persistent questionnaire series it is. |
| 31 | `LINK_TEXT` | VARCHAR |  | This item stores the display text for the associated hyperlink of this task. |
| 32 | `LINK_TYPE_C_NAME` | VARCHAR |  | This item stores the type of content found at the associated link of this task. |
| 33 | `APPOINTMENT_MODALITY_C_NAME` | VARCHAR |  | The modality of the appointment the patient will schedule for this task. |
| 34 | `TELEHEALTH_REASON_FOR_VISIT_C_NAME` | VARCHAR | org | The telehealth reason for visit that will be used when the patient schedules the video visit. |
| 35 | `DEF_DISCHRG_BEHAV_C_NAME` | VARCHAR |  | This item defines the behavior for the task during admission. |
| 36 | `SERIES_ANS_ID` | NUMERIC | FK→ | The questionnaire series answer associated with the task. |
| 37 | `ORDER_ID` | NUMERIC | shared | The medication order associated with the task. |
| 38 | `POINT_TEACHING_TTP_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 39 | `TOPIC_TEACHING_TTP_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 40 | `TITLE_TEACHING_TTP_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 41 | `TOTAL_INST_CNT` | INTEGER |  | The total number of patient-assigned task instances which are no longer actionable or have been acted upon. |
| 42 | `COMPLETED_INST_CNT` | INTEGER |  | The total number of completed patient-assigned task instances. |
| 43 | `LINK_DESCRIPTION_SMARTTEXT_ID` | VARCHAR |  | This column stores a smart text record ID that displays a detailed description of a link task to the patient on MyChart. This stores a particular instance of a task. |
| 44 | `LINK_DESCRIPTION_SMARTTEXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 45 | `UNANC_BEHAV_C_NAME` | VARCHAR |  | The behavior when this task is unanchored from its anchor target. |
| 46 | `AE_EVENT_UTC_DTTM` | DATETIME (UTC) |  | The instant in UTC of the event associated with an anchored task. |
| 47 | `AE_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The CSN of the encounter associated with this anchored task. Only applies to if the anchor target is of type rule defined date (encounter level). |
| 48 | `AE_EVENT_DTTM` | DATETIME (Local) |  | The instant in local of the event associated with an anchored task. |
| 49 | `PRIOR_TIME` | INTEGER |  | Indicates how long before its due time a patient can complete a task |
| 50 | `PRIOR_TIME_UNIT_C_NAME` | VARCHAR |  | Unit for how long before its due time a patient can complete a task |
| 51 | `POST_TIME` | INTEGER |  | Indicates how long after its due time a patient can complete a task |
| 52 | `POST_TIME_UNIT_C_NAME` | VARCHAR |  | Unit for how long after its due time a patient can complete a task |
| 53 | `IS_AUTOGENERATED_YN` | VARCHAR |  | This item determines whether a task is autogenerated. |
| 54 | `AI_SUGGESTED_SOURCE_C_NAME` | VARCHAR |  | Stores what source the AI model used to generate a suggested task from. |
| 55 | `AI_PREDICTED_DURATION_C_NAME` | VARCHAR |  | Stores the predicted duration it will take a patient to complete an AI generated suggested task. This predicted duration is determined by an AI model. |
| 56 | `AI_IS_RECURRING_YN` | VARCHAR |  | Virtual item that returns whether or not the AI suggested task is recurring. |
| 57 | `DOCSIGN_DOC_INFO_TYPE_C_NAME` | VARCHAR | org | This item stores the document type of the document signing task. |
| 58 | `DOCSIGN_DOC_TMPLT_ID_TEMPLT_DISPLAY_NAME` | VARCHAR |  | A name for the template designed for display purposes. |
| 59 | `DOCSIGN_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 60 | `DOCSIGN_PXP_RECORD_ID` | NUMERIC |  | This item stores the Procedure Pass ID of a document signing task when it is autogenerated for Procedure Pass. |
| 61 | `DOCSIGN_OUTREACH_TASK_ID` | VARCHAR |  | This item stores the outreach task ID of a document signing task when it is autogenerated for an outreach workflow. |
| 62 | `PAUSE_REASON_C_NAME` | VARCHAR |  | The pause reason if the task is currently paused. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ADMISSION_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `AE_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `CARE_INTG_ID` | [CAREPLAN_INFO](CAREPLAN_INFO.md) | sole_pk | high |
| `FREQ_ID` | [IP_FREQUENCY](IP_FREQUENCY.md) | sole_pk | high |
| `GOAL_ID` | [GOAL](GOAL.md) | name_stem | high |
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |
| `SERIES_ANS_ID` | [SRS_ASGN_INFO](SRS_ASGN_INFO.md) | sole_pk | high |

