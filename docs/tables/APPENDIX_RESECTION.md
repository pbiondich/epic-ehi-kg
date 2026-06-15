# APPENDIX_RESECTION

> Stores single response data for College of American Pathologists (CAP) form 76004-APPENDIX: RESECTION.

**Primary key:** `RESULT_ID`  
**Columns:** 39  
**Org-specific columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 3 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 4 | `SPEC_INTEGRITY_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Integrity. |
| 5 | `SPEC_INTEGRITY_SPFY` | VARCHAR |  | CAP synoptic form item: Specify specimen integrity. |
| 6 | `NUM_PIECE_FRAG_SPEC` | NUMERIC |  | CAP synoptic form item: Number of Pieces in Fragmented Specimens. |
| 7 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 8 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 9 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 10 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 11 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 12 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 13 | `TMR_PENETR_PERITONM` | VARCHAR |  | CAP synoptic form item: Tumor Penetrates to the Surface of Visceral Peritoneum. |
| 14 | `MARGIN_UNITS_C_NAME` | VARCHAR | org | CAP synoptic form item: Margin Units. |
| 15 | `PERINEURAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineural Invasion. |
| 16 | `ANC_STDIES_SPFY_TYP` | VARCHAR |  | CAP synoptic form item: Ancillary Studies Specify Types. |
| 17 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 18 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 19 | `REG_LN_NUM_EXM` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Examined. |
| 20 | `REG_LN_NUM_INV` | NUMERIC |  | CAP synoptic form item: Regional Lymph Nodes Number Involved. |
| 21 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 22 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 23 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastasis Sites. |
| 24 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 25 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 26 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 27 | `PROX_MRG_INV_CARC_C_NAME` | VARCHAR | org | CAP synoptic form item: Proximal Margin Involved With Carcinoma. |
| 28 | `PROX_MRG_INVAS_C_NAME` | VARCHAR | org | CAP synoptic form item: Proximal Margin Involvement. |
| 29 | `DISTAL_MRG_INVAS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distal Margin Invasive Carcinoma Involvement. |
| 30 | `MESENTERIC_MARGIN_C_NAME` | VARCHAR |  | CAP synoptic form item: Mesenteric Margin. |
| 31 | `CIRCUMFERENTL_MRG_C_NAME` | VARCHAR |  | CAP synoptic form item: Circumferential (Radial) Margin. |
| 32 | `SATELL_PERITMR_ND_C_NAME` | VARCHAR |  | CAP synoptic form item: Satellite Peritumoral Nodules. |
| 33 | `NUM_PERITUMORAL_ND` | NUMERIC |  | CAP synoptic form item: Specify Number of Peritumoral Nodules Identified. |
| 34 | `LENGTH_OF_APPENDIX` | NUMERIC |  | CAP synoptic form item: Length of Appendix. |
| 35 | `LENGTH_COLONIC_SEG` | NUMERIC |  | CAP synoptic form item: Length of Colonic Segment. |
| 36 | `DIRECTLY_INVADS_ADJ` | VARCHAR |  | CAP synoptic form item: Tumor directly invades other adjacent organs. |
| 37 | `GRADE_DYSPLSIA_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Grade of Dysplasia. |
| 38 | `CARC_TYP_CNNT_DETER` | VARCHAR |  | CAP synoptic form item: Specify why carcinoma type cannot be determined. |
| 39 | `INV_CARC_CLOSE_MRG` | NUMERIC |  | CAP synoptic form item: Invasive Carcinoma Distance from Closest Margin. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

