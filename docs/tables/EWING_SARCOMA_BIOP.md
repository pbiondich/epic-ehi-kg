# EWING_SARCOMA_BIOP

> Stores data for College of American Pathologists (CAP) form 76018-EWING SARCOMA/PRIMITIVE NEUROECTODERMAL TUMOR: Biopsy.

**Primary key:** `RESULT_ID`  
**Columns:** 20  
**Org-specific columns:** 2

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
| 9 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 10 | `EXT_OSSEOS_TMR_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Extent of Osseous Tumors. |
| 11 | `EXTRAOSS_TMR_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Extent of Primary Extraosseous Tumors. |
| 12 | `DIST_CLSEST_BNE_MRG` | NUMERIC |  | CAP synoptic form item: Distance of Tumor from Closest Bone Margin. |
| 13 | `DIST_CLSEST_SFT_TIS` | NUMERIC |  | CAP synoptic form item: Distance of Tumor from Closest Soft Tissue Margin. |
| 14 | `NECROSIS_POSTCHEM_C_NAME` | VARCHAR | org | CAP synoptic form item: Necrosis Postchemotherapy. |
| 15 | `CYTOGENETICS_C_NAME` | VARCHAR | org | CAP synoptic form item: Cytogenetics. |
| 16 | `CYTOGENETICS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify cytogenetics. |
| 17 | `MOLECULAR_PATH_C_NAME` | VARCHAR |  | CAP synoptic form item: Molecular Pathology. |
| 18 | `MOLECULAR_PATH_SPFY` | VARCHAR |  | CAP synoptic form item: Specify molecular pathology. |
| 19 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 20 | `NECROSIS_EXTENT` | NUMERIC |  | CAP synoptic form item: Necrosis Extent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

