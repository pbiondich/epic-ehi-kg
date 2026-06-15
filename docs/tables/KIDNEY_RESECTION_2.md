# KIDNEY_RESECTION_2

> Stores single response data for College of American Pathologists (CAP) form 76069-Kidney: Resection for Pediatric Renal Tumor - Second.

**Overflow of:** [KIDNEY_RESECTION](KIDNEY_RESECTION.md)  
**Primary key:** `RESULT_ID`  
**Columns:** 33  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `SPEC_PROC_SPECIFY_2` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 3 | `SPEC_SZ_KDN_DMSN1_2` | NUMERIC |  | CAP synoptic form item: Specify kidney dimension 1 for specimen size. |
| 4 | `SPEC_SZ_KDN_DMSN2_2` | NUMERIC |  | CAP synoptic form item: Specify kidney dimension 2 for specimen size. |
| 5 | `SPEC_SZ_KDN_DMSN3_2` | NUMERIC |  | CAP synoptic form item: Specify kidney dimension 3 for specimen size. |
| 6 | `SPEC_SZ_WT_2` | NUMERIC |  | CAP synoptic form item: Specify weight for specimen size. |
| 7 | `TM_FCLT_MFCL_NUM_2` | NUMERIC |  | CAP synoptic form item: Specify the number of tumors in specimen for Tumor Focality Multifocal. |
| 8 | `TUMOR_SITE_SPEC_2` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 9 | `TUMOR_SIZE_GREAT_2` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 10 | `TUMOR_SIZE_ADDL_2` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 11 | `TUMOR_SIZE_ADDL2_2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 12 | `TUMOR_SIZE_IND_SP_2` | VARCHAR |  | CAP synoptic form item: Specify Reason Why Tumor Size Is Indeterminate. |
| 13 | `TM_SZ_GD_GRT_DMS2_2` | NUMERIC |  | CAP synoptic form item: Specify Greatest dimension tumor 2 for Tumor Size. |
| 14 | `TM_SZ_GD_GRT_DMS3_2` | NUMERIC |  | CAP synoptic form item: Specify Greatest dimension tumor 3 for Tumor Size. |
| 15 | `TS_MGD_SP_2` | VARCHAR |  | CAP synoptic form item: Specify details for greatest dimension of multiple tumor size. |
| 16 | `GEROTA_FASCIA_2_C_NAME` | VARCHAR | org | CAP synoptic form item: Gerotas Fascia. |
| 17 | `RENAL_VEIN_2_C_NAME` | VARCHAR | org | CAP synoptic form item: Renal Vein. |
| 18 | `TM_XTN_AO_PRS_SPC_2` | VARCHAR |  | CAP synoptic form item: Specify organ when Tumor extension into adjacent organ present. |
| 19 | `DSTC_TM_FRM_MG_IV_2` | NUMERIC |  | CAP synoptic form item: Specify Distance of Tumor from Closest Margin when Margin involvement by tumor not identified. |
| 20 | `MG_IVLV_NI_UNIT_2_C_NAME` | VARCHAR | org | CAP synoptic form item: Specify unit when Margin involvement by tumor not identified. |
| 21 | `MG_IVLV_NI_MS_2_C_NAME` | VARCHAR | org | CAP synoptic form item: Specify Margin when Margin involvement by tumor not identified. |
| 22 | `MG_IVLV_TM_NI_OTH_2` | VARCHAR |  | CAP synoptic form item: Specify other details for Margin involvement by tumor not identified. |
| 23 | `MRG_IVLV_TM_OTHER_2` | VARCHAR |  | CAP synoptic form item: Specify other details when Margin involved by tumor. |
| 24 | `NEPHRC_REST_2_C_NAME` | VARCHAR | org | CAP synoptic form item: Nephrogenic Rests. |
| 25 | `RLNM_PRSNT_SITE_2` | VARCHAR |  | CAP synoptic form item: Specify site for Regional lymph node metastasis present. |
| 26 | `LYMPH_ND_NUM_XMD_2` | INTEGER |  | CAP synoptic form item: Specify the number of lymph nodes examined. |
| 27 | `LYM_ND_NUM_IVLV_2` | INTEGER |  | CAP synoptic form item: Specify number of lymph nodes involved. |
| 28 | `DSTNC_MTSS_PRT_ST_2` | VARCHAR |  | CAP synoptic form item: Specify Site for Distant metastasis present. |
| 29 | `S5_BRID_RT_KD_2_C_NAME` | VARCHAR | org | CAP synoptic form item: Stage V Bilateral renal involvement at diagnosis Specify Right Kidney Stage. |
| 30 | `S5_BRID_LT_KD_2_C_NAME` | VARCHAR |  | CAP synoptic form item: Stage V Bilateral renal involvement at diagnosis Specify Left Kidney Stage. |
| 31 | `ADDL_PATH_FIND_SP_2` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 32 | `HIST_TYPE_SPECIFY_2` | VARCHAR |  | CAP synoptic form item: Second Specify Histologic Type. |
| 33 | `CAP_COMMENTS_2` | VARCHAR |  | CAP synoptic form item: General comments. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

