# ORDER_RES

> The ORDER_RES table contains result finding information for an order. Result findings include mammography pathology results, cardiovascular palette findings, and other result findings.

**Overflow family:** [ORDER_RES_2](ORDER_RES_2.md), [ORDER_RES_3](ORDER_RES_3.md)  
**Primary key:** `FINDING_ID`  
**Columns:** 98  
**Org-specific columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier of the finding record corresponding to the result. |
| 2 | `RESULT_TYPE_C_NAME` | VARCHAR |  | The result type category ID for the order result. |
| 3 | `FINDING_SIDE_C_NAME` | VARCHAR |  | The finding side category ID for the finding. |
| 4 | `FINDING_TYPE_C_NAME` | VARCHAR | org | The finding type category ID for the finding. |
| 5 | `RECOMMENDATION_C_NAME` | VARCHAR | org | The mammography recommendation category number for the finding. |
| 6 | `RECO_SIDE_C_NAME` | VARCHAR |  | The side of the body category ID for which side a mammography recommendation is for. Maps to Right, Left, or Bilateral. |
| 7 | `CLASS_OF_LESION_C_NAME` | VARCHAR | org | The classification of lesion category ID for the pathology result. |
| 8 | `SIZE_OF_TUMOR` | NUMERIC |  | The size of the tumor (mm) for pathology results of mammogram biopsies. |
| 9 | `PATH_FND_SIDE_C_NAME` | VARCHAR |  | The finding side category ID for the pathology result. |
| 10 | `HISTOLOGY_GRADE_C_NAME` | VARCHAR | org | The histology grade category ID for the pathology result. |
| 11 | `MARGIN_STATUS_C_NAME` | VARCHAR | org | The margin status category ID for the pathology result. |
| 12 | `NIPPLE_INVOLVED_YN_NAME` | VARCHAR |  | Indicates if nipple is included in the pathology result. |
| 13 | `NODES_REMOVED` | INTEGER |  | The number of nodes removed. |
| 14 | `NODES_POSITIVE` | INTEGER |  | The number of nodes positive in the pathology result. |
| 15 | `STAGE_C_NAME` | VARCHAR | org | The cancer staging category number for the finding. |
| 16 | `ESTROGEN_RECP_C_NAME` | VARCHAR | org | The estrogen receptor category ID for the estrogen receptor associated with the finding. |
| 17 | `PROGESTERONE_RCP_C_NAME` | VARCHAR |  | The estrogen receptor category ID that clarifies the progesterone receptor in the pathology result. |
| 18 | `S_PHASE` | INTEGER |  | The S phase for a specific pathology result. |
| 19 | `OB_ULTRASOUND_GA` | VARCHAR |  | The gestational age interpreted for the entire ultrasound, in days, for the result corresponding to ultrasound findings. |
| 20 | `NEEDS_FOLLOW_UP_C_NAME` | VARCHAR | org | The needs follow up category number for the order results. This is used as a flag for a recommendation record that needs follow up. |
| 21 | `MAMMO_DUE_DT` | DATETIME |  | Due date for the recommendation. |
| 22 | `MAMMO_FIND_CTX_C_NAME` | VARCHAR | org | The context category number for the mammography finding. This is populated using the enhanced drawing tools to document on breast diagrams within the radiology mammography module. |
| 23 | `ORIGINAL_FINDING_ID` | NUMERIC |  | The unique ID of the original finding this finding record was copied from. |
| 24 | `GRAFT_ID` | VARCHAR |  | The graft ID for this result. |
| 25 | `DOMINANCE_C_NAME` | VARCHAR | org | The coronary dominance category ID for the finding. |
| 26 | `ANNOTATION_TYPE_C_NAME` | VARCHAR |  | The annotation type category ID for the coronary diagram annotation result finding. |
| 27 | `ANNOT_VESSEL_ID` | NUMERIC |  | The major vessel of the annotation. |
| 28 | `ANNOT_VESSEL_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 29 | `ANNOT_SEGM_ID` | NUMERIC |  | The vessel segment ID. |
| 30 | `ANNOT_SEGM_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 31 | `ANNOT_END_SEGM_ID` | NUMERIC |  | The ending vessel segment ID. |
| 32 | `ANNOT_END_SEGM_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 33 | `COLLAT_END_VES_ID` | NUMERIC |  | The major vessel ID of the destination of a collateral. |
| 34 | `COLLAT_END_VES_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 35 | `COLLAT_END_SEGM_ID` | NUMERIC |  | The vessel segment of the destination of a collateral. |
| 36 | `COLLAT_END_SEGM_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 37 | `VESSEL_LOCATION_C_NAME` | VARCHAR | org | The vessel location category ID for the result record. |
| 38 | `SEGMENT_LOC_C_NAME` | VARCHAR |  | The location of the body category ID for an annotation of a segment. Used to distinguish between two separate annotations in the same segment. Maps to proximal and distal. |
| 39 | `LESION_PRE_STEN` | INTEGER |  | The pre-stent stenosis percentage for this result. |
| 40 | `LESION_POST_STEN` | INTEGER |  | The post-stent stenosis percentage for this result. |
| 41 | `INTERVENTION_TYPE_C_NAME` | VARCHAR | org | The intervention type category ID of the intervention. |
| 42 | `ATMOS_INFLATION` | NUMERIC |  | The measures of the balloon atmospheres inflation for the result. |
| 43 | `SEC_OF_INFLATION` | INTEGER |  | The number of seconds of balloon inflation measured for the result. |
| 44 | `STENT_LENGTH` | VARCHAR |  | Indicates length of the stent. |
| 45 | `STENT_DIAMETER` | VARCHAR |  | Indicates diameter of the stent. |
| 46 | `INTERVENTIO_SEQ_NUM` | INTEGER |  | The sequence of the intervention. |
| 47 | `GRAFT_PROX_ANAST_ID` | NUMERIC |  | The proximal anastomosis for a graft. |
| 48 | `GRAFT_PROX_ANAST_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 49 | `GR_DIST_ANST_VEL_ID` | NUMERIC |  | The major vessel of the distal anastomosis for a graft. |
| 50 | `GR_DIST_ANST_VEL_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 51 | `GR_DIST_ANST_SEG_ID` | NUMERIC |  | The vessel segment of the distal anastomosis for a graft. |
| 52 | `GR_DIST_ANST_SEG_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 53 | `GRAFT_SEQ_NUM` | INTEGER |  | The graft sequence number in a multi-vessel graft. |
| 54 | `CONDITION_C_NAME` | VARCHAR | org | The patient condition category ID for the result finding. |
| 55 | `TECH_DOC_DTTM` | DATETIME (UTC) |  | The instant at which this finding was documented in the procedure log. |
| 56 | `MAMMO_FIND_PULFW_YN` | VARCHAR |  | Indicates, at the finding level, whether or not a Mammo finding in Image Documentation should be pulled forward to future studies. |
| 57 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record with whom the result finding is associated. This column is frequently used to link to the PATIENT table. |
| 58 | `MAMFND_SRC_FIND_ID` | NUMERIC |  | The result finding unique identifier for the source result finding from which the current result finding record was copied. Typically populated for permanent findings such as scars or tattoos. |
| 59 | `MAMMO_BIOPSY_TYPE_C_NAME` | VARCHAR | org | The mammography biopsy type category ID for the pathology result. |
| 60 | `MAMFND_PFWD_VERF_YN` | VARCHAR |  | Indicates if a finding was verified in the Mammo Image Documentation section. |
| 61 | `PAT_CSN` | NUMERIC | FK→ | The unique contact serial number (CSN) of the patient for whom the contact was moved. |
| 62 | `LAST_FINDING_ID` | NUMERIC |  | The unique identifier for the most recent finding for a breast lesion. Use this column to join to another copy of ORDER_RES on the FINDING_ID column. This will only be populated for lesion records in ORDER_RES where RESULT_TYPE_C is equal to 52013 (Lesion). |
| 63 | `LAST_LSN_STAT_C_NAME` | VARCHAR |  | The mammography last lesion status for the lesion. |
| 64 | `CONF_OF_TARGET_C_NAME` | VARCHAR | org | The confirmation of target category ID for a breast biopsy lesion that indicates whether or not the suspicious lesion was obtained. |
| 65 | `IMG_DEVICE_USED_C_NAME` | VARCHAR | org | The imaging device used category ID for the finding of a breast biopsy. |
| 66 | `TECHNIQUE_USED_C_NAME` | VARCHAR | org | The technique used category ID for a breast biopsy. |
| 67 | `BIOPSY_REPEAT_TYP_C_NAME` | VARCHAR |  | The category number of the type of biopsy that was performed for a repeat procedure. |
| 68 | `MYOCARDIAL_TYPE_C_NAME` | VARCHAR | org | The myocardial finding type category ID for the finding, allowing the distinction of RES records used for echo documentation. |
| 69 | `PATH_RESULT_DATE` | DATETIME |  | The date on which a pathology result was returned from the lab after a breast biopsy was performed. |
| 70 | `INVASIVE_SIZE_MM` | NUMERIC |  | The size (mm) of the invasive component of a breast lesion. |
| 71 | `IN_SITU_SIZE_MM` | NUMERIC |  | The size (mm) of the in situ component of a breast legion. |
| 72 | `NUM_OF_MARGINS` | INTEGER |  | The number of margins that were identified anatomically and measured in metric units for a breast lesion. |
| 73 | `SPEC_COMP_SUBMTD_YN` | VARCHAR |  | Indicates whether the specimen was completely submitted (totally embedded) for microscopic evaluation following a surgical breast procedure. |
| 74 | `MAM_SURGERY_TYPE_C_NAME` | VARCHAR | org | The surgery type category ID for the pathology result. |
| 75 | `LN_EXTRA_EXTNSN_C_NAME` | VARCHAR |  | The extracapsular extension status category ID for the pathology result. |
| 76 | `HER2_IHC_C_NAME` | VARCHAR |  | The HER2/neu IHC category ID for the pathology result. |
| 77 | `HER2_FISH_C_NAME` | VARCHAR |  | The HER2/neu FISH category ID for the pathology result. |
| 78 | `STATUS_C_NAME` | VARCHAR |  | The lab status category ID for a follow-up recommendation. |
| 79 | `GENERAL_RECOM_C_NAME` | VARCHAR | org | The general recommendation category ID for the follow-up recommendation of a non-mammography study. |
| 80 | `GEN_REC_ANAT_RGN_C_NAME` | VARCHAR | org | The anatomical region category ID for the follow-up recommendation of a non-mammography study. |
| 81 | `GEN_RECOM_MOD_TYP_C_NAME` | VARCHAR | org | The modality type category ID for the follow-up recommendation of a non-mammography study. |
| 82 | `GEN_RECOM_DUE_IN_C_NAME` | VARCHAR | org | The general recommendation due within category ID due date that defines the recommended time frame for the follow-up recommendation of a non-mammography study. |
| 83 | `GEN_RECOM_NOTE_ID` | VARCHAR |  | The comment entered for a follow-up recommendation for a non-mammography study. |
| 84 | `REC_SRC_FINDING_ID` | NUMERIC |  | The finding record ID associated with a follow-up recommendation placed on a study. |
| 85 | `RSLT_TRK_ACTY_C_NAME` | VARCHAR | org | The acuity level category ID for the finding. |
| 86 | `RSLT_TRK_FINDING_C_NAME` | VARCHAR | org | The acuity notification findings category ID for the critical result. |
| 87 | `RSLT_TRK_BGN_USR_ID` | VARCHAR |  | The user who documented a critical result. |
| 88 | `RSLT_TRK_BGN_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 89 | `RSLT_TRK_BEGIN_DTTM` | DATETIME (UTC) |  | The instant at which a critical result was documented on a study. |
| 90 | `RSLT_TRK_END_USR_ID` | VARCHAR |  | The user who completed the follow-up communication on a critical result. |
| 91 | `RSLT_TRK_END_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 92 | `RSLT_TRK_END_DTTM` | DATETIME (UTC) |  | The instant at which a critical result follow-up communication was completed on a study. |
| 93 | `PATH_LAB_ORDER_ID` | NUMERIC |  | The lab order that the pathology finding is documenting. |
| 94 | `PATH_DOCUMENT_ID` | VARCHAR |  | The scanned document that the pathology finding is linked to. |
| 95 | `PATH_BIOPSY_DATE` | DATETIME |  | The biopsy date for the tissue sample that the pathology finding corresponds to. This column will not include pre-upgrade data until after a specific workflow is done (ORD conversion 248404 has run to completion). If you are unsure whether this has happened yet, you can get the entire set of data if you COALESCE this column with the old column for the pathology biopsy date (ORDER_PROC_2.PATH_RSLT_DATE). |
| 96 | `PATH_NOTE_ID` | VARCHAR |  | The unique ID of the user-entered, free-form text note that stores the comment/narrative text for the pathology finding as rich text format data. This column will not include pre-upgrade data until after a specific workflow is done (ORD conversion 248404 run to completion). If you are unsure whether this has happened yet, you can get the entire set of data if you COALESCE this column with the old column for pathology comment/narrative text (ORDER_PROC_4.PATH_NARR_NOTE_ID). |
| 97 | `RSLT_TRK_FND_COMMNT` | VARCHAR |  | The comment associated with a critical result finding. |
| 98 | `RESULT_NAME` | VARCHAR |  | Stores the result name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

