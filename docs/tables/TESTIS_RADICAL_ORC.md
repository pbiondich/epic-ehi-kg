# TESTIS_RADICAL_ORC

> Stores data for College of American Pathologists (CAP) form 76053-TESTIS: Radical Orchiectomy.

**Primary key:** `RESULT_ID`  
**Columns:** 26  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 3 | `DIM_ADD_TMR_NODULE` | NUMERIC |  | CAP synoptic form item: Greatest Dimension of Additional Tumor Nodule. |
| 4 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 5 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 6 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 7 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 8 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 9 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 10 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 11 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 12 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastatis Sites. |
| 13 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 14 | `SPERMATIC_MARGIN_C_NAME` | VARCHAR | org | CAP synoptic form item: Spermatic Cord Margin. |
| 15 | `OTHER_MARGIN_C_NAME` | VARCHAR |  | CAP synoptic form item: Other Margin. |
| 16 | `OTHER_MARGIN_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other margin. |
| 17 | `HIS_TYP_GERM_COMPS` | VARCHAR |  | CAP synoptic form item: Histologic Type - Specify Mixed Germ Cell Tumor Components and Approximate Percentages. |
| 18 | `HIST_TYPE_TERATOMA` | VARCHAR |  | CAP synoptic form item: Histologic Type - Specify Teratoma with a Secondary Somatic-type Malignant Component. |
| 19 | `HIST_TYP_MONOD_OTH` | VARCHAR |  | CAP synoptic form item: Histologic Type - Specify Monodermal Teratoma Other. |
| 20 | `HIS_TYP_SEX_CRD_OTH` | VARCHAR |  | CAP synoptic form item: Histologic Type - Specify Mixed Germ Cell-Sex Cord-Stromal Tumor, Others. |
| 21 | `HIS_TYP_TEST_SCAR_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Type Testicular Scar. |
| 22 | `HIST_TP_SQUA_CCNM_S` | VARCHAR |  | CAP synoptic form item: Specify details for Histologic Type Squamous cell carcinoma. |
| 23 | `MACRO_EXTENT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Macroscopic Extent. |
| 24 | `SERUM_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Serum Tumor Markers Grade. |
| 25 | `HIS_TYP_SX_CRD_STRM` | VARCHAR |  | CAP synoptic form item: Histologic Type Sex Cord-Stromal Tumor. |
| 26 | `TUMOR_SIZE_INDETER` | VARCHAR |  | CAP synoptic form item: Specify Reason Why Tumor Size Is Indeterminate. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

