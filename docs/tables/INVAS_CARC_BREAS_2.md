# INVAS_CARC_BREAS_2

> Stores data for College of American Pathologists (CAP) form 76012-INVASIVE CARCINOMA OF THE BREAST: Complete Excision (Less Than Total Mastectomy, Including Specimens Designated Biopsy, Lumpectomy, Quadrantectomy, and Partial Mastectomy With or Without Axillary Contents) and Mastectomy (Total, Modified Radical, Radical With or Without Axillary Contents).

**Primary key:** `RESULT_ID`  
**Columns:** 47  
**Org-specific columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `ESTRGN_RECP_IMM_QNT` | NUMERIC |  | CAP synoptic form item: Estrogen Receptor Immunoreactive Tumor Cells Quantitation. |
| 3 | `ESTRGN_RECP_PC_SPFY` | VARCHAR |  | CAP synoptic form item: Estrogen Receptor - Specify Results Percentage. |
| 4 | `ESTRGN_RCP_AVG_SPFY` | VARCHAR |  | CAP synoptic form item: Estrogen Receptor - Specify Results Average. |
| 5 | `ESTRGN_RECP_INTRP_C_NAME` | VARCHAR | org | CAP synoptic form item: Estrogen Receptor Results (interpretation). |
| 6 | `ESTRGN_INTRP_SPFY` | VARCHAR |  | CAP synoptic form item: Estrogen Receptor - Specify Interpretation. |
| 7 | `ESTRGN_EXT_CN_C_NAME` | VARCHAR | org | CAP synoptic form item: Estrogen Receptor External Controls (immunoreactivity in normal cells, carcinomas, or cell lines). |
| 8 | `ESTRGN_EXT_CN_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Estrogen Receptor External Controls. |
| 9 | `ESTRGN_RECP_IN_CN_C_NAME` | VARCHAR | org | CAP synoptic form item: Estrogen Receptor Internal Controls (immunoreactivity in normal cells). |
| 10 | `ESTRGN_IN_CN_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Estrogen Receptor Internal Controls. |
| 11 | `ESTRGN_ASSAY_CND_C_NAME` | VARCHAR | org | CAP synoptic form item: Estrogen Receptor - Standard Assay Conditions. |
| 12 | `ESTRGN_ASY_CND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Estrogen Receptor - Standard Assay Conditions. |
| 13 | `ESTRGN_ANTBOD_VEND` | VARCHAR |  | CAP synoptic form item: Estrogen Receptor - Antibody Vendor and Clone. |
| 14 | `ESTRGN_TYPE_FIXTVE` | VARCHAR |  | CAP synoptic form item: Estrogen Receptor - Type of Fixative. |
| 15 | `PROGESTERONE_RECP_C_NAME` | VARCHAR | org | CAP synoptic form item: Progesterone Receptor. |
| 16 | `PRGSTN_RECP_PERF_C_NAME` | VARCHAR | org | CAP synoptic form item: Progesterone Receptor Performed. |
| 17 | `PRGSTN_RECP_SPEC` | VARCHAR |  | CAP synoptic form item: Progesterone Receptor - Specify Performed Specimen. |
| 18 | `PRGSTN_RECP_PERCN_C_NAME` | VARCHAR | org | CAP synoptic form item: Progesterone Receptor Results (percentage of cells). |
| 19 | `PRGSTN_RECP_PC_SPFY` | VARCHAR |  | CAP synoptic form item: Progesterone Receptor - Specify Results Percentage. |
| 20 | `PRGSTN_RCP_AVG_SPFY` | VARCHAR |  | CAP synoptic form item: Progesterone Receptor - Specify Results Average. |
| 21 | `PRGSTN_RECP_AVG_C_NAME` | VARCHAR | org | CAP synoptic form item: Progesterone Receptor Results (average intensity of tumor cell nuclei staining). |
| 22 | `PRGSTN_RECP_INTRP_C_NAME` | VARCHAR |  | CAP synoptic form item: Progesterone Receptor Results (interpretation). |
| 23 | `PRGSTN_INTRP_SPFY` | VARCHAR |  | CAP synoptic form item: Progesterone Receptor - Specify Interpretation. |
| 24 | `PRGSTN_RECP_IMM_QTY` | NUMERIC |  | CAP synoptic form item: Progesterone Receptor Immunoreactive Tumor Cells Quantitation. |
| 25 | `PRGSTN_RECP_IN_CN_C_NAME` | VARCHAR |  | CAP synoptic form item: Progesterone Receptor Internal Controls (immunoreactivity in normal cells). |
| 26 | `PRGSTN_IN_CN_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Progesterone Receptor Internal Controls. |
| 27 | `PRGSTN_RECP_EX_CN_C_NAME` | VARCHAR |  | CAP synoptic form item: Progesterone Receptor External Controls (immunoreactivity in normal cells, carcinomas, or cell lines). |
| 28 | `PRGSTN_EXT_CN_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Progesterone Receptor External Controls. |
| 29 | `PRGSTN_ASSAY_CND_C_NAME` | VARCHAR |  | CAP synoptic form item: Progesterone Receptor - Standard Assay Conditions. |
| 30 | `PRGSTN_ASY_CND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Progesterone Receptor Standard Assay Conditions. |
| 31 | `PRGSTN_ANTBOD_VEND` | VARCHAR |  | CAP synoptic form item: Progesterone Receptor - Antibody Vendor. |
| 32 | `PRGSTN_TYPE_FIXTIVE` | VARCHAR |  | CAP synoptic form item: Progesterone Receptor - Type of Fixative. |
| 33 | `PRGSTRN_RECP_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Progesterone Receptor. |
| 34 | `THIS_SPEC_TEST_NAME` | VARCHAR |  | CAP synoptic form item: Ancillary Studies - This Specimen - Name of Test. |
| 35 | `THIS_SPEC_TEST_RSLT` | VARCHAR |  | CAP synoptic form item: Ancillary Studies - This Specimen - Results. |
| 36 | `ANOTHER_SPEC_SPFY` | VARCHAR |  | CAP synoptic form item: Ancillary Studies - Specify Another Specimen. |
| 37 | `ANOTH_SPEC_TEST_NAM` | VARCHAR |  | CAP synoptic form item: Ancillary Studies - Another Specimen - Name of Test. |
| 38 | `ANOTHER_SPEC_RESULT` | VARCHAR |  | CAP synoptic form item: Ancillary Studies - Another Specimen - Results. |
| 39 | `IMMUNPRXD_STD_C_NAME` | VARCHAR |  | CAP synoptic form item: Immunoperoxidase Studies. |
| 40 | `IMMUNPRXD_PERF_C_NAME` | VARCHAR |  | CAP synoptic form item: Immunoperoxidase Studies Performed. |
| 41 | `IMMUNPRXD_SPEC_SPFY` | VARCHAR |  | CAP synoptic form item: Immunoperoxidase Studies - Specify Specimen. |
| 42 | `IMMUNPRXD_RESULT_C_NAME` | VARCHAR | org | CAP synoptic form item: Immunoperoxidase Study Results. |
| 43 | `IMMUNPRXD_RSLT_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Immunoperoxidase Study Results. |
| 44 | `IMMUNPRXD_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Immunoperoxidase Studies. |
| 45 | `IMMUNPRXD_ANTBD_CLN` | VARCHAR |  | CAP synoptic form item: Immunoperoxidase Studies - Antibody and Clone. |
| 46 | `FISH_FOR_HER2_C_NAME` | VARCHAR |  | CAP synoptic form item: Fluorescence In Situ Hybridization (FISH) for HER2 / neu. |
| 47 | `FISH_PERFORMED_C_NAME` | VARCHAR |  | CAP synoptic form item: Fluorescence In Situ Hybridization (FISH) for HER2 / neu Performed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

