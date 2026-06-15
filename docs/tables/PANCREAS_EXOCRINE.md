# PANCREAS_EXOCRINE

> Stores single response data for College of American Pathologists (CAP) form 76039-PANCREAS: Exocrine.

**Primary key:** `RESULT_ID`  
**Columns:** 37  
**Org-specific columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 3 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 4 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 5 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 6 | `MRG_CANNOT_ASSES_YN` | VARCHAR |  | CAP synoptic form item: Margins Cannot Be Assessed. |
| 7 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 8 | `TREATMENT_EFFECT_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect. |
| 9 | `TREAT_EFF_PRES_C_NAME` | VARCHAR | org | CAP synoptic form item: Treatment Effect Present. |
| 10 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 11 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 12 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 13 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 14 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 15 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 16 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 17 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastatis Sites. |
| 18 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 19 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 20 | `SPEC_ADJ_VES_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Specimen Adjacent large vessels. |
| 21 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 22 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 23 | `MOLECULAR_PATH_SPFY` | VARCHAR |  | CAP synoptic form item: Specify molecular pathology. |
| 24 | `MRG_INV_CARCINOMA_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Invasive Carcinoma. |
| 25 | `INV_IMP_SITE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Invasive Implant Site. |
| 26 | `MRG_IVLV_TM_SPEC` | VARCHAR |  | CAP synoptic form item: Specify site for Margins Involved by Tumor. |
| 27 | `MAR_TMR_INV_PAN_YN` | VARCHAR |  | CAP synoptic form item: Tumor Involves posterior retroperitoneal surface of pancreas. |
| 28 | `HIST_TYPE_MUC_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Type - Mucinous Cystic Neoplasm. |
| 29 | `HIS_TYPE_IN_PAP_C_NAME` | VARCHAR | org | CAP synoptic form item: Intraductal Papillary-Mucinous Carcinoma. |
| 30 | `PANC_NEO_HIGH_GRADE` | VARCHAR |  | CAP synoptic form item: Pancreatic intraepithelial neoplasia Highest Grade. |
| 31 | `MARG_INV_DIST_CLOSE` | NUMERIC |  | CAP synoptic form item: Margins Invasive Distance of Invasive Carcinoma from Closest Margin. |
| 32 | `MG_IVLV_CCNM_ST_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Involvement by Carcinoma in situ. |
| 33 | `TMR_INV_PER_SFT_SFY` | VARCHAR |  | CAP synoptic form item: Specify tumor invades peripancreatic soft tissue. |
| 34 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 35 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 36 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 37 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

