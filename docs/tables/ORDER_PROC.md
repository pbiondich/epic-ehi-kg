# ORDER_PROC

> The ORDER_PROC table enables you to report on the procedures ordered in the clinical system. We have also included patient and contact identification information for each record.

**Overflow family:** [ORDER_PROC_2](ORDER_PROC_2.md), [ORDER_PROC_3](ORDER_PROC_3.md), [ORDER_PROC_4](ORDER_PROC_4.md), [ORDER_PROC_5](ORDER_PROC_5.md), [ORDER_PROC_6](ORDER_PROC_6.md), [ORDER_PROC_7](ORDER_PROC_7.md)  
**Primary key:** `ORDER_PROC_ID`  
**Columns:** 82  
**Org-specific columns:** 13  
**Joined by:** 41 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK | The unique ID of the order record associated with this procedure order. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this order. This column is frequently used to link to the PATIENT table. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across patients and encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 5 | `RESULT_LAB_ID` | NUMERIC |  | The unique ID of the lab or other resulting agency, such as radiology, that provided the order results. |
| 6 | `RESULT_LAB_ID_LLB_NAME` | VARCHAR |  | Interface laboratory name. |
| 7 | `ORDERING_DATE` | DATETIME |  | The date when the procedure order was placed. |
| 8 | `ORDER_TYPE_C_NAME` | VARCHAR | org | The order type category number for the procedure order. |
| 9 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 10 | `DESCRIPTION` | VARCHAR |  | A brief summary of the procedure order. |
| 11 | `ORDER_CLASS_C_NAME` | VARCHAR | org | The order class category number of the procedure order. |
| 12 | `AUTHRZING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 13 | `ABNORMAL_YN` | VARCHAR |  | Indicates whether or not this order contains abnormal results. This column will contain a Y if there are abnormal results and an N or null if it does not. For orders with lab component results, if any one component of this order has an abnormal result value then this will hold a Y. |
| 14 | `BILLING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 15 | `ORD_CREATR_USER_ID` | VARCHAR |  | The unique identifier of the user who signed the order, or the last person who performed a sign and hold or release action for a signed and held order. |
| 16 | `ORD_CREATR_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 17 | `LAB_STATUS_C_NAME` | VARCHAR |  | The category number for the status of results for an order, as of the date and time the record was extracted. |
| 18 | `ORDER_STATUS_C_NAME` | VARCHAR |  | The order status category number of the procedure order. |
| 19 | `MODIFIER1_ID` | VARCHAR |  | The unique ID of the modifier record. This is the first modifier entered for the procedure and affects how the procedure is billed. |
| 20 | `MODIFIER1_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |
| 21 | `MODIFIER2_ID` | VARCHAR |  | The unique ID of the modifier record. This is the second modifier entered for the procedure and affects how the procedure is billed. |
| 22 | `MODIFIER2_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |
| 23 | `MODIFIER3_ID` | VARCHAR |  | The unique ID of the modifier record. This is the third modifier entered for the procedure and affects how the procedure is billed. |
| 24 | `MODIFIER3_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |
| 25 | `MODIFIER4_ID` | VARCHAR |  | The unique ID of the modifier record. This is the fourth modifier entered for the procedure and affects how the procedure is billed. |
| 26 | `MODIFIER4_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |
| 27 | `QUANTITY` | INTEGER |  | The number of procedures authorized for this order. |
| 28 | `REASON_FOR_CANC_C_NAME` | VARCHAR | org | The reason for cancellation category number for the procedure order. |
| 29 | `FUTURE_OR_STAND` | VARCHAR |  | This column indicates whether an order is a Once (Future) (O) or Standing (S) order. |
| 30 | `STANDING_EXP_DATE` | DATETIME |  | The date when a recurring procedure order expires. |
| 31 | `FUT_EXPECT_COMP_DT` | DATETIME |  | The date by which each Once (Future) procedure order should be completed. Displayed in calendar format. |
| 32 | `STANDING_OCCURS` | INTEGER |  | The number of individual occurrences remaining for this procedure order. |
| 33 | `STAND_ORIG_OCCUR` | INTEGER |  | The total number of occurrences that a recurring order was authorized for. |
| 34 | `REFERRING_PROV_ID` | VARCHAR | FK→ | The unique ID of the provider who has referred this order, i.e. the referring provider. |
| 35 | `REFERRING_PROV_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 36 | `REFD_TO_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 37 | `REFD_TO_SPECLTY_C_NAME` | VARCHAR | org | The category value for the medical specialty of the provider to which the patient is referred. This field does not contain data for referral orders created within Epic. |
| 38 | `REQUESTED_SPEC_C_NAME` | VARCHAR | org | The medical specialty category number of the provider to which the patient was referred for the procedure order. |
| 39 | `RFL_CLASS_C_NAME` | VARCHAR |  | The referral class category number for the procedure order. |
| 40 | `RFL_TYPE_C_NAME` | VARCHAR | org | The referral type category number for the procedure order. |
| 41 | `RSN_FOR_RFL_C_NAME` | VARCHAR | org | The reason for referral category number for the procedure order. |
| 42 | `RFL_NUM_VIS` | INTEGER |  | The number of visits this referral order is authorized for. |
| 43 | `RFL_EXPIRE_DT` | DATETIME |  | The expiration date for this referral order. |
| 44 | `ABN_NOTE_ID` | VARCHAR | FK→ | The unique ID of the notes record representing the Advanced Beneficiary Notice form associated with this order. |
| 45 | `RADIOLOGY_STATUS_C_NAME` | VARCHAR |  | The category ID for the imaging study status (e.g. technician ended the exam, reading physician finalized the exam) of the procedure order. |
| 46 | `INT_STUDY_C_NAME` | VARCHAR | org | The category ID for denoting the reason a study is worth being marked for later review, as in for an educational case or for group reading physician review. |
| 47 | `INT_STUDY_USER_ID` | VARCHAR |  | The unique ID of the employee record who denoted a study as worth being marked for later review, as in for an educational case or for group reading physician review. |
| 48 | `INT_STUDY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 49 | `TECHNOLOGIST_ID` | VARCHAR |  | The unique ID of the employee record of the technologist who performed this procedure. |
| 50 | `TECHNOLOGIST_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 51 | `PROC_BGN_TIME` | DATETIME (Local) |  | The date and time when the procedure order (exam) is to begin. |
| 52 | `RIS_TRANS_ID` | VARCHAR |  | The unique ID of the user record of the transcriptionist for this order. |
| 53 | `RIS_TRANS_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 54 | `ORDER_INST` | DATETIME (Local) |  | The instant when the order was created. |
| 55 | `DISPLAY_NAME` | VARCHAR |  | The name of the order as it appears in the patient's record. |
| 56 | `HV_HOSPITALIST_YN` | VARCHAR |  | Indicates whether or not this order was placed by a hospitalist. ‘Y’ indicates that this order was placed by a hospitalist. ‘N’ or NULL indicate that this order was not placed by a hospitalist. |
| 57 | `ORDER_PRIORITY_C_NAME` | VARCHAR | org | The overall priority category number for the procedure order. |
| 58 | `CHRG_DROPPED_TIME` | DATETIME (Local) |  | The date and time when the charge was generated for the procedure order. |
| 59 | `PANEL_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 60 | `STAND_INTERVAL` | VARCHAR |  | The time interval set for a recurring order, indicating the time between one instance of the order and the next instance. |
| 61 | `DISCRETE_INTERVAL_NAME` | VARCHAR | org | The discrete interval for the order. This is extracted as the category title. |
| 62 | `INSTANTIATED_TIME` | DATETIME |  | The date and time of instantiation when a child order is generated from a parent order. |
| 63 | `INSTNTOR_USER_ID` | VARCHAR |  | The unique ID of the user who instantiated the order. |
| 64 | `INSTNTOR_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 65 | `DEPT_REF_PROV_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 66 | `SPECIALTY_DEP_C_NAME` | VARCHAR |  | The category value for the requested medical specialty of the department to which the patient is referred. |
| 67 | `SPECIMEN_TYPE_C_NAME` | VARCHAR | org | The specimen type category number for the procedure order. |
| 68 | `SPECIMEN_SOURCE_C_NAME` | VARCHAR | org | The source category number for the procedure order. |
| 69 | `ORDER_TIME` | DATETIME (Local) |  | The date and time when the procedure order was placed. |
| 70 | `RESULT_TIME` | DATETIME (Local) |  | The most recent date and time when the procedure order was resulted. |
| 71 | `IS_PENDING_ORD_YN` | VARCHAR |  | Indicates whether or not the order has a pending status. 'Y' indicates that the order has a pending status. 'N' or NULL indicates that the order does not have a pending status. |
| 72 | `PROC_START_TIME` | DATETIME (Local) |  | The date and time when the procedure order is to start. |
| 73 | `PROBLEM_LIST_ID` | NUMERIC | FK→ | The unique ID of the problem list record that is associated with this order. This column is mainly used for immunization orders. |
| 74 | `RSLTS_INTERPRETER` | VARCHAR |  | The name of the principal results interpreter, the person who reviewed and interpreted the results. |
| 75 | `PROC_ENDING_TIME` | DATETIME (Local) |  | The date and time when the procedure order is to end. |
| 76 | `SPECIFIED_FIRST_TM` | DATETIME (Local) |  | The first occurrence time specified by a user, if the order was signed with a frequency record containing a schedule of specified dates and times. |
| 77 | `SCHED_START_TM` | DATETIME (Local) |  | This column stores the scheduling start instant used when the order was last scheduled. |
| 78 | `SESSION_KEY` | VARCHAR |  | The unique key associated with the order at the time of signing. Other orders will share this key if they were signed at the same time. |
| 79 | `LABCORP_BILL_TYPE_C_NAME` | VARCHAR | org | The reference lab bill type category ID for the order record, indicating how reference labs should bill for services performed. |
| 80 | `LABCORP_CLIENT_ID` | VARCHAR |  | The client ID or account ID assigned by the reference lab. |
| 81 | `LABCORP_CONTROL_NUM` | INTEGER |  | Required information for LabCorp requisition and order messages. |
| 82 | `CHNG_ORDER_PROC_ID` | NUMERIC |  | The unique ID of the changed or reordered procedure order that this procedure replaced. This column is frequently used to link back to ORDER_PROC table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ABN_NOTE_ID` | [ABN_NOTES](ABN_NOTES.md) | sole_pk | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |
| `REFERRING_PROV_ID` | [REFERRAL_SOURCE](REFERRAL_SOURCE.md) | sole_pk | high |

## Joined in — referenced by (41)

| From | Column | Confidence |
|------|--------|------------|
| [HV_ORDER_PROC](HV_ORDER_PROC.md) | `ORDER_PROC_ID` | high |
| [IB_MESSAGES](IB_MESSAGES.md) | `ORDER_PROC_ID` | high |
| [INDICATOR_REL_ORD_TBL](INDICATOR_REL_ORD_TBL.md) | `ORDER_PROC_ID` | high |
| [ORDER_DX_PROC](ORDER_DX_PROC.md) | `ORDER_PROC_ID` | high |
| [ORDER_IMPRESSION](ORDER_IMPRESSION.md) | `ORDER_PROC_ID` | high |
| [ORDER_LINKED_FILMS](ORDER_LINKED_FILMS.md) | `ORDER_PROC_ID` | high |
| [ORDER_MYC_INFO](ORDER_MYC_INFO.md) | `ORDER_PROC_ID` | high |
| [ORDER_MYC_RELEASE](ORDER_MYC_RELEASE.md) | `ORDER_PROC_ID` | high |
| [ORDER_NARRATIVE](ORDER_NARRATIVE.md) | `ORDER_PROC_ID` | high |
| [ORDER_RAD_ACC_NUM](ORDER_RAD_ACC_NUM.md) | `ORDER_PROC_ID` | high |
| [ORDER_RAD_ASMT](ORDER_RAD_ASMT.md) | `ORDER_PROC_ID` | high |
| [ORDER_RAD_AUDIT](ORDER_RAD_AUDIT.md) | `ORDER_PROC_ID` | high |
| [ORDER_RAD_DICTATE](ORDER_RAD_DICTATE.md) | `ORDER_PROC_ID` | high |
| [ORDER_RAD_FILMS](ORDER_RAD_FILMS.md) | `ORDER_PROC_ID` | high |
| [ORDER_RAD_IMG_UID](ORDER_RAD_IMG_UID.md) | `ORDER_PROC_ID` | high |
| [ORDER_RAD_MODS](ORDER_RAD_MODS.md) | `ORDER_PROC_ID` | high |
| [ORDER_RAD_OWNERS](ORDER_RAD_OWNERS.md) | `ORDER_PROC_ID` | high |
| [ORDER_RAD_PATH_RES](ORDER_RAD_PATH_RES.md) | `ORDER_PROC_ID` | high |
| [ORDER_RAD_PRELIM](ORDER_RAD_PRELIM.md) | `ORDER_PROC_ID` | high |
| [ORDER_RAD_READING](ORDER_RAD_READING.md) | `ORDER_PROC_ID` | high |
| [ORDER_RAD_REC_ID](ORDER_RAD_REC_ID.md) | `ORDER_PROC_ID` | high |
| [ORDER_RAD_REPEATS](ORDER_RAD_REPEATS.md) | `ORDER_PROC_ID` | high |
| [ORDER_RAD_RSLT_CD](ORDER_RAD_RSLT_CD.md) | `ORDER_PROC_ID` | high |
| [ORDER_RAD_RVSN_RSN](ORDER_RAD_RVSN_RSN.md) | `ORDER_PROC_ID` | high |
| [ORDER_RAD_STUDY](ORDER_RAD_STUDY.md) | `ORDER_PROC_ID` | high |
| [ORDER_RESULTS](ORDER_RESULTS.md) | `ORDER_PROC_ID` | high |
| [ORDER_RES_ORDS](ORDER_RES_ORDS.md) | `ORDER_PROC_ID` | high |
| [ORDER_SENSITIVITY](ORDER_SENSITIVITY.md) | `ORDER_PROC_ID` | high |
| [ORDER_SIGNED_PROC](ORDER_SIGNED_PROC.md) | `ORDER_PROC_ID` | high |
| [ORDER_SUPPLY](ORDER_SUPPLY.md) | `ORDER_PROC_ID` | high |
| [ORD_ASMT_RMNDR_LTR](ORD_ASMT_RMNDR_LTR.md) | `ORDER_PROC_ID` | high |
| [ORD_FINDINGS](ORD_FINDINGS.md) | `ORDER_PROC_ID` | high |
| [RIS_ASGN_POOL](RIS_ASGN_POOL.md) | `ORDER_PROC_ID` | high |
| [RIS_ASGN_PROV](RIS_ASGN_PROV.md) | `ORDER_PROC_ID` | high |
| [RIS_BGN_PROC_ANS](RIS_BGN_PROC_ANS.md) | `ORDER_PROC_ID` | high |
| [RIS_END_PROC_ANS](RIS_END_PROC_ANS.md) | `ORDER_PROC_ID` | high |
| [RIS_INT_STUDY_CMT](RIS_INT_STUDY_CMT.md) | `ORDER_PROC_ID` | high |
| [RIS_SGND_INFO](RIS_SGND_INFO.md) | `ORDER_PROC_ID` | high |
| [RIS_STUDY_NOTES](RIS_STUDY_NOTES.md) | `ORDER_PROC_ID` | high |
| [RIS_SUPP_STAFF](RIS_SUPP_STAFF.md) | `ORDER_PROC_ID` | high |
| [TECH_COMPLETE_INFO](TECH_COMPLETE_INFO.md) | `ORDER_PROC_ID` | high |

