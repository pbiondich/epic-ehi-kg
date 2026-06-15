# OR_LOG_2

> The OR_LOG_2 table contains OR management system log records.

**Overflow of:** [OR_LOG](OR_LOG.md)  
**Primary key:** `LOG_ID`  
**Columns:** 89  
**Org-specific columns:** 45

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log record. |
| 2 | `SURGICAL_RISK_C_NAME` | VARCHAR | org | This column contains the category level of the surgical risk in the log record. |
| 3 | `POTENTL_BLOODLOSS_C_NAME` | VARCHAR | org | This column contains the category level of the potential blood loss in the log record. |
| 4 | `AWARENESS_DT` | DATETIME |  | This column contains the date the patient was made aware of the surgery in the log record. |
| 5 | `VIDEO_PIC_TAKEN_YN` | VARCHAR |  | Indicates whether a video or picture was taken for this log. Y indicates that a video or picture was taken, and N indicates that a video or picture was not taken. |
| 6 | `VIDEO_PIC_DISP_C_NAME` | VARCHAR | org | The disposition category number for the picture or video taken in the log. |
| 7 | `OB_CSECT_TYPE_C_NAME` | VARCHAR | org | The category number for the c-section type as recorded in the surgical log. |
| 8 | `PREOP_HOLD_LOC_C_NAME` | VARCHAR | org | Stores the location where the patient is being held in preop holding. |
| 9 | `NO_COUNT_NEEDED_YN` | VARCHAR |  | This item marks the log/procedure as a no counts needed log. |
| 10 | `INTRAOP_XRAYS_CMT` | VARCHAR |  | This column displays the comment about intraop x-ray needs. |
| 11 | `IOP_XRAYS_C_NAME` | VARCHAR | org | The intraop x-rays needed category ID for the log record. |
| 12 | `ARE_PROPH_AB_REQ_C_NAME` | VARCHAR | org | The prophylactic antibiotics required category ID for the log record. |
| 13 | `CHARGE_BILL_AREA_ID` | NUMERIC |  | The bill area with which log charges should be associated. This is used for cost center routing. |
| 14 | `CHARGE_BILL_AREA_ID_BILL_AREA_NAME` | VARCHAR |  | The record name of this bill area, financial subdivision, or financial division. |
| 15 | `RSN_RETURN_OR_C_NAME` | VARCHAR | org | The reason a patient is returned to the OR. |
| 16 | `NHSN_SPINAL_LEVEL_C_NAME` | VARCHAR | org | Stores the NHSN spinal level. The category list is the standard list of spinal levels released by NHSN. |
| 17 | `HOLDING_BED_ID` | VARCHAR |  | Stores the bed record for the patient when in the Holding phase. |
| 18 | `HOLDING_BED_ID_BED_LABEL` | VARCHAR |  | The name of the bed. |
| 19 | `SPEC_NOT_REQUIRED_YN` | VARCHAR |  | Specimens were not required for this procedure. |
| 20 | `RAD_DAP_UNIT_C_NAME` | VARCHAR | org | Documents the unit for Dose Area Product (DAP) in the radiation tracking event for the current log. |
| 21 | `RETURN_TO_OR_TYPE_C_NAME` | VARCHAR | org | The category ID for the return to OR type. It indicates how the log relates to the past case. |
| 22 | `RETURN_TO_OR_ORIGINAL_CASE_ID` | VARCHAR |  | The unique ID of the case which is responsible for this log's return to OR. |
| 23 | `RETURN_TO_OR_REASON_C_NAME` | VARCHAR | org | The category ID for the return to OR reason. It further indicates how the log relates to the past case. |
| 24 | `RETURN_TO_OR_REASON_CMT` | VARCHAR |  | The comments specific to the return to OR reason. Entered by the user who documented the log as return to OR or a user who verified the return to OR documentation. |
| 25 | `RETURN_TO_OR_VERIFIED_BY_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 26 | `RETURN_TO_OR_ADDL_CMT` | VARCHAR |  | Additional comments for the return to OR. Entered by the user who documented the log as return to OR or a user who verified the return to OR documentation. |
| 27 | `RETURN_TO_OR_SUR_AGREE_YN` | VARCHAR |  | Indicates whether the surgeon of the original case agrees or disagrees with the return to OR documentation. |
| 28 | `RETURN_TO_OR_REV_STAT_C_NAME` | VARCHAR |  | The category ID for the return to OR review status. The status reflects the compliance from the original case's surgeon with reviewing the Return to OR documentation. |
| 29 | `CASE_CLASS_APPROPRIATE_C_NAME` | VARCHAR | org | This item stores whether or not the case classification is appropriate. |
| 30 | `REOPERATION_C_NAME` | VARCHAR |  | Indicates whether this surgical log is a re-operation. Y indicates that the surgical log is a re-operation. N or N/A indicates the surgical log is not a re-operation. |
| 31 | `PREVIOUS_OPERATION_DATE` | DATETIME |  | The date when a previous procedure associated with this surgical log was performed. |
| 32 | `IMPLANT_APPROACH_C_NAME` | VARCHAR | org | The surgical approach category ID for the surgical log. |
| 33 | `CEMENT_TECHNIQUE_C_NAME` | VARCHAR | org | The cement technique category ID for the surgical log. |
| 34 | `CEMENT_MIX_C_NAME` | VARCHAR | org | The bone cement mix category ID for the surgical log. |
| 35 | `BONE_GRAFT_C_NAME` | VARCHAR | org | The bone graft category ID for the surgical log. |
| 36 | `DEGEN_GLENOHUMERAL_C_NAME` | VARCHAR | org | The category ID for the type of glenohumeral joint degeneration for the surgical log. |
| 37 | `AP_CONGRUENCE_C_NAME` | VARCHAR | org | The anteposterior congruence category ID for the surgical log. |
| 38 | `CENTRIC_JOINT_C_NAME` | VARCHAR | org | The centric joint category ID for the surgical log. |
| 39 | `POST_ECCENTRIC_CAPUT_C_NAME` | VARCHAR | org | The posteriorly eccentric caput category ID for the surgical log. |
| 40 | `ANT_ECCENTRIC_CAPUT_C_NAME` | VARCHAR | org | The anteriorly eccentric caput category ID for the surgical log. |
| 41 | `CRANIO_CONGRUENCE_C_NAME` | VARCHAR | org | The joint craniocaudal congruence category ID for the surgical log. |
| 42 | `SUP_ECCENTRIC_CAPUT_C_NAME` | VARCHAR | org | The superiorly eccentric caput category ID for the surgical log. |
| 43 | `JOINT_CONGRUENCE_C_NAME` | VARCHAR | org | The joint congruence category ID for the surgical log. |
| 44 | `GLENOID_COMPONENT_C_NAME` | VARCHAR | org | The glenoid component category ID for the surgical log. |
| 45 | `HUMERAL_COMPONENT_C_NAME` | VARCHAR | org | The humeral component category ID for the surgical log. |
| 46 | `HUMERUS_STATUS_C_NAME` | VARCHAR | org | The humerus status category ID for the surgical log. |
| 47 | `GLENOID_STATUS_C_NAME` | VARCHAR | org | The glenoid status category ID for the surgical log. |
| 48 | `PREVIOUS_OPERATION_LOCATION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 49 | `SUPPORT_NET_YN` | VARCHAR |  | Indicates whether a support net was used for the surgical log. Y indicates a support net was used. N or a null value indicates a support net was not used. |
| 50 | `OR_LOG_P_CATS_C_NAME` | VARCHAR | org | For each surgical case, Canadian pediatric organizations submit a Pediatric Canadian Access Targets for Surgery (P-CATS) code that corresponds to a diagnosis. This is extracted and sent to a database where the data is used to analyze wait times for procedures in relation to diagnoses |
| 51 | `CLAVIEN_SCORE_PRIMARY_C_NAME` | VARCHAR | org | This item contains the documented Clavien score that defines complication severity for a procedure on a log. This item stores a single Clavien score. If multiple Clavien scores per log are needed, I ORL 4800 should be used. |
| 52 | `LOG_SERVICE_DATE` | DATETIME |  | This item stores the service date to be used when calculating charges for a log. This service date is calculated via case tracking events mapped in System and Location Definitions. It does not calculate based on Anesthesia or Patient events. |
| 53 | `OPERATION_INTENTION_C_NAME` | VARCHAR | org | The operation intention category ID for the surgical log. |
| 54 | `COMPLICATION_RSN_SURG_C_NAME` | VARCHAR | org | The complication as reason for surgery category ID for the surgical log. |
| 55 | `PREOP_ANTIBIOTICS_C_NAME` | VARCHAR | org | The preoperative antibiotics category ID for the surgical log. |
| 56 | `LAPAROSCOPY_C_NAME` | VARCHAR | org | The laparoscopy category ID for the surgical log. |
| 57 | `TEACHING_ASSISTANCE_YN` | VARCHAR |  | Indicates whether the surgery was for teaching assistance. Y indicates the surgery was for teaching assistance. N or a null value indicates the surgery was not for teaching assistance. |
| 58 | `FIRST_ASSIST_CO_SURGEON_YN` | VARCHAR |  | Indicates whether the assistant was a co-surgeon for the surgical log. Y indicates the assistant was a co-surgeon. N or a null value indicates the assistant was not a co-surgeon. |
| 59 | `COMPLICAT_GRADE_INTRA_C_NAME` | VARCHAR | org | The intra-op complication grade category ID for the surgical log. |
| 60 | `COMPLICAT_GRADE_POST_C_NAME` | VARCHAR | org | The post-op complication grade category ID for the surgical log. |
| 61 | `ANATOMICAL_RESECTION_C_NAME` | VARCHAR | org | The anatomical resection category ID for the surgical log. |
| 62 | `ACATS_CODE_C_NAME` | VARCHAR | org | For each surgical case, organizations in the Alberta province of Canada submit an Adult Coding Access Targets for Surgery (ACATS) code that corresponds to a diagnosis. This is extracted and sent to a database where the data is used to analyze wait times for procedures in relation to diagnoses. |
| 63 | `PANEL1_NO_COUNT_NEEDED_C_NAME` | VARCHAR |  | This item stores the "No Counts Needed" status for Panel 1. |
| 64 | `PANEL2_NO_COUNT_NEEDED_C_NAME` | VARCHAR |  | This item stores the "No Counts Needed" status for Panel 2. |
| 65 | `PANEL3_NO_COUNT_NEEDED_C_NAME` | VARCHAR |  | This item stores the "No Counts Needed" status for Panel 3. |
| 66 | `PANEL4_NO_COUNT_NEEDED_C_NAME` | VARCHAR |  | This item stores the "No Counts Needed" status for Panel 4. |
| 67 | `PANEL5_NO_COUNT_NEEDED_C_NAME` | VARCHAR |  | This item stores the "No Counts Needed" status for Panel 5. |
| 68 | `COSMETIC_PROC_LENGTH` | INTEGER |  | The cosmetic procedure length in minutes to be billed. |
| 69 | `NHSN_KNEE_PROSTHESIS_1_C_NAME` | VARCHAR |  | The type of knee prosthesis. Used for NHSN reporting. |
| 70 | `NHSN_KNEE_PROSTHESIS_2_C_NAME` | VARCHAR |  | The type of knee prosthesis. Used for NHSN reporting. |
| 71 | `NHSN_HIP_PROSTHESIS_1_C_NAME` | VARCHAR |  | The type of hip prosthesis. Used for NHSN reporting. |
| 72 | `NHSN_HIP_PROSTHESIS_2_C_NAME` | VARCHAR |  | The type of hip prosthesis. Used for NHSN reporting. |
| 73 | `RTLS_STAFF_TRACKING_ST_C_NAME` | VARCHAR |  | The RTLS tracking status for the log. |
| 74 | `PRE_OP_BED_ID` | VARCHAR |  | Pre-Op Bed |
| 75 | `PRE_OP_BED_ID_BED_LABEL` | VARCHAR |  | The name of the bed. |
| 76 | `PREOP_COND_C_NAME` | VARCHAR | org | Pre-Op Assessment |
| 77 | `POST_OP_BED_ID` | VARCHAR |  | Post-Op Bed |
| 78 | `POST_OP_BED_ID_BED_LABEL` | VARCHAR |  | The name of the bed. |
| 79 | `POST_OP_DEST_C_NAME` | VARCHAR | org | Post-Op Destination |
| 80 | `POSTOP_COND_C_NAME` | VARCHAR | org | Post-Op Condition |
| 81 | `PHASETWO_BED_ID` | VARCHAR |  | Phase II Bed |
| 82 | `PHASETWO_BED_ID_BED_LABEL` | VARCHAR |  | The name of the bed. |
| 83 | `LOG_PROC_LEVEL_C_NAME` | VARCHAR | org | Log Procedure Level used for billing |
| 84 | `CLIN_TRIAL_YN` | VARCHAR |  | Stores whether the log is a clinical trial log |
| 85 | `JNT_REVISION_YN` | VARCHAR |  | This item documents whether the log is for a revision of a joint procedure. It is used for Surgical Care Improvement Project (SCIP) reports. |
| 86 | `MISC_DEST` | VARCHAR |  | Destination |
| 87 | `ASA_RATE_C_NAME` | VARCHAR | org | ASA Rating |
| 88 | `PRE_CONSCISNS_C_NAME` | VARCHAR | org | Pre-Op Level of Consciousness |
| 89 | `POST_CONSCISNS_C_NAME` | VARCHAR |  | Post-Op Level of Consciousness |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

