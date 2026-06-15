# ESOPHAGUS_RESEC

> Stores data for College of American Pathologists (CAP) form 76017-ESOPHAGUS: Endoscopic Resection, Esophagectomy, or Esophagogastrectomy (Note A).

**Primary key:** `RESULT_ID`  
**Columns:** 44  
**Org-specific columns:** 14

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
| 11 | `ALL_MRG_UNIN_CAR_YN` | VARCHAR |  | CAP synoptic form item: All Margins Uninvolved By Invasive Carcinoma. |
| 12 | `SPFY_MARGIN_CATEG_C_NAME` | VARCHAR | org | CAP synoptic form item: Specify Margin Category. |
| 13 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 14 | `TREAT_EFF_PRES_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect Present. |
| 15 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 16 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 17 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 18 | `RELTNSHP_TMR_JNCT_C_NAME` | VARCHAR | org | CAP synoptic form item: Relationship of Tumor to Esophagogastric Junction. |
| 19 | `DST_ESOPG_JNCT_SPFY` | NUMERIC |  | CAP synoptic form item: Specify Distance of Tumor Center from Esophagogastric Junction. |
| 20 | `TMR_ST_MIDESOPHGS_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor Site - Midesophagus. |
| 21 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 22 | `MICRO_TMR_EXT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Microscopic Tumor Extension. |
| 23 | `PROX_MRG_CNNT_BE_YN` | VARCHAR |  | CAP synoptic form item: Proximal Margin Cannot Be Assessed. |
| 24 | `PROX_MRG_INVAS_C_NAME` | VARCHAR | org | CAP synoptic form item: Proximal Margin Involvement. |
| 25 | `PROX_DYSPLAS_INVL_C_NAME` | VARCHAR | org | CAP synoptic form item: Proximal Margin Dysplasia Involvement. |
| 26 | `PROX_INTESTN_MET_YN` | VARCHAR |  | CAP synoptic form item: Proximal Margin Involved by intestinal metaplasia (Barretts esophagus) without dysplasia. |
| 27 | `CIRCUMF_DEEP_MRG_C_NAME` | VARCHAR |  | CAP synoptic form item: Circumferential (Adventitial) Margin (esophagectomy or esophagogastrectomy specimens) or Deep Margin (endoscopic resection specimens). |
| 28 | `DIST_MRG_CNNT_BE_YN` | VARCHAR |  | CAP synoptic form item: Distal Margin Cannot Be Assessed. |
| 29 | `DIST_DYSPLAS_INVL_C_NAME` | VARCHAR |  | CAP synoptic form item: Distal Margin Dysplasia Involvement. |
| 30 | `DISTAL_MRG_INVAS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distal Margin Invasive Carcinoma Involvement. |
| 31 | `DIST_INTESTN_MET_YN` | VARCHAR |  | CAP synoptic form item: Distal Margin Involved by intestinal metaplasia (Barretts esophagus) without dysplasia. |
| 32 | `INV_CARC_CLOSE_MRG` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Distance from Closest Margin. |
| 33 | `ANC_STDIES_SPFY_TYP` | VARCHAR |  | CAP synoptic form item: Ancillary Studies Specify Types. |
| 34 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 35 | `PT_INVAD_ADJ_STRUT` | VARCHAR |  | CAP synoptic form item: Specify Primary Tumor - Invades Adjacent Structures. |
| 36 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 37 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 38 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 39 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 40 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastasis Sites. |
| 41 | `ADDL_PATH_DYSPLAS_C_NAME` | VARCHAR | org | CAP synoptic form item: Additional Pathologic Findings - Dysplasia. |
| 42 | `ADDL_PATH_GASTRITIS` | VARCHAR |  | CAP synoptic form item: Specify Additional Pathologic Findings - Gastritis. |
| 43 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 44 | `ADDL_PATH_ESOPHAGIT` | VARCHAR |  | CAP synoptic form item: Specify Additional Pathologic Findings - Esophagitis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

