# INVAS_CARC_BREAST

> Stores data for College of American Pathologists (CAP) form 76012-INVASIVE CARCINOMA OF THE BREAST: Complete Excision (Less Than Total Mastectomy, Including Specimens Designated Biopsy, Lumpectomy, Quadrantectomy, and Partial Mastectomy With or Without Axillary Contents) and Mastectomy (Total, Modified Radical, Radical With or Without Axillary Contents).

**Primary key:** `RESULT_ID`  
**Columns:** 96  
**Org-specific columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 3 | `CLOCK_POSITION_C_NAME` | VARCHAR | org | CAP synoptic form item: Specify Clock Position of Tumor Site. |
| 4 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 5 | `SPEC_INTEGRITY_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Integrity. |
| 6 | `SPEC_INTEGRITY_SPFY` | VARCHAR |  | CAP synoptic form item: Specify specimen integrity. |
| 7 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 8 | `SPEC_SIZE_GREATEST` | NUMERIC |  | CAP synoptic form item: Specimen Greatest Size. |
| 9 | `SPEC_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Specimen size additional dimension (length). |
| 10 | `SPEC_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Specimen size additional dimension (width). |
| 11 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 12 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 13 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 14 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 15 | `DERML_LYM_VAS_INV_C_NAME` | VARCHAR | org | CAP synoptic form item: Dermal Lymph-Vascular Invasion. |
| 16 | `RADIOLOG_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Radiologic Findings. |
| 17 | `HST_BRST_CANCR_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Prior History of Breast Cancer. |
| 18 | `PRESRG_INV_CNM_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Prior Presurgical (neoadjuvant) Therapy for this Diagnosis of Invasive Carcinoma. |
| 19 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 20 | `LYMPH_ND_SAMPL_SPFY` | VARCHAR |  | CAP synoptic form item: Specify lymph node sampling. |
| 21 | `DCIS_IS_PRESENT_C_NAME` | VARCHAR | org | CAP synoptic form item: Ductal Carcinoma In Situ (DCIS) Is Present. |
| 22 | `LOBUL_CARC_IN_SIT_C_NAME` | VARCHAR | org | CAP synoptic form item: Lobular Carcinoma In Situ (LCIS). |
| 23 | `HIST_INV_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Type of Invasive Carcinoma. |
| 24 | `HIST_INV_CARC_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Histologic Type of Invasive Carcinoma. |
| 25 | `SIZE_DCIS_GREAT_DIM` | NUMERIC |  | CAP synoptic form item: Estimated Size of Ductal Carcinoma In Situ (DCIS) Greatest Dimension. |
| 26 | `DCIS_ADDL_DIMENSION` | NUMERIC |  | CAP synoptic form item: Ductal Carcinoma In Situ (DCIS) Additional Dimension Length. |
| 27 | `DCIS_ADDL_DIM_2` | NUMERIC |  | CAP synoptic form item: Ductal Carcinoma In Situ (DCIS) Additional Dimension Width. |
| 28 | `NUM_BLOCK_EXAM_DCIS` | NUMERIC |  | CAP synoptic form item: Number of Blocks Examined for Ductal Carcinoma In Situ (DCIS). |
| 29 | `NUM_BLOCKS_DCIS` | NUMERIC |  | CAP synoptic form item: Number of Blocks With Ductal Carcinoma In Situ (DCIS). |
| 30 | `ARCHITECT_PAT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Architectural Patterns. |
| 31 | `NUCLEAR_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Nuclear Grade. |
| 32 | `NECROSIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Necrosis. |
| 33 | `GLANDUL_TUBL_DIFF_C_NAME` | VARCHAR | org | CAP synoptic form item: Glandular (Acinar) / Tubular Differentiation. |
| 34 | `NUCLEAR_PLEOMRPHS_C_NAME` | VARCHAR | org | CAP synoptic form item: Nuclear Pleomorphism. |
| 35 | `MITOTIC_COUNT_C_NAME` | VARCHAR | org | CAP synoptic form item: Mitotic Count. |
| 36 | `NUM_MITOSE_10_H_PWR` | NUMERIC |  | CAP synoptic form item: Number of Mitoses per 10 High-Power Fields. |
| 37 | `DIAMETR_MICRSCP_FLD` | NUMERIC |  | CAP synoptic form item: Diameter of Microscope Field. |
| 38 | `HIST_OVERALL_GRD_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade - Overall Grade. |
| 39 | `TMR_DUCT_CARC_SIT_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor Ductal Carcinoma In Situ (DCIS). |
| 40 | `TMR_NO_RESID_CAR_YN` | VARCHAR |  | CAP synoptic form item: Tumor No Residual Invasive Carcinoma After Presurgical (Neoadjuvant) Therapy for the Presence of Invasive Carcinoma section. |
| 41 | `MICROINVASN_ONLY_YN` | VARCHAR |  | CAP synoptic form item: Microinvasion Only. |
| 42 | `TMR_FOC_NUM_FOCI` | NUMERIC |  | CAP synoptic form item: Tumor Focality Number of Foci. |
| 43 | `TMR_FOC_SZ_IND_FOCI` | VARCHAR |  | CAP synoptic form item: Tumor Focality Size of Individual Foci. |
| 44 | `EXTENT_TMR_NIPPLE_C_NAME` | VARCHAR | org | CAP synoptic form item: Extent of Tumor - Nipple. |
| 45 | `EXT_TMR_SKEL_MUSC_C_NAME` | VARCHAR | org | CAP synoptic form item: Extent of Tumor - Skeletal Muscle. |
| 46 | `MRG_INV_CARCINOMA_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Invasive Carcinoma. |
| 47 | `MARGIN_DCIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Ductal Carcinoma In Situ (DCIS). |
| 48 | `INV_CARC_CLOSE_MRG` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Distance from Closest Margin. |
| 49 | `INV_CARC_SUPER_MRG` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Distance to Superior Margin. |
| 50 | `INV_CARC_INFER_MRG` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Distance to Inferior Margin. |
| 51 | `INV_CARC_ANTER_MRG` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Distance to Anterior Margin. |
| 52 | `INV_CARC_POSTR_MRG` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Distance to Posterior Margin. |
| 53 | `INV_CARC_MEDIAL_MRG` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Distance to Medial Margin. |
| 54 | `INV_CARC_LATER_MRG` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Distance to Lateral Margin. |
| 55 | `INV_CARC_OTHER_MRG` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Distance from Other Specified Margin. |
| 56 | `INV_CARC_DESIGNAT` | VARCHAR |  | CAP synoptic form item: Invasive Carcinoma Designation of Other Margin. |
| 57 | `INV_SUPER_MRG_EXT_C_NAME` | VARCHAR | org | CAP synoptic form item: Invasive Carcinoma Superior Margin Extent. |
| 58 | `INV_INFER_MRG_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Invasive Carcinoma Inferior Margin Extent. |
| 59 | `INV_ANTER_MRG_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Invasive Carcinoma Anterior Margin Extent. |
| 60 | `INV_POSTR_MRG_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Invasive Carcinoma Posterior Margin Extent. |
| 61 | `INV_MEDL_MRG_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Invasive Carcinoma Medial Margin Extent. |
| 62 | `INV_LATER_MRG_EX_C_NAME` | VARCHAR |  | CAP synoptic form item: Invasive Carcinoma Lateral Margin Extent. |
| 63 | `DCIS_CLOSEST_MARGIN` | NUMERIC |  | CAP synoptic form item: Ductal Carcinoma In Situ (DCIS) Distance from Closest Margin. |
| 64 | `DCIS_SUPERIOR_MRG` | NUMERIC |  | CAP synoptic form item: Ductal Carcinoma In Situ (DCIS) Distance to Superior Margin. |
| 65 | `DCIS_INFERIOR_MRG` | NUMERIC |  | CAP synoptic form item: Ductal Carcinoma In Situ (DCIS) Distance to Inferior Margin. |
| 66 | `DCIS_ANTERIOR_MRG` | NUMERIC |  | CAP synoptic form item: Ductal Carcinoma In Situ (DCIS) Distance to Anterior Margin. |
| 67 | `DCIS_POSTERIOR_MRG` | NUMERIC |  | CAP synoptic form item: Ductal Carcinoma In Situ (DCIS) Distance to Posterior margin. |
| 68 | `DCIS_MEDIAL_MARGIN` | NUMERIC |  | CAP synoptic form item: Ductal Carcinoma In Situ (DCIS) Distance to Medial Margin. |
| 69 | `DCIS_LATERAL_MARGIN` | NUMERIC |  | CAP synoptic form item: Ductal Carcinoma In Situ (DCIS) Distance to Lateral Margin. |
| 70 | `DCIS_OTHER_MARGIN` | NUMERIC |  | CAP synoptic form item: Ductal Carcinoma In Situ (DCIS) Distance from Other Specified margin. |
| 71 | `DCIS_DESIGNAT_MRG` | VARCHAR |  | CAP synoptic form item: Ductal Carcinoma In Situ (DCIS) Designation of Margin. |
| 72 | `DCIS_SUPERIOR_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Ductal Carcinoma In Situ (DCIS) Superior Margin Extent. |
| 73 | `DCIS_INFERIOR_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Ductal Carcinoma In Situ (DCIS) Inferior Margin Extent. |
| 74 | `DCIS_ANTERIOR_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Ductal Carcinoma In Situ (DCIS) Anterior Margin Extent. |
| 75 | `DCIS_POSTERR_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Ductal Carcinoma In Situ (DCIS) Posterior Margin Extent. |
| 76 | `DCIS_MEDIAL_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Ductal Carcinoma In Situ (DCIS) Medial Margin Extent. |
| 77 | `DCIS_LATER_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Ductal Carcinoma In Situ (DCIS) Lateral Margin Extent. |
| 78 | `TREAT_EFF_BREAST_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect - Neoadjuvant Therapy In The Breast. |
| 79 | `TREAT_EFF_LYMPH_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect Neoadjuvant Therapy In The Lymph Nodes. |
| 80 | `LYM_ND_NOT_PRES_YN` | VARCHAR |  | CAP synoptic form item: Lymph Nodes Present in Specimen. |
| 81 | `TOT_NUM_LYM_ND_EXAM` | NUMERIC |  | CAP synoptic form item: Total Number of Lymph Nodes Examined (Sentinel and Nonsentinel). |
| 82 | `NUM_LYM_ND_ISO_TMR` | NUMERIC |  | CAP synoptic form item: Number of Lymph Nodes with Isolated Tumor Cells. |
| 83 | `MIC_MC_METAS_PRE_YN` | VARCHAR |  | CAP synoptic form item: Micro/Macro Metastases Present. |
| 84 | `NUM_LYM_ND_MACROMET` | NUMERIC |  | CAP synoptic form item: Number of Lymph Nodes with Macrometastases. |
| 85 | `NUM_LYM_ND_MICROMET` | NUMERIC |  | CAP synoptic form item: Number of Lymph Nodes with Micrometastases. |
| 86 | `SZ_LRGST_METAS_DEP` | NUMERIC |  | CAP synoptic form item: Size of Largest Metastatic Deposit. |
| 87 | `LYMPH_NODES_UNITS_C_NAME` | VARCHAR | org | CAP synoptic form item: Lymph Nodes - Specify Units. |
| 88 | `SENT_BIOP_NT_PER_YN` | VARCHAR |  | CAP synoptic form item: Sentinel Lymph Node - Biopsy Not Performed. |
| 89 | `LYM_ND_EXNDL_EXT_C_NAME` | VARCHAR | org | CAP synoptic form item: Lymph Nodes, Extranodal Extension. |
| 90 | `NUM_SENT_LYM_EXAM` | NUMERIC |  | CAP synoptic form item: Number of Sentinel Lymph Nodes Examined. |
| 91 | `EVAL_SENT_ND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Method of Evaluation of Sentinel Lymph Nodes. |
| 92 | `ESTRGN_RECEPTOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Estrogen Receptor. |
| 93 | `ESTRGN_RECP_PERF_C_NAME` | VARCHAR | org | CAP synoptic form item: Estrogen Receptor Performed. |
| 94 | `ESTROGEN_RECP_SPEC` | VARCHAR |  | CAP synoptic form item: Estrogen Receptor - Specify Performed Specimen. |
| 95 | `ESTRGN_RECP_PERCN_C_NAME` | VARCHAR | org | CAP synoptic form item: Estrogen Receptor Results (percentage of cells). |
| 96 | `ESTRGN_RECP_AVG_C_NAME` | VARCHAR | org | CAP synoptic form item: Estrogen Receptor Results (average intensity of tumor cell nuclei staining). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

