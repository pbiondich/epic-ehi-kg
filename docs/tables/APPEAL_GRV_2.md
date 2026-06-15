# APPEAL_GRV_2

> This table contains information about an individual appeal or grievance as an extension of APPEAL_GRV.

**Overflow of:** [APPEAL_GRV](APPEAL_GRV.md)  
**Primary key:** `APPEAL_GRV_ID`  
**Columns:** 64  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `APPEAL_GRV_ID` | NUMERIC | PK | The unique identifier (.1 item) for the appeal/grievance record. |
| 2 | `NEXT_OUTST_DECISION_UTC_DTTM` | DATETIME (UTC) |  | The date and time of the earliest outstanding decision due requirement, in UTC. If there are no outstanding decision due requirements, this item will be null. |
| 3 | `NEXT_OUTST_DECISION_LOCAL_DTTM` | DATETIME (Attached) |  | The date and time of the earliest outstanding decision due requirement. If there are no outstanding decision due requirements, this item will be null. Stored in the time zone determined by column APPEAL_GRV.TAT_RPT_TIME_ZONE_C. |
| 4 | `NEXT_OUTST_EFFECT_UTC_DTTM` | DATETIME (UTC) |  | The date and time of the earliest outstanding effectuation due requirement, in UTC. If there are no outstanding effectuation due requirements, this item will be null. |
| 5 | `NEXT_OUTST_EFFECT_LOCAL_DTTM` | DATETIME (Attached) |  | The date and time of the earliest outstanding effectuation due requirement. If there are no outstanding effectuation due requirements, this item will be null. Stored in the time zone determined by column APPEAL_GRV.TAT_RPT_TIME_ZONE_C. |
| 6 | `NEXT_OUTST_NOTIF_UTC_DTTM` | DATETIME (UTC) |  | The date and time of the earliest outstanding notification due requirement, in UTC. If there are no outstanding notification due requirements, this item will be null. |
| 7 | `NEXT_OUTST_NOTIF_LOCAL_DTTM` | DATETIME (Attached) |  | The date and time of the earliest outstanding notification due requirement. If there are no outstanding notification due requirements, this item will be null. Stored in the time zone determined by column APPEAL_GRV.TAT_RPT_TIME_ZONE_C. |
| 8 | `REQUIREMENTS_COMP_UTC_DTTM` | DATETIME (UTC) |  | The instant when all required decision, effectuation, and notification requirements were met, in UTC. |
| 9 | `REQUIREMENTS_COMP_LOCAL_DTTM` | DATETIME (Attached) |  | The instant when all required decision, effectuation, and notification requirements were met. Stored in the time zone determined by column APPEAL_GRV.TAT_RPT_TIME_ZONE_C. |
| 10 | `DECISION_ON_TIME_C_NAME` | VARCHAR |  | The on time status category ID of decision timeliness requirements. |
| 11 | `EFFECTUATION_ON_TIME_C_NAME` | VARCHAR |  | The on time status category ID of effectuation timeliness requirements. |
| 12 | `NOTIFICATIONS_ON_TIME_C_NAME` | VARCHAR |  | The on time status category ID of notification timeliness requirements. |
| 13 | `OVERALL_ON_TIME_C_NAME` | VARCHAR |  | The overall on time status category ID of the appeal or grievance, including decision, effectuation, and notification requirements. |
| 14 | `APPEAL_GRV_WKFL_STEP_C_NAME` | VARCHAR |  | The current workflow step category ID for the Appeal or Grievance |
| 15 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for the patient contact associated with this appeal or grievance used to associate notes. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 16 | `FILED_LATE_EXCPTNS_ALLOWED_YN` | VARCHAR |  | Whether exceptions to the timely filing timeframe can be made for any applicable timeliness standard. |
| 17 | `FILED_LATE_OVERRIDE_YN` | VARCHAR |  | Used if the appeal/grievance was filed late, but the system is not automatically marking it as late. Yes means the appeal/grievance was filed outside of the filing timeframe, no or blank means it was not, or the system was able to automatically determine the status in FILED_ON_TIME_C. |
| 18 | `DISMISSED_YN` | VARCHAR |  | Stores whether the appeal/grievance was dismissed. |
| 19 | `NEXT_OUTST_ACTION_UTC_DTTM` | DATETIME (UTC) |  | The date and time of the earliest outstanding required action, in UTC. If there are no outstanding required actions, this item will be null. |
| 20 | `NEXT_OUTST_ACTION_LOCAL_DTTM` | DATETIME (Attached) |  | The date and time of the earliest outstanding required action. If there are no outstanding required actions, this item will be null. Stored in the time zone determined by column APPEAL_GRV.TAT_RPT_TIME_ZONE_C. |
| 21 | `CURRENT_REQUESTED_URGENCY_C_NAME` | VARCHAR |  | The current requested urgency category ID for the appeal or grievance. |
| 22 | `REQUESTED_EXP_PROCESSED_STD_YN` | VARCHAR |  | Indicates whether an expedited urgency was requested, but not granted. 'Y' indicates that there was an expedite request, but the appeal or grievance was still processed on standard timelines. 'N' or NULL indicates that the appeal or grievance was processed as expedited, or there were no requests to expedite. |
| 23 | `MEM_OUT_ORAL_NOTIF_UTC_DTTM` | DATETIME (UTC) |  | The UTC date/time that the member was verbally notified of the outcome of the appeal/grievance. |
| 24 | `MEM_OUT_ORAL_NOTIF_LOCAL_DTTM` | DATETIME (Attached) |  | The local date/time that the member was verbally notified of the outcome of the appeal/grievance. Stored in the time zone determined by column APPEAL_GRV.TAT_RPT_TIME_ZONE_C. |
| 25 | `MEM_OUT_WRIT_NOTIF_UTC_DTTM` | DATETIME (UTC) |  | The UTC date/time that the member was notified of the outcome of the appeal/grievance in writing. This includes mail lag if it is configured in the Mail Department activity. |
| 26 | `MEM_OUT_WRIT_NOTIF_LOCAL_DTTM` | DATETIME (Attached) |  | The local date/time that the member was notified of the outcome of the appeal/grievance in writing. This includes mail lag if it is configured in the Mail Department activity. Stored in the time zone determined by column APPEAL_GRV.TAT_RPT_TIME_ZONE_C. |
| 27 | `QUEUED_COMPLETE_USER_ID` | VARCHAR |  | The unique ID of the user that attempted to advance from the Finalize workflow step to the Completed workflow step and queued this appeal/grievance for auto-completion. |
| 28 | `QUEUED_COMPLETE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 29 | `COMPLETED_UTC_DTTM` | DATETIME (UTC) |  | The UTC datetime that the workflow step (APPEAL_GRV_2.APPEAL_GRV_WKFL_STEP_C) of this appeal or grievance was advanced from the Finalize workflow step to the Completed workflow step (in UTC). Even if this appeal or grievance was previously queued for auto-completion, this is when the workflow step was actually changed. |
| 30 | `COMPLETED_LOCAL_DTTM` | DATETIME (Attached) |  | The local datetime that the workflow step (APPEAL_GRV_2.APPEAL_GRV_WKFL_STEP_C) of this appeal or grievance was advanced from the Finalize workflow step to the Completed workflow step. Even if this appeal or grievance was previously queued for auto-completion, this is when the workflow step was actually changed. Stored in the time zone determined by column APPEAL_GRV.TAT_RPT_TIME_ZONE_C. |
| 31 | `PROCESSING_TYPE_C_NAME` | VARCHAR |  | The processing type category ID for the appeal or grievance |
| 32 | `AG_CREATION_METHOD_C_NAME` | VARCHAR |  | The creation method category ID for the appeal/grievance. |
| 33 | `REQ_ADDL_REVIEW_C_NAME` | VARCHAR |  | Enter the type of additional review required for the appeal. |
| 34 | `SUGGESTED_APPEAL_DECISION_C_NAME` | VARCHAR |  | The suggested decision category ID for the appeal. |
| 35 | `SUGGESTED_DECISION_USER_ID` | VARCHAR |  | The unique ID associated with the user record that made the suggested decision for the appeal. This column is frequently used to link to the CLARITY_EMP table. |
| 36 | `SUGGESTED_DECISION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 37 | `SUGGESTED_DECISION_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) when the appeal suggested decision was made. |
| 38 | `SUGGESTED_DECISION_LOCAL_DTTM` | DATETIME (Attached) |  | The date/time that the appeal suggested decision was made. Stored in the time zone determined by column APPEAL_GRV.TAT_RPT_TIME_ZONE_C. |
| 39 | `EDITED_AFTER_COMPLETION_YN` | VARCHAR |  | Indicates whether the appeal or grievance was edited after completion. 'Y' indicates that it was edited after completion. 'N' or NULL indicate that it was not edited after completion. |
| 40 | `DECISION_LOGIN_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 41 | `SUGGESTED_DECISION_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 42 | `MEDICARE_CVG_TYP_C_NAME` | VARCHAR |  | The Medicare part that this appeal/grievance involves. |
| 43 | `IS_PART_B_DRUG_YN` | VARCHAR |  | If this appeal/grievance involves a Part B drug. |
| 44 | `LATE_FILING_RCV_LOCAL_DTTM` | DATETIME (Attached) |  | The local datetime that the reasons for late filing were received. Stored in the time zone determined by column APPEAL_GRV.TAT_RPT_TIME_ZONE_C. |
| 45 | `REQUESTING_REP_DOCUMENT_REQ_YN` | VARCHAR |  | Whether a document is required for the requesting representative. 'Y' indicates that a document is required. 'N' indicates that a document is not required. 'NULL' indicates that the appeal or grievance was not requested by a representative. |
| 46 | `CASE_FILE_DUE_UTC_DTTM` | DATETIME (UTC) |  | The date and time that the case file must be forwarded for the higher level appeal in order to stay compliant for all timeliness standards. Stored in UTC. |
| 47 | `CASE_FILE_DUE_LOCAL_DTTM` | DATETIME (Attached) |  | The date and time that the case file must be forwarded for the higher level appeal in order to stay compliant for all timeliness standards. Stored in the time zone determined by column APPEAL_GRV.TAT_RPT_TIME_ZONE_C. |
| 48 | `APPEAL_ORIG_DENIAL_RSN_C_NAME` | VARCHAR | org | The original denial reason category ID for the appeal. |
| 49 | `NEXT_OUTST_CASE_FWD_UTC_DTTM` | DATETIME (UTC) |  | The date and time of the earliest outstanding case file due requirement, in UTC. If there are no outstanding case file due requirements, this item will be null. |
| 50 | `NEXT_OUTST_CASE_FWD_LOCAL_DTTM` | DATETIME (Attached) |  | The date and time of the earliest outstanding case file due requirement. If there are no outstanding case file due requirements, this item will be null. Stored in the time zone determined by column APPEAL_GRV.TAT_RPT_TIME_ZONE_C. |
| 51 | `CASE_FILE_ON_TIME_C_NAME` | VARCHAR |  | The on time status category ID of case file timeliness requirements. |
| 52 | `FILED_LATE_REPORTABLE_YN` | VARCHAR |  | Yes means that the appeal or grievance was filed outside of the filing timeframe, either as calculated by the system in FILED_ON_TIME_C or specified in the override FILED_LATE_OVERRIDE_YN. No or blank means it was not filed outside of the timeframe. |
| 53 | `RECORD_CREATE_LOCAL_DTTM` | DATETIME (Attached) |  | Record Create Instant (UTC) (I TAG 9000) converted to local time based on TAT Reportable Time Zone (I TAG 10502). |
| 54 | `PROCESS_AS_FORMAL_GRIEVANCE_YN` | VARCHAR |  | Indicates whether this grievance should always go through the formal grievance process. 'Y' indicates that it should. 'N' or NULL indicate that the grievance can go through the informal grievance process. |
| 55 | `UPGRADE_TO_FORMAL_UTC_DTTM` | DATETIME (UTC) |  | The date and time of the deadline for when an informal grievance must be upgraded to a formal grievance, in UTC. |
| 56 | `UPGRADE_TO_FORMAL_LOCAL_DTTM` | DATETIME (Attached) |  | The date and time of the deadline for when an informal grievance must be upgraded to a formal grievance, in local time based on TAT Reportable Time Zone (I TAG 10502). |
| 57 | `AG_FORMALITY_C_NAME` | VARCHAR |  | The formality category ID of the appeal/grievance (formal or informal). |
| 58 | `UPGRD_FRML_OCCR_UTC_DTTM` | DATETIME (UTC) |  | The date and time when an informal grievance was upgraded to a formal grievance in UTC. |
| 59 | `UPGRD_FRML_OCCR_LOC_DTTM` | DATETIME (Attached) |  | The date and time when an informal grievance was upgraded to a formal grievance in local time based on TAT Reportable Time Zone (I TAG 10502). |
| 60 | `TAG_SOURCE_TYPE_C_NAME` | NUMERIC | org | How this appeal or grievance was submitted to the health plan. |
| 61 | `APPEAL_EXCEPTION_TYPE_C_NAME` | NUMERIC |  | The exception type category ID of the appeal/grievance. |
| 62 | `INITIATING_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 63 | `REQUESTING_PROV_ADDRESSID` | VARCHAR |  | This stores the address ID of the requesting provider. The format is as follows: ProvID-AddressID. AddressID is the line number of the multiple response address items in the SER masterfile. To use this column, join to CLARITY_SER_ADDR on APPEAL_GRV_2.REQUESTING_PROV_ADDRESSID= CLARITY_SER_ADDR.ADDR_UNIQUE_ID. If you use IntraConnect, also join on APPEAL_GRV.INITIATING_PROV_ID = CLARITY_SER_ADDR.PROV_ID. |
| 64 | `SUBJECT_PROV_ADDRESSID` | VARCHAR |  | This stores the address ID of the subject provider. The format is as follows: ProvID-AddressID. AddressID is the line number of the multiple response address items in the SER masterfile. To use this column, join to CLARITY_SER_ADDR on APPEAL_GRV_2.SUBJECT_PROV_ADDRESSID= CLARITY_SER_ADDR.ADDR_UNIQUE_ID. If you use IntraConnect, also join on APPEAL_GRV.SUBJECT_PROV_ID = CLARITY_SER_ADDR.PROV_ID. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

## Joined in

Inbound joins are tracked on the logical base [APPEAL_GRV](APPEAL_GRV.md).

