# INTRAH_BILE_RESEC

> Stores single response data for College of American Pathologists (CAP) form 76006-INTRAHEPATIC BILE DUCTS: RESECTION.

**Primary key:** `RESULT_ID`  
**Columns:** 36  
**Org-specific columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 3 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 4 | `PART_HEPATECTOMY_C_NAME` | VARCHAR | org | CAP synoptic form item: Partial Hepatectomy. |
| 5 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 6 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 7 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 8 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 9 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 10 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 11 | `VENOUS_INVASION_C_NAME` | VARCHAR | org | CAP synoptic form item: Venous (Major Vessel) Invasion. |
| 12 | `SMALL_VESL_INVAS_C_NAME` | VARCHAR |  | CAP synoptic form item: Small Vessel Invasion. |
| 13 | `PERINEURAL_INVASN_C_NAME` | VARCHAR |  | CAP synoptic form item: Perineural Invasion. |
| 14 | `ANC_STDIES_SPFY_TYP` | VARCHAR |  | CAP synoptic form item: Ancillary Studies Specify Types. |
| 15 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 16 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 17 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 18 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 19 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 20 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 21 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastasis Sites. |
| 22 | `ADDL_PATH_FNDNG_SPF` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 23 | `CHRON_HEPATITS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify chronic hepatitis. |
| 24 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 25 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 26 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 27 | `OTHER_MARGIN_C_NAME` | VARCHAR | org | CAP synoptic form item: Other Margin. |
| 28 | `OTHER_MARGIN_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other margin. |
| 29 | `BILE_DUCT_MARGIN_C_NAME` | VARCHAR | org | CAP synoptic form item: Bile Duct Margin. |
| 30 | `BILE_DCT_UNN_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Bile Duct Uninvolved by Invasive Carcinoma. |
| 31 | `TUMOR_GROWTH_PAT_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor Growth Pattern. |
| 32 | `TMR_FOC_MULTIP_SPFY` | VARCHAR |  | CAP synoptic form item: Specify tumor focality: multiple. |
| 33 | `TMR_FOC_SOLITY_SPFY` | VARCHAR |  | CAP synoptic form item: Specify tumor focality: solitary. |
| 34 | `DIRECTLY_INVADS_ADJ` | VARCHAR |  | CAP synoptic form item: Tumor directly invades other adjacent organs. |
| 35 | `HEP_PARENCHY_MRG_C_NAME` | VARCHAR |  | CAP synoptic form item: Hepatic Parenchymal Margin. |
| 36 | `INV_CARC_CLOSE_MRG` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Distance from Closest Margin. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

