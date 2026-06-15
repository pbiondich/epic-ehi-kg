# PERITONEUM_RESECT

> Stores data for College of American Pathologists (CAP) form 76040-PERITONEUM: Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 38  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 3 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 4 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 5 | `TUMOR_OTHER_SIZE_C_NAME` | VARCHAR | org | CAP synoptic form item: Other Tumor Size. |
| 6 | `TUMOR_OTHER_GREAT` | NUMERIC |  | CAP synoptic form item: Other Tumor Size Greatest. |
| 7 | `TUMOR_OTHER_ADDT1` | NUMERIC |  | CAP synoptic form item: Other Tumor Size Additional. |
| 8 | `TUMOR_OTHER_ADDT2` | NUMERIC |  | CAP synoptic form item: Other Tumor Size Additional 2. |
| 9 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 10 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 11 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 12 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 13 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 14 | `EFFUSIONS_C_NAME` | VARCHAR | org | CAP synoptic form item: Effusions. |
| 15 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 16 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 17 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 18 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 19 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 20 | `LYMPH_ND_SAMPL_SPFY` | VARCHAR |  | CAP synoptic form item: Specify lymph node sampling. |
| 21 | `METASTASIS_SPECIFY` | VARCHAR |  | CAP synoptic form item: Metastasis Specify. |
| 22 | `TUMOR_OVARY_RIGHT_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor Size Right Ovary. |
| 23 | `TUMOR_OVARY_RI_GR` | NUMERIC |  | CAP synoptic form item: Tumor Size Right Ovary Greatest. |
| 24 | `TUMOR_OVARY_RI_GR2` | NUMERIC |  | CAP synoptic form item: Tumor Size Right Ovary Greatest 2. |
| 25 | `TUMOR_OVARY_GR_ADD` | NUMERIC |  | CAP synoptic form item: Tumor Size Right Ovary Additional Dimension. |
| 26 | `TUMOR_OVARY_GR_SPEC` | VARCHAR |  | CAP synoptic form item: Tumor Size Right Ovary Specify. |
| 27 | `TUMOR_OVARY_LEFT_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor Size Left Ovary. |
| 28 | `TUMOR_OVARY_LF_GR` | NUMERIC |  | CAP synoptic form item: Tumor Size Left Ovary Greatest. |
| 29 | `TUMOR_OVARY_LF_GR2` | NUMERIC |  | CAP synoptic form item: Tumor Size Left Ovary Greatest 2. |
| 30 | `TUMOR_OVARY_LF_ADD` | NUMERIC |  | CAP synoptic form item: Tumor Size Left Ovary Additional Dimension. |
| 31 | `TUMOR_OVARY_LF_SPEC` | VARCHAR |  | CAP synoptic form item: Tumor Size Left Ovary Specify. |
| 32 | `HIS_TYP_MAL_MESO_SP` | VARCHAR |  | CAP synoptic form item: Histologic Type Malignant mesothelioma Specify. |
| 33 | `HIS_TYP_MAL_MULL_SP` | VARCHAR |  | CAP synoptic form item: Histologic Type Other malignant tumor of Mullerian type specify. |
| 34 | `TUMOR_OTHER_SPEC1` | VARCHAR |  | CAP synoptic form item: Other Tumor Size Specify. |
| 35 | `TUMOR_OVARY_RI_SP2` | VARCHAR |  | CAP synoptic form item: Tumor Size Right Ovary Specify 2. |
| 36 | `TUMOR_OVARY_LF_SP2` | VARCHAR |  | CAP synoptic form item: Tumor Size Left Ovary Specify 2. |
| 37 | `TUMOR_OTHER_SPEC2` | VARCHAR |  | CAP synoptic form item: Other Tumor Size Specify 2. |
| 38 | `ANCLR_STD_SPEC` | VARCHAR |  | CAP synoptic form item: Specify details for ancillary studies. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

