# UVEAL_MELANOMA

> Stores single response data for College of American Pathologists (CAP) form 76064-UVEAL MELANOMA: Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 36  
**Org-specific columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `SPEC_SITE_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Site. |
| 3 | `TM_BS_SZ_SPC` | NUMERIC |  | CAP synoptic form item: Specify Tumor Basal Size on Transillumination. |
| 4 | `TM_BS_SZ_TSLM2` | NUMERIC |  | CAP synoptic form item: Specify another Tumor Basal Size on Transillumination. |
| 5 | `TLS_DSTN_AET_LCE` | NUMERIC |  | CAP synoptic form item: Specify Distance from Anterior Edge of Tumor to Limbus at Cut Edge for Tumor Location After Sectioning. |
| 6 | `TLS_DSTN_OD_MTB` | NUMERIC |  | CAP synoptic form item: Specify Distance of Posterior Margin of Tumor Base from Edge of Optic Disc for Tumor Location After Sectioning. |
| 7 | `SPEC_SZ_XNTRTN_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Size For Exenteration. |
| 8 | `SPEC_SZ_NCLTN_NDS` | VARCHAR |  | CAP synoptic form item: Specify Specimen Size For Enucleation Cannot be determined. |
| 9 | `SP_SZ_NCT_ND_AD` | NUMERIC |  | CAP synoptic form item: Specify Anteroposterior Diameter of specimen size For Enucleation when Cannot be determined. |
| 10 | `SP_SZ_NCLT_ND_HD` | NUMERIC |  | CAP synoptic form item: Specify Horizontal Diameter of specimen size For Enucleation when Cannot be determined. |
| 11 | `SP_SZ_NCLT_ND_VD` | NUMERIC |  | CAP synoptic form item: Specify Vertical Diameter of specimen size For Enucleation when Cannot be determined. |
| 12 | `SP_SZ_NCLT_ND_ONL` | NUMERIC |  | CAP synoptic form item: Specify Length of optic nerve of specimen size For Enucleation when Cannot be determined. |
| 13 | `SP_SZ_NCLT_ND_OND` | NUMERIC |  | CAP synoptic form item: Specify Diameter of optic nerve of specimen size For Enucleation when Cannot be determined. |
| 14 | `SP_SZ_XTRT_GDS` | NUMERIC |  | CAP synoptic form item: Specify the greatest dimension of specimen size for exenteration. |
| 15 | `SP_SZ_XNTR_GDAD` | NUMERIC |  | CAP synoptic form item: Specify additional dimension for the greatest dimension of specimen size for exenteration. |
| 16 | `SP_SZ_XNTR_GDAD2` | NUMERIC |  | CAP synoptic form item: Specify another additional dimension for the greatest dimension of specimen size for exenteration. |
| 17 | `SP_SZ_XNTR_NDS` | VARCHAR |  | CAP synoptic form item: Specify details for the specimen size for exenteration that cannot be determined. |
| 18 | `HIST_TP_SPDL_CT_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Type Spindle cell type. |
| 19 | `ACSR_FND_GRW_PTRN_C_NAME` | VARCHAR | org | CAP synoptic form item: Accessory Findings Growth Pattern. |
| 20 | `HISTOPATH_TYPE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histopathologic Type. |
| 21 | `SCLERAL_INVOLVE_C_NAME` | VARCHAR | org | CAP synoptic form item: Scleral Involvement. |
| 22 | `PRMR_TMR_IRIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor Iris. |
| 23 | `PT_CLR_BD_CHRD_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor Ciliary Body and Choroid. |
| 24 | `ADTNL_PATH_FND_MTRT` | NUMERIC |  | CAP synoptic form item: Specify Mitotic Rate for Additional Pathologic Findings. |
| 25 | `OTHER_MARGIN_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other margin. |
| 26 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 27 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 28 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 29 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 30 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 31 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 32 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 33 | `TUMOR_BASE_CUT_EDGE` | NUMERIC |  | CAP synoptic form item: Tumor Size After Sectioning Base at Cut Edge. |
| 34 | `TUMOR_HT_CUT_EDGE` | NUMERIC |  | CAP synoptic form item: Tumor Size After Sectioning Height at Cut Edge. |
| 35 | `TUMOR_GREAT_CUT_ED` | NUMERIC |  | CAP synoptic form item: Tumor Size After Sectioning Greatest Height. |
| 36 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

