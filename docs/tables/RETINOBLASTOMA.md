# RETINOBLASTOMA

> Stores data for College of American Pathologists (CAP) form 76046-RETINOBLASTOMA: Enucleation, Partial or Complete Exenteration (Notes A, B, C).

**Primary key:** `RESULT_ID`  
**Columns:** 37  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 3 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 4 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 5 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 6 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 7 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 8 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 9 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 10 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 11 | `ADTNL_PATH_FND_MTRT` | NUMERIC |  | CAP synoptic form item: Specify Mitotic Rate for Additional Pathologic Findings. |
| 12 | `TUMOR_LOC_CANNOT_YN` | VARCHAR |  | CAP synoptic form item: Tumor Location After Sectioning Cannot Be Determined. |
| 13 | `DIST_LIMBUS_CUT_EDG` | NUMERIC |  | CAP synoptic form item: Distance from Anterior Edge of Tumor to Limbus at Cut Edge. |
| 14 | `DIST_POST_OPTIC_EDG` | NUMERIC |  | CAP synoptic form item: Distance of Posterior Margin of Tumor Base from Edge of Optic Disc. |
| 15 | `TRAN_ANT_POS_LENGTH` | NUMERIC |  | CAP synoptic form item: Tumor Basal Size on Transillumination Anterior-Posterior Length. |
| 16 | `TRANSILLU_CANNOT_YN` | VARCHAR |  | CAP synoptic form item: Tumor Basal Size on Transillumination Cannot Be Determined. |
| 17 | `TRAN_ANT_POS_LENGT2` | NUMERIC |  | CAP synoptic form item: Tumor Basal Size on Transillumination Anterior-Posterior Length 2. |
| 18 | `BASAL_TRANS_LENGTH` | NUMERIC |  | CAP synoptic form item: Tumor Basal Size on Transillumination Transverse Length. |
| 19 | `BASAL_TRANS_LENGTH2` | NUMERIC |  | CAP synoptic form item: Tumor Basal Size on Transillumination Transverse Length 2. |
| 20 | `TUMOR_SEC_CANNOT_YN` | VARCHAR |  | CAP synoptic form item: Tumor Size After Sectioning Cannot Be Determined. |
| 21 | `EXT_OPTIC_NER_INV_C_NAME` | VARCHAR | org | CAP synoptic form item: Extent of Optic Nerve Invasion. |
| 22 | `TUMOR_BASE_CUT_EDGE` | NUMERIC |  | CAP synoptic form item: Tumor Size After Sectioning Base at Cut Edge. |
| 23 | `TUMOR_HT_CUT_EDGE` | NUMERIC |  | CAP synoptic form item: Tumor Size After Sectioning Height at Cut Edge. |
| 24 | `TUMOR_GREAT_CUT_ED` | NUMERIC |  | CAP synoptic form item: Tumor Size After Sectioning Greatest Height. |
| 25 | `SPEC_SZ_XNTRTN_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Size For Exenteration. |
| 26 | `SPEC_SZ_NCLTN_NDS` | VARCHAR |  | CAP synoptic form item: Specify Specimen Size For Enucleation Cannot be determined. |
| 27 | `SP_SZ_NCT_ND_AD` | NUMERIC |  | CAP synoptic form item: Specify Anteroposterior Diameter of specimen size For Enucleation when Cannot be determined. |
| 28 | `SP_SZ_NCLT_ND_HD` | NUMERIC |  | CAP synoptic form item: Specify Horizontal Diameter of specimen size For Enucleation when Cannot be determined. |
| 29 | `SP_SZ_NCLT_ND_VD` | NUMERIC |  | CAP synoptic form item: Specify Vertical Diameter of specimen size For Enucleation when Cannot be determined. |
| 30 | `SP_SZ_NCLT_ND_ONL` | NUMERIC |  | CAP synoptic form item: Specify Length of optic nerve of specimen size For Enucleation when Cannot be determined. |
| 31 | `SP_SZ_NCLT_ND_OND` | NUMERIC |  | CAP synoptic form item: Specify Diameter of optic nerve of specimen size For Enucleation when Cannot be determined. |
| 32 | `SP_SZ_XTRT_GDS` | NUMERIC |  | CAP synoptic form item: Specify the greatest dimension of specimen size for exenteration. |
| 33 | `SP_SZ_XNTR_GDAD` | NUMERIC |  | CAP synoptic form item: Specify additional dimension for the greatest dimension of specimen size for exenteration. |
| 34 | `SP_SZ_XNTR_GDAD2` | NUMERIC |  | CAP synoptic form item: Specify another additional dimension for the greatest dimension of specimen size for exenteration. |
| 35 | `SP_SZ_XNTR_NDS` | VARCHAR |  | CAP synoptic form item: Specify details for the specimen size for exenteration that cannot be determined. |
| 36 | `ACSR_FND_GRW_PTRN_C_NAME` | VARCHAR | org | CAP synoptic form item: Accessory Findings Growth Pattern. |
| 37 | `ADD_PATH_NEOVA_SPEC` | VARCHAR |  | CAP synoptic form item: Additional Pathologic Findings Neovascularization (Specify). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

