# ORDER_RAD_AUDIT

> ORDER_RAD_AUDIT stores information about imaging audit actions logged on procedure records.

**Primary key:** `ORDER_PROC_ID`, `LINE`  
**Columns:** 43  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `LINE` | INTEGER | PK | The line count for this table as determined by the number of audit actions performed on an order. |
| 3 | `AUDIT_ACT_C_NAME` | VARCHAR |  | The auditing category ID for the radiology action that took place. |
| 4 | `AUDIT_TM` | DATETIME (Local) |  | The date and time that an audit action took place. |
| 5 | `USER_ID` | VARCHAR | FK→ | The user that performed the audited action. |
| 6 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `AUDIT_ORDER_STAT_C_NAME` | VARCHAR |  | The study status category number for the order at the time of the audited event. |
| 8 | `AUD_TECH_USER_ID` | VARCHAR |  | The unique identifier of the user that was the technologist user related to the audit action. The source item is located at ORDER_PROC.TECHNOLOGIST_ID. |
| 9 | `AUD_TECH_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `AUD_TRANS_USER_ID` | VARCHAR |  | The unique identifier of the user that is the transcriptionist related to the audit action. The source item is located at ORDER_PROC.RIS_TRANS_ID. |
| 11 | `AUD_TRANS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `AUD_CHG_STAT_REASON_C_NAME` | VARCHAR | org | The change status reason category ID for the audited order. The source item is located at ORDER_PROC_2.CHANGE_REASON_C. |
| 13 | `AUD_EXAM_BG_DTTM` | DATETIME (Attached) |  | This column contains the audited information about the begin exam date and time. The source item is located at ORDER_PROC.PROC_BGN_TIME. |
| 14 | `AUD_EXAM_END_DTTM` | DATETIME (Attached) |  | This column contains the audited information about the end exam date and time. The source item is located at ORDER_PROC.PROC_END_TIME. |
| 15 | `AUD_PROC_BEG_DTTM` | DATETIME (Local) |  | This column contains the audited information about the begin date and time for the procedure. The source item is located at ORDER_PROC_2.MOD_BEGIN_TM. |
| 16 | `AUD_PROC_END_DTTM` | DATETIME (Local) |  | This column contains the audited information about the end date and time for the procedure. The source item is located at ORDER_PROC_2.MOD_END_TM. |
| 17 | `AUD_OVRD_BGNEND_HS_DTTM` | DATETIME (Attached) |  | This column contains the audit information for the last time a user overrode a hard stop at begin/end. The source item is located at ORDER_PROC_2.OVERRIDE_TM. |
| 18 | `AUD_CHG_STAT_CMT` | VARCHAR |  | This column contains comments about the change status reason. The source item is located at ORDER_PROC_2.CHANGE_CMT. |
| 19 | `AUD_RSLT_PRTY_C_NAME` | VARCHAR | org | The priority category ID of the result priority of the audited order. The source item is located at ORDER_PROC_2.ORDER_PRIORITY_C. |
| 20 | `AUD_RELEASED_ORD` | VARCHAR |  | This column contains the audited information about the future/standing order released child instant. The source item is located at ORDER_PROC.INSTANTIATED_TIME. |
| 21 | `AUD_NUM_SIG_REQ` | INTEGER |  | This column contains the audited information about the number of signatures required for the study. The source item is located at ORDER_PROC_3.NUM_SIG_REQ. |
| 22 | `AUD_GROUPER_ORDER_ID` | NUMERIC |  | The unique identifier of the order that represents the MOPS (Multiple Orders Per Study) Order ID. The source item is located at ORDER_PROC_2.GRP_ORDER_PROC_ID. |
| 23 | `AUD_OVERALL_BRST_DENS_C_NAME` | VARCHAR | org | The overall breast density category ID for the audited order. The source item is located at ORDER_STATUS.OVRL_BREAST_DENS_C. |
| 24 | `AUD_RIGHT_BRST_DENS_C_NAME` | VARCHAR |  | The right breast density category ID for the audited order. The source item is located at ORDER_STATUS.RIGHT_BREAST_DENS_C. |
| 25 | `AUD_LEFT_BRST_DENS_C_NAME` | VARCHAR |  | The left breast density category ID for the audited order. The source item is located at ORDER_STATUS.LEFT_BREAST_DENS_C. |
| 26 | `AUD_OVERALL_ASMT_C_NAME` | VARCHAR | org | The overall assessment category ID for the audited order. The source item is located at ORDER_RAD_ASMT.ASSESSMENT_C. |
| 27 | `AUD_RIGHT_ASMT_C_NAME` | VARCHAR |  | The right assessment category ID for the audited order. The source item is located at ORDER_RAD_ASMT.RIGHT_ASMT_C. |
| 28 | `AUD_LEFT_ASMT_C_NAME` | VARCHAR |  | The left assessment category ID for the audited order. The source item is located at ORDER_RAD_ASMT.LEFT_ASMT_C. |
| 29 | `AUD_READING_PRI_C_NAME` | VARCHAR |  | The priority category ID of the imaging reading priority for the audited order. The source item is located at ORDER_PROC_2.READING_PRIORITY_C. |
| 30 | `AUD_MAM_LTR_TMPLT_SMARTTEXT_ID` | VARCHAR |  | This column contains the audited information about the result letter template. The source item is located at ORDER_STATUS.RIS_LET_TEMPLT_ID. |
| 31 | `AUD_MAM_LTR_TMPLT_SMARTTEXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 32 | `AUD_OVRL_TC_C_NAME` | VARCHAR |  | The overall tissue composition category ID for the audited order. The source item is located at ORDER_STATUS.OVRL_TISSUE_COMP_C. |
| 33 | `AUD_RIGHT_TC_C_NAME` | VARCHAR |  | The right tissue composition category ID for the audited order. The source item is located at ORDER_STATUS.RIGHT_TISSUE_COMP_C. |
| 34 | `AUD_LEFT_TC_C_NAME` | VARCHAR |  | The left tissue composition category ID for the audited order.The source item is located at ORDER_STATUS.LEFT_TISSUE_COMP_C. |
| 35 | `AUD_OVRL_FGT_C_NAME` | VARCHAR |  | The overall amount of fibroglandular tissue category ID for the audited order. The source item is located at ORDER_STATUS.OVRL_FGT_C. |
| 36 | `AUD_RIGHT_FGT_C_NAME` | VARCHAR |  | The right amount of fibroglandular tissue category ID for the audited order. The source item is located at ORDER_STATUS.RIGHT_FGT_C. |
| 37 | `AUD_LEFT_FGT_C_NAME` | VARCHAR |  | The left amount of fibroglandular tissue category ID for the audited order. The source item is located at ORDER_STATUS.LEFT_FGT_C. |
| 38 | `AUD_OVRL_BPE_C_NAME` | VARCHAR |  | The overall background parenchymal enhancement category ID for the audited order. The source item is located at ORDER_STATUS.OVRL_BPE_C. |
| 39 | `AUD_RIGHT_BPE_C_NAME` | VARCHAR |  | The right background parenchymal enhancement category ID for the audited order. The source item is located at ORDER_STATUS.RIGHT_BPE_C. |
| 40 | `AUD_LEFT_BPE_C_NAME` | VARCHAR |  | The left background parenchymal enhancement category ID for the audited order. The source item is located at ORDER_STATUS.LEFT_BPE_C. |
| 41 | `AUD_SYMMETRIC_BPE_C_NAME` | VARCHAR |  | The symmetric background parenchymal enhancement category ID for the audited order. The source item is located at ORDER_STATUS.SYMMETRIC_BPE_C. |
| 42 | `AUD_IL_PRI_ORDER_ID` | NUMERIC |  | The unique identifier of the order that is the image linked primary order. The source item is located at ORDER_PROC_4.IMG_PRIMARY_ORD_ID. |
| 43 | `AUD_HORMONES_NO_HISTORY` | VARCHAR |  | Audit of the 'No Hormone History' item for hormones relevant to breast imaging exams captured in the hormone history navigator. The source item is located at ORDER_PROC_4.MAM_HORMONE_NONE_YN. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

