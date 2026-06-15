# PLEURA_RESECTION

> Stores single response data for College of American Pathologists (CAP) form 76032-PLEURA: Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 29  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 3 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 4 | `SPEC_INTEGRITY_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Integrity. |
| 5 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 6 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 7 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 8 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 9 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 10 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 11 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 12 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 13 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 14 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 15 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 16 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 17 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 18 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 19 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastatis Sites. |
| 20 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 21 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 22 | `TMR_EXTENSION_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Extension. |
| 23 | `INFLAMMATION_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Inflammation. |
| 24 | `TMR_EXT_MEDIASTINAL` | VARCHAR |  | CAP synoptic form item: Specify Tumor Extension Mediastinal organs. |
| 25 | `HISTOCHM_STAIN_RSLT` | VARCHAR |  | CAP synoptic form item: Specify Histochemical Stain Results. |
| 26 | `ELECTRON_MICROSC_RS` | VARCHAR |  | CAP synoptic form item: Specify Electron Microscopy Results. |
| 27 | `IMMUNO_STAINS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Immunohistochemical Stains. |
| 28 | `ANCLR_STD_SPEC` | VARCHAR |  | CAP synoptic form item: Specify details for ancillary studies. |
| 29 | `REG_LMPH_NUM_CBT_YN` | VARCHAR |  | CAP synoptic form item: Regional Lymph Nodes Number Cannot be Determined. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

