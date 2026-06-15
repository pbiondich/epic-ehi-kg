# BONE_BIOPSY

> Stores single response data for College of American Pathologists (CAP) form 76008-BONE: BIOPSY.

**Primary key:** `RESULT_ID`  
**Columns:** 23  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `RADIOGRAP_FIND_C_NAME` | VARCHAR | org | CAP synoptic form item: Radiographic Findings. |
| 3 | `RADIOGRAP_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify radiographic findings. |
| 4 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 5 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 6 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 7 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 8 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 9 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 10 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 11 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 12 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 13 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 14 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 15 | `NECROSIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Necrosis. |
| 16 | `NECROSIS_EXTENT` | NUMERIC |  | CAP synoptic form item: Necrosis Extent. |
| 17 | `IMMUNOHISTOCHEM_C_NAME` | VARCHAR | org | CAP synoptic form item: Immunohistochemistry. |
| 18 | `IMMUNOHISTOCHM_SPFY` | VARCHAR |  | CAP synoptic form item: Specify immunohistochemistry. |
| 19 | `CYTOGENETICS_C_NAME` | VARCHAR |  | CAP synoptic form item: Cytogenetics. |
| 20 | `CYTOGENETICS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify cytogenetics. |
| 21 | `MOLECULAR_PATH_C_NAME` | VARCHAR |  | CAP synoptic form item: Molecular Pathology. |
| 22 | `MOLECULAR_PATH_SPFY` | VARCHAR |  | CAP synoptic form item: Specify molecular pathology. |
| 23 | `MITOTIC_RATE` | NUMERIC |  | CAP synoptic form item: Mitotic Rate. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

