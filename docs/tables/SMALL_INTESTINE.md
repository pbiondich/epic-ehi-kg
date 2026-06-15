# SMALL_INTESTINE

> Stores data for College of American Pathologists (CAP) form 76048-SMALL INTESTINE: Segmental Resection, Pancreaticoduodenectomy (Whipple Resection).

**Primary key:** `RESULT_ID`  
**Columns:** 55  
**Org-specific columns:** 16

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
| 10 | `MACRO_TMR_PERFRTN_C_NAME` | VARCHAR | org | CAP synoptic form item: Macroscopic Tumor Perforation. |
| 11 | `TMR_PENETR_PERITONM` | VARCHAR |  | CAP synoptic form item: Tumor Penetrates to the Surface of Visceral Peritoneum. |
| 12 | `SPECIAL_STD_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Special Studies. |
| 13 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 14 | `REG_LN_NUM_EXM` | INTEGER |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 15 | `REG_LN_NUM_INV` | INTEGER |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 16 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 17 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 18 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastatis Sites. |
| 19 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 20 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 21 | `POLYPOSIS_SYND_SPEC` | VARCHAR |  | CAP synoptic form item: Clinical History Other Polyposis Syndrome Specify. |
| 22 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 23 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 24 | `PROX_MRG_CNNT_BE_YN` | VARCHAR |  | CAP synoptic form item: Proximal Margin Cannot Be Assessed. |
| 25 | `PROX_MRG_INVAS_C_NAME` | VARCHAR | org | CAP synoptic form item: Proximal Margin Involvement. |
| 26 | `PROX_MRG_INT_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Proximal Margin Involvement by Carcinoma / Adenoma. |
| 27 | `DIST_MRG_CNNT_BE_YN` | VARCHAR |  | CAP synoptic form item: Distal Margin Cannot Be Assessed. |
| 28 | `DISTAL_MRG_INVAS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distal Margin Invasive Carcinoma Involvement. |
| 29 | `DIST_MRG_INT_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Distal Margin Intramucosal Carcinoma - Adenoma. |
| 30 | `BILE_DUCT_MARGIN_C_NAME` | VARCHAR |  | CAP synoptic form item: Bile Duct Margin. |
| 31 | `CIRCUMFERENTL_MRG_C_NAME` | VARCHAR |  | CAP synoptic form item: Circumferential (Radial) Margin. |
| 32 | `PANCREATIC_MARGIN_C_NAME` | VARCHAR | org | CAP synoptic form item: Pancreatic Margin. |
| 33 | `MICRO_INSTBLTY_MTHD` | VARCHAR |  | CAP synoptic form item: Microsatellite Instability Testing Method. |
| 34 | `SPECIAL_STDS_MLH1_C_NAME` | VARCHAR | org | CAP synoptic form item: Special Studies MLH1. |
| 35 | `SPECL_STD_MLH1_SPFY` | VARCHAR |  | CAP synoptic form item: Special Studies MLH1 Specify. |
| 36 | `SPECIAL_STDS_MSH2_C_NAME` | VARCHAR |  | CAP synoptic form item: Special Studies MLH2. |
| 37 | `SPECL_STD_MSH2_SPFY` | VARCHAR |  | CAP synoptic form item: Special Studies MLH2 Specify. |
| 38 | `SPECIAL_STDS_MSH6_C_NAME` | VARCHAR |  | CAP synoptic form item: Special Studies MSH6. |
| 39 | `SPECL_STD_MSH6_SPFY` | VARCHAR |  | CAP synoptic form item: Special Studies PMS2. |
| 40 | `SPECIAL_STDS_PMS2_C_NAME` | VARCHAR |  | CAP synoptic form item: Special Studies PMS2. |
| 41 | `SPECL_STD_PMS2_SPFY` | VARCHAR |  | CAP synoptic form item: Special Studies PMS2 Specify. |
| 42 | `TMR_INTEST_DUO_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumor Site Small Intestine, Other than Duodenum. |
| 43 | `SEG_MARGIN_CARCI_YN` | VARCHAR |  | CAP synoptic form item: Segmental Resection or Pancreaticoduodenectomy (Whipple) Margins Uninvolved by Invasive Carcinoma. |
| 44 | `SEG_DIST_CARCINOMA` | NUMERIC |  | CAP synoptic form item: Segmental Resection or Pancreaticoduodenectomy (Whipple) Distance of Invasive Carcinoma from Closest Margin. |
| 45 | `SEGMENTAL_UNITS_C_NAME` | VARCHAR | org | CAP synoptic form item: Segmental Resection or Pancreaticoduodenectomy (Whipple) Specify Units. |
| 46 | `SEGMENT_MARGINS_C_NAME` | VARCHAR | org | CAP synoptic form item: Segmental Resection or Pancreaticoduodenectomy (Whipple) Specify Margin. |
| 47 | `SEG_OTHER_MARGIN_SP` | VARCHAR |  | CAP synoptic form item: Segmental Resection or Pancreaticoduodenectomy (Whipple) Other Margin Specify. |
| 48 | `PAN_MARGIN_CARCI_YN` | VARCHAR |  | CAP synoptic form item: Pancreaticoduodenectomy (Whipple) Margins Uninvolved by Invasive Carcinoma. |
| 49 | `PAN_DIST_CARCINOMA` | NUMERIC |  | CAP synoptic form item: Pancreaticoduodenectomy (Whipple) Distance of Invasive Carcinoma from Closest Margin. |
| 50 | `PANCREATIC_UNITS_C_NAME` | VARCHAR | org | CAP synoptic form item: Pancreaticoduodenectomy (Whipple) Specify Units. |
| 51 | `PANCREATI_MARGINS_C_NAME` | VARCHAR | org | CAP synoptic form item: Pancreaticoduodenectomy (Whipple) Specify Margin. |
| 52 | `PAN_OTHER_MARGIN_SP` | VARCHAR |  | CAP synoptic form item: Pancreaticoduodenectomy (Whipple) Other Margin Specify. |
| 53 | `TMR_ADJACENT_STRUCT` | VARCHAR |  | CAP synoptic form item: Tumor directly invades adjacent structures. |
| 54 | `ADDT_PATH_FIND_POLY` | VARCHAR |  | CAP synoptic form item: Additional Pathologic Findings Other Polyps Specify. |
| 55 | `SPEC_OTHER_ORGAN_SP` | VARCHAR |  | CAP synoptic form item: Specimen Other Organs Received Specify. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

