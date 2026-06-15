# NON_HODGKIN_LYMPH

> Stores single response data for College of American Pathologists (CAP) form 76036-NON-HODGKIN LYMPHOMA/LYMPHOID NEOPLASMS: Biopsy, Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 29  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `PROGNSTC_FACT_SPFY` | VARCHAR |  | CAP synoptic form item: Clinical Prognostic Factors and Indices Specify. |
| 3 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 4 | `TUMOR_LYM_NODE_SITE` | VARCHAR |  | CAP synoptic form item: Tumor Site Lymph Nodes Site Specify. |
| 5 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 6 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 7 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 8 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 9 | `CYTOGENETICS_C_NAME` | VARCHAR | org | CAP synoptic form item: Cytogenetics. |
| 10 | `CYTOGENETICS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify cytogenetics. |
| 11 | `CYTOGEN_RPT_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Cytogenetic Studies Report. |
| 12 | `IMM_PHENOTYPE_C_NAME` | VARCHAR |  | CAP synoptic form item: Immunophenotyping (flow cytometry and/or immunohistochemistry). |
| 13 | `IMM_PHENO_RPT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Immunophenotyping Report. |
| 14 | `IMM_PHENO_RSLT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Immunophenotyping Results. |
| 15 | `PRECUR_LYM_NPLSM_C_NAME` | VARCHAR | org | CAP synoptic form item: Precursor Lymphoid Neoplasms. |
| 16 | `MATURE_B_NEOPLASM_C_NAME` | VARCHAR | org | CAP synoptic form item: Mature B-cell Neoplasms. |
| 17 | `MATURE_T_NK_NPLSM_C_NAME` | VARCHAR | org | CAP synoptic form item: Mature T- and NK-cell Neoplasms. |
| 18 | `HISTIO_DEND_NPLSM_C_NAME` | VARCHAR | org | CAP synoptic form item: Histiocytic and Dendritic Cell Neoplasms. |
| 19 | `MONOMRPHC_PTLD_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Monomorphic PTLD (B- and T / NK-cell types). |
| 20 | `POSTTRANSPLT_PTLD_C_NAME` | VARCHAR | org | CAP synoptic form item: Post-transplant Lymphoproliferative Disorders (PTLD). |
| 21 | `MOL_GENETIC_STUDY_C_NAME` | VARCHAR |  | CAP synoptic form item: Molecular Genetic Studies. |
| 22 | `MOL_GEN_STDY_RPT` | VARCHAR |  | CAP synoptic form item: Specify Molecular Genetic Studies Report. |
| 23 | `MOL_GEN_STDY_RES` | VARCHAR |  | CAP synoptic form item: Specify Molecular Genetic Studies Results. |
| 24 | `INVOLV_LYM_ND_REG` | VARCHAR |  | CAP synoptic form item: Involvement of a single lymph node region Specify. |
| 25 | `EXT_INVOLVEMNT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Extent Involvement. |
| 26 | `FLIPI_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Follicular Lymphoma International Prognostic Index (FLIPI). |
| 27 | `MATURE_B_NPLSM_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Mature B-cell Neoplasms. |
| 28 | `MATR_T_NK_CELL_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Mature T- and NK-cell Neoplasms. |
| 29 | `IPI_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify International Prognostic Index (IPI). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

