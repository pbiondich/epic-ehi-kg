# ORDER_RES_2

> The ORDER_RES_2 table contains result finding information for an order. Result findings include mammography pathology results, cardiovascular palette findings, and other result findings.

**Overflow of:** [ORDER_RES](ORDER_RES.md)  
**Primary key:** `FINDING_ID`  
**Columns:** 90  
**Org-specific columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record. |
| 2 | `EXTERNAL_RESULT_YN` | VARCHAR |  | Indicates if the biopsy or surgery for a pathology result was performed outside of the organization. 'Y' indicates it was performed externally. Typically used to exclude these result findings from measures that evaluate the quality of an organization's pathology resulting. |
| 3 | `EXTERNAL_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 4 | `EXTERNAL_LOC_CMT` | VARCHAR |  | The free-text name of the external location that resulted the pathology. Used in cases where the location does not have a location definitions (EAF) record. |
| 5 | `PATH_SPECIMEN_ID` | NUMERIC |  | Links to the specimen that this pathology finding is documenting. |
| 6 | `FIRST_DOCUMENTED_DT` | DATETIME |  | The date on which a mammography lesion was first documented. |
| 7 | `FINDING_INCLUDED_YN` | VARCHAR |  | Indicates whether this finding has been marked as included on an imaging study. Y indicates that the finding is included. N indicates that the finding is not included on the study. A null value indicates data from before the 2014 release and should be considered the same as Y. |
| 8 | `LESION_NAME` | INTEGER |  | A unique identifier for a lesion on a patient to track its changes. |
| 9 | `LESION_ASSESSMENT_C_NAME` | VARCHAR | org | The mammography assessment category ID for the lesion. |
| 10 | `REM_LET_SUPPRESS_YN` | VARCHAR |  | Indicates if an automated process for reminder letters should suppress the creation of a reminder letters for this record. 'Y' indicates that automatic reminder letters should be suppressed for this recommendation. |
| 11 | `REM_LET_SUPP_RSN_C_NAME` | VARCHAR | org | The category ID for the reason why reminder letters were suppressed for a particular recommendation record. For example, letters may be suppressed due to an import of recommendations from a legacy system, or they may be suppressed due to logic in the reminder letter batch. |
| 12 | `PRIMARY_TUMOR_C_NAME` | VARCHAR |  | The primary tumor category ID, as defined in NMD 3.0., for a result. |
| 13 | `REGIONAL_LYMPH_ND_C_NAME` | VARCHAR |  | The regional lymph nodes category ID, as defined in NMD 3.0, for a result. |
| 14 | `DIST_METASTASES_C_NAME` | VARCHAR |  | The distant metastases category ID of a result, as defined for NMD 3.0 |
| 15 | `VESSEL_PROC_TYPE_C_NAME` | VARCHAR |  | The procedure type category ID for a vessel result finding. |
| 16 | `CLOSEST_MRGN_NAME_C_NAME` | VARCHAR | org | The closest margin category ID for a breast legion. |
| 17 | `CLOSEST_MARGIN_DIST` | NUMERIC |  | The closest margin measurement for a breast lesion |
| 18 | `LESION_PRE_ST_GRD_C_NAME` | VARCHAR | org | The pre-stenosis value category ID for the lesion, when the value is saved as a grade. |
| 19 | `LESION_POS_ST_GRD_C_NAME` | VARCHAR |  | The post-stenosis value category ID for the lesion, when the value is saved as a grade. |
| 20 | `LAST_SX_PROG_REC_C_NAME` | VARCHAR | org | The recommendation category ID for the most recent type of this follow-up recommendation, which should be associated with a study for a screening program. |
| 21 | `LST_SX_PG_REC_LOC_C_NAME` | VARCHAR |  | The location of the body category ID for the most recent location associated with this follow-up recommendation. |
| 22 | `SX_PROGRAM_TYPE_C_NAME` | VARCHAR |  | The screening program type category ID associated with this finding. |
| 23 | `PATH_LOCATION_CMT` | VARCHAR |  | Lung cancer location comment for a pathology finding. |
| 24 | `PATH_LOCATION_C_NAME` | VARCHAR |  | The location of the body category ID for a pathology result finding. |
| 25 | `LUNG_STAGE_C_NAME` | VARCHAR |  | The lung cancer staging category ID for a pathology finding. |
| 26 | `LUNG_HISTOLOGY_C_NAME` | VARCHAR |  | The lung cancer histology category ID for a pathology finding. |
| 27 | `LUNG_NON_SMALL_C_NAME` | VARCHAR |  | The lung cancer histology category ID for a non small cell cancer pathology finding. |
| 28 | `LUNG_NON_SMALL_COMM` | VARCHAR |  | Lung cancer histology comment for a non small cell cancer pathology finding. |
| 29 | `LUNG_MALIG_C_NAME` | VARCHAR |  | The lung malignancy type category ID for a pathology finding. |
| 30 | `LUNG_PERIOD_FU_MON` | INTEGER |  | Lung cancer period of follow-up for a pathology finding. |
| 31 | `LUNG_DX_METHOD_C_NAME` | VARCHAR |  | The lung cancer tissue diagnosis method category ID for a pathology finding. |
| 32 | `LUNG_T_STATUS_C_NAME` | VARCHAR |  | The lung cancer histology T status category ID for a pathology finding. |
| 33 | `LUNG_N_STATUS_C_NAME` | VARCHAR |  | The lung cancer histology N status category ID for a pathology finding. |
| 34 | `LUNG_M_STATUS_C_NAME` | VARCHAR |  | The lung cancer histology M status category ID for a pathology finding. |
| 35 | `LUNG_STAGE_METHOD_C_NAME` | VARCHAR |  | The lung cancer staging method category ID for a pathology finding. |
| 36 | `LESION_INCOMP_RSN_C_NAME` | VARCHAR |  | The incomplete reason category ID for the breast imaging finding. Only radiologist findings that have an assessment of incomplete (0) have a value populated for this column. |
| 37 | `SEGMENT_LOCATION_ID` | INTEGER |  | The location of an annotation within the vessel segment if there are multiple annotations in the same segment. |
| 38 | `ORIGIN_GRAFT_ID` | VARCHAR |  | The specific branch and sequence of the current graft that this branch comes off of. |
| 39 | `GRAFT_BRANCH_NUM` | INTEGER |  | The branch identifier of the graft. |
| 40 | `INST_EXAM_UTC_DTTM` | DATETIME (UTC) |  | The instant (in UTC) when the Audiology exam was administered. |
| 41 | `AUDIO_RELIABILITY_C_NAME` | VARCHAR |  | The reliability category ID for the audiogram results. The possible responses are Good, Fair, or Poor. |
| 42 | `PROBE_TONE` | INTEGER |  | The probe tone frequency in Hz. |
| 43 | `RES_LINK_ORDER_ID` | NUMERIC |  | The unique ID of the order with which the result finding is associated. |
| 44 | `FINDING_SUBTYPE_C_NAME` | VARCHAR |  | The finding subtype category ID for the procedural finding. |
| 45 | `OB_US_EDD_ASOF_DATE` | DATETIME |  | The patient's working estimated date of delivery at the time the ultrasound exam started. |
| 46 | `OB_US_EDD_BASIS_C_NAME` | VARCHAR | org | The category ID for the basis for the patient's estimated date of delivery (EDD), at the time when the ultrasound started. |
| 47 | `REPORTING_CAT_C_NAME` | VARCHAR | org | The category ID for the reporting category to use for a finding. |
| 48 | `LESION_FINDING_RSLT_NOTE_ID` | VARCHAR |  | The rich text format result text for this lesion finding. |
| 49 | `ANTERIOR_MARGIN_DIST` | NUMERIC |  | The distance for anterior margin in millimeters (mm). |
| 50 | `POSTERIOR_MARGIN_DIST` | NUMERIC |  | The distance for posterior margin in millimeters (mm). |
| 51 | `SUPERIOR_MARGIN_DIST` | NUMERIC |  | The distance for superior margin in millimeters (mm). |
| 52 | `INFERIOR_MARGIN_DIST` | NUMERIC |  | The distance for inferior margin in millimeters (mm). |
| 53 | `MEDIAL_MARGIN_DIST` | NUMERIC |  | The distance for medial margin in millimeters (mm). |
| 54 | `LATERAL_MARGIN_DIST` | NUMERIC |  | The distance for lateral margin in millimeters (mm). |
| 55 | `REMAINING_MARGINS_GT_DIST` | NUMERIC |  | The greater than distance for the remaining margins (mm). |
| 56 | `LAST_STATUS_CHNG_RSN_C_NAME` | VARCHAR | org | The status change reason category ID for the recommendation. |
| 57 | `RECORD_STATUS_2_C_NAME` | VARCHAR |  | The record status category ID for the result finding. |
| 58 | `RADIOLOGIST_FINDING_ORDER_ID` | NUMERIC |  | The unique ID of the associated order for the radiologist finding. Null means that the finding is not on the latest version of the order and has been replaced by another result finding record. |
| 59 | `LAST_INCLUDED_FINDING_ID` | NUMERIC |  | The unique ID of the last finding documented for a breast lesion that was included in a study. This column represents the finding where a radiologist last documented on the lesion. Null means that the lesion was created but all associated findings were deleted and all associated orders were cancelled. This item will also be null for technologist findings. |
| 60 | `FINDING_TEXT_HAS_EDITS_YN` | VARCHAR |  | Indicates whether the finding text generated automatically (from a SmartForm) has been manually edited by users. 'Y' indicates there have been manual edits. |
| 61 | `MAMMO_NEOADJUVANT_CHEMO_YN` | VARCHAR |  | Indicates whether the patient has had neoadjuvant chemotherapy. 'Y' indicates that neoadjuvant chemotherapy was administered. |
| 62 | `OB_US_CLASS_C_NAME` | VARCHAR | org | The OB ultrasound classification category ID for the order. |
| 63 | `LUNG_DX_COMMENT` | VARCHAR |  | The diagnosis comment for the patient's pathology result. |
| 64 | `LUNG_OTHER_ILD_TYPE_C_NAME` | VARCHAR |  | The interstitial lung disease type category ID for the finding. |
| 65 | `LUNG_LCSR_SPECIFICATION` | VARCHAR |  | The specified details entered by the user for the finding. |
| 66 | `OB_UTZ_USERDEF_GA` | VARCHAR |  | User defined GA for an ultrasound. |
| 67 | `OB_UTZ_EDD_ON_SAVE_DATE` | DATETIME |  | The working estimated date of delivery that was used to calculate the ultrasound study's gestational age. This item is not set if a Fetus GA was selected as the Study GA. |
| 68 | `SIDE_C_NAME` | VARCHAR | discont. | The documented side of the mark. |
| 69 | `MARK_SIZE` | NUMERIC | discont. | The size of the mark. |
| 70 | `MARK1_POSX` | INTEGER | discont. | The X coordinate for mark 1. |
| 71 | `MARK1_POSY` | INTEGER | discont. | The Y coordinate for mark 1. |
| 72 | `MARK2_POSX` | INTEGER | discont. | The X coordinate for mark 2. |
| 73 | `MARK2_POSY` | INTEGER | discont. | The Y coordinate for mark 2. |
| 74 | `DRAW1_COORDS` | VARCHAR | discont. | The coordinates of the drawing in view 1 of the breast image. |
| 75 | `DRAW2_COORDS` | VARCHAR | discont. | The coordinates of the drawing in view 2 of the breast image. |
| 76 | `OLD_LOCATION_C_NAME` | VARCHAR | discont. | The location of a mark. |
| 77 | `OLD_DEPTH` | NUMERIC | discont. | The depth of a mark. |
| 78 | `MARK1_X_POS` | INTEGER | discont. | The X position of the mark in view 1 of the breast image. |
| 79 | `MARK1_Y_POS` | INTEGER | discont. | The Y position of the mark in view 1 of the breast image. |
| 80 | `MARK2_X_POS` | INTEGER | discont. | The X position of the mark in view 2 of the breast image. |
| 81 | `MARK2_Y_POS` | INTEGER | discont. | The Y position of the mark in view 2 of the breast image. |
| 82 | `VIEW1_COORDS` | VARCHAR | discont. | The coordinates of the drawing in view 1 of the breast image. |
| 83 | `VIEW2_COORDS` | VARCHAR | discont. | The coordinates of the drawing in view 2 of the breast image. |
| 84 | `BI_LESION_REVIEW_C_NAME` | VARCHAR |  | This item indicates whether there is currently review needed on this finding, which can be used to drive notifications in Study Review and before-signing warnings. |
| 85 | `RES_NOTE_TAG` | VARCHAR |  | Used to uniquely identify the sentence that corresponds to the findings from a note. |
| 86 | `STDY_LVL_FINDING_IDENT` | VARCHAR |  | This column stores a unique identifier for a breast imaging finding on an individual study. |
| 87 | `MAMMO_PATH_ORDER_ID` | NUMERIC |  | This column stores the order ID that the mammo pathology result is attached to. |
| 88 | `AUTOLINK_START_DATE` | DATETIME |  | Earliest date for general recommendations where auto-linking is allowed. |
| 89 | `AUTOLINK_END_DATE` | DATETIME |  | Latest date for general recommendations where auto-linking is allowed. |
| 90 | `AJCC_VERSION_C_NAME` | VARCHAR |  | The AJCC Version category ID for the pathology result. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

