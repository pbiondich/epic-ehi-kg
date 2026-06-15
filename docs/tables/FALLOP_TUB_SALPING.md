# FALLOP_TUB_SALPING

> Stores data for College of American Pathologists (CAP) form 76020-FALLOPIAN TUBE: Unilateral Salpingectomy, Salpingo-oophorectomy, or Hysterectomy with Salpingo-oophorectomy.

**Primary key:** `RESULT_ID`  
**Columns:** 43  
**Org-specific columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 3 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 4 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 5 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 6 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 7 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 8 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 9 | `MICRO_TMR_EXT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Microscopic Tumor Extension. |
| 10 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 11 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 12 | `RIGHT_TUBE_OVARY_C_NAME` | VARCHAR | org | CAP synoptic form item: Right Fallopian Tube Relationship to Ovary. |
| 13 | `LEFT_TUBE_OVARY_C_NAME` | VARCHAR |  | CAP synoptic form item: Left Fallopian Tube Relationship to Ovary. |
| 14 | `LEFT_TUBE_FIMBRI_C_NAME` | VARCHAR | org | CAP synoptic form item: Left Fallopian Tube Status of Fimbriated End. |
| 15 | `RIGHT_SPEC_INTEG_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Integrity Right. |
| 16 | `RGT_SPEC_INTEG_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Specimen Integrity Right. |
| 17 | `LEFT_SPEC_INTEG_C_NAME` | VARCHAR |  | CAP synoptic form item: Specimen Integrity Left. |
| 18 | `LFT_SPEC_INTEG_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Specimen Integrity Left. |
| 19 | `RIGHT_TUBE_FIMBRI_C_NAME` | VARCHAR |  | CAP synoptic form item: Right Fallopian Tube Status of Fimbriated End. |
| 20 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 21 | `P53_IMMUNOSTAIN_C_NAME` | VARCHAR | org | CAP synoptic form item: P53 Immunostaining. |
| 22 | `SPECIAL_STD_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Special Studies. |
| 23 | `COMN_ILIAC_NUM_EXAM` | NUMERIC |  | CAP synoptic form item: Common Iliac Number Examined. |
| 24 | `COMN_ILIAC_NUM_POS` | NUMERIC |  | CAP synoptic form item: Common Iliac Number Positive. |
| 25 | `EXTN_ILIAC_NUM_EXAM` | NUMERIC |  | CAP synoptic form item: External Iliac Number Examined. |
| 26 | `EXTN_ILIAC_NUM_POS` | NUMERIC |  | CAP synoptic form item: External Iliac Number Positive. |
| 27 | `INTN_ILIAC_NUM_EXAM` | NUMERIC |  | CAP synoptic form item: Internal Iliac (hypergastric) Number Examined. |
| 28 | `INTN_ILIAC_NUM_POS` | NUMERIC |  | CAP synoptic form item: Internal Iliac (hypergastric) Number Positive. |
| 29 | `OBTURATOR_NUM_EXAM` | NUMERIC |  | CAP synoptic form item: Obturator Number Examined. |
| 30 | `OBTURATOR_NUM_POS` | NUMERIC |  | CAP synoptic form item: Obturator Number Positive. |
| 31 | `PARA_AORTC_NUM_EXAM` | NUMERIC |  | CAP synoptic form item: Para-aortic Number Examined. |
| 32 | `PARA_AORTC_NUM_POS` | NUMERIC |  | CAP synoptic form item: Para-aortic Number Positive. |
| 33 | `PELVIC_ND_NUM_EXAM` | NUMERIC |  | CAP synoptic form item: Pelvic Nodes, Not otherwise specified (NOS) Number Examined. |
| 34 | `PELVIC_NODE_NUM_POS` | NUMERIC |  | CAP synoptic form item: Pelvic Nodes, Not otherwise specified (NOS) Number Positive. |
| 35 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 36 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 37 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 38 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 39 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 40 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastasis Sites. |
| 41 | `SALPRINGITIS_SPFY` | VARCHAR |  | CAP synoptic form item: Salpingitis Specify. |
| 42 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 43 | `TUBAL_INTRA_CARCINM` | VARCHAR |  | CAP synoptic form item: Specify Tubal intraepithelial carcinoma. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

