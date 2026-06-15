# PROSTATE_RADICAL

> Stores data for College of American Pathologists (CAP) form 76043-PROSTATE GLAND: Radical Prostatectomy.

**Primary key:** `RESULT_ID`  
**Columns:** 33  
**Org-specific columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 3 | `SIZE_LARGST_POS_LYM` | NUMERIC |  | CAP synoptic form item: Size (greatest dimension, in cm) of the Largest Positive Lymph Node. |
| 4 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 5 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 6 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 7 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 8 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 9 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 10 | `SEMINAL_VESICLE_C_NAME` | VARCHAR | org | CAP synoptic form item: Seminal Vesicle Invasion. |
| 11 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 12 | `REG_LN_NUM_EXM` | INTEGER |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 13 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 14 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 15 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 16 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 17 | `TUMOR_FOCAL_SPECIFY` | VARCHAR |  | CAP synoptic form item: Tumor Focality Other Specify. |
| 18 | `PRIMARY_GLEASON_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Gleason Pattern. |
| 19 | `SECONDARY_GLEASON_C_NAME` | VARCHAR | org | CAP synoptic form item: Secondary Gleason Pattern. |
| 20 | `TOTAL_GLEASON_SCORE` | INTEGER |  | CAP synoptic form item: Total Gleason Score. |
| 21 | `EXTRAPROST_EXT_C_NAME` | VARCHAR | org | CAP synoptic form item: Extraprostatic Extension. |
| 22 | `EXTRAPROS_EXT_PRE_C_NAME` | VARCHAR | org | CAP synoptic form item: Extraprostatic Extension Present. |
| 23 | `EXTRAPROS_EXT_SPECI` | VARCHAR |  | CAP synoptic form item: Extraprostatic Extension Present Site Specify. |
| 24 | `PROSTATE_TUMOR_WT` | NUMERIC |  | CAP synoptic form item: Prostate Tumor Weight. |
| 25 | `PROSTATE_TUMOR_SIZE` | NUMERIC |  | CAP synoptic form item: Prostate Tumor Size. |
| 26 | `PROSTATE_TUMOR_ADD1` | NUMERIC |  | CAP synoptic form item: Prostate Tumor Additional Size. |
| 27 | `PROSTATE_TUMOR_ADD2` | NUMERIC |  | CAP synoptic form item: Prostate Tumor Additional Size 2. |
| 28 | `PATH_INFLAM_SPFY` | VARCHAR |  | CAP synoptic form item: Additional Pathological Findings - Specify Inflammation. |
| 29 | `ANCLR_STD_SPEC` | VARCHAR |  | CAP synoptic form item: Specify details for ancillary studies. |
| 30 | `TERTIARY_GLEASON_C_NAME` | VARCHAR | org | CAP synoptic form item: Tertiary Gleason Pattern. |
| 31 | `PROP_PROSTATE_TUMOR` | NUMERIC |  | CAP synoptic form item: Proportion (percentage) of Prostate Involved by Tumor. |
| 32 | `TREAT_EFCT_CARC_SPE` | VARCHAR |  | CAP synoptic form item: Treatment Effect on Carcinoma Specify. |
| 33 | `REG_LN_NUM_INV` | INTEGER |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

