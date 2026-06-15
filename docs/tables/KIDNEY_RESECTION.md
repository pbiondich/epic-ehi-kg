# KIDNEY_RESECTION

> Stores single response data for College of American Pathologists (CAP) form 76068-KIDNEY: Resection for Pediatric Renal Tumor.

**Overflow family:** [KIDNEY_RESECTION_2](KIDNEY_RESECTION_2.md)  
**Primary key:** `RESULT_ID`  
**Columns:** 33  
**Org-specific columns:** 6

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
| 8 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 9 | `HIST_TYP_NONCL_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other or nonclassifiable histologic type. |
| 10 | `TUMOR_SIZE_INDETER` | VARCHAR |  | CAP synoptic form item: Specify Reason Why Tumor Size Is Indeterminate. |
| 11 | `LYMPH_ND_NUM_XMD` | NUMERIC |  | CAP synoptic form item: Specify the number of lymph nodes examined. |
| 12 | `SPEC_SZ_KDN_DMSN1` | NUMERIC |  | CAP synoptic form item: Specify kidney dimension 1 for specimen size. |
| 13 | `SPEC_SZ_KDN_DMSN2` | NUMERIC |  | CAP synoptic form item: Specify kidney dimension 2 for specimen size. |
| 14 | `SPEC_SZ_KDN_DMSN3` | NUMERIC |  | CAP synoptic form item: Specify kidney dimension 3 for specimen size. |
| 15 | `SPEC_SZ_WT` | NUMERIC |  | CAP synoptic form item: Specify weight for specimen size. |
| 16 | `TM_SZ_GRT_DMSN2` | NUMERIC |  | CAP synoptic form item: Specify Greatest dimension tumor 2 for Tumor Size. |
| 17 | `TM_SZ_GRT_DMSN3` | NUMERIC |  | CAP synoptic form item: Specify Greatest dimension tumor 3 for Tumor Size. |
| 18 | `TMR_SZ_ND_OTHER` | VARCHAR |  | CAP synoptic form item: Specify details for other tumor size that cannot be determined. |
| 19 | `GEROTA_FASCIA_C_NAME` | VARCHAR | org | CAP synoptic form item: Gerotas Fascia. |
| 20 | `RENAL_VEIN_C_NAME` | VARCHAR | org | CAP synoptic form item: Renal Vein. |
| 21 | `TM_XTN_AO_PRS_SPEC` | VARCHAR |  | CAP synoptic form item: Specify organ when Tumor extension into adjacent organ present. |
| 22 | `DSTC_TM_FRM_MRG_IVL` | NUMERIC |  | CAP synoptic form item: Specify Distance of Tumor from Closest Margin when Margin involvement by tumor not identified. |
| 23 | `MG_IVLV_NI_UNIT_C_NAME` | VARCHAR | org | CAP synoptic form item: Specify unit when Margin involvement by tumor not identified. |
| 24 | `MG_IVLV_TM_NI_MS_C_NAME` | VARCHAR | org | CAP synoptic form item: Specify Margin when Margin involvement by tumor not identified. |
| 25 | `MG_IVLV_TM_NI_OTHER` | VARCHAR |  | CAP synoptic form item: Specify other details for Margin involvement by tumor not identified. |
| 26 | `MRG_IVLV_TM_OTHER` | VARCHAR |  | CAP synoptic form item: Specify other details when Margin involved by tumor. |
| 27 | `NEPHROGENIC_RESTS_C_NAME` | VARCHAR | org | CAP synoptic form item: Nephrogenic Rests. |
| 28 | `LYM_ND_NUM_IVLV` | NUMERIC |  | CAP synoptic form item: Specify number of lymph nodes involved. |
| 29 | `DSTNC_MTSS_PRST_ST` | VARCHAR |  | CAP synoptic form item: Specify Site for Distant metastasis present. |
| 30 | `S5_BRID_RIGHT_KD_C_NAME` | VARCHAR | org | CAP synoptic form item: Stage V Bilateral renal involvement at diagnosis Specify Right Kidney Stage. |
| 31 | `S5_BRID_LEFT_KD_C_NAME` | VARCHAR |  | CAP synoptic form item: Stage V Bilateral renal involvement at diagnosis Specify Left Kidney Stage. |
| 32 | `TM_FCLT_MFCL_NUM` | NUMERIC |  | CAP synoptic form item: Specify the number of tumors in specimen for Tumor Focality Multifocal. |
| 33 | `RLNM_PRSNT_SITE` | VARCHAR |  | CAP synoptic form item: Specify site for Regional lymph node metastasis present. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

