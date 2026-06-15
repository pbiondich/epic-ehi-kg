# PROSTATE_NEEDLE_BI

> Stores data for College of American Pathologists (CAP) form 76042-PROSTATE GLAND: Needle Biopsy.

**Primary key:** `RESULT_ID`  
**Columns:** 19  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 3 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 4 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 5 | `SEMINAL_VESICLE_C_NAME` | VARCHAR | org | CAP synoptic form item: Seminal Vesicle Invasion. |
| 6 | `PERIPROSTATIC_FAT_C_NAME` | VARCHAR | org | CAP synoptic form item: Periprostatic Fat Invasion. |
| 7 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 8 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 9 | `PRIMARY_GLEASON_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Gleason Pattern. |
| 10 | `SECONDARY_GLEASON_C_NAME` | VARCHAR | org | CAP synoptic form item: Secondary Gleason Pattern. |
| 11 | `TOTAL_GLEASON_SCORE` | INTEGER |  | CAP synoptic form item: Total Gleason Score. |
| 12 | `POSITIVE_CORE_NUM` | INTEGER |  | CAP synoptic form item: Number of Cores Positive. |
| 13 | `TOTAL_CORES_NUM` | INTEGER |  | CAP synoptic form item: Total Number of Cores. |
| 14 | `PROSTATIC_TISSUE_PR` | NUMERIC |  | CAP synoptic form item: Proportion (%) of prostatic tissue involved by tumor. |
| 15 | `TUMOR_QUANTITATION` | NUMERIC |  | CAP synoptic form item: Tumor Quantitation Millimeters Specify. |
| 16 | `CARCINOMA_LINEAR` | NUMERIC |  | CAP synoptic form item: Total Linear Millimeters of Carcinoma. |
| 17 | `NEEDLE_CORE_LINEAR` | NUMERIC |  | CAP synoptic form item: Total Linear Millimeters of Needle Core Tissue. |
| 18 | `PROS_TISSUE_PR_GRT` | NUMERIC |  | CAP synoptic form item: Proportion (%) of Prostatic Tissue Involved by Tumor for Core with the Greatest Amount of Tumor. |
| 19 | `PATH_INFLAM_SPFY` | VARCHAR |  | CAP synoptic form item: Additional Pathological Findings - Specify Inflammation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

