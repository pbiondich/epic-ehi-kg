# RHABDOMYOSARCOMA

> Stores data for College of American Pathologists (CAP) form 76047-RHABDOMYOSARCOMA AND RELATED NEOPLASMS: Resection or biopsy.

**Primary key:** `RESULT_ID`  
**Columns:** 31  
**Org-specific columns:** 10

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
| 12 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 13 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastasis Sites. |
| 14 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 15 | `SPEC_PROC_AMPU_SPFY` | VARCHAR |  | CAP synoptic form item: Specimen Procedure Amputation Specify. |
| 16 | `ALVEOLAR_PERCENTAGE` | NUMERIC |  | CAP synoptic form item: Histologic Type Percentage of Alveolar. |
| 17 | `EMBRYONAL_PERCENT` | NUMERIC |  | CAP synoptic form item: Histologic Type Percentage of Embryonal. |
| 18 | `SOFT_TISSUE_TMR_SP` | VARCHAR |  | CAP synoptic form item: Tumor Depth for Soft Tissue-Based Tumors Specify. |
| 19 | `ANAPLASIA_C_NAME` | VARCHAR | org | CAP synoptic form item: Anaplasia. |
| 20 | `RHABDOMYO_GRP_SYS_C_NAME` | VARCHAR | org | CAP synoptic form item: The Intergroup Rhabdomyosarcoma Study Postsurgical Clinical Grouping System. |
| 21 | `RHABDOMY_GRP_SYS_SP` | VARCHAR |  | CAP synoptic form item: The Intergroup Rhabdomyosarcoma Study Postsurgical Clinical Grouping System Specify. |
| 22 | `STAGING_RHABDOMYO_C_NAME` | VARCHAR | org | CAP synoptic form item: Modified Site, Size, Metastasis Staging for Rhabdomyosarcoma (for relevant stage). |
| 23 | `RHABDOM_STAGE_SPEC` | VARCHAR |  | CAP synoptic form item: Modified Site, Size, Metastasis Staging for Rhabdomyosarcoma Specify. |
| 24 | `DIST_SARCOMA_MARGIN` | NUMERIC |  | CAP synoptic form item: Distance of Sarcoma from Closest Margin. |
| 25 | `LYMPH_ND_NUM_XMD` | INTEGER |  | CAP synoptic form item: Specify the number of lymph nodes examined. |
| 26 | `LYM_ND_NUM_IVLV` | INTEGER |  | CAP synoptic form item: Specify number of lymph nodes involved. |
| 27 | `NO_REGION_LYMPH_C_NAME` | VARCHAR | org | CAP synoptic form item: Lymph Nodes No Regional Lymph Nodes. |
| 28 | `RHAB_GRP_SYS_I_C_NAME` | VARCHAR | org | CAP synoptic form item: The Intergroup Rhabdomyosarcoma Study Postsurgical Clinical Grouping System Group I. |
| 29 | `RHAB_GRP_SYS_II_C_NAME` | VARCHAR | org | CAP synoptic form item: The Intergroup Rhabdomyosarcoma Study Postsurgical Clinical Grouping System Group II. |
| 30 | `RHAB_GRP_SYS_III_C_NAME` | VARCHAR | org | CAP synoptic form item: The Intergroup Rhabdomyosarcoma Study Postsurgical Clinical Grouping System Group III. |
| 31 | `RHAB_GRP_SYS_IV_C_NAME` | VARCHAR | org | CAP synoptic form item: The Intergroup Rhabdomyosarcoma Study Postsurgical Clinical Grouping System Group IV. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

