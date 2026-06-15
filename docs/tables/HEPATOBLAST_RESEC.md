# HEPATOBLAST_RESEC

> Stores data for College of American Pathologists (CAP) form 76023-HEPATOBLASTOMA (PEDIATRIC LIVER): Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 31  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `OTHER_CLIN_FNDGS` | VARCHAR |  | CAP synoptic form item: Other Clinical Findings. |
| 3 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 4 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 5 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 6 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 7 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 8 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 9 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 10 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 11 | `MARGIN_UNITS_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Units. |
| 12 | `RESECTION_MARGIN_C_NAME` | VARCHAR | org | CAP synoptic form item: Resection Margin. |
| 13 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 14 | `PERCENT_HIST_FEATUR` | NUMERIC |  | CAP synoptic form item: Percentage of Tumor with this Histologic Feature. |
| 15 | `HEPATOBLASTOMA_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Hepatoblastoma. |
| 16 | `MACRO_EXTENT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Macroscopic Extent. |
| 17 | `RESEC_MRG_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Resection Margin. |
| 18 | `DIST_INV_TMR_MRG` | NUMERIC |  | CAP synoptic form item: Distance of Invasive Tumor from Closest Margin. |
| 19 | `CAPSULAR_SURFACE_C_NAME` | VARCHAR |  | CAP synoptic form item: Capsular Surface. |
| 20 | `SURFACE_MARGIN_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Surface Margin. |
| 21 | `DIST_TMR_SURFACE` | NUMERIC |  | CAP synoptic form item: Distance of Invasive Tumor from Closest Surface. |
| 22 | `MARGIN_UNITS_2_C_NAME` | VARCHAR |  | CAP synoptic form item: Margin Units (second measurement). |
| 23 | `LYM_ND_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Lymph Node Metastasis. |
| 24 | `LYM_ND_METAS_LOC` | VARCHAR |  | CAP synoptic form item: Lymph Node Metastasis Location. |
| 25 | `LYM_ND_METAS_EXAM` | NUMERIC |  | CAP synoptic form item: Lymph Node Metastasis Nodes Examined. |
| 26 | `LYM_ND_METAS_INVOLV` | NUMERIC |  | CAP synoptic form item: Lymph Node Metastasis Nodes Involved by Tumor. |
| 27 | `SPECIAL_STD_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Special Studies. |
| 28 | `ADDL_PATH_HEPATITIS` | VARCHAR |  | CAP synoptic form item: Additional Pathologic Findings Hepatitis. |
| 29 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 30 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 31 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastasis Sites. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

