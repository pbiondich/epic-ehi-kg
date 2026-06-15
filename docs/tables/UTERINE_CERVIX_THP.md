# UTERINE_CERVIX_THP

> Stores single response data for College of American Pathologists (CAP) form field 76063-UTERINE CERVIX: Trachelectomy, Hysterectomy, Pelvic Exenteration.

**Primary key:** `RESULT_ID`  
**Columns:** 26  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 3 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 4 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 5 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 6 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 7 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 8 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 9 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 10 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 11 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 12 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 13 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 14 | `HIST_TYP_NONCL_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other or nonclassifiable histologic type. |
| 15 | `HIST_TP_SQUA_CCNM_S` | VARCHAR |  | CAP synoptic form item: Specify details for Histologic Type Squamous cell carcinoma. |
| 16 | `HIST_TP_ADCCNM_OS` | VARCHAR |  | CAP synoptic form item: Specify other details for Histologic Type Adenocarcinoma. |
| 17 | `ADF_ITAPTLL_NPLS_S` | VARCHAR |  | CAP synoptic form item: Specify type and grade for Intraepithelial neoplasia in Additional Pathologic Findings section. |
| 18 | `MG_UVLV_IC_DSTNC_IC` | NUMERIC |  | CAP synoptic form item: Margins uninvolved by invasive carcinoma - Distance of Invasive Carcinoma from Closest Margin. |
| 19 | `MG_UVLV_IC_SM` | VARCHAR |  | CAP synoptic form item: Specify Margin for Margins uninvolved by invasive carcinoma. |
| 20 | `MGN_UVLV_IVS_CCNM_C_NAME` | VARCHAR | org | CAP synoptic form item: Margins uninvolved by invasive carcinoma. |
| 21 | `MGN_IVLV_IVS_CCNM_S` | VARCHAR |  | CAP synoptic form item: Specify details for Margin Involvement by Invasive Carcinoma. |
| 22 | `ANCLR_STD_SPEC` | VARCHAR |  | CAP synoptic form item: Specify details for ancillary studies. |
| 23 | `PN1_RGNL_LNM_NUM_XM` | VARCHAR |  | CAP synoptic form item: Specify number examined for Regional Lymph Nodes (pN) pN1 Regional lymph node metastasis. |
| 24 | `PN1_RGNL_LNM_NUM_IV` | VARCHAR |  | CAP synoptic form item: Specify number involved for Regional Lymph Nodes (pN) pN1 Regional lymph node metastasis. |
| 25 | `DSTNT_MTSTS_PM1_ST` | VARCHAR |  | CAP synoptic form item: Specify Site for Distant Metastases pM pM1 IVB Distant metastasis. |
| 26 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

