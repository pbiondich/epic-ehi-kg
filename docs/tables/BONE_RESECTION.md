# BONE_RESECTION

> Stores data for all fields in College of American Pathologists (CAP) form 76010-Bone: Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 32  
**Org-specific columns:** 8

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
| 9 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 10 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 11 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 12 | `TREAT_EFF_NECR_SPFY` | NUMERIC |  | CAP synoptic form item: Treatment Effect - Specify Necrotic Tumor. |
| 13 | `NECROSIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Necrosis. |
| 14 | `NECROSIS_EXTENT` | NUMERIC |  | CAP synoptic form item: Necrosis Extent. |
| 15 | `MITOTIC_RATE` | NUMERIC |  | CAP synoptic form item: Mitotic Rate. |
| 16 | `IMMUNOHISTOCHEM_C_NAME` | VARCHAR | org | CAP synoptic form item: Immunohistochemistry. |
| 17 | `IMMUNOHISTOCHM_SPFY` | VARCHAR |  | CAP synoptic form item: Specify immunohistochemistry. |
| 18 | `MOLECULAR_PATH_C_NAME` | VARCHAR |  | CAP synoptic form item: Molecular Pathology. |
| 19 | `MOLECULAR_PATH_SPFY` | VARCHAR |  | CAP synoptic form item: Specify molecular pathology. |
| 20 | `CYTOGENETICS_C_NAME` | VARCHAR |  | CAP synoptic form item: Cytogenetics. |
| 21 | `CYTOGENETICS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify cytogenetics. |
| 22 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 23 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 24 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastasis Sites. |
| 25 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 26 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 27 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 28 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 29 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 30 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 31 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 32 | `DIST_FROM_MARGIN` | NUMERIC |  | CAP synoptic form item: Distance From Closest Margin. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

