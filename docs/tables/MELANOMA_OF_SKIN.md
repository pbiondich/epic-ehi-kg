# MELANOMA_OF_SKIN

> Stores single response data for College of American Pathologists (CAP) form 76033-MELANOMA OF THE SKIN: Biopsy, Excision, Re-Excision.

**Primary key:** `RESULT_ID`  
**Columns:** 53  
**Org-specific columns:** 16

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
| 8 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 9 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 10 | `LYM_ND_EXNDL_EXT_C_NAME` | VARCHAR |  | CAP synoptic form item: Lymph Nodes, Extranodal Extension. |
| 11 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 12 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 13 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 14 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastasis Sites. |
| 15 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 16 | `NUM_LYM_ND_IDEN` | NUMERIC |  | CAP synoptic form item: Number of Lymph Nodes Identified. |
| 17 | `TOT_NUM_LYM_ND_EXAM` | NUMERIC |  | CAP synoptic form item: Total Number of Lymph Nodes Examined (Sentinel and Nonsentinel). |
| 18 | `NUM_SENT_LYM_EXAM` | NUMERIC |  | CAP synoptic form item: Number of Sentinel Lymph Nodes Examined. |
| 19 | `MACRO_SATEL_NODUL_C_NAME` | VARCHAR |  | CAP synoptic form item: Macroscopic Satellite Nodules. |
| 20 | `MACRO_PIGMENTATN_C_NAME` | VARCHAR | org | CAP synoptic form item: Macroscopic Pigmentation. |
| 21 | `PROC_LYMPHADENECTM` | VARCHAR |  | CAP synoptic form item: Specimen Procedure - Specify Lymphadenectomy, regional nodes. |
| 22 | `MAX_TUMOR_THICK_C_NAME` | VARCHAR | org | CAP synoptic form item: Maximum Tumor Thickness. |
| 23 | `MAX_TMR_THICK_SPFY` | NUMERIC |  | CAP synoptic form item: Specify Maximum Tumor Thickness. |
| 24 | `MAX_TMR_THICK_LEAST` | NUMERIC |  | CAP synoptic form item: Maximum Tumor Thickness - At Least this Length. |
| 25 | `MAX_TMR_THICK_EXPLN` | VARCHAR |  | CAP synoptic form item: Explain the Maximum Tumor Thickness. |
| 26 | `ANATOMIC_LEVEL_C_NAME` | VARCHAR | org | CAP synoptic form item: Anatomic Level. |
| 27 | `ULCERATION_C_NAME` | VARCHAR |  | CAP synoptic form item: Ulceration. |
| 28 | `PER_MRG_CNT_ASSE_YN` | VARCHAR |  | CAP synoptic form item: Peripheral Margins Cannot Be Assessed. |
| 29 | `PER_MRG_INV_MELNM_C_NAME` | VARCHAR | org | CAP synoptic form item: Peripheral Margin Invasive Melanoma. |
| 30 | `PER_MRG_UNV_MELNM_C_NAME` | VARCHAR | org | CAP synoptic form item: Peripheral margin Uninvolved by Invasive Melanoma. |
| 31 | `PER_MRG_DIST_CLOSES` | NUMERIC |  | CAP synoptic form item: Peripheral Margin Distance of Invasive melanoma from Closest Peripheral Margin. |
| 32 | `PER_MRG_LOC_SPFY` | VARCHAR |  | CAP synoptic form item: Peripheral Margin - Specify Invasive Melanoma Location. |
| 33 | `PER_MRG_MELNM_STU_C_NAME` | VARCHAR | org | CAP synoptic form item: Peripheral Margin Melanoma in Situ. |
| 34 | `PER_MRG_UNIN_SITU_C_NAME` | VARCHAR | org | CAP synoptic form item: Peripheral Margin Uninvolved by Melanoma in Situ. |
| 35 | `PER_MRG_SITU_DIST` | NUMERIC |  | CAP synoptic form item: Peripheral margin Distance of Melanoma in Situ from Closest Margin. |
| 36 | `PER_MRG_SITU_LOC` | VARCHAR |  | CAP synoptic form item: Peripheral Margin - Specify Melanoma in Situ Location. |
| 37 | `DP_MRG_CNT_ASSES_YN_NAME` | VARCHAR |  | CAP synoptic form item: Deep margin which cannot be assessed. |
| 38 | `DP_MRG_UNIN_MELNM_C_NAME` | VARCHAR |  | CAP synoptic form item: Deep Margin Invasive Melanoma. |
| 39 | `DP_MRG_INV_MEL_DIST` | NUMERIC |  | CAP synoptic form item: Deep Margin Distance of Invasive Melanoma from Margin. |
| 40 | `DP_MRG_LOC_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Deep Margin Location. |
| 41 | `MITOTIC_INDEX_C_NAME` | VARCHAR | org | CAP synoptic form item: Mitotic Index. |
| 42 | `MITOTIC_INDEX_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Mitotic Index. |
| 43 | `MICROSATELLITOSS_C_NAME` | VARCHAR |  | CAP synoptic form item: Microsatellitosis. |
| 44 | `TMR_INFLT_LYMPHCY_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor-Infiltrating Lymphocytes. |
| 45 | `TUMOR_REGRESSION_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor Regression. |
| 46 | `GROWTH_PHASE_C_NAME` | VARCHAR | org | CAP synoptic form item: Growth Phase. |
| 47 | `NUM_LYM_ND_METAST` | NUMERIC |  | CAP synoptic form item: Number of Lymph Nodes with Metastases. |
| 48 | `SZE_METASTATIC_FOCS` | NUMERIC |  | CAP synoptic form item: Size of Largest Metastatic Focus (for sentinel node). |
| 49 | `LOC_METAST_TMR_C_NAME` | VARCHAR | org | CAP synoptic form item: Location of Metastatic Tumor (for sentinel node). |
| 50 | `NUM_METAST_MACRO` | NUMERIC |  | CAP synoptic form item: Number containing metastases identified macroscopically. |
| 51 | `NUM_METAST_MICRO` | NUMERIC |  | CAP synoptic form item: Number containing metastases identified microscopically. |
| 52 | `MATTED_NODES_C_NAME` | VARCHAR |  | CAP synoptic form item: Matted Nodes. |
| 53 | `TUMOR_SIZE_INDETER` | VARCHAR |  | CAP synoptic form item: Specify Reason Why Tumor Size Is Indeterminate. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

