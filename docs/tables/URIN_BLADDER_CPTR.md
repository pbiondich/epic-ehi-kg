# URIN_BLADDER_CPTR

> Stores single response data for College of American Pathologists (CAP) form 76061-URINARY BLADDER: Cystectomy, Partial, Total, or Radical.

**Primary key:** `RESULT_ID`  
**Columns:** 34  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 3 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 4 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 5 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 6 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 7 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 8 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 9 | `MICRO_TMR_EXT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Microscopic Tumor Extension. |
| 10 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 11 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 12 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 13 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 14 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 15 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 16 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastatis Sites. |
| 17 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 18 | `SPEC_MG_IVLV_INV_CC` | VARCHAR |  | CAP synoptic form item: Specify Margin Involved by Invasive Carcinoma. |
| 19 | `OTHER_TM_CONFIG_S` | VARCHAR |  | CAP synoptic form item: Specify other tumor configuration. |
| 20 | `HIST_TYP_NONCL_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other or nonclassifiable histologic type. |
| 21 | `HG_URTL_CCNM_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade Urothelial Carcinoma. |
| 22 | `HG_URTL_CCNM_S` | VARCHAR |  | CAP synoptic form item: Specify the details of Histologic Grade Urothelial carcinoma. |
| 23 | `HG_ADEN_SQUA_CC_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade Adenocarcinoma and Squamous Cell Carcinoma. |
| 24 | `ADEN_SQUA_CCS` | VARCHAR |  | CAP synoptic form item: Specify Histologic Grade Adenocarcinoma and Squamous Cell Carcinoma. |
| 25 | `UROT_CCM_W_VAR_HIST` | VARCHAR |  | CAP synoptic form item: Specify the details of Urothelial carcinoma with variant histology. |
| 26 | `SQM_C_CCNM_VAR_HIST` | VARCHAR |  | CAP synoptic form item: Specify the details of Squamous cell carcinoma, variant histology. |
| 27 | `ADNCCNM_VAR_HIST` | VARCHAR |  | CAP synoptic form item: Specify the details of Adenocarcinoma, variant histology. |
| 28 | `UNDIFF_CCNM` | VARCHAR |  | CAP synoptic form item: Specify the details of undifferentiated carcinoma. |
| 29 | `HIST_TP_MIX_CT` | VARCHAR |  | CAP synoptic form item: Specify the details of mixed cell type. |
| 30 | `MG_IVLV_INV_CCNM_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Involvement by Invasive Carcinoma. |
| 31 | `MG_UVLV_IC_DSTNC_IC` | NUMERIC |  | CAP synoptic form item: Margins uninvolved by invasive carcinoma - Distance of Invasive Carcinoma from Closest Margin. |
| 32 | `MG_UVLV_IC_SM` | VARCHAR |  | CAP synoptic form item: Specify Margin for Margins uninvolved by invasive carcinoma. |
| 33 | `MG_IVLV_CCNM_SS` | VARCHAR |  | CAP synoptic form item: Specify Margins involved by carcinoma in situ. |
| 34 | `MG_IVLV_CCNM_ST_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Involvement by Carcinoma in situ. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

