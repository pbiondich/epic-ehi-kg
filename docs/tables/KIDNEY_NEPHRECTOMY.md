# KIDNEY_NEPHRECTOMY

> Stores data for College of American Pathologists (CAP) form 76027-KIDNEY: Nephrectomy, Partial or Radical.

**Primary key:** `RESULT_ID`  
**Columns:** 28  
**Org-specific columns:** 6

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
| 11 | `MACRO_EXTENT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Macroscopic Extent. |
| 12 | `SARCOMATOID_FEAT_C_NAME` | VARCHAR | org | CAP synoptic form item: Sarcomatoid Features. |
| 13 | `PERCN_SARCOMAT_ELEM` | NUMERIC |  | CAP synoptic form item: Specify Percentage Sarcomatoid Element. |
| 14 | `FUHRMAN_NUCLR_GRD_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade (Fuhrman Nuclear Grade). |
| 15 | `FUHR_NUCLR_GRD_SPFY` | VARCHAR |  | CAP synoptic form item: Histologic Grade (Fuhrman Nuclear Grade) Specify. |
| 16 | `DIRECTLY_INVADS_ADJ` | VARCHAR |  | CAP synoptic form item: Tumor directly invades other adjacent organs. |
| 17 | `NECROSIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Necrosis. |
| 18 | `OTHER_TUMOR_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Other Tumors. |
| 19 | `CYSTS_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Cyst Type. |
| 20 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 21 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 22 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 23 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 24 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 25 | `GLOMERULAR_DIS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Glomerular disease. |
| 26 | `TUBULNTST_DIS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Tubulointerstitial disease. |
| 27 | `VASCULAR_DIS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Vascular disease. |
| 28 | `PATH_NON_KIDNY_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Pathologic Findings in Nonneoplastic Kidney. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

