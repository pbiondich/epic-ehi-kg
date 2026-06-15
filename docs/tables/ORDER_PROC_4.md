# ORDER_PROC_4

> The ORDER_PROC_4 table enables you to report on the procedures ordered in the clinical system. This procedure table has the same basic structure as ORDER_PROC, but was created as a fourth table to prevent ORDER_PROC_3 from getting any larger.

**Overflow of:** [ORDER_PROC](ORDER_PROC.md)  
**Primary key:** `ORDER_ID`  
**Columns:** 64  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record for this row. |
| 2 | `LAST_MAMMO_ORD_ID` | NUMERIC |  | The last breast procedure that was performed on this patient prior to this order. |
| 3 | `LAST_MAMMO_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 4 | `LAST_MAMMO_PROC_NAM` | VARCHAR |  | The last breast procedure that was performed. This field allows you to freely specify a procedure name in case it was performed outside the organization. |
| 5 | `LAST_MAMMO_DATE` | DATETIME |  | The date when the last breast procedure was performed. |
| 6 | `LAST_MAMMO_WEIGHT` | NUMERIC |  | The patient's weight (oz.) at the last breast procedure. |
| 7 | `EXAM_MAMMO_WEIGHT` | NUMERIC |  | The patient's weight (oz.) at the time of this procedure. |
| 8 | `LAST_MAM_WT_RECD_DT` | DATETIME |  | The date when the weight at last breast procedure was recorded. |
| 9 | `EXAM_MAM_WT_RECD_DT` | DATETIME |  | The date when patient's current weight was recorded. |
| 10 | `MAM_HX_REVD_USER_ID` | VARCHAR |  | The last person to review the last breast procedure information. |
| 11 | `MAM_HX_REVD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `MAMMO_BASELINE_YN` | VARCHAR |  | Whether or not this is the patient's first breast procedure. |
| 13 | `LAST_MAMMO_EXT_YN` | VARCHAR |  | Whether the last breast procedure was done externally. |
| 14 | `MAMMO_WEIGHT_CHANGE` | NUMERIC |  | The patient's weight change (oz.). |
| 15 | `MAM_WT_CHNG_RECD_DT` | NUMERIC |  | The date the patient's weight change was recorded. |
| 16 | `MAM_HORMONE_NONE_YN` | VARCHAR |  | Whether the patient has no mammography-relevant hormone history, documented by the tech in the visit navigator. |
| 17 | `MAMMO_HX_REVD_DTTM` | DATETIME (UTC) |  | The instant the last breast procedure information was reviewed. |
| 18 | `MAM_HORMNE_REV_U_ID` | VARCHAR |  | The last user to review the hormone history. |
| 19 | `MAM_HORMNE_REV_U_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 20 | `MAM_HORMNE_REV_DTTM` | DATETIME (UTC) |  | The instant the hormone history was last reviewed. |
| 21 | `BREAST_SELF_EXAM_C_NAME` | VARCHAR |  | The category ID that indicates whether or not a patient performs breast self-exams, which map to Yes, No, or N/A. |
| 22 | `RIS_LTR_NOT_NEED_YN` | VARCHAR |  | Indicates whether a study is marked as not needing a mammography result letter. 'Y' indicates a study has been marked as not needing a result letter. |
| 23 | `REQ_PER_PERIOD` | INTEGER |  | Requested units/visits per period. This along with the Requested periods (REQ_PERIODS) determines the total 'requested units'. |
| 24 | `REQ_FREQ_C_NAME` | VARCHAR |  | The category ID for the frequency of visits/units requested for the procedure (e.g. day, week, month, year). |
| 25 | `REQ_PERIODS` | INTEGER |  | Requested periods. Requested units per period (REQ_PER_PERIOD) along with the requested periods determines the total 'requested units'. |
| 26 | `APPR_PER_PERIOD` | INTEGER |  | Approved units/visits per period. This along with the approved periods (APPR_PERIODS) determines the total 'approved units'. |
| 27 | `APPR_FREQ_C_NAME` | VARCHAR |  | The category ID for the frequency of visits/units approved for the procedure (e.g. day, week, month, year). |
| 28 | `APPR_PERIODS` | INTEGER |  | Approved periods. Also known as duration. Approved units per period (APPR_PER_PERIOD) along with the approved periods determines the total 'approved units'. |
| 29 | `PROC_LNC_ID_LNC_LONG_NAME` | VARCHAR |  | The more readable format than the fully specified name in Logical Observation Identifiers Names and Codes (LOINC®) code. |
| 30 | `ABNORMAL_NOADD_YN` | VARCHAR |  | Indicates whether the most recent result is abnormal. 'Y' indicates that the most recent update of the result was marked abnormal. 'N' indicates that the abnormal flag is not set, or marked as normal. This is set to 'N' when a result is in progress, and will be updated as result updates are filed. |
| 31 | `NUM_IMGS_PERFORMED` | INTEGER |  | The number of images performed by a tech during the imaging exam linked to this order. This number is a total for the exam and includes images done on other procedures linked to the same appointment. |
| 32 | `IPROC_STATUS_C_NAME` | VARCHAR |  | The imaging and procedure status category ID of an order. |
| 33 | `SPEC_DRAW_TYPE_C_NAME` | VARCHAR | org | The specimen draw type category ID for the order. |
| 34 | `ANTICOAG_INR_GOAL_C_NAME` | VARCHAR | org | The International Normalized Ratio (INR) goal category ID for a patient on anticoagulation therapy. |
| 35 | `ANTICOAG_RESP_POOL_ID` | NUMERIC |  | Pool of providers responsible for a patient on anticoagulation therapy. |
| 36 | `ANTICOAG_RESP_POOL_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 37 | `ANTICOAG_NEXT_INR_DT` | DATETIME |  | The date of the next International Normalized Ratio (INR) check for a patient on anticoagulation therapy. |
| 38 | `ANTICOAG_WEEKLY_MAX_DOSE` | NUMERIC |  | Weekly maximum dose of anticoagulant for a patient on anticoagulation therapy. |
| 39 | `ANTICOAG_TARGET_END_DT` | DATETIME |  | Targeted end date for the patient's anticoagulation therapy. |
| 40 | `ANTICOAG_INDEFINITE_YN` | VARCHAR |  | Indicates whether a patient is indefinitely on anticoagulation. 'Y' indicates anticoagulation is indefinite (no end date set for anticoagulation). |
| 41 | `IPROC_STATUS_INST_DTTM` | DATETIME (Local) |  | The instant of the last Imaging and Procedure (IProc) status update of an order. |
| 42 | `SCREENING_FORM_ID` | NUMERIC |  | The unique ID of the screening form linked to the order. |
| 43 | `SUBMITTER_ID` | NUMERIC |  | The unique ID of the external site (submitter) associated that originally placed the order. |
| 44 | `SUBMITTER_ID_RECORD_NAME` | VARCHAR |  | The name of the submitter record. |
| 45 | `INDICATION_COMMENTS` | VARCHAR |  | The comment entered for the indications of use for this order. |
| 46 | `COLL_END_DT` | DATETIME |  | This is the end date for an observation. This typically equates to the end date of a specimen collection or the end date of a procedure. |
| 47 | `COLL_END_TM` | DATETIME |  | This is the end time for an observation. This typically equates to the end time of a specimen collection or the end time of a procedure. |
| 48 | `COLL_AMT` | VARCHAR |  | The amount of specimen that was collected. The identifier for the units for this amount are in COLL_AMT_UNIT_ID. |
| 49 | `COLL_AMT_UNIT_ID` | NUMERIC |  | The unique identifier for unit of the specimen collection amount (COLL_AMT) for this order. |
| 50 | `COLL_AMT_UNIT_ID_UNIT_NAME` | VARCHAR |  | Record name |
| 51 | `DEST_ANCILLARY_C_NAME` | VARCHAR | org | The ancillary category ID for the destination ancillary that is responsible for this order. |
| 52 | `REF_TO_PROV_ADDR_ID` | VARCHAR |  | Address selected for the referred-to provider. Format: {External provider ID}-{Address Line #} |
| 53 | `REFLEX_SOURCE_C_NAME` | VARCHAR |  | The reflex source category ID for the order. |
| 54 | `BREAST_IMG_TYPE_C_NAME` | VARCHAR |  | The imaging type category ID used to indicate whether standard imaging only, or standard plus additional imaging, was performed. Category values used for the NMD 3.0 extract. |
| 55 | `SCHED_DUR` | INTEGER |  | The amount of time (in minutes) the order will contribute to an appointment |
| 56 | `SCHED_DUR_IS_CALC_YN` | VARCHAR |  | Indicates whether the scheduling duration was calculated by the system. 'Y' indicates it was calculated by the system. 'N' or NULL indicate it was not. |
| 57 | `SCHED_DUR_BUFFER` | INTEGER |  | The amount of time (in minutes) that should be added to system calculated scheduling duration as a buffer. |
| 58 | `SCHED_TOL_BEF` | INTEGER |  | How far before the expected date for the order the appointment can still be safely made. |
| 59 | `SCHED_TOL_AFTR` | INTEGER |  | How long after the expected date for the order the appointment can still be safely made. |
| 60 | `SCHED_TOL_NO_RESTR_BEF_YN` | VARCHAR |  | Indicates if the No restriction checkbox is checked for scheduling tolerance before the expected treatment date for a schedulable procedure. 'Y' indicates there are no restrictions. |
| 61 | `SCHED_TOL_NO_RESTR_AFTR_YN` | VARCHAR |  | Indicates if the No restriction checkbox is checked for scheduling tolerance after the expected treatment date for a schedulable procedure. 'Y' indicates there are no restrictions. |
| 62 | `PROTOCOLLED_ORD_ID` | NUMERIC |  | For an order that was placed from an imaging protocol, this item contains the protocolled imaging procedure order from which the order was placed. This item can be used to help associate contrast, medication, and point-of-care lab test orders with the protocolled procedure orders for which they were placed. |
| 63 | `PROTOCOL_SOURCE_ID` | NUMERIC |  | This item stores a pointer to the last order record that had its protocol edited by a user. When a protocol is edited this item should be populated on the order record that was edited. When a protocol is copied forward to another order record, this item should be populated on the destination order. |
| 64 | `FINAL_APPROVAL_YN` | VARCHAR |  | Whether final approval has been received for a procedure. If Yes, more approval does not need to be obtained. This item is used primarily for reporting purposes. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [ORDER_PROC](ORDER_PROC.md).

