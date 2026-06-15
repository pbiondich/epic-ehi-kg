# BRAIN_SPINAL_BIOP

> Stores data for College of American Pathologists (CAP) form 76011-BRAIN/SPINAL CORD: Biopsy/Resection.

**Primary key:** `RESULT_ID`  
**Columns:** 60  
**Org-specific columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 3 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 4 | `SPEC_HANDLING_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Specimen Handling. |
| 5 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 6 | `SPEC_SIZE_GREATEST` | NUMERIC |  | CAP synoptic form item: Specimen Greatest Size. |
| 7 | `SPEC_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Specimen size additional dimension (length). |
| 8 | `SPEC_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Specimen size additional dimension (width). |
| 9 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 10 | `MOL_GEN_STDY_RPT` | VARCHAR |  | CAP synoptic form item: Specify Molecular Genetic Studies Report. |
| 11 | `MOL_GEN_STDY_RES` | VARCHAR |  | CAP synoptic form item: Specify Molecular Genetic Studies Results. |
| 12 | `MOLEC_STD_19Q_DEL_C_NAME` | VARCHAR | org | CAP synoptic form item: Molecular Genetic Studies 19q Deletion. |
| 13 | `MOLEC_STD_1P_DEL_C_NAME` | VARCHAR | org | CAP synoptic form item: Molecular Genetic Studies 1p Deletion. |
| 14 | `IMMUNOHISTOCHM_SPFY` | VARCHAR |  | CAP synoptic form item: Specify immunohistochemistry. |
| 15 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 16 | `HIST_TYP_NONCLASS_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Type - Other/Nonclassifiable. |
| 17 | `HIST_TYP_NONCL_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other or nonclassifiable histologic type. |
| 18 | `TUMORS_SELLAR_REG_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumors of the Sellar Region. |
| 19 | `TMR_SELLAR_REG_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Tumors of the Sellar Region. |
| 20 | `PITUITRY_ADENO_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Pituitary Adenoma. |
| 21 | `GERM_CELL_TUMORS_C_NAME` | VARCHAR | org | CAP synoptic form item: Germ Cell Tumors. |
| 22 | `MALGNT_MIX_OTH_SPFY` | VARCHAR |  | CAP synoptic form item: Malignant Mixed Germ Cell Tumor - Specify Other. |
| 23 | `MALGNT_MIX_GRM_SPFY` | VARCHAR |  | CAP synoptic form item: Specify malignant mixed germ cell tumor. |
| 24 | `LYPHM_HEMTPTC_TMR_C_NAME` | VARCHAR | org | CAP synoptic form item: Lymphoma and Hematopoietic Tumors. |
| 25 | `HEMATPTC_NPLSM_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Hematopoietic Neoplasm. |
| 26 | `PRIMRY_MELNTC_TMR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Melanotic Tumors. |
| 27 | `MALGNT_LYMPH_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Malignant Lymphoma. |
| 28 | `MESENCHYMAL_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Mesenchymal (Nonmeningothelial) Tumors. |
| 29 | `MESENCHYML_TMR_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Mesenchymal (Nonmeningothelial) Tumors. |
| 30 | `SARCM_PMRY_CNS_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Sarcoma, Primary Central Nervous System (CNS). |
| 31 | `TMR_MNNG_MNNGTHLL_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumors of the Meninges / Meningothelial Cells. |
| 32 | `TMR_MNG_MNGTHL_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Tumors of the Meninges / Meningothelial Cells. |
| 33 | `MENINGIOMA_C_NAME` | VARCHAR | org | CAP synoptic form item: Meningioma (WHO grade I). |
| 34 | `TMR_CRANL_PARASPN_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumors of Cranial and Paraspinal Nerves. |
| 35 | `SCHWANNOMA_C_NAME` | VARCHAR | org | CAP synoptic form item: Schwannoma (WHO grade I). |
| 36 | `PERINEUROMA_C_NAME` | VARCHAR | org | CAP synoptic form item: Perineuroma. |
| 37 | `MPNST_C_NAME` | VARCHAR | org | CAP synoptic form item: Malignant peripheral nerve sheath tumor (MPNST) (WHO grade II-IV). |
| 38 | `EMBRYONAL_TUMORS_C_NAME` | VARCHAR | org | CAP synoptic form item: Embryonal Tumors. |
| 39 | `MEDULBLSTM_NT_OTH_C_NAME` | VARCHAR | org | CAP synoptic form item: Medulloblastoma, not otherwise characterized (WHO grade IV). |
| 40 | `CNS_PNET_C_NAME` | VARCHAR | org | CAP synoptic form item: Central nervous system (CNS) primitive neuroectodermal tumor (PNET) (WHO grade IV). |
| 41 | `TMR_OF_PINEAL_REG_C_NAME` | VARCHAR | org | CAP synoptic form item: Tumors of the Pineal Region. |
| 42 | `NERNL_MXD_N_G_TMR_C_NAME` | VARCHAR | org | CAP synoptic form item: Neuronal and Mixed Neuronal-Glial Tumors. |
| 43 | `OTHR_NEUREPTH_TMR_C_NAME` | VARCHAR | org | CAP synoptic form item: Other Neuroepithelial Tumors. |
| 44 | `CHOROID_PLEXS_TMR_C_NAME` | VARCHAR | org | CAP synoptic form item: Choroid Plexus Tumors. |
| 45 | `EPENDYMAL_TUMORS_C_NAME` | VARCHAR | org | CAP synoptic form item: Ependymal Tumors. |
| 46 | `EPENDYMOMA_C_NAME` | VARCHAR | org | CAP synoptic form item: Ependymoma (WHO grade II). |
| 47 | `OLIGOASTRCYTC_TMR_C_NAME` | VARCHAR | org | CAP synoptic form item: Oligoastrcytic Tumors (mixed glioma). |
| 48 | `ASTROCYTIC_TUMORS_C_NAME` | VARCHAR | org | CAP synoptic form item: Astrocytic Tumors. |
| 49 | `DIFFUSE_ASTROCYTM_C_NAME` | VARCHAR | org | CAP synoptic form item: Diffuse Astrocytoma (WHO grade II). |
| 50 | `GLIOBLASTOMA_C_NAME` | VARCHAR | org | CAP synoptic form item: Glioblastoma (WHO grade IV). |
| 51 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 52 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 53 | `HIST_TMR_FAMILIAL_C_NAME` | VARCHAR | org | CAP synoptic form item: History of Previous Tumor/Familial Syndrome. |
| 54 | `HIST_TMR_FAMIL_SPFY` | VARCHAR |  | CAP synoptic form item: History of Previous Tumor/Familial Syndrome. |
| 55 | `BRAIN_CEREBRUM_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Brain/Cerebrum. |
| 56 | `BRAIN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Brain, Other. |
| 57 | `BRAINSTEM_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Brainstem. |
| 58 | `DURA_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Dura. |
| 59 | `LEPTOMENINGES_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Leptomeninges. |
| 60 | `OLIGODENDRGL_TMR_C_NAME` | VARCHAR | org | CAP synoptic form item: Oligondendroglial Tumors. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

