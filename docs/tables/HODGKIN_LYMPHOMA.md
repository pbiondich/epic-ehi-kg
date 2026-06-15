# HODGKIN_LYMPHOMA

> Stores data for College of American Pathologists (CAP) form 76025-HODGKIN LYMPHOMA: Biopsy, Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 14  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `IPS_SPECIFY` | VARCHAR |  | CAP synoptic form item: International Prognostic Score (IPS) specify. |
| 3 | `PROGNSTC_FACT_SPFY` | VARCHAR |  | CAP synoptic form item: Clinical Prognostic Factors and Indices Specify. |
| 4 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 5 | `TUMOR_LYM_NODE_SITE` | VARCHAR |  | CAP synoptic form item: Tumor Site Lymph Nodes Site Specify. |
| 6 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 7 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 8 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 9 | `INVOLV_LYM_ND_REG` | VARCHAR |  | CAP synoptic form item: Involvement of a single lymph node region Specify. |
| 10 | `EXT_INVOLVEMNT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Extent Involvement. |
| 11 | `IMM_PHENOTYPE_C_NAME` | VARCHAR | org | CAP synoptic form item: Immunophenotyping (flow cytometry and/or immunohistochemistry). |
| 12 | `IMM_PHENO_RPT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Immunophenotyping Report. |
| 13 | `IMM_PHENO_RSLT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Immunophenotyping Results. |
| 14 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

