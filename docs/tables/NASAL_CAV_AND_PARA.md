# NASAL_CAV_AND_PARA

> Stores single response data for College of American Pathologists (CAP) form 76034-NASAL CAVITY AND PARANASAL SINUSES: Incisional Biopsy, Excisional Biopsy, Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 68  
**Org-specific columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `NEOADJUVANT_THRPY_C_NAME` | VARCHAR | org | CAP synoptic form item: Neoadjuvant Therapy. |
| 3 | `NEOADJ_THRPY_TYPE` | VARCHAR |  | CAP synoptic form item: Neoadjuvant Therapy Type. |
| 4 | `OTHER_CLIN_FNDGS` | VARCHAR |  | CAP synoptic form item: Other Clinical Findings. |
| 5 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 6 | `SPEC_RECEIVED_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Received. |
| 7 | `SPEC_RECV_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Other Specimens Received. |
| 8 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 9 | `SPEC_INTEGRITY_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Integrity. |
| 10 | `SIZE_LARGST_POS_LYM` | NUMERIC |  | CAP synoptic form item: Size (greatest dimension, in cm) of the Largest Positive Lymph Node. |
| 11 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 12 | `SPEC_SIZE_GREATEST` | NUMERIC |  | CAP synoptic form item: Specimen Greatest Size. |
| 13 | `SPEC_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Specimen size additional dimension (length). |
| 14 | `SPEC_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Specimen size additional dimension (width). |
| 15 | `SPEC_ADDL_GREATEST` | NUMERIC |  | CAP synoptic form item: Additional specimen greatest size. |
| 16 | `SPEC_ADDL_LENGTH` | NUMERIC |  | CAP synoptic form item: Additional specimen size additional dimension (length). |
| 17 | `SPEC_ADDL_WIDTH` | NUMERIC |  | CAP synoptic form item: Additional specimen size additional dimension (width). |
| 18 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 19 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 20 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 21 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 22 | `MICRO_TMR_EXT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Microscopic Tumor Extension. |
| 23 | `MRG_CANNOT_ASSES_YN` | VARCHAR |  | CAP synoptic form item: Margins Cannot Be Assessed. |
| 24 | `MARGIN_UNITS_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Units. |
| 25 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 26 | `TREAT_EFF_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify treatment effect. |
| 27 | `TUMOR_DESC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor description. |
| 28 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 29 | `LYM_ND_EXNDL_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Lymph Nodes, Extranodal Extension. |
| 30 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 31 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 32 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 33 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 34 | `SRC_PATH_METAS_SPEC` | VARCHAR |  | CAP synoptic form item: Source of Pathologic Metastatic Specimen Specify. |
| 35 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 36 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastasis Sites. |
| 37 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 38 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 39 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 40 | `MRG_INV_CARCINOMA_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Invasive Carcinoma. |
| 41 | `MARGIN_UNITS_2_C_NAME` | VARCHAR |  | CAP synoptic form item: Margin Units (second measurement). |
| 42 | `NECK_DISSECTN_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Neck (Lymph Node) Dissection. |
| 43 | `MUCOEPIDRMD_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Mucoepidermoid carcinoma. |
| 44 | `PATHOLOGIC_STAGE_C_NAME` | VARCHAR | org | CAP synoptic form item: Pathologic Staging. |
| 45 | `INFLAMMATION_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Inflammation. |
| 46 | `MINOR_SALV_GLD_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Carcinomas of Minor Salivary Glands. |
| 47 | `NON_SALV_ADENOC_C_NAME` | VARCHAR |  | CAP synoptic form item: Non-Salivary Gland Adenocarcinoma, not otherwise specified (NOS). |
| 48 | `NEUROEND_CARC_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Neuroendocrine Carcinoma. |
| 49 | `SQM_CELL_CARC_CON_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Type Squamous Cell Carcinoma, Conventional. |
| 50 | `ADENOC_INTEST_TYP_C_NAME` | VARCHAR | org | CAP synoptic form item: Adenocarcinoma Intestinal Type. |
| 51 | `ADENOC_NON_INTEST_C_NAME` | VARCHAR |  | CAP synoptic form item: Adenocarcinoma Non-Intestinal Type. |
| 52 | `PT_MAXILLRY_SINUS_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT): Maxillary Sinus. |
| 53 | `PT_NASAL_CAVITY_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT): Nasal Cavity and Ethmoid Sinus. |
| 54 | `NUM_POS_LYMPH_NDS` | NUMERIC |  | CAP synoptic form item: Number of Positive Lymph Nodes. |
| 55 | `SZ_ASSOC_METAS_FCS` | NUMERIC |  | CAP synoptic form item: Size of the Associated Metastatic Focus. |
| 56 | `POSITION_INVOLVD_NO` | VARCHAR |  | CAP synoptic form item: Position of the Involved Node (level). |
| 57 | `EPITH_DYSPLAS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Epithelial dysplasia. |
| 58 | `MARGIN_IN_SITU_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin In Situ. |
| 59 | `TMR_FOC_MUL_SPFY` | VARCHAR |  | CAP synoptic form item: Tumor Focality - Specify Multifocal. |
| 60 | `MACRO_EXTENT_OF_TUM` | VARCHAR |  | CAP synoptic form item: Macroscopic Extent of Tumor (Extent of Invasion). |
| 61 | `MARGIN_INV_SPECIFY` | VARCHAR |  | CAP synoptic form item: Margins Invasive Specify Margins Per Orientation. |
| 62 | `MARG_INV_DIST_CLOSE` | NUMERIC |  | CAP synoptic form item: Margins Invasive Distance of Invasive Carcinoma from Closest Margin. |
| 63 | `MARGIN_SITU_CLOSE` | NUMERIC |  | CAP synoptic form item: Margins in Situ Distance of Carcinoma in Situ from Closest. |
| 64 | `MARGIN_IN_SITU_SPFY` | VARCHAR |  | CAP synoptic form item: Margins In Situ Specify Margins Per Orientation. |
| 65 | `PT_FOR_MUC_MAL_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor for Mucosal Malignant Melanoma. |
| 66 | `SPECIAL_STUDY_TYPES` | VARCHAR |  | CAP synoptic form item: Special Studies - Specify Types. |
| 67 | `SPECIAL_STUDY_RESUL` | VARCHAR |  | CAP synoptic form item: Special Studies - Specify Results. |
| 68 | `REG_LYM_MUCOS_MEL_C_NAME` | VARCHAR |  | CAP synoptic form item: Regional Lymph Nodes (pN) for Mucosal Malignant Melanoma. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

