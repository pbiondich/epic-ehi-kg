# OR_CASE_2

> The OR_CASE_2 table enables you to report on surgical and procedural case data. This table has the same basic structure as OR_CASE, but was created as a second table to prevent OR_CASE from getting any larger.

**Overflow of:** [OR_CASE](OR_CASE.md)  
**Primary key:** `CASE_ID`  
**Columns:** 84  
**Org-specific columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique ID for the case request record. |
| 2 | `SURGICAL_RISK_C_NAME` | VARCHAR | org | The surgical risk level category ID for the surgical case. |
| 3 | `POTENTL_BLOODLOSS_C_NAME` | VARCHAR | org | The potential blood loss category ID for the surgical case. |
| 4 | `AWARENESS_DT` | DATETIME |  | This column contains the date the patient was made aware of the surgery in the case record. |
| 5 | `READY_TO_SCHED_C_NAME` | VARCHAR | org | The ready to schedule category ID for the surgical case. |
| 6 | `SURGEON_REQ_LEN` | INTEGER |  | This column contains the surgeon requested length for the case in the case record. |
| 7 | `PAT_PAGER_NUM` | VARCHAR |  | This column contains the patient pager number assigned in the case record. |
| 8 | `SPEC_NEED_RESOLV_DT` | DATETIME |  | This column contains the date special needs were resolved in the case record. |
| 9 | `AUTH_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 10 | `PAT_START_TIME` | DATETIME (Local) |  | Shows the time the patient is scheduled to arrive at the OR. |
| 11 | `OB_CSECT_TYPE_C_NAME` | VARCHAR | org | The c-section type category ID for the surgical case. |
| 12 | `CASE_PULLED_C_NAME` | VARCHAR | org | The case picking status category ID for the surgical case. |
| 13 | `RSN_RETURN_OR_C_NAME` | VARCHAR | org | The reason why a patient returns to the OR category ID for the surgical case. |
| 14 | `INTER_BETWEEN_CASES` | INTEGER |  | The number of days that should be between two cases. |
| 15 | `PAT_FIRST_AVAIL_DT` | DATETIME |  | The date the patient is first available for surgery. |
| 16 | `PAT_COMPLEXITY_C_NAME` | VARCHAR | org | The patient complexity category ID for the surgical case. |
| 17 | `ANES_APPROVAL_DATE` | DATETIME |  | The date anesthesia was approved. |
| 18 | `APPROX_HEIGHT` | NUMERIC |  | The approximate height of the patient in inches. |
| 19 | `INS_SELF_PAY_YN` | VARCHAR |  | This item contains whether the patient's insurance is self-pay. |
| 20 | `PRE_OP_BED_ID` | VARCHAR |  | The patient's pre-op bed can be entered in the case, prior to their arrival. |
| 21 | `PRE_OP_BED_ID_BED_LABEL` | VARCHAR |  | The name of the bed. |
| 22 | `INTRAOP_XRAYS_CMT` | VARCHAR |  | This column displays the comment about intraop x-ray needs in a case. |
| 23 | `TRANSLATN_NEEDS_CMT` | VARCHAR |  | This column displays the comment about translation needs in a case. |
| 24 | `LASER_NEEDS_COMMENT` | VARCHAR |  | This column displays the comment about specific laser needs in a case. |
| 25 | `READY_TO_SCHED_DTTM` | DATETIME (Local) |  | This column displays the date and time that a case was marked as ready to schedule in order to help end-users prioritize cases when scheduling. |
| 26 | `IOP_XRAYS_C_NAME` | VARCHAR | org | The intraop x-rays needed category ID for the surgical case. |
| 27 | `ARE_PROPH_AB_REQ_C_NAME` | VARCHAR | org | The prophylactic antibiotics required category ID for the surgical case. |
| 28 | `PAT_SCHED_NOTICE` | INTEGER |  | Store number of days notice patient needs before surgery. |
| 29 | `CLASS_APPROP_C_NAME` | VARCHAR | org | The case classification appropriateness category ID for the surgical case. |
| 30 | `REVISD_CASE_CLASS_C_NAME` | VARCHAR | org | The revised case classification category ID for the surgical case. |
| 31 | `PREOP_VISIT_STAT_C_NAME` | VARCHAR | org | The pre-op visit status category ID for the surgical case. |
| 32 | `ADMIT_TYPE_C_NAME` | VARCHAR | org | The admit type category ID for the surgical case. |
| 33 | `CANCELED_AT_LAST_MINUTE_YN` | VARCHAR |  | Indicates whether the case was canceled for a non-clinical reason at the last minute (i.e., on the day of surgery or on the day of admission). |
| 34 | `CANCEL_TARGET_DT` | DATETIME |  | Stores the target date associated with the last minute canceled case. The target date is the date by which the last minute canceled case should be rescheduled to avoid a breach. |
| 35 | `IGNORE_TARGET_DATE_YN` | VARCHAR |  | Stores whether the target date for rescheduling a case should be ignored. If this item is set to Yes, the case will be ignored when reporting on target date breaches for last minute canceled cases. |
| 36 | `IGNORE_TARGET_DATE_REASON_C_NAME` | VARCHAR | org | The category ID of the last minute cancel reason for ignoring the target date for the surgical case. The target date is the date by which the last minute canceled case should be rescheduled to avoid a breach. |
| 37 | `TARGET_IGNORE_SET_BY_USER_ID` | VARCHAR |  | Stores the ID of the user who flags the last minute canceled case to ignore the target date. The target date is the date by which the last minute canceled case should be rescheduled to avoid a breach. |
| 38 | `TARGET_IGNORE_SET_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 39 | `LAST_MIN_CANC_ORIGINAL_SURG_DT` | DATETIME |  | Stores the original surgery date associated with the last minute canceled case. Original surgery date is the scheduled surgery date when the case is canceled at the last minute for the first time. |
| 40 | `IN_OR_TO_PROC_LEN` | INTEGER |  | Records the estimated time to prep the patient from the time wheeled into the room until the procedure starts. |
| 41 | `CLOSE_TO_OUT_OR_LEN` | INTEGER |  | Records the estimated time between the procedure ending and the patient being wheeled out of the room. |
| 42 | `POSTOP_BED1_TYPE_C_NAME` | VARCHAR | org | The first post-op bed category ID for the surgical case. |
| 43 | `POSTOP_BED1_DAYS_NEEDED` | INTEGER |  | The length in days the first post-op bed will be needed. |
| 44 | `POSTOP_BED1_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 45 | `POSTOP_BED2_TYPE_C_NAME` | VARCHAR |  | The second post-op bed category ID for the surgical case. |
| 46 | `POSTOP_BED2_DAYS_NEEDED` | INTEGER |  | The length in days the second post-op bed will be needed. |
| 47 | `POSTOP_BED2_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 48 | `CUSTOM_STATUS_C_NAME` | VARCHAR | org | The custom status category ID for the surgical case. |
| 49 | `FOLLOWUP_APPT_DTTM` | DATETIME (Local) |  | This item stores the time and date of a patient's post surgical follow-up appointment. |
| 50 | `WTIS_DX_CAT_C_NAME` | VARCHAR | org | The WTIS diagnosis category ID for the surgical case. |
| 51 | `WTIS_INTENT_SURGERY_C_NAME` | VARCHAR | org | The WTIS intent of surgery category ID for the surgical case. |
| 52 | `WTIS_PEDIATRIC_YN` | VARCHAR |  | This item determines whether or not a case is considered pediatric for WTIS purposes. This item is only respected if the patient's age is between 18 and 23 as of the Decision to Treat Date (I ORC 8001). If a patient is under 18 the case will always be considered pediatric. If the patient is over 23 the case will never be considered pediatric. |
| 53 | `WTIS_SERVICE_AREA_C_NAME` | VARCHAR | org | The WTIS service area category ID for the surgical case. |
| 54 | `WTIS_SERVICE_DETAIL_1_C_NAME` | VARCHAR | org | The WTIS service detail 1 category ID for the surgical case. |
| 55 | `WTIS_SERVICE_DETAIL_2_C_NAME` | VARCHAR | org | The WTIS service detail 2 category ID for the surgical case. |
| 56 | `WTIS_PROC_CODE` | VARCHAR |  | This item contains the full WTIS procedure code for a case. |
| 57 | `WTIS_WAIT_LIST_ID` | VARCHAR |  | Stores the wait list ID of the WTIS wait list for the case. This item is automatically generated by the system based on the case ID. The wait list ID is in the format <case ID> or <case ID>.<unique number>. |
| 58 | `WTIS_WAIT_LIST_CREATED_YN` | VARCHAR |  | Stores whether the WTIS create wait list message was already sent for the case. This is used by interfaces to suppress sending other update messages for the case, if the create message has not been sent yet. |
| 59 | `PREOP_REQUESTED_VISIT_DTTM` | DATETIME (UTC) |  | This column stores the date/time for the requested pre-op visit. |
| 60 | `GRAVIDITY` | INTEGER |  | The number of times the patient has been pregnant. |
| 61 | `PARITY` | INTEGER |  | The number of pregnancies the patient has carried to viable gestational age. |
| 62 | `DESIRED_DTTM` | DATETIME (UTC) |  | The desired date and time to schedule the patient's planned C-section. |
| 63 | `EST_DUE_DATE` | DATETIME |  | The expected date of delivery/estimated date of confinement. |
| 64 | `DESIRED_DATE_GEST_AGE` | NUMERIC |  | The gestational age, in weeks, of the baby at the time of the desired date of the patient's planned C-section. |
| 65 | `WTIS_CODE_PROC_C_NAME` | VARCHAR | org | The Wait Time Information System (WTIS) procedure code category ID for the surgical case. |
| 66 | `SERVICE_TARGET_EFFORT_YN` | VARCHAR |  | Flag to indicate that additional effort was needed on behalf of staff to work this encounter in order to meet service targets. |
| 67 | `P_CATS_CODE_C_NAME` | VARCHAR | org | The Pediatric Canadian Access Targets for Surgery (P-CATS) diagnosis code category ID for the surgical case. |
| 68 | `EXPECTED_ADMISSION_TIME` | DATETIME (Local) |  | This item stores the time the patient is expected to be admitted for surgery, as documented in the surgical case in I ORC 7617 - EXPECTED ADMISSION TIME. Column PAT_ENC_HSP__EXP_ADMISSION_TIME should be used to report on the expected admission date and time for the admission linked to the surgery (I EPT 10301 - EXPECTED ADMISSION DATE and I EPT 10300 - EXPECTED ADMISSION TIME). If a time is set in I ORC 7617, the expected admission time in the linked admission is set to that time. If I ORC 7617 is not set, the expected admission time in the linked admission is calculated as the scheduled surgery time (OR_CASE__TIME_SCHEDULED) minus the number of hours in OR_CASE_2__EXPECTED_ADMISSION_TIME_OFFSET. If multiple cases are linked to the same admission, the earliest time from the list of linked cases will be set as the expected admission time on the linked admission. |
| 69 | `OPERATION_INTENTION_C_NAME` | VARCHAR | org | The operation intention category ID for the surgical case. |
| 70 | `TRIAGE_SCORE` | INTEGER |  | Stores a triage score for the case. This information would be obtained from a third-party. |
| 71 | `REGISTRY_SCORE` | INTEGER |  | Stores a registry score for the case. This information would be obtained from a third-party. |
| 72 | `ACATS_CODE_C_NAME` | VARCHAR | org | The Adult Coding Access Targets for Surgery (ACATS) code diagnosis category ID for the surgical case. |
| 73 | `EXTERNAL_STATUS_C_NAME` | VARCHAR | org | The external systems case status category ID for the surgical case. |
| 74 | `PREP_TIME_MOD_YN` | VARCHAR |  | Has patient prep time been modified by user |
| 75 | `POSTOP_LEVEL_OF_CARE_C_NAME` | VARCHAR | org | The planned post-op level of care category ID for the surgical case. |
| 76 | `CASE_ACCESS_UTC_DTTM` | DATETIME (UTC) |  | Date and time of the last time case entry was opened. |
| 77 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Record status flag. Used in conjunction with record archived flag for encounter archiving. |
| 78 | `CLASS_REVIEW_DATE` | DATETIME |  | The most recent time clinical prioritization was reviewed. |
| 79 | `CLINICAL_SAFE_DATE` | DATETIME |  | How long clinical prioritization is valid. |
| 80 | `NHSN_TRAUMA_ORC_YN` | VARCHAR |  | This is used to indicate whether the case qualifies as an NHSN trauma case (blunt or penetrating injury). |
| 81 | `TRAUMA_CASE_ORC_YN` | VARCHAR |  | This is used to indicate whether the case should be classified as a trauma case. |
| 82 | `NHSN_EMERG_ORC_YN` | VARCHAR |  | This is used to indicated whether the case qualifies as an NHSN emergency case (unplanned or unscheduled). |
| 83 | `CENTRAL_INTAKE_NUMBER` | VARCHAR |  | This stores the Central Intake Number also called RAC number. |
| 84 | `CASE_VERIFIED_C_NAME` | VARCHAR | org | Whether the case has been verified. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [OR_CASE](OR_CASE.md).

