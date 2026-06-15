# BONE_MARROW_ASPIR

> Stores single response data for College of American Pathologists (CAP) form 76009-BONE MARROW: ASPIRATION.

**Primary key:** `RESULT_ID`  
**Columns:** 41  
**Org-specific columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 3 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 4 | `SPEC_PROC_ASPR_SPFY` | VARCHAR |  | CAP synoptic form item: Specimen Procedure Aspiration. |
| 5 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 6 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 7 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 8 | `SPEC_PROC_BIOP_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Specimen Procedure Biopsy. |
| 9 | `MYELOPRO_NPLSM_C_NAME` | VARCHAR | org | CAP synoptic form item: Myeloproliferative Neoplasms. |
| 10 | `MYELD_NPLSM_EOSIN_C_NAME` | VARCHAR | org | CAP synoptic form item: Myeloid and Lymphoid Neoplasms with Eosinophilia and Abnormalities of PDGFRA, PDGFRB, FGFR1. |
| 11 | `MASTOCYTOSS_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Mastocytosis. |
| 12 | `MYELD_MYELP_NPLSM_C_NAME` | VARCHAR | org | CAP synoptic form item: Myelodysplastic/Myeloproliferative Neoplasms. |
| 13 | `MYELODYPLSTC_SYND_C_NAME` | VARCHAR | org | CAP synoptic form item: Myelodysplastic Syndromes. |
| 14 | `AML_RECUR_GEN_ABN_C_NAME` | VARCHAR | org | CAP synoptic form item: Acute Myeloid Leukemia (AML) with Recurrent Genetic Abnormalities. |
| 15 | `THPY_MYELD_NPLSM_C_NAME` | VARCHAR | org | CAP synoptic form item: Therapy-related Myeloid Neoplasms. |
| 16 | `ACUTE_MYELD_NOS_C_NAME` | VARCHAR | org | CAP synoptic form item: Acute Myeloid Leukemia, Not Otherwise Specified (NOS). |
| 17 | `MYELD_PROLIF_DOWN_C_NAME` | VARCHAR | org | CAP synoptic form item: Myeloid Proliferations Related to Down Syndrome. |
| 18 | `ACUT_AMBIG_LINEAG_C_NAME` | VARCHAR | org | CAP synoptic form item: Acute Leukemias of Ambiguous Lineage. |
| 19 | `MXD_PHENO_ACUT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Mixed phenotype acute leukemia, NOS, rare types. |
| 20 | `PRECUR_LYM_NPLSM_C_NAME` | VARCHAR | org | CAP synoptic form item: Precursor Lymphoid Neoplasms. |
| 21 | `MATURE_B_NPLSM_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Mature B-cell Neoplasms. |
| 22 | `MATURE_B_NEOPLASM_C_NAME` | VARCHAR | org | CAP synoptic form item: Mature B-cell Neoplasms. |
| 23 | `MATURE_T_NK_NPLSM_C_NAME` | VARCHAR | org | CAP synoptic form item: Mature T- and NK-cell Neoplasms. |
| 24 | `HODGKIN_LYMPHOMA_C_NAME` | VARCHAR | org | CAP synoptic form item: Hodgkin Lymphoma. |
| 25 | `HISTIO_DEND_NPLSM_C_NAME` | VARCHAR | org | CAP synoptic form item: Histiocytic and Dendritic Cell Neoplasms. |
| 26 | `POSTTRANSPLT_PTLD_C_NAME` | VARCHAR | org | CAP synoptic form item: Post-transplant Lymphoproliferative Disorders (PTLD). |
| 27 | `MONOMRPHC_PTLD_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Monomorphic PTLD (B- and T / NK-cell types). |
| 28 | `CYTOGEN_RPT_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Cytogenetic Studies Report. |
| 29 | `IMM_PHENOTYPE_C_NAME` | VARCHAR | org | CAP synoptic form item: Immunophenotyping (flow cytometry and/or immunohistochemistry). |
| 30 | `IMM_PHENO_RSLT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Immunophenotyping Results. |
| 31 | `CYTOCHEMICAL_SS_C_NAME` | VARCHAR |  | CAP synoptic form item: Cytochemical/Special Stains. |
| 32 | `CYTOCHM_SS_RES_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Cytochemical/Special Stains Results. |
| 33 | `MOL_GENETIC_STUDY_C_NAME` | VARCHAR |  | CAP synoptic form item: Molecular Genetic Studies. |
| 34 | `MOL_GEN_STDY_RPT` | VARCHAR |  | CAP synoptic form item: Specify Molecular Genetic Studies Report. |
| 35 | `MOL_GEN_STDY_RES` | VARCHAR |  | CAP synoptic form item: Specify Molecular Genetic Studies Results. |
| 36 | `FLOUR_SITU_HYBRID_C_NAME` | VARCHAR |  | CAP synoptic form item: Fluorescence in Situ Hybridization. |
| 37 | `FLOUR_SITU_RPT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Fluorescence in Situ Hybridization Report. |
| 38 | `FLOUR_SITU_RES_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Fluorescence in Situ Hybridization Results. |
| 39 | `IMM_PHENO_RPT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Immunophenotyping Report. |
| 40 | `CYTOGENETICS_C_NAME` | VARCHAR |  | CAP synoptic form item: Cytogenetics. |
| 41 | `CYTOGENETICS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify cytogenetics. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

