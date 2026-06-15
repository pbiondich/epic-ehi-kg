# NEUROBLASTOMA

> Stores single response data for College of American Pathologists (CAP) form 76035-NEUROBLASTOMA: Resection, Biopsy.

**Primary key:** `RESULT_ID`  
**Columns:** 34  
**Org-specific columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 3 | `SPEC_LATERAL_SPFY` | VARCHAR |  | CAP synoptic form item: Other specimen laterality data. |
| 4 | `TUMOR_WEIGHT_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor Weight. |
| 5 | `TUMOR_WEIGHT_SPFY` | NUMERIC |  | CAP synoptic form item: Specify Tumor Weight. |
| 6 | `SPECIMEN_WEIGHT` | NUMERIC |  | CAP synoptic form item: Specimen Weight. |
| 7 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 8 | `SPEC_SIZE_GREATEST` | NUMERIC |  | CAP synoptic form item: Specimen Greatest Size. |
| 9 | `SPEC_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Specimen size additional dimension (length). |
| 10 | `SPEC_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Specimen size additional dimension (width). |
| 11 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 12 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 13 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 14 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 15 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 16 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 17 | `REG_LMPH_SITE_SPEC` | VARCHAR |  | CAP synoptic form item: Specify Regional Lymph Nodes Site. |
| 18 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 19 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 20 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 21 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastasis Sites. |
| 22 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 23 | `PATIENT_AGE_C_NAME` | VARCHAR | org | CAP synoptic form item: Patient Age. |
| 24 | `TREATMENT_HISTORY_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment History. |
| 25 | `HIST_TYP_GANGLNBL_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Type Ganglioneuroblastoma. |
| 26 | `NUM_NODULES_SPFY` | NUMERIC |  | CAP synoptic form item: Nodular Subtype - Specify Number of Nodules. |
| 27 | `DEG_DIFFERENTIAT_C_NAME` | VARCHAR | org | CAP synoptic form item: Degree of Differentiation (neuroblastic component). |
| 28 | `MITOTC_KARY_INDEX_C_NAME` | VARCHAR | org | CAP synoptic form item: Mitotic-Karyorrhectic Index (MKI). |
| 29 | `TMR_CALCIFICATION_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor Calcification. |
| 30 | `INPC_C_NAME` | VARCHAR | org | CAP synoptic form item: International Neuroblastoma Pathology Classification (INPC). |
| 31 | `INSS_C_NAME` | VARCHAR | org | CAP synoptic form item: International Neuroblastoma Staging System (INSS). |
| 32 | `MYCN_AMPLIF_STATS_C_NAME` | VARCHAR | org | CAP synoptic form item: MYCN Amplification Status. |
| 33 | `DIST_META_NON_PM_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis (non-pM). |
| 34 | `REG_LYM_ND_NON_PN_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (Non pN version). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

