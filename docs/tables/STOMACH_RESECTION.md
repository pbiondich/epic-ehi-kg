# STOMACH_RESECTION

> Stores data for College of American Pathologists (CAP) form 76052-STOMACH: Local Resection, Gastrectomy.

**Primary key:** `RESULT_ID`  
**Columns:** 36  
**Org-specific columns:** 12

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
| 10 | `DIST_FROM_MARGIN` | NUMERIC |  | CAP synoptic form item: Distance From Closest Margin. |
| 11 | `ALL_MRG_UNIN_CAR_YN` | VARCHAR |  | CAP synoptic form item: All Margins Uninvolved By Invasive Carcinoma. |
| 12 | `SPFY_MARGIN_CATEG_C_NAME` | VARCHAR | org | CAP synoptic form item: Specify Margin Category. |
| 13 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 14 | `TREAT_EFF_PRES_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect Present. |
| 15 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 16 | `ANC_STDIES_SPFY_TYP` | VARCHAR |  | CAP synoptic form item: Ancillary Studies Specify Types. |
| 17 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 18 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 19 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 20 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 21 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 22 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastatis Sites. |
| 23 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 24 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 25 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 26 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 27 | `PROX_MRG_INVAS_C_NAME` | VARCHAR | org | CAP synoptic form item: Proximal Margin Involvement. |
| 28 | `DISTAL_MRG_INVAS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distal Margin Invasive Carcinoma Involvement. |
| 29 | `DIST_MRG_INV_SITU_C_NAME` | VARCHAR | org | CAP synoptic form item: Distal Margin Involvement by Carcinoma in Situ / Adenoma. |
| 30 | `OTHER_MARGIN_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other margin. |
| 31 | `ADDL_PATH_GASTRITIS` | VARCHAR |  | CAP synoptic form item: Specify Additional Pathologic Findings - Gastritis. |
| 32 | `SPEC_PROC_PART_GAST` | VARCHAR |  | CAP synoptic form item: Specify Specimen Procedure Partial Gastrectomy. |
| 33 | `TMR_ADJACENT_STRUCT` | VARCHAR |  | CAP synoptic form item: Tumor directly invades adjacent structures. |
| 34 | `ADDT_PATH_FIND_POLY` | VARCHAR |  | CAP synoptic form item: Additional Pathologic Findings Other Polyps Specify. |
| 35 | `CLIN_HIST_PREV_GAST` | VARCHAR |  | CAP synoptic form item: Specify Clinical History - Previous Gastric Surgery. |
| 36 | `PROX_MARG_IN_SITU_C_NAME` | VARCHAR | org | CAP synoptic form item: Proximal Margin Carcinoma In Situ Involvement. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

