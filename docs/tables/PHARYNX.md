# PHARYNX

> Stores data for College of American Pathologists (CAP) form 76041-PHARYNX (OROPHARYNX, HYPOPHARYNX, NASOPHARYNX): Incisional Biopsy, Excisional Biopsy, Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 72  
**Org-specific columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `NEOADJUVANT_THRPY_C_NAME` | VARCHAR | org | CAP synoptic form item: Neoadjuvant Therapy. |
| 3 | `NEOADJ_THRPY_TYPE` | VARCHAR |  | CAP synoptic form item: Neoadjuvant Therapy Type. |
| 4 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 5 | `SPEC_RECEIVED_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Received. |
| 6 | `SPEC_RECV_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Other Specimens Received. |
| 7 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 8 | `SPEC_INTEGRITY_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Integrity. |
| 9 | `SIZE_LARGST_POS_LYM` | NUMERIC |  | CAP synoptic form item: Size (greatest dimension, in cm) of the Largest Positive Lymph Node. |
| 10 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 11 | `SPEC_SIZE_GREATEST` | NUMERIC |  | CAP synoptic form item: Specimen Greatest Size. |
| 12 | `SPEC_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Specimen size additional dimension (length). |
| 13 | `SPEC_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Specimen size additional dimension (width). |
| 14 | `SPEC_ADDL_GREATEST` | NUMERIC |  | CAP synoptic form item: Additional specimen greatest size. |
| 15 | `SPEC_ADDL_LENGTH` | NUMERIC |  | CAP synoptic form item: Additional specimen size additional dimension (length). |
| 16 | `SPEC_ADDL_WIDTH` | NUMERIC |  | CAP synoptic form item: Additional specimen size additional dimension (width). |
| 17 | `MICRO_TMR_EXT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Microscopic Tumor Extension. |
| 18 | `MRG_CANNOT_ASSES_YN` | VARCHAR |  | CAP synoptic form item: Margins Cannot Be Assessed. |
| 19 | `MARGIN_UNITS_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Units. |
| 20 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 21 | `TREAT_EFF_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify treatment effect. |
| 22 | `TUMOR_DESC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor description. |
| 23 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 24 | `LYM_ND_EXNDL_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Lymph Nodes, Extranodal Extension. |
| 25 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 26 | `REG_LN_NUM_EXM` | INTEGER |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 27 | `REG_LN_NUM_INV` | INTEGER |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 28 | `SRC_PATH_METAS_SPEC` | VARCHAR |  | CAP synoptic form item: Source of Pathologic Metastatic Specimen Specify. |
| 29 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 30 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastatis Sites. |
| 31 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 32 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 33 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 34 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 35 | `MRG_INV_CARCINOMA_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Invasive Carcinoma. |
| 36 | `MARGIN_UNITS_2_C_NAME` | VARCHAR |  | CAP synoptic form item: Margin Units (second measurement). |
| 37 | `MACRO_EXTENT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Macroscopic Extent. |
| 38 | `NECK_DISSECTN_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Neck (Lymph Node) Dissection. |
| 39 | `MUCOEPIDRMD_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Mucoepidermoid carcinoma. |
| 40 | `PATHOLOGIC_STAGE_C_NAME` | VARCHAR | org | CAP synoptic form item: Pathologic Staging. |
| 41 | `KERAT_DYSPLS_C_NAME` | VARCHAR | org | CAP synoptic form item: Keratinizing dysplasia. |
| 42 | `NON_KERAT_DYSPLS_C_NAME` | VARCHAR |  | CAP synoptic form item: Non-keratinizing dysplasia. |
| 43 | `MINOR_SALV_GLD_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Carcinomas of Minor Salivary Glands. |
| 44 | `NON_SALV_ADENOC_C_NAME` | VARCHAR |  | CAP synoptic form item: Non-Salivary Gland Adenocarcinoma, not otherwise specified (NOS). |
| 45 | `NON_SALIV_GLD_SPFY` | VARCHAR |  | CAP synoptic form item: Non-Salivary Gland - Specify Adenocarcinoma. |
| 46 | `NEUROEND_CARC_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Neuroendocrine Carcinoma. |
| 47 | `MARGIN_IN_SITU_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin In Situ. |
| 48 | `HUMAN_PAPILLOMAVI_C_NAME` | VARCHAR | org | CAP synoptic form item: Human Papillomavirus Associated Carcinoma. |
| 49 | `EPSTEIN_BAR_VIRU_C_NAME` | VARCHAR | org | CAP synoptic form item: Epstein-Barr virus. |
| 50 | `PATH_INFLAM_SPFY` | VARCHAR |  | CAP synoptic form item: Additional Pathological Findings - Specify Inflammation. |
| 51 | `TMR_FOC_MUL_SPFY` | VARCHAR |  | CAP synoptic form item: Tumor Focality - Specify Multifocal. |
| 52 | `HIST_TYPE_ADE_NOS_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Type Adenocarcinomas, Not Otherwise Specified. |
| 53 | `MARGIN_INV_SPECIFY` | VARCHAR |  | CAP synoptic form item: Margins Invasive Specify Margins Per Orientation. |
| 54 | `MARGIN_IN_SITU_SPFY` | VARCHAR |  | CAP synoptic form item: Margins In Situ Specify Margins Per Orientation. |
| 55 | `MARG_INV_DIST_CLOSE` | NUMERIC |  | CAP synoptic form item: Margins Invasive Distance of Invasive Carcinoma from Closest Margin. |
| 56 | `PT_FOR_MUC_MAL_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor for Mucosal Malignant Melanoma. |
| 57 | `ANCLR_STD_SPEC` | VARCHAR |  | CAP synoptic form item: Specify details for ancillary studies. |
| 58 | `PATH_STAGE_PT_PN_C_NAME` | VARCHAR | org | CAP synoptic form item: Pathologic staging pT and pN. |
| 59 | `HIS_TYP_NONKERATE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Type - Carcinomas of the Nasopharynx - Nonkeratinizing carcinoma. |
| 60 | `MARGIN_SITU_CLOSE` | NUMERIC |  | CAP synoptic form item: Margins in Situ Distance of Carcinoma in Situ from Closest. |
| 61 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 62 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 63 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 64 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 65 | `SPEC_PROC_RESECT_SP` | VARCHAR |  | CAP synoptic form item: Specify Specimen Procedure Resection. |
| 66 | `PT_OROPHARYNX_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT): Oropharynx. |
| 67 | `PT_NASOPHARYNX_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT): Nasopharynx. |
| 68 | `PT_HYPOPHARYNX_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT): Hypopharynx. |
| 69 | `PN_OROPHARYNX_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN): Oropharynx. |
| 70 | `PN_NASOPHARYNX_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN): Nasopharynx. |
| 71 | `PN_HYPOPHARYNX_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN): Hypopharynx. |
| 72 | `REG_LYM_MUCOS_MEL_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN) for Mucosal Malignant Melanoma. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

