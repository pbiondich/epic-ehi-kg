# OR_CASE

> The OR_CASE table contains OR management system case records.

**Overflow family:** [OR_CASE_2](OR_CASE_2.md), [OR_CASE_3](OR_CASE_3.md)  
**Primary key:** `OR_CASE_ID`  
**Columns:** 115  
**Org-specific columns:** 19  
**Joined by:** 36 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_CASE_ID` | VARCHAR | PK | The unique ID of the procedural case record. |
| 2 | `CASE_NAME` | VARCHAR |  | The name of the surgical case record. |
| 3 | `SURGERY_DATE` | DATETIME |  | The date on which the surgery is scheduled to take place. |
| 4 | `CASE_TYPE_C_NAME` | VARCHAR | org | The case type category number for the case. Example case types include elective and emergency. This column is frequently used to link to ZC_OR_CASE_TYPE. |
| 5 | `CASE_CLASS_C_NAME` | VARCHAR | org | The case classification category number for the case. Example case types include elective and trauma. This column is frequently used to link to ZC_OR_CASE_CLASS. |
| 6 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient associated with the procedural case record. |
| 7 | `PAT_AGE` | INTEGER |  | The age of the patient associated with the surgical case. |
| 8 | `PAT_CLASS_C_NAME` | VARCHAR | org | The category value which represents the type of the patient associated with the surgical case record. |
| 9 | `SERVICE_C_NAME` | VARCHAR | org | The category value which identifies the surgical service of the case record. |
| 10 | `NUM_OF_PANELS` | INTEGER |  | The total number of procedure panels in the surgical case record. A panel is a grouping of surgical procedures performed together. |
| 11 | `EXP_DATE` | DATETIME |  | The date on which this surgical case expires. The case should be scheduled on or before this date. |
| 12 | `REQUESTED_BY` | VARCHAR |  | The name of the person who requested that the surgical case be created. |
| 13 | `SETUP_OFFSET` | INTEGER |  | The amount of time in minutes required to set up at the beginning of the case. |
| 14 | `CLEANUP_OFFSET` | INTEGER |  | The amount of time in minutes required to clean up at the end of the case. |
| 15 | `START_AT_OR_AFTER` | DATETIME (Local) |  | The time of day before which the case cannot begin. |
| 16 | `START_AT_OR_BEFORE` | DATETIME (Local) |  | The time of day after which the case cannot begin. |
| 17 | `TOTAL_TIME_NEEDED` | INTEGER |  | The total amount of time required to perform the case. |
| 18 | `REFERRING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 19 | `PREOP_XRAYS_YN` | VARCHAR |  | Yes/No flag which indicates whether or not x-rays were taken before the surgery was performed. |
| 20 | `PREOP_VISIT_YN` | VARCHAR |  | Yes/No flag which indicates whether or not the patient completed a pre-op clinic visit. |
| 21 | `LATEX_ALLERGIC_YN` | VARCHAR |  | Yes/No flag which indicates whether or not the patient has a latex allergy. |
| 22 | `OR_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 23 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 24 | `PRIORITY_C_NAME` | VARCHAR |  | The category value which represents the priority of the case. |
| 25 | `ADD_ON_CASE_YN` | VARCHAR |  | Indicates whether a case is an add-on. Y indicates that the add-on check box is checked, and this is done manually by the scheduler for cases that have been scheduled after the usual scheduling window is closed. N or null indicates that the case is not an add-on. |
| 26 | `SCHED_STATUS_C_NAME` | VARCHAR | org | The category number for the case scheduling status. |
| 27 | `CASE_PROGRESS_C_NAME` | VARCHAR | org | The category value which represents the current progress status of the case as it proceeds. |
| 28 | `CANCEL_REASON_C_NAME` | VARCHAR | org | The category number of the most recent reason the case was canceled or removed from the schedule. This column will remain populated even if the case is put back on the schedule. This column is frequently used to link to ZC_OR_CANCEL_RSN. |
| 29 | `CANCEL_USER_ID` | VARCHAR |  | The unique ID of the user who most recently canceled the case or removed it from the schedule. This column will remain populated even if the case is put back on the schedule. This column is frequently used to link to CLARITY_EMP. |
| 30 | `CANCEL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 31 | `CANCEL_COMMENTS` | VARCHAR |  | The comments entered by the user that canceled the case. |
| 32 | `TIME_SCHEDULED` | DATETIME (Local) |  | The date and time at which the case is scheduled to be performed on the surgery date. |
| 33 | `VOID_REASON_C_NAME` | VARCHAR | org | The category number for the reason the case was voided. This column is frequently used to link to ZC_OR_VOID_REASON. |
| 34 | `CANCEL_CHKIN_RSN_C_NAME` | VARCHAR | org | The category value which represents the reason the check-in was canceled. |
| 35 | `CHECKIN_INSTANT` | DATETIME (Local) |  | The date and time at which the case was checked-in. |
| 36 | `PATIENT_ESCORT` | VARCHAR |  | The person escorting the patient for the surgery. This is a free text value. |
| 37 | `PANEL1_START_AT` | INTEGER |  | Indicates at what time within the case panel 1 should begin. This is measured in minutes relative to the beginning of the case. |
| 38 | `PANEL1_LENGTH` | INTEGER |  | The total amount of time required for panel 1 to be performed. This includes the times of all the procedures within the panel. |
| 39 | `PANEL2_START_AT` | INTEGER |  | Indicates at what time within the case panel 2 should begin. This is measured in minutes relative to the beginning of the case. |
| 40 | `PANEL2_LENGTH` | INTEGER |  | The total amount of time required for panel 2 to be performed. This includes the times of all the procedures within the panel. |
| 41 | `PANEL3_START_AT` | INTEGER |  | Indicates at what time within the case panel 3 should begin. This is measured in minutes relative to the beginning of the case. |
| 42 | `PANEL3_LENGTH` | INTEGER |  | The total amount of time required for panel 3 to be performed. This includes the times of all the procedures within the panel. |
| 43 | `PANEL4_START_AT` | INTEGER |  | Indicates at what time within the case panel 4 should begin. This is measured in minutes relative to the beginning of the case. |
| 44 | `PANEL4_LENGTH` | INTEGER |  | The total amount of time required for panel 4 to be performed. This includes the times of all the procedures within the panel. |
| 45 | `PANEL5_START_AT` | INTEGER |  | Indicates at what time within the case panel 5 should begin. This is measured in minutes relative to the beginning of the case. |
| 46 | `PANEL5_LENGTH` | INTEGER |  | The total amount of time required for panel 5 to be performed. This includes the times of all the procedures within the panel. |
| 47 | `RECORD_CREATE_DATE` | DATETIME |  | The date on which the case was created. |
| 48 | `REC_CREATE_USER_ID` | VARCHAR |  | The unique ID of the user who created the case. |
| 49 | `REC_CREATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 50 | `ADT_CSN` | NUMERIC |  | Contact serial number for an Admission Discharge Transfer (ADT) admit contact. |
| 51 | `CASE_REQST_USER_ID` | VARCHAR |  | The unique ID of the user who placed the web request. |
| 52 | `CASE_REQST_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 53 | `SHUFFLE_USER_ID` | VARCHAR |  | The unique ID of the user who placed the case in the shuffle depot. |
| 54 | `SHUFFLE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 55 | `FORMS_PRINTED_YN` | VARCHAR |  | Yes/No flag indicating whether or not forms have been printed. |
| 56 | `CONFIDENTIAL_YN` | VARCHAR |  | Yes/No flag indicating whether or not the case is confidential. |
| 57 | `PAT_LEVEL_C_NAME` | VARCHAR | org | The category value representing the patient level in the case. |
| 58 | `INTL_PATIENT_YN` | VARCHAR |  | Yes/No flag which indicates whether or not the patient is international. |
| 59 | `PAIN_MGMT_C_NAME` | VARCHAR | org | The category value which represents the patient's participation in pain management. |
| 60 | `ADMIT_DATE` | DATETIME |  | The date on which the patient was admitted. |
| 61 | `LENGTH_OF_STAY` | INTEGER |  | The length of the patient's stay while admitted. |
| 62 | `RESEARCH_IND_C_NAME` | VARCHAR | org | The category value which represents the candidacy of the case for research. |
| 63 | `WEIGHT` | NUMERIC |  | The approximate weight of the patient in pounds. |
| 64 | `ADMIT_SOURCE_C_NAME` | VARCHAR | org | The category value which indicates the admit source for the patient's stay. |
| 65 | `ADMITTING_SRVC_C_NAME` | VARCHAR | org | The category value which indicates the admitting service for the patient's stay. |
| 66 | `ADMITTING_PHYS_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 67 | `ADMIT_BED_TYPE_C_NAME` | VARCHAR | org | The category value which indicates the admitting bed type. |
| 68 | `ADD_ON_DATE` | DATETIME |  | The date the case first shows up as an add-on. |
| 69 | `MODIFIED_CASE_LEN` | INTEGER |  | The length of the case, in minutes, if it has been shortened or lengthened. |
| 70 | `PAT_TOTAL_TIME` | INTEGER |  | The amount of time in minutes for which the patient is present. |
| 71 | `BUMPED_CASE_YN` | VARCHAR |  | Yes/No flag indicating whether or not the case has been bumped. |
| 72 | `BUMPED_INSTANT` | DATETIME (Local) |  | The date and time at which the case was bumped. |
| 73 | `VOID_COMMENTS` | VARCHAR |  | The free text comments entered when the case was voided. |
| 74 | `CASE_ACCEPTED_YN` | VARCHAR |  | Yes/No flag indicating whether or not the case was accepted in Case Entry. |
| 75 | `PROJ_START_INST` | DATETIME (Local) |  | The projected date and time for the start of this case. |
| 76 | `PROJ_END_INST` | DATETIME (Local) |  | The projected date and time for the end of this case. |
| 77 | `REAL_TIME_OR_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 78 | `PANEL1_IS_COMB_YN` | VARCHAR |  | Indicates whether the time for Panel 1 is the procedures' combination time from procedure time averaging. Y indicates that the time is from the procedures' combination procedure time average; N indicates it is not. A null value indicates the panel was not added in the case. |
| 79 | `PANEL2_IS_COMB_YN` | VARCHAR |  | Indicates whether the time for Panel 2 is the procedures' combination time from procedure time averaging. Y indicates that the time is from the procedures' combination procedure time average; N indicates it is not. A null value indicates the panel was not added in the case. |
| 80 | `PANEL3_IS_COMB_YN` | VARCHAR |  | Indicates whether the time for Panel 3 is the procedures' combination time from procedure time averaging. Y indicates that the time is from the procedures' combination procedure time average; N indicates it is not. A null value indicates the panel was not added in the case. |
| 81 | `PANEL4_IS_COMB_YN` | VARCHAR |  | Indicates whether the time for Panel 4 is the procedures' combination time from procedure time averaging. Y indicates that the time is from the procedures' combination procedure time average; N indicates it is not. A null value indicates the panel was not added in the case. |
| 82 | `PANEL5_IS_COMB_YN` | VARCHAR |  | Indicates whether the time for Panel 5 is the procedures' combination time from procedure time averaging. Y indicates that the time is from the procedures' combination procedure time average; N indicates it is not. A null value indicates the panel was not added in the case. |
| 83 | `PANEL1_DEF_LEN` | NUMERIC |  | The panel length defaulted by the system for Panel 1. |
| 84 | `PANEL2_DEF_LEN` | NUMERIC |  | The panel length defaulted by the system for Panel 2. |
| 85 | `PANEL3_DEF_LEN` | NUMERIC |  | The panel length defaulted by the system for Panel 3. |
| 86 | `PANEL4_DEF_LEN` | NUMERIC |  | The panel length defaulted by the system for Panel 4. |
| 87 | `PANEL5_DEF_LEN` | NUMERIC |  | The panel length defaulted by the system for Panel 5. |
| 88 | `PANEL1_LEN_MOD_YN` | VARCHAR |  | Indicates whether the length of the panel 1 was modified by the user. |
| 89 | `PANEL2_LEN_MOD_YN` | VARCHAR |  | Indicates whether the length of the panel 2 was modified by the user. |
| 90 | `PANEL3_LEN_MOD_YN` | VARCHAR |  | Indicates whether the length of the panel 3 was modified by the user. |
| 91 | `PANEL4_LEN_MOD_YN` | VARCHAR |  | Indicates whether the length of the panel 4 was modified by the user. |
| 92 | `PANEL5_LEN_MOD_YN` | VARCHAR |  | Indicates whether the length of the panel 5 was modified by the user. |
| 93 | `REQUESTED_DATE` | DATETIME |  | The preferred date requested for this case. |
| 94 | `REQUESTED_TIME` | DATETIME (Local) |  | The time (of the day) requested for this case. |
| 95 | `EXP_ADM_DTE_OFFSET` | INTEGER |  | Stores the number of days prior to the day of surgery, the patient is expected to be admitted. |
| 96 | `PAT_ALLERGIES_YN` | VARCHAR |  | Indicates if the patient has Allergies. |
| 97 | `PAT_HEALTH_ISSUE_YN` | VARCHAR |  | Indicates if patient has health issues. |
| 98 | `FILMS_FOR_SURGER_YN` | VARCHAR |  | Indicates if the patient is bringing films to surgery. |
| 99 | `PREOP_VISIT_NEED_YN` | VARCHAR |  | Indicates if a PreOp Visit is needed. |
| 100 | `PREOP_VISIT_COMP_YN` | VARCHAR |  | Indicates if PreOp Visit has been completed. |
| 101 | `LOG_ID` | VARCHAR | shared | This columns stores the log ID for this case. |
| 102 | `CASE_ACCEPT_NEED_YN` | VARCHAR |  | Stores whether the case accept programming point needs to be fired. Used when a case was created from a order to fire the accept programming points before the case can be scheduled. |
| 103 | `IS_CLINICAL_TRL_YN` | VARCHAR |  | Indicates if the case is a clinical trial case. |
| 104 | `PEND_STATUS_C_NAME` | VARCHAR | org | The status of a pending web request. |
| 105 | `POSTOP_DEST_C_NAME` | VARCHAR | org | The patient's post-operative destination. |
| 106 | `TRANSLATOR_C_NAME` | VARCHAR | org | The category value of the language of the case translator. |
| 107 | `PTA_LAST_UPD_DATE` | DATETIME |  | Stores the date the procedure time was last updated in the case |
| 108 | `CASE_BEGIN_INSTANT` | DATETIME (Local) |  | Stores the datetime instant in which the case began. |
| 109 | `CASE_END_INSTANT` | DATETIME (Local) |  | Stores the datetime instant in which the case ended. |
| 110 | `MULT_PROC_COMP_YN` | VARCHAR |  | Indicates whether there were multiple procedures used in calculation of procedure time for this case. |
| 111 | `USING_EAP_YN` | VARCHAR |  | This item defines whether this case is using the Procedure master file (EAP) for scheduling procedures? Default value is 'No'. |
| 112 | `ANESTHESIA_C_NAME` | VARCHAR | org | The anesthesia type category number for the case. |
| 113 | `CASE_SOURCE_DEPL_ID` | VARCHAR |  | ID of the source deployment that created the case through cross deployment scheduling. |
| 114 | `PRIMARY_PHYSICIAN_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 115 | `PRIMARY_PERFORMING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (36)

| From | Column | Confidence |
|------|--------|------------|
| [IB_MESSAGES_2](IB_MESSAGES_2.md) | `OR_CASE_ID` | high |
| [OR_CASE_ADTL_RES](OR_CASE_ADTL_RES.md) | `OR_CASE_ID` | high |
| [OR_CASE_ALL_PROC](OR_CASE_ALL_PROC.md) | `OR_CASE_ID` | high |
| [OR_CASE_ALL_SURG](OR_CASE_ALL_SURG.md) | `OR_CASE_ID` | high |
| [OR_CASE_ANES_COMM](OR_CASE_ANES_COMM.md) | `OR_CASE_ID` | high |
| [OR_CASE_ANES_CONT](OR_CASE_ANES_CONT.md) | `OR_CASE_ID` | high |
| [OR_CASE_ANES_EQUIP](OR_CASE_ANES_EQUIP.md) | `OR_CASE_ID` | high |
| [OR_CASE_ANES_STAF](OR_CASE_ANES_STAF.md) | `OR_CASE_ID` | high |
| [OR_CASE_ANES_TYPE](OR_CASE_ANES_TYPE.md) | `OR_CASE_ID` | high |
| [OR_CASE_APPTS_PR](OR_CASE_APPTS_PR.md) | `OR_CASE_ID` | high |
| [OR_CASE_APPTS_PS](OR_CASE_APPTS_PS.md) | `OR_CASE_ID` | high |
| [OR_CASE_AUDIT_TRL](OR_CASE_AUDIT_TRL.md) | `OR_CASE_ID` | high |
| [OR_CASE_BLOCKS](OR_CASE_BLOCKS.md) | `OR_CASE_ID` | high |
| [OR_CASE_BLOOD_PROD](OR_CASE_BLOOD_PROD.md) | `OR_CASE_ID` | high |
| [OR_CASE_COMMENTS](OR_CASE_COMMENTS.md) | `OR_CASE_ID` | high |
| [OR_CASE_DATES](OR_CASE_DATES.md) | `OR_CASE_ID` | high |
| [OR_CASE_DX_CODE](OR_CASE_DX_CODE.md) | `OR_CASE_ID` | high |
| [OR_CASE_EQUIP_NEED](OR_CASE_EQUIP_NEED.md) | `OR_CASE_ID` | high |
| [OR_CASE_IB_BODY](OR_CASE_IB_BODY.md) | `OR_CASE_ID` | high |
| [OR_CASE_IB_HIST](OR_CASE_IB_HIST.md) | `OR_CASE_ID` | high |
| [OR_CASE_INF_STAT](OR_CASE_INF_STAT.md) | `OR_CASE_ID` | high |
| [OR_CASE_INSTR_NEED](OR_CASE_INSTR_NEED.md) | `OR_CASE_ID` | high |
| [OR_CASE_ISOLATST](OR_CASE_ISOLATST.md) | `OR_CASE_ID` | high |
| [OR_CASE_PAT_MD_REQ](OR_CASE_PAT_MD_REQ.md) | `OR_CASE_ID` | high |
| [OR_CASE_POS_DEVS](OR_CASE_POS_DEVS.md) | `OR_CASE_ID` | high |
| [OR_CASE_PREOPDX](OR_CASE_PREOPDX.md) | `OR_CASE_ID` | high |
| [OR_CASE_PROC_RQST](OR_CASE_PROC_RQST.md) | `OR_CASE_ID` | high |
| [OR_CASE_QUEST_ANS](OR_CASE_QUEST_ANS.md) | `OR_CASE_ID` | high |
| [OR_CASE_QUEST_AN_P](OR_CASE_QUEST_AN_P.md) | `OR_CASE_ID` | high |
| [OR_CASE_REQ_DOCS](OR_CASE_REQ_DOCS.md) | `OR_CASE_ID` | high |
| [OR_CASE_RESCHED](OR_CASE_RESCHED.md) | `OR_CASE_ID` | high |
| [OR_CASE_SCHED_HIST](OR_CASE_SCHED_HIST.md) | `OR_CASE_ID` | high |
| [OR_CASE_SPECNEED](OR_CASE_SPECNEED.md) | `OR_CASE_ID` | high |
| [OR_CASE_STAFF_NEED](OR_CASE_STAFF_NEED.md) | `OR_CASE_ID` | high |
| [OR_CASE_SURG_RSC](OR_CASE_SURG_RSC.md) | `OR_CASE_ID` | high |
| [OR_CASE_VIRTUAL](OR_CASE_VIRTUAL.md) | `OR_CASE_ID` | high |

