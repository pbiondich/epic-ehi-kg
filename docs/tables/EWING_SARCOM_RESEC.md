# EWING_SARCOM_RESEC

> Stores data for College of American Pathologists (CAP) form 76019-EWING SARCOMA/PRIMITIVE NEUROECTODERMAL TUMOR: Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 34  
**Org-specific columns:** 8

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
| 9 | `SPEC_PROC_AMPU_SPFY` | VARCHAR |  | CAP synoptic form item: Specimen Procedure Amputation Specify. |
| 10 | `EXT_OSSEOS_TMR_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Extent of Osseous Tumors. |
| 11 | `EXTRAOSS_TMR_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Extent of Primary Extraosseous Tumors. |
| 12 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 13 | `DIST_CLSEST_BNE_MRG` | NUMERIC |  | CAP synoptic form item: Distance of Tumor from Closest Bone Margin. |
| 14 | `DIST_CLSEST_SFT_TIS` | NUMERIC |  | CAP synoptic form item: Distance of Tumor from Closest Soft Tissue Margin. |
| 15 | `NECROSIS_POSTCHEM_C_NAME` | VARCHAR | org | CAP synoptic form item: Necrosis Postchemotherapy. |
| 16 | `NECROSIS_EXTENT` | NUMERIC |  | CAP synoptic form item: Necrosis Extent. |
| 17 | `CYTOGENETICS_C_NAME` | VARCHAR | org | CAP synoptic form item: Cytogenetics. |
| 18 | `CYTOGENETICS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify cytogenetics. |
| 19 | `MOLECULAR_PATH_C_NAME` | VARCHAR |  | CAP synoptic form item: Molecular Pathology. |
| 20 | `MOLECULAR_PATH_SPFY` | VARCHAR |  | CAP synoptic form item: Specify molecular pathology. |
| 21 | `STG_OSS_EXTRA_TMR_C_NAME` | VARCHAR | org | CAP synoptic form item: Stage for Osseous and Extraosseous Tumors. |
| 22 | `PT_PRM_EXTRAOS_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT) for Primary Extraosseous Tumors. |
| 23 | `PT_PRM_OSSEOUS_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT) for Primary Osseous Tumors. |
| 24 | `PM_PRM_EXTRAOS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis (pM) for Primary Extraosseous Tumors. |
| 25 | `PM_PRM_OSSEOUS_C_NAME` | VARCHAR |  | CAP synoptic form item: Distant Metastasis (pM) for Primary Osseous Tumors. |
| 26 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 27 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 28 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 29 | `NONREGION_LYM_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Nonregional Lymph Nodes. |
| 30 | `NONREGION_NUM_EXAM` | NUMERIC |  | CAP synoptic form item: Nonregional Lymph Nodes - Number Examined. |
| 31 | `NONREGION_NUM_INVOL` | NUMERIC |  | CAP synoptic form item: Nonregional Lymph Nodes - Number Involved. |
| 32 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 33 | `PM_PRM_OSSEOUS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Distant Metastasis (pM) for Primary Osseous Tumors. |
| 34 | `PM_PRM_EXTRAOS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Distant Metastasis (pM) for Primary Extraosseous Tumors. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

