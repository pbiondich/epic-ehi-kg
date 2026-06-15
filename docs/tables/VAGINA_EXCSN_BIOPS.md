# VAGINA_EXCSN_BIOPS

> Stores single response data for College of American Pathologists (CAP) form field 76066-VAGINA: Excisional Biopsy, Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 22  
**Org-specific columns:** 5

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
| 8 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 9 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 10 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 11 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 12 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 13 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 14 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 15 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 16 | `HIST_TYP_NONCL_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other or nonclassifiable histologic type. |
| 17 | `MG_UVLV_IC_DSTNC_IC` | NUMERIC |  | CAP synoptic form item: Margins uninvolved by invasive carcinoma - Distance of Invasive Carcinoma from Closest Margin. |
| 18 | `MG_UVLV_IC_SM` | VARCHAR |  | CAP synoptic form item: Specify Margin for Margins uninvolved by invasive carcinoma. |
| 19 | `MGN_UVLV_IVS_CCNM_C_NAME` | VARCHAR | org | CAP synoptic form item: Margins uninvolved by invasive carcinoma. |
| 20 | `MGN_IVLV_IVS_CCNM_S` | VARCHAR |  | CAP synoptic form item: Specify details for Margin Involvement by Invasive Carcinoma. |
| 21 | `DSTNT_MTSTS_PM1_ST` | VARCHAR |  | CAP synoptic form item: Specify Site for Distant Metastases pM pM1 IVB Distant metastasis. |
| 22 | `CCNM_IN_SITU_GRD_MG` | VARCHAR |  | CAP synoptic form item: Specify grade for Dysplasia / carcinoma in situ present when margins uninvolved by invasive carcinoma. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

