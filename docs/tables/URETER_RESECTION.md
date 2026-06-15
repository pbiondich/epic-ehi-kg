# URETER_RESECTION

> Stores data for College of American Pathologists (CAP) form 76059-URETER: Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 35  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 3 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 4 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 5 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 6 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 7 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 8 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 9 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 10 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 11 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 12 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 13 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 14 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastatis Sites. |
| 15 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 16 | `OTHER_MARGIN_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other margin. |
| 17 | `OTHER_TM_CONFIG_S` | VARCHAR |  | CAP synoptic form item: Specify other tumor configuration. |
| 18 | `HG_URTL_CCNM_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade Urothelial Carcinoma. |
| 19 | `HG_URTL_CCNM_S` | VARCHAR |  | CAP synoptic form item: Specify the details of Histologic Grade Urothelial carcinoma. |
| 20 | `HG_ADEN_SQUA_CC_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade Adenocarcinoma and Squamous Cell Carcinoma. |
| 21 | `ADEN_SQUA_CCS` | VARCHAR |  | CAP synoptic form item: Specify Histologic Grade Adenocarcinoma and Squamous Cell Carcinoma. |
| 22 | `UROT_CCM_W_VAR_HIST` | VARCHAR |  | CAP synoptic form item: Specify the details of Urothelial carcinoma with variant histology. |
| 23 | `SQM_C_CCNM_VAR_HIST` | VARCHAR |  | CAP synoptic form item: Specify the details of Squamous cell carcinoma, variant histology. |
| 24 | `ADNCCNM_VAR_HIST` | VARCHAR |  | CAP synoptic form item: Specify the details of Adenocarcinoma, variant histology. |
| 25 | `UNDIFF_CCNM` | VARCHAR |  | CAP synoptic form item: Specify the details of undifferentiated carcinoma. |
| 26 | `HIST_TP_MIX_CT` | VARCHAR |  | CAP synoptic form item: Specify the details of mixed cell type. |
| 27 | `GLOMERULAR_DIS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Glomerular disease. |
| 28 | `TUBULNTST_DIS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Tubulointerstitial disease. |
| 29 | `VASCULAR_DIS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Vascular disease. |
| 30 | `PATH_NON_KIDNY_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Pathologic Findings in Nonneoplastic Kidney. |
| 31 | `INFLAMMATION_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Inflammation. |
| 32 | `MARGIN_INV_SPECIFY` | VARCHAR |  | CAP synoptic form item: Margins Invasive Specify Margins Per Orientation. |
| 33 | `MARG_INV_DIST_CLOSE` | NUMERIC |  | CAP synoptic form item: Margins Invasive Distance of Invasive Carcinoma from Closest Margin. |
| 34 | `MG_IVLV_INV_CCNM_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Involvement by Invasive Carcinoma. |
| 35 | `MG_IVLV_CCNM_ST_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Involvement by Carcinoma in situ. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

