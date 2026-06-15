# APPEAL_GRV

> This table contains information about an individual appeal or grievance.

**Overflow family:** [APPEAL_GRV_2](APPEAL_GRV_2.md)  
**Primary key:** `APPEAL_GRV_ID`  
**Columns:** 103  
**Org-specific columns:** 3  
**Joined by:** 24 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `APPEAL_GRV_ID` | NUMERIC | PK | The unique identifier (.1 item) for the appeal/grievance record. |
| 2 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 3 | `CM_LOG_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| 4 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc.). |
| 5 | `APPEAL_GRV_TYPE_C_NAME` | VARCHAR |  | The type of request this record represents. This is either an appeal or grievance. |
| 6 | `SERIES_IDENTIFIER` | VARCHAR |  | The series ID for the appeal/grievance. This value is shared across levels of appeal/grievance. |
| 7 | `EXTERNAL_IDENTIFIER` | VARCHAR |  | The identifier assigned to an appeal/grievance by an external entity. |
| 8 | `INITIATED_BY_TYPE_C_NAME` | VARCHAR |  | The type of person which initiated the appeal or grievance. |
| 9 | `INITIATING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 10 | `INITIATING_REP_MEM_RESP_GUID` | VARCHAR |  | If this record was initiated by an authorized representative this stores their Member Responsible GUID from the member's coverage. |
| 11 | `SUBMISSION_METHOD_C_NAME` | VARCHAR |  | How this appeal or grievance was submitted. |
| 12 | `REVIEW_LEVEL_C_NAME` | VARCHAR |  | The level of review within the appeals process. |
| 13 | `PAT_ID` | VARCHAR | FK→ | The member associated with the appeal or grievance. |
| 14 | `APPEAL_SUBJECT_TYPE_C_NAME` | VARCHAR |  | What the appeal was filed about. This is either an authorization or a claim. |
| 15 | `SUBJECT_AUTH_REQUEST_ID` | NUMERIC |  | Authorization that is being appealed or grieved about. |
| 16 | `SUBJECT_CLAIM_ID` | NUMERIC |  | The claim that the grievance is about. |
| 17 | `RESULT_AUTH_REQUEST_ID` | NUMERIC |  | The authorization created to effectuate the appeal decision in Epic. |
| 18 | `RESULT_CLAIM_ID` | NUMERIC |  | This column has been replaced by column RESULT_CLAIM_ID (TAG/430) in the table APPEAL_GRV_SUBJECT_RESULT. If the conversion has not run for this appeal, then this column will store the resulting claim for the appeal. |
| 19 | `RECORD_CREATE_UTC_DTTM` | DATETIME (UTC) |  | The instant that this record was created. |
| 20 | `RECORD_CREATE_USER_ID` | VARCHAR |  | The unique ID of the user who created this record. |
| 21 | `RECORD_CREATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 22 | `URGENCY_C_NAME` | VARCHAR |  | The urgency of the appeal or grievance. |
| 23 | `SUBMISSION_OVRIDE_UTC_DTTM` | DATETIME (UTC) |  | If Submission System Instant (UTC) (I TAG 10010) is incorrect, this stores the override. Stored in UTC. |
| 24 | `DECISION_SYS_UTC_DTTM` | DATETIME (UTC) |  | The system calculated date and time that a decision was made for the appeal or grievance. Stored in UTC. |
| 25 | `DECISION_USER_ID` | VARCHAR |  | The unique ID of the user that finalized the appeal decision. |
| 26 | `DECISION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 27 | `DECISION_OVRIDE_UTC_DTTM` | DATETIME (UTC) |  | If the System Calculated Decision Instant (UTC) (I TAG 10100) is incorrect, this will store the override. Stored in UTC. |
| 28 | `APPEAL_DECISION_C_NAME` | VARCHAR |  | The decision for the appeal. |
| 29 | `TIMEFRAME_START_UTC_DTTM` | DATETIME (UTC) |  | The earliest date and time across all relevant timeliness standards that the clock for processing the appeal ot grievance begins based on the table APPEAL_GRV_TAT_MILESTONES. Stored in UTC. |
| 30 | `SUBMISSION_RPT_UTC_DTTM` | DATETIME (UTC) |  | The compiled date and time an appeal or grievance was submitted to the organization. Equal to the Organization Submission instant (UTC) - Override (I TAG 10011) if it is set, otherwise Organization Submission instant (UTC) (I TAG 10010). Stored in UTC. |
| 31 | `SUBMISSION_SYS_UTC_DTTM` | DATETIME (UTC) |  | The system calculated date and time that the appeal or grievance was submitted to the organization. Stored in UTC. |
| 32 | `EXP_REQ_REC_UTC_DTTM` | DATETIME (UTC) |  | The date and time the request to expedite was received. Stored in UTC. |
| 33 | `WAS_UPGRADED_TO_EXP_YN` | VARCHAR |  | Indicates whether the urgency was changed from standard to expedited for this appeal or grievance. 'Y' indicates that the appeal or grievance was initially submitted with a standard urgency and then later upgraded to an expedited urgency. 'N' or NULL indicates that either the appeal or grievance was initially submitted with an expedited urgency, or the appeal or grievance was initially submitted with a standard priority, and the priority is still standard. |
| 34 | `EXP_REQ_DEC_UTC_DTTM` | DATETIME (UTC) |  | The date and time that a decision was made on whether to upgrade the appeal or grievance to an expedited priority. Stored in UTC. |
| 35 | `EXT_REQ_REC_UTC_DTTM` | DATETIME (UTC) |  | The date and time the request to extend the timeframe was received. Stored in UTC. |
| 36 | `EXT_DAYS` | NUMERIC |  | The number of days the deadline for the appeal or grievance was extended. |
| 37 | `EXT_REQ_DEC_UTC_DTTM` | DATETIME (UTC) |  | The date and time the decision was made on whether to extend the timeframe. Stored in UTC. |
| 38 | `EXT_MAX_DAYS` | NUMERIC |  | The maximum number of days the deadline can be extended. |
| 39 | `EFFECT_SYS_UTC_DTTM` | DATETIME (UTC) |  | The system calculated date and time for when the appeal was effectuated. Stored in UTC. |
| 40 | `EFFECT_OVR_UTC_DTTM` | DATETIME (UTC) |  | If Effectuation System Instant (UTC) (I TAG 10050) is incorrect, this will store the override. Stored in UTC. |
| 41 | `EFFECT_RPT_UTC_DTTM` | DATETIME (UTC) |  | The compiled date and time an was effectuated. Equal to the Effectuation override instant (UTC) (I TAG 10051) if it is set, otherwise Effectuation system instant (UTC) (I TAG 10050). Stored in UTC. |
| 42 | `EFFECT_DUE_UTC_DTTM` | DATETIME (UTC) |  | The date and time an appeal must be effectuated in order to stay compliant with all timeliness standards. Stored in UTC. |
| 43 | `OVERALL_DUE_UTC_DTTM` | DATETIME (UTC) |  | The date and time that the appeal or grievance must be fully completed in order to stay compliant with all timeliness standards. Stored in UTC. |
| 44 | `DECISION_RPT_UTC_DTTM` | DATETIME (UTC) |  | The date and time that a decision was made for an appeal or grievance. Equal to Decision Instant (UTC) - Override (I TAG 10101) if it is set, otherwise Decision Instant (UTC) (I TAG 10100). Stored in UTC. |
| 45 | `DECISION_DUE_UTC_DTTM` | DATETIME (UTC) |  | The date and time a decision must be made on an appeal or grievance in order to stay compliant with all timeliness standards. Stored in UTC. |
| 46 | `TAT_SYS_TIME_ZONE_C_NAME` | VARCHAR |  | The system calculated time zone category ID to use for TAT calculations based on the time zone of where the appeal/grievance record was created. |
| 47 | `TAT_OVR_TIME_ZONE_C_NAME` | VARCHAR |  | If TAT system time zone (I TAG 10500) is incorrect, this will store the category ID of the override. |
| 48 | `TAT_RPT_TIME_ZONE_C_NAME` | VARCHAR |  | The compiled time zone category ID to use for TAT calculations. Equal to TAT Override Time Zone (I TAG 10501) if it is set, otherwise TAT System Time Zone (I TAG 10500). |
| 49 | `TIMEFRAME_START_LOCAL_DTTM` | DATETIME (Attached) |  | The earliest date and time across all relevant timeliness standards that the clock for processing the appeal or grievance begins based on the table APPEAL_GRV_TAT_MILESTONES. Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 50 | `SUBMISSION_SYS_LOCAL_DTTM` | DATETIME (Attached) |  | The system calculated date and time that the appeal or grievance was submitted to the organization. Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 51 | `SUBMISSION_OVR_LOCAL_DTTM` | DATETIME (Attached) |  | If Submission System Instant (I TAG 10910) is incorrect, this stores the override. Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 52 | `SUBMISSION_RPT_LOCAL_DTTM` | DATETIME (Attached) |  | The compiled date and time an appeal or grievance was submitted to the organization. Equal to the Organization Submission instant - Override (I TAG 10911) if it is set, otherwise Organization Submission instant (I TAG 10910). Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 53 | `EXP_REQ_REC_LOCAL_DTTM` | DATETIME (Attached) |  | The date and time the request to expedite was received. Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 54 | `EXP_DEC_LOCAL_DTTM` | DATETIME (Attached) |  | The date and time that a decision was made on whether to upgrade the appeal or grievance to an expedited priority. Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 55 | `EXT_REQ_LOCAL_DTTM` | DATETIME (Attached) |  | The date and time the request to extend the timeframe was received. Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 56 | `EXT_DEC_LOCAL_DTTM` | DATETIME (Attached) |  | The date and time the decision was made on whether to extend the timeframe. Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 57 | `EFFECT_SYS_LOCAL_DTTM` | DATETIME (Attached) |  | The system calculated date and time for when the appeal was effectuated. Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 58 | `EFFECT_OVR_LOCAL_DTTM` | DATETIME (Attached) |  | If Effectuation System Instant (I TAG 10950) is incorrect, this will store the override. Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 59 | `EFFECT_RPT_LOCAL_DTTM` | DATETIME (Local) |  | The compiled date and time an appeal was effectuated. Equal to the Effectuation override instant (I TAG 10951) if it is set, otherwise Effectuation system instant (I TAG 10950). Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 60 | `EFFECT_DUE_LOCAL_DTTM` | DATETIME (Attached) |  | The date and time an appeal must be effectuated in order to stay compliant with all timeliness standards. Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 61 | `OVERALL_DUE_LOCAL_DTTM` | DATETIME (Attached) |  | The date and time that the appeal or grievance must be fully completed in order to stay compliant with all timeliness standards. Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 62 | `DECISION_LOCAL_DTTM` | DATETIME (Attached) |  | The system calculated date and time that a decision was made for the appeal or grievance. Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 63 | `DECISION_OVR_LOCAL_DTTM` | DATETIME (Attached) |  | If the System Calculated Decision Instant (I TAG 10990) is incorrect, this will store the override. Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 64 | `DECISION_RPT_LOCAL_DTTM` | DATETIME (Attached) |  | The date and time that a decision was made for an appeal or grievance. Equal to Decision Instant - Override (I TAG 10991) if it is set, otherwise Decision Instant (I TAG 10990). Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 65 | `DECISION_DUE_LOCAL_DTTM` | DATETIME (Attached) |  | The date and time a decision must be made on an appeal or grievance in order to stay compliant with all timeliness standards. Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 66 | `GRIEVANCE_SUBJECT_TYPE_C_NAME` | VARCHAR | org | The subject type category ID for the grievance. This specifies what the grievance is about. |
| 67 | `REASON_FOR_GRIEVANCE_C_NAME` | VARCHAR | org | The reason category ID for the grievance. |
| 68 | `SUBJECT_APPEAL_APPEAL_GRV_ID` | NUMERIC |  | The unique ID of the appeal that is the subject of this grievance. |
| 69 | `SUBJECT_GRIEVANC_APPEAL_GRV_ID` | NUMERIC |  | The unique ID of the grievance that is the subject of this grievance. |
| 70 | `SUBJECT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 71 | `SUBJECT_FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 72 | `SUBJECT_EMPLOYEE_USER_ID` | VARCHAR |  | The unique ID of the employee that is the subject of this grievance. |
| 73 | `SUBJECT_EMPLOYEE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 74 | `SUBJECT_RESOURCE_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 75 | `SUBJECT_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 76 | `SUBJECT_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 77 | `SUBJECT_BUS_SEG_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 78 | `SUBJECT_REGION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 79 | `SUBJECT_GROUP_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 80 | `SUBJECT_COVERAGE_ID` | NUMERIC |  | The unique ID of the coverage related to this grievance. |
| 81 | `GRIEVANCE_INCIDENT_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time that the incident occurred for this grievance. |
| 82 | `GRIEVANCE_INCIDENT_LOCAL_DTTM` | DATETIME (Attached) |  | The local date and time that the incident occurred for this grievance. Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 83 | `EXTENSION_INITIATED_BY_TYPE_C_NAME` | VARCHAR |  | Whether the extension was initiated by the health plan, or the appeal or grievance submitter. |
| 84 | `DECISION_OVR_USER_ID` | VARCHAR |  | If the Decision User ID System (I TAG 10103) is incorrect, this will store the override value. |
| 85 | `DECISION_OVR_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 86 | `DECISION_RPT_USER_ID` | VARCHAR |  | Stores the Decision User ID Override (I TAG 10104) if it is set. Otherwise stores the Decision User ID System (I TAG 10103). |
| 87 | `DECISION_RPT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 88 | `LATE_FILING_RCV_UTC_DTTM` | DATETIME (UTC) |  | The instant, in UTC, when the reasons for late filing were received. |
| 89 | `FILED_ON_TIME_C_NAME` | VARCHAR | org | The on time status category ID for the appeal/grievance. |
| 90 | `AG_REVIEW_TYPE_C_NAME` | VARCHAR |  | If the appeal/grievance is being reviewed internally or externally. |
| 91 | `REVIEW_AGENCY_ID` | VARCHAR |  | The unique ID of the agency responsible for processing the appeal/grievance. |
| 92 | `REVIEW_AGENCY_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |
| 93 | `CASE_SENT_REVW_ENTITY_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time that the appeal/grievance case file information was sent to the review entity. |
| 94 | `CASE_SENT_REVW_ENTY_LOCAL_DTTM` | DATETIME (Attached) |  | The local date and time that the appeal/grievance case file information was sent to the review entity. Stored in the time zone determined by column TAT_RPT_TIME_ZONE_C. |
| 95 | `COVERAGE_ID` | NUMERIC | FK→ | The unique ID of the coverage associated with the appeal or grievance. |
| 96 | `PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 97 | `BENEFIT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 98 | `LOB_ID` | VARCHAR | FK→ | The unique ID of the line of business associated with the appeal or grievance. |
| 99 | `LOB_ID_LOB_NAME` | VARCHAR |  | The name of the line of business record. |
| 100 | `MC_PEER_GROUP_C_NAME` | VARCHAR |  | The category ID of the managed care peer group of the coverage associated with the appeal or grievance. |
| 101 | `REGION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 102 | `MEDICAL_GROUP_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 103 | `SUBJECT_FREE_TEXT` | VARCHAR |  | Stores the name and/or the ID of the subject of the appeal/grievance if the subject is not a record in Epic. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `LOB_ID` | [CLARITY_LOB](CLARITY_LOB.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (24)

| From | Column | Confidence |
|------|--------|------------|
| [APPEAL_GRV_APPEAL_REASONS](APPEAL_GRV_APPEAL_REASONS.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_AUDIT_TRAIL](APPEAL_GRV_AUDIT_TRAIL.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_CHANGE_URGENCY](APPEAL_GRV_CHANGE_URGENCY.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_DSMISS_REASONS](APPEAL_GRV_DSMISS_REASONS.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_LATE_FILE_RSNS](APPEAL_GRV_LATE_FILE_RSNS.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_LETTER](APPEAL_GRV_LETTER.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_LETTER_ADDRESS](APPEAL_GRV_LETTER_ADDRESS.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_LETTER_GEN_HX](APPEAL_GRV_LETTER_GEN_HX.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_MAX_EXTENSION](APPEAL_GRV_MAX_EXTENSION.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_NOTIF_TAT](APPEAL_GRV_NOTIF_TAT.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_OUTCOMES](APPEAL_GRV_OUTCOMES.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_OVRTRN_REASONS](APPEAL_GRV_OVRTRN_REASONS.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_POST_APL_UPD](APPEAL_GRV_POST_APL_UPD.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_REC_STAT_HX](APPEAL_GRV_REC_STAT_HX.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_REOPEN_REASONS](APPEAL_GRV_REOPEN_REASONS.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_REQ_ATTACHMENT](APPEAL_GRV_REQ_ATTACHMENT.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_ROOT_CAUSES](APPEAL_GRV_ROOT_CAUSES.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_STEP_COMPLETE](APPEAL_GRV_STEP_COMPLETE.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_SUBJECT_RESULT](APPEAL_GRV_SUBJECT_RESULT.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_TAT_MILESTONES](APPEAL_GRV_TAT_MILESTONES.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_UPHOLD_REASONS](APPEAL_GRV_UPHOLD_REASONS.md) | `APPEAL_GRV_ID` | high |
| [APPEAL_GRV_VACATE_REASONS](APPEAL_GRV_VACATE_REASONS.md) | `APPEAL_GRV_ID` | high |
| [IB_MESSAGES_5](IB_MESSAGES_5.md) | `APPEAL_GRV_ID` | high |
| [V_EHI_AUDIT_TAG](V_EHI_AUDIT_TAG.md) | `APPEAL_GRV_ID` | high |

