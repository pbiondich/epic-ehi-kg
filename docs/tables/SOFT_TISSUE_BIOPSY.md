# SOFT_TISSUE_BIOPSY

> Stores data for College of American Pathologists (CAP) form 76049-SOFT TISSUE: Biopsy.

**Primary key:** `RESULT_ID`  
**Columns:** 26  
**Org-specific columns:** 4

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
| 10 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 11 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 12 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 13 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 14 | `OTHER_CLOSE_MARGINS` | VARCHAR |  | CAP synoptic form item: Other Close Margins Specify. |
| 15 | `MITOTIC_RATE` | NUMERIC |  | CAP synoptic form item: Mitotic Rate. |
| 16 | `NECROSIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Necrosis. |
| 17 | `NECROSIS_EXTENT` | NUMERIC |  | CAP synoptic form item: Necrosis Extent. |
| 18 | `IMMUNOHISTOCHEM_C_NAME` | VARCHAR | org | CAP synoptic form item: Immunohistochemistry. |
| 19 | `IMMUNOHISTOCHM_SPFY` | VARCHAR |  | CAP synoptic form item: Specify immunohistochemistry. |
| 20 | `MOLECULAR_PATH_C_NAME` | VARCHAR |  | CAP synoptic form item: Molecular Pathology. |
| 21 | `MOLECULAR_PATH_SPFY` | VARCHAR |  | CAP synoptic form item: Specify molecular pathology. |
| 22 | `CYTOGENETICS_C_NAME` | VARCHAR |  | CAP synoptic form item: Cytogenetics. |
| 23 | `CYTOGENETICS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify cytogenetics. |
| 24 | `MACRO_TUMOR_DEEP_SP` | VARCHAR |  | CAP synoptic form item: Macroscopic Extent of Tumor Deep Specify. |
| 25 | `DIST_SARCOMA_MARGIN` | NUMERIC |  | CAP synoptic form item: Distance of Sarcoma from Closest Margin. |
| 26 | `PERCENT_VIABLE_TMR` | NUMERIC |  | CAP synoptic form item: Percentage of Viable Tumor. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

