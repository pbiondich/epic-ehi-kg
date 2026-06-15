# LIP_AND_ORAL_CAVTY

> Stores single response data for College of American Pathologists (CAP) form 76029-LIP AND ORAL CAVITY: INCISIONAL BIOPSY, EXCISIONAL BIOPSY, RESECTION.

**Primary key:** `RESULT_ID`  
**Columns:** 67  
**Org-specific columns:** 19

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
| 17 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 18 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 19 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 20 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 21 | `MICRO_TMR_EXT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Microscopic Tumor Extension. |
| 22 | `MRG_CANNOT_ASSES_YN` | VARCHAR |  | CAP synoptic form item: Margins Cannot Be Assessed. |
| 23 | `MARGIN_UNITS_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Units. |
| 24 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 25 | `TREAT_EFF_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify treatment effect. |
| 26 | `TUMOR_DESC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor description. |
| 27 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 28 | `LYM_ND_EXNDL_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Lymph Nodes, Extranodal Extension. |
| 29 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 30 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 31 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 32 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 33 | `SRC_PATH_METAS_SPEC` | VARCHAR |  | CAP synoptic form item: Source of Pathologic Metastatic Specimen Specify. |
| 34 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 35 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastasis Sites. |
| 36 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 37 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 38 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 39 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 40 | `MRG_INV_CARCINOMA_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Invasive Carcinoma. |
| 41 | `MARGIN_UNITS_2_C_NAME` | VARCHAR |  | CAP synoptic form item: Margin Units (second measurement). |
| 42 | `MACRO_EXTENT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Macroscopic Extent. |
| 43 | `NECK_DISSECTN_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Neck (Lymph Node) Dissection. |
| 44 | `MUCOEPIDRMD_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Mucoepidermoid carcinoma. |
| 45 | `PATHOLOGIC_STAGE_C_NAME` | VARCHAR | org | CAP synoptic form item: Pathologic Staging. |
| 46 | `KERAT_DYSPLS_C_NAME` | VARCHAR | org | CAP synoptic form item: Keratinizing dysplasia. |
| 47 | `NON_KERAT_DYSPLS_C_NAME` | VARCHAR |  | CAP synoptic form item: Non-keratinizing dysplasia. |
| 48 | `PROC_GLOSSECTOMY` | VARCHAR |  | CAP synoptic form item: Procedure - Specify Glossectomy. |
| 49 | `PROC_MANDIBULECTOMY` | VARCHAR |  | CAP synoptic form item: Procedure - Specify Mandibulectomy. |
| 50 | `PROC_MAXILLECTOMY` | VARCHAR |  | CAP synoptic form item: Procedure - Specify Maxillectomy. |
| 51 | `CARC_EX_PLEOM_C_NAME` | VARCHAR | org | CAP synoptic form item: Carcinoma ex pleomorphic adenoma (malignant mixed tumor). |
| 52 | `EX_PLEOM_INVASIVE_C_NAME` | VARCHAR | org | CAP synoptic form item: Carcinoma ex pleomorphic adenoma Invasive. |
| 53 | `MINOR_SALV_GLD_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Carcinomas of Minor Salivary Glands. |
| 54 | `NON_SALV_ADENOC_C_NAME` | VARCHAR |  | CAP synoptic form item: Non-Salivary Gland Adenocarcinoma, not otherwise specified (NOS). |
| 55 | `NON_SALIV_GLD_SPFY` | VARCHAR |  | CAP synoptic form item: Non-Salivary Gland - Specify Adenocarcinoma. |
| 56 | `NEUROEND_CARC_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Neuroendocrine Carcinoma. |
| 57 | `PT1_OR_PT2_TUMOR_YN` | VARCHAR |  | CAP synoptic form item: Tumor Thickness For pT1 or pT2 Tumors. |
| 58 | `TMR_THICK_MEASURE` | NUMERIC |  | CAP synoptic form item: Tumor Thickness Measurement. |
| 59 | `TMR_THICK_DESC_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor Thickness Description. |
| 60 | `MARGIN_IN_SITU_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin In Situ. |
| 61 | `PATH_INFLAM_SPFY` | VARCHAR |  | CAP synoptic form item: Additional Pathological Findings - Specify Inflammation. |
| 62 | `TMR_FOC_MUL_SPFY` | VARCHAR |  | CAP synoptic form item: Tumor Focality - Specify Multifocal. |
| 63 | `HIST_TYPE_ADE_NOS_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Type Adenocarcinomas, Not Otherwise Specified. |
| 64 | `SPECIAL_STUDY_RESUL` | VARCHAR |  | CAP synoptic form item: Special Studies - Specify Results. |
| 65 | `MARGIN_INV_SPECIFY` | VARCHAR |  | CAP synoptic form item: Margins Invasive Specify Margins Per Orientation. |
| 66 | `MARG_INV_DIST_CLOSE` | NUMERIC |  | CAP synoptic form item: Margins Invasive Distance of Invasive Carcinoma from Closest Margin. |
| 67 | `PT_CARC_EX_MALIG_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor for All Carcinomas Excluding Mucosal Malignant Melanoma. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

