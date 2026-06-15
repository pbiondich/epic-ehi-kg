# AMPULLA_OF_VATER

> Stores single response data for College of American Pathologists (CAP) form 76001-AMPULLA OF VATER: AMPULLECTOMY, PANCREATICODUODENECTOMY.

**Primary key:** `RESULT_ID`  
**Columns:** 40  
**Org-specific columns:** 12

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
| 9 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 10 | `MARGIN_UNITS_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Units. |
| 11 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 12 | `ALL_MRG_UNIN_CAR_YN` | VARCHAR |  | CAP synoptic form item: All Margins Uninvolved By Invasive Carcinoma. |
| 13 | `SPFY_MARGIN_CATEG_C_NAME` | VARCHAR | org | CAP synoptic form item: Specify Margin Category. |
| 14 | `CLOSEST_MRG_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Closest Margin. |
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
| 27 | `TISSUE_SPEC_TYPE_C_NAME` | VARCHAR | org | CAP synoptic form item: Tissue Specimen Type. |
| 28 | `PROX_MRG_CNNT_BE_YN` | VARCHAR |  | CAP synoptic form item: Proximal Margin Cannot Be Assessed. |
| 29 | `PROX_MRG_INVAS_C_NAME` | VARCHAR | org | CAP synoptic form item: Proximal Margin Involvement. |
| 30 | `PROX_MRG_INT_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Proximal Margin Involvement by Carcinoma / Adenoma. |
| 31 | `DIST_MRG_CNNT_BE_YN` | VARCHAR |  | CAP synoptic form item: Distal Margin Cannot Be Assessed. |
| 32 | `DISTAL_MRG_INVAS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distal Margin Invasive Carcinoma Involvement. |
| 33 | `DIST_MRG_INT_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Distal Margin Intramucosal Carcinoma - Adenoma. |
| 34 | `PANCR_RETRO_MRG_C_NAME` | VARCHAR |  | CAP synoptic form item: Pancreatic Retroperitoneal Margin. |
| 35 | `BILE_DUCT_MARGIN_C_NAME` | VARCHAR |  | CAP synoptic form item: Bile Duct Margin. |
| 36 | `DISTAL_PANC_MRG_C_NAME` | VARCHAR |  | CAP synoptic form item: Distal Pancreatic Margin. |
| 37 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 38 | `AMPULLEC_SPEC_MRG_C_NAME` | VARCHAR |  | CAP synoptic form item: Ampullectomy Specimen Margin. |
| 39 | `DIRECTLY_INVADS_ADJ` | VARCHAR |  | CAP synoptic form item: Tumor directly invades other adjacent organs. |
| 40 | `INV_CARC_CLOSE_MRG` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Distance from Closest Margin. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

