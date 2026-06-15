# UTERINE_CERVIX_EXC

> Stores single response data for College of American Pathologists (CAP) form 76062-UTERINE CERVIX: Excision.

**Primary key:** `RESULT_ID`  
**Columns:** 39  
**Org-specific columns:** 6

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
| 9 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 10 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 11 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 12 | `HIST_TYP_NONCL_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other or nonclassifiable histologic type. |
| 13 | `HIST_TP_SQUA_CCNM_S` | VARCHAR |  | CAP synoptic form item: Specify details for Histologic Type Squamous cell carcinoma. |
| 14 | `HIST_TP_ADCCNM_OS` | VARCHAR |  | CAP synoptic form item: Specify other details for Histologic Type Adenocarcinoma. |
| 15 | `STRML_INVSN_DEPTH` | NUMERIC |  | CAP synoptic form item: Specify Stromal Invasion Depth. |
| 16 | `STRML_INVSN_HRZL_XT` | NUMERIC |  | CAP synoptic form item: Specify Stromal Invasion Horizontal Extent. |
| 17 | `ENDC_MG_CNNT_ASSD_C_NAME` | VARCHAR | org | CAP synoptic form item: Endocervical Margin invasive carcinoma. |
| 18 | `ENDC_MG_IVLV_IC_C_NAME` | VARCHAR | org | CAP synoptic form item: Endocervical Margin Involved by Invasive Carcinoma. |
| 19 | `DSTC_INVS_CCNM_XM` | NUMERIC |  | CAP synoptic form item: Specify Distance of Invasive Carcinoma from Margin for Not involved by invasive carcinoma when Exocervical Margin cannot be assessed. |
| 20 | `XCVL_MG_INV_CCNM_LC` | VARCHAR |  | CAP synoptic form item: Specify location for Exocervical Margin Involved by invasive carcinoma. |
| 21 | `XCVC_MG_IVLV_IC_C_NAME` | VARCHAR | org | CAP synoptic form item: Exocervical Margin Involved by Invasive Carcinoma. |
| 22 | `ITAEP_SQM_NPS_GRD` | VARCHAR |  | CAP synoptic form item: Specify grade for Exocervical Margin Involved by intraepithelial squamous neoplasia. |
| 23 | `DSTNC_INV_CCNM_EM` | NUMERIC |  | CAP synoptic form item: Specify distance of invasive carcinoma from Endocervical Margin when invasive carcinoma not involved. |
| 24 | `EM_NINVSV_CCNM_LOC` | VARCHAR |  | CAP synoptic form item: Specify location for Endocervical Margin not Involved by invasive carcinoma. |
| 25 | `EM_INVSV_CCNM_LOC` | VARCHAR |  | CAP synoptic form item: Specify location for Endocervical Margin Involved by invasive carcinoma. |
| 26 | `EM_IVLV_ISN_GRD` | VARCHAR |  | CAP synoptic form item: Specify grade for Endocervical Margin Involved by intraepithelial squamous neoplasia. |
| 27 | `DSTNC_INV_CCNM_DMNA` | NUMERIC |  | CAP synoptic form item: Specify Distance of Invasive Carcinoma from Margin for Deep Margin when Margins cannot be assessed and Not involved by invasive carcinoma. |
| 28 | `DM_NA_UIC_LOC` | VARCHAR |  | CAP synoptic form item: Specify location for Deep Margin when Uninvolved. |
| 29 | `DM_NA_IIC_LOC` | VARCHAR |  | CAP synoptic form item: Specify location for Deep Margin when Involved. |
| 30 | `DM_NA_IISN_GRD` | VARCHAR |  | CAP synoptic form item: Specify grade for Deep Margin when Margins cannot be assessed and involved by intraepithelial squamous neoplasia. |
| 31 | `XCRVCL_MG_IIC_LOC` | VARCHAR |  | CAP synoptic form item: Specify location for Exocervical Margin Not involved by invasive carcinoma. |
| 32 | `END_MG_INT_SQM_NP_C_NAME` | VARCHAR | org | CAP synoptic form item: Endocervical Margin intraepithelial squamous neoplasia. |
| 33 | `END_MG_ADC_ST_C_NAME` | VARCHAR | org | CAP synoptic form item: Endocervical Margin adenocarcinoma in situ. |
| 34 | `DM_INV_CCNM_C_NAME` | VARCHAR |  | CAP synoptic form item: Deep Margin invasive carcinoma. |
| 35 | `DM_INT_SQM_NPS_C_NAME` | VARCHAR |  | CAP synoptic form item: Deep Margin intraepithelial squamous neoplasia. |
| 36 | `DM_ADCNM_ST_C_NAME` | VARCHAR |  | CAP synoptic form item: Deep Margin adenocarcinoma in situ. |
| 37 | `XM_INT_SQM_NPS_C_NAME` | VARCHAR |  | CAP synoptic form item: Exocervical Margin intraepithelial squamous neoplasia. |
| 38 | `XM_ADNCNM_ST_C_NAME` | VARCHAR |  | CAP synoptic form item: Exocervical Margin adenocarcinoma in situ. |
| 39 | `XCVCL_MG_CNNT_ASD_C_NAME` | VARCHAR |  | CAP synoptic form item: Exocervical Margin invasive carcinoma. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

