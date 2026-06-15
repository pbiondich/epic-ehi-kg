# LARYNX_BIOPSY

> Stores single response data for College of American Pathologists (CAP) form 76028-LARYNX: INCISIONAL BIOPSY, EXCISIONAL BIOPSY, RESECTION.

**Primary key:** `RESULT_1_ID`  
**Columns:** 68  
**Org-specific columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_1_ID` | VARCHAR | PK | The unique identifier for the result record. |
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
| 22 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 23 | `MICRO_TMR_EXT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Microscopic Tumor Extension. |
| 24 | `MRG_CANNOT_ASSES_YN` | VARCHAR |  | CAP synoptic form item: Margins Cannot Be Assessed. |
| 25 | `DIST_FROM_MARGIN` | NUMERIC |  | CAP synoptic form item: Distance From Closest Margin. |
| 26 | `MARGIN_UNITS_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Units. |
| 27 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 28 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 29 | `TREAT_EFF_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify treatment effect. |
| 30 | `TUMOR_DESC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor description. |
| 31 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 32 | `ANC_STDIES_SPFY_TYP` | VARCHAR |  | CAP synoptic form item: Ancillary Studies Specify Types. |
| 33 | `ANC_STDIES_SPFY_RSL` | VARCHAR |  | CAP synoptic form item: Ancillary Studies Specify Results. |
| 34 | `LYM_ND_EXNDL_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Lymph Nodes, Extranodal Extension. |
| 35 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 36 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 37 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 38 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 39 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 40 | `PT_SUPRAGLOTTIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT): Supraglottis. |
| 41 | `PT_GLOTTIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT): Glottis. |
| 42 | `PT_SUBGLOTTIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT): Subglottis. |
| 43 | `SRC_PATH_METAS_SPEC` | VARCHAR |  | CAP synoptic form item: Source of Pathologic Metastatic Specimen Specify. |
| 44 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 45 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastasis Sites. |
| 46 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 47 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 48 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 49 | `TMR_FOC_MULTIP_SPFY` | VARCHAR |  | CAP synoptic form item: Specify tumor focality: multiple. |
| 50 | `LARYNGECTOMY_C_NAME` | VARCHAR | org | CAP synoptic form item: Laryngectomy. |
| 51 | `MRG_INV_CARCINOMA_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Invasive Carcinoma. |
| 52 | `INV_CARC_CLOSE_MRG` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Distance from Closest Margin. |
| 53 | `INV_CARCINOMA_SPFY` | VARCHAR |  | CAP synoptic form item: Invasive Carcinoma Specify. |
| 54 | `MARGIN_UNITS_2_C_NAME` | VARCHAR |  | CAP synoptic form item: Margin Units (second measurement). |
| 55 | `MACRO_EXTENT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Macroscopic Extent. |
| 56 | `VERTICAL_HEMILARYNG` | VARCHAR |  | CAP synoptic form item: Specify Vertical hemilaryngectomy Side. |
| 57 | `PARTIAL_LARYNGECTOM` | VARCHAR |  | CAP synoptic form item: Specify Partial laryngectomy Type. |
| 58 | `NECK_DISSECTN_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Neck (Lymph Node) Dissection. |
| 59 | `TMR_TRANSGLOTTIC_YN` | VARCHAR |  | CAP synoptic form item: Tumor Laterality Transglottic. |
| 60 | `MUCOEPIDRMD_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Mucoepidermoid carcinoma. |
| 61 | `HIST_TYPE_OTHR_CARC` | VARCHAR |  | CAP synoptic form item: Histologic Type - Specify Other Carcinoma. |
| 62 | `PATHOLOGIC_STAGE_C_NAME` | VARCHAR | org | CAP synoptic form item: Pathologic Staging. |
| 63 | `KERAT_DYSPLS_C_NAME` | VARCHAR | org | CAP synoptic form item: Keratinizing dysplasia. |
| 64 | `NON_KERAT_DYSPLS_C_NAME` | VARCHAR |  | CAP synoptic form item: Non-keratinizing dysplasia. |
| 65 | `INFLAMMATION_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Inflammation. |
| 66 | `MARGIN_IN_SITU_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin In Situ. |
| 67 | `PT_FOR_MUC_MAL_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor for Mucosal Malignant Melanoma. |
| 68 | `REG_LYM_MUCOS_MEL_C_NAME` | VARCHAR |  | CAP synoptic form item: Regional Lymph Nodes (pN) for Mucosal Malignant Melanoma. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

