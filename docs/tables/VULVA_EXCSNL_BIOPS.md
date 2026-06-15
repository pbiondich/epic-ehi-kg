# VULVA_EXCSNL_BIOPS

> Stores single response data for College of American Pathologists (CAP) form 76067-VULVA: Excisional Biopsy.

**Primary key:** `RESULT_ID`  
**Columns:** 47  
**Org-specific columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 3 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 4 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 5 | `SPEC_SIZE_GREATEST` | NUMERIC |  | CAP synoptic form item: Specimen Greatest Size. |
| 6 | `SPEC_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Specimen size additional dimension (length). |
| 7 | `SPEC_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Specimen size additional dimension (width). |
| 8 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 9 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 10 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 11 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 12 | `MICRO_TMR_EXT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Microscopic Tumor Extension. |
| 13 | `LYM_ND_EXNDL_EXT_C_NAME` | VARCHAR | org | CAP synoptic form item: Lymph Nodes, Extranodal Extension. |
| 14 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 15 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 16 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 17 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 18 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastatis Sites. |
| 19 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 20 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 21 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 22 | `TUMOR_FOCAL_SPECIFY` | VARCHAR |  | CAP synoptic form item: Tumor Focality Other Specify. |
| 23 | `HIST_TYP_NONCL_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other or nonclassifiable histologic type. |
| 24 | `LYMPH_ND_SAMPL_SPFY` | VARCHAR |  | CAP synoptic form item: Specify lymph node sampling. |
| 25 | `HIST_TP_SQUA_CCNM_S` | VARCHAR |  | CAP synoptic form item: Specify details for Histologic Type Squamous cell carcinoma. |
| 26 | `CARC_TYP_CNNT_DETER` | VARCHAR |  | CAP synoptic form item: Specify why carcinoma type cannot be determined. |
| 27 | `TUMOR_BORDER_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor border. |
| 28 | `MG_UVLV_IC_DSTNC_IC` | NUMERIC |  | CAP synoptic form item: Margins uninvolved by invasive carcinoma - Distance of Invasive Carcinoma from Closest Margin. |
| 29 | `MG_UVLV_IC_SM` | VARCHAR |  | CAP synoptic form item: Specify Margin for Margins uninvolved by invasive carcinoma. |
| 30 | `MGN_UVLV_IVS_CCNM_C_NAME` | VARCHAR | org | CAP synoptic form item: Margins uninvolved by invasive carcinoma. |
| 31 | `MGN_IVLV_IVS_CCNM_S` | VARCHAR |  | CAP synoptic form item: Specify details for Margin Involvement by Invasive Carcinoma. |
| 32 | `SPEC_SZ_ND_SPEC` | VARCHAR |  | CAP synoptic form item: Specify details for specimen size when it cannot be determined. |
| 33 | `MTX_DEPTH_INVASION` | NUMERIC |  | CAP synoptic form item: Specify Microscopic Tumor Extension Depth of Invasion. |
| 34 | `MTX_NT_DTMD_SPEC` | VARCHAR |  | CAP synoptic form item: Specify Microscopic Tumor Extension When Cannot be determined. |
| 35 | `MG_NT_DTMD_SPEC` | VARCHAR |  | CAP synoptic form item: Specify margin when it cannot be determined. |
| 36 | `LVI_NT_DTMD_SPEC` | VARCHAR |  | CAP synoptic form item: Specify Lymph-Vascular Invasion When Cannot be determined. |
| 37 | `LYMPH_ND_NUM_XMD` | NUMERIC |  | CAP synoptic form item: Specify the number of lymph nodes examined. |
| 38 | `LYM_ND_NUM_W_MTSTSS` | NUMERIC |  | CAP synoptic form item: Specify Number of Lymph Nodes with Metastasis. |
| 39 | `NUM_LN_WM_LESS_5` | NUMERIC |  | CAP synoptic form item: Specify the number of lymph nodes with metastasis < 5 mm. |
| 40 | `NUM_LNWM_GE5` | NUMERIC |  | CAP synoptic form item: Specify Number of Lymph Nodes with Metastasis >= 5 mm. |
| 41 | `LN_XTNDL_XTSN_NDS` | VARCHAR |  | CAP synoptic form item: Specify Lymph Nodes, Extranodal Extension Cannot be determined. |
| 42 | `LN_LATERALITY_C_NAME` | VARCHAR | org | CAP synoptic form item: LYMPH NODES Laterality. |
| 43 | `FXD_ULCRT_FI_LN_C_NAME` | VARCHAR |  | CAP synoptic form item: Fixed or Ulcerated Femoral-Inguinal Lymph Nodes. |
| 44 | `FXD_UCRT_FI_LN_NDS` | VARCHAR |  | CAP synoptic form item: Specify Fixed or Ulcerated Femoral-Inguinal Lymph Nodes Cannot be determined. |
| 45 | `PN1_1OR2_RLN_FTR_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes pN1: One or two regional lymph nodes with the following features. |
| 46 | `PN2_RLNM_FTRS_C_NAME` | VARCHAR | org | CAP synoptic form item: pN2 [FIGO IIIB]: Regional lymph node metastasis with the following features. |
| 47 | `HT_BTLN_GLND_TMR_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Type Bartholin Gland Tumors. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

