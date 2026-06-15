# TESTIS_RETRO_LYMPH

> Stores data for College of American Pathologists (CAP) form 76054-TESTIS: Retroperitoneal Lymphadenectomy.

**Primary key:** `RESULT_ID`  
**Columns:** 18  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 3 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 4 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 5 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 6 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 7 | `HIS_TYP_GERM_COMPS` | VARCHAR |  | CAP synoptic form item: Histologic Type - Specify Mixed Germ Cell Tumor Components and Approximate Percentages. |
| 8 | `HIST_TYPE_TERATOMA` | VARCHAR |  | CAP synoptic form item: Histologic Type - Specify Teratoma with a Secondary Somatic-type Malignant Component. |
| 9 | `HIST_TYP_MONOD_OTH` | VARCHAR |  | CAP synoptic form item: Histologic Type - Specify Monodermal Teratoma Other. |
| 10 | `HIST_TP_SQUA_CCNM_S` | VARCHAR |  | CAP synoptic form item: Specify details for Histologic Type Squamous cell carcinoma. |
| 11 | `SZ_LRGST_METAS_DEP` | NUMERIC |  | CAP synoptic form item: Size of Largest Metastatic Deposit. |
| 12 | `PRELYMPH_TREATMNT_C_NAME` | VARCHAR | org | CAP synoptic form item: Prelymphadenectomy Treatment. |
| 13 | `NUM_NODAL_GROUPS_C_NAME` | VARCHAR | org | CAP synoptic form item: Number of Nodal Groups Present. |
| 14 | `NUM_NOD_GRP_PRESENT` | NUMERIC |  | CAP synoptic form item: Specify the Number of Nodal Groups Present. |
| 15 | `SIZE_META_DEP_ADD_1` | NUMERIC |  | CAP synoptic form item: Size of Largest Metastatic Deposit (additional measurement 1). |
| 16 | `SIZE_META_DEP_ADD_2` | NUMERIC |  | CAP synoptic form item: Size of Largest Metastatic Deposit (additional measurement 2). |
| 17 | `HIST_VIABILITY_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Viability of Tumor. |
| 18 | `NON_REG_LYM_META_C_NAME` | VARCHAR | org | CAP synoptic form item: Nonregional Lymph Node Metastasis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

