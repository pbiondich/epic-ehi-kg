# MAJOR_SALIV_GLANDS

> Stores single response data for College of American Pathologists (CAP) form 76031-Major Salivary Glands: Incisional biopsy, Excisional Biopsy, Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 53  
**Org-specific columns:** 18

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
| 22 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 23 | `MICRO_TMR_EXT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Microscopic Tumor Extension. |
| 24 | `DIST_FROM_MARGIN` | NUMERIC |  | CAP synoptic form item: Distance From Closest Margin. |
| 25 | `MARGIN_UNITS_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Units. |
| 26 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 27 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 28 | `TREAT_EFF_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify treatment effect. |
| 29 | `TUMOR_DESC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor description. |
| 30 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 31 | `ANC_STDIES_SPFY_TYP` | VARCHAR |  | CAP synoptic form item: Ancillary Studies Specify Types. |
| 32 | `ANC_STDIES_SPFY_RSL` | VARCHAR |  | CAP synoptic form item: Ancillary Studies Specify Results. |
| 33 | `LYM_ND_EXNDL_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Lymph Nodes, Extranodal Extension. |
| 34 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 35 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 36 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 37 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 38 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 39 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 40 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 41 | `NECK_DISSECTN_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Neck (Lymph Node) Dissection. |
| 42 | `MUCOEPIDRMD_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Mucoepidermoid carcinoma. |
| 43 | `CARC_EX_PLEOM_C_NAME` | VARCHAR | org | CAP synoptic form item: Carcinoma ex pleomorphic adenoma (malignant mixed tumor). |
| 44 | `EX_PLEOM_INVASIVE_C_NAME` | VARCHAR | org | CAP synoptic form item: Carcinoma ex pleomorphic adenoma Invasive. |
| 45 | `SPEC_PAROTID_GLND_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Parotid Gland. |
| 46 | `PROC_RESECT_PAROT_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Procedure Resection, Parotid Gland. |
| 47 | `TMR_ST_PAROT_GLND_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor Site Parotid Gland. |
| 48 | `HIST_SEB_ADENOC_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Type Sebaceous adenocarcinoma. |
| 49 | `TMR_FOC_MUL_SPFY` | VARCHAR |  | CAP synoptic form item: Tumor Focality - Specify Multifocal. |
| 50 | `HIST_TYPE_ADE_NOS_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Type Adenocarcinomas, Not Otherwise Specified. |
| 51 | `MACRO_EXTENT_OF_TUM` | VARCHAR |  | CAP synoptic form item: Macroscopic Extent of Tumor (Extent of Invasion). |
| 52 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastasis Sites. |
| 53 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

