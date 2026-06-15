# ANUS_ABDOMIN_RESEC

> Stores single response data for College of American Pathologists (CAP) form 76002-ANUS: ABDOMINOPERINEAL RESECTION.

**Primary key:** `RESULT_ID`  
**Columns:** 34  
**Org-specific columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `NEOADJ_THRPY_TYPE` | VARCHAR |  | CAP synoptic form item: Neoadjuvant Therapy Type. |
| 3 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 4 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 5 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 6 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 7 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 8 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 9 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 10 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 11 | `ALL_MRG_UNIN_CAR_YN` | VARCHAR |  | CAP synoptic form item: All Margins Uninvolved By Invasive Carcinoma. |
| 12 | `SPFY_MARGIN_CATEG_C_NAME` | VARCHAR | org | CAP synoptic form item: Specify Margin Category. |
| 13 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 14 | `TREATMNT_EFF_PRES_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect Present. |
| 15 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 16 | `ANC_STDIES_SPFY_TYP` | VARCHAR |  | CAP synoptic form item: Ancillary Studies Specify Types. |
| 17 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 18 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 19 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 20 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 21 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 22 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 23 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastasis Sites. |
| 24 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 25 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 26 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 27 | `PROX_MRG_INVAS_C_NAME` | VARCHAR | org | CAP synoptic form item: Proximal Margin Involvement. |
| 28 | `PROX_UNIN_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Proximal Margin Uninvolved With Carcinoma. |
| 29 | `DISTAL_MRG_INVAS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distal Margin Invasive Carcinoma Involvement. |
| 30 | `DIST_UNIN_CARC_C_NAME` | VARCHAR |  | CAP synoptic form item: Distal Margin Uninvolved With Carcinoma. |
| 31 | `CIRCUMFERENTL_MRG_C_NAME` | VARCHAR |  | CAP synoptic form item: Circumferential (Radial) Margin. |
| 32 | `DIRECTLY_INVADS_ADJ` | VARCHAR |  | CAP synoptic form item: Tumor directly invades other adjacent organs. |
| 33 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 34 | `INV_CARC_CLOSE_MRG` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Distance from Closest Margin. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

