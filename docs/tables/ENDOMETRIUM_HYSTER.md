# ENDOMETRIUM_HYSTER

> Stores data for College of American Pathologists (CAP) form 76016-ENDOMETRIUM: Hysterectomy, With or Without Other Organs or Tissues.

**Primary key:** `RESULT_ID`  
**Columns:** 55  
**Org-specific columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier for the result record. |
| 2 | `TUMOR_SITE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify tumor site. |
| 3 | `CAP_COMMENTS` | VARCHAR |  | CAP synoptic form item: General comments. |
| 4 | `SPEC_INTEGRITY_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Integrity. |
| 5 | `SPEC_PROC_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify the Specimen Procedure. |
| 6 | `TUMOR_SIZE_GREAT` | NUMERIC |  | CAP synoptic form item: Tumor Greatest Size. |
| 7 | `TUMOR_SIZE_ADDL` | NUMERIC |  | CAP synoptic form item: Tumor Size (length). |
| 8 | `TUMOR_SIZE_ADDL2` | NUMERIC |  | CAP synoptic form item: Tumor Size (width). |
| 9 | `TUMOR_SIZE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify Tumor Size. |
| 10 | `HISTO_TYPE_SPECIFY` | VARCHAR |  | CAP synoptic form item: Specify histologic type. |
| 11 | `SPECIFIC_MARGINS` | VARCHAR |  | CAP synoptic form item: Specific Margins. |
| 12 | `INVOLV_CERVIX_C_NAME` | VARCHAR | org | CAP synoptic form item: Involvement of Cervix. |
| 13 | `INVOLV_CERVIX_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Involvement of Cervix. |
| 14 | `CLINICAL_HIST_SPFY` | VARCHAR |  | CAP synoptic form item: Specify clinical history. |
| 15 | `SPECIMEN_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify other specimen. |
| 16 | `LYMPH_ND_SAMPL_SPFY` | VARCHAR |  | CAP synoptic form item: Specify lymph node sampling. |
| 17 | `HISTOLOGIC_GRADE_C_NAME` | VARCHAR | org | CAP synoptic form item: Histologic Grade. |
| 18 | `HISTOLGC_GRADE_SPFY` | VARCHAR |  | CAP synoptic form item: Specify histologic grade. |
| 19 | `MYOMETRIAL_INVASN_C_NAME` | VARCHAR | org | CAP synoptic form item: Myometrial Invasion. |
| 20 | `MYOMETRL_INV_DEPTH` | NUMERIC |  | CAP synoptic form item: Myometrial Invasion - Depth of Invasion. |
| 21 | `MYOMETRL_INV_PRES_C_NAME` | VARCHAR | org | CAP synoptic form item: Myometrial Invasion Present. |
| 22 | `MYOMETRIAL_THICKNSS` | NUMERIC |  | CAP synoptic form item: Myometrial Thickness. |
| 23 | `EXT_BLADDER_MUCUS_C_NAME` | VARCHAR | org | CAP synoptic form item: Extent - Bladder Mucosa and/or Bowel Mucosa. |
| 24 | `EXT_BLADDER_WALL_C_NAME` | VARCHAR |  | CAP synoptic form item: Extent - Bladder Wall. |
| 25 | `EXT_LEFT_FALL_TB_C_NAME` | VARCHAR |  | CAP synoptic form item: Extent Left Fallopian Tube. |
| 26 | `EXTENT_LEFT_OVARY_C_NAME` | VARCHAR |  | CAP synoptic form item: Extent Left Ovary. |
| 27 | `EXT_LEFT_PARAMET_C_NAME` | VARCHAR |  | CAP synoptic form item: Extent - Left Parametrium. |
| 28 | `EXTENT_OMENTUM_C_NAME` | VARCHAR |  | CAP synoptic form item: Extent Omentum. |
| 29 | `EXTENT_OTHER_SPFY` | VARCHAR |  | CAP synoptic form item: Specify Other Extent. |
| 30 | `EXT_PELVIC_WALL_C_NAME` | VARCHAR |  | CAP synoptic form item: Extent - Pelvic Wall. |
| 31 | `EXT_RECTAL_WALL_C_NAME` | VARCHAR |  | CAP synoptic form item: Extent - Rectal Wall. |
| 32 | `EXT_RIGHT_FALL_TB_C_NAME` | VARCHAR |  | CAP synoptic form item: Extent Right Fallopian Tube. |
| 33 | `EXT_RIGHT_OVARY_C_NAME` | VARCHAR |  | CAP synoptic form item: Extent Right ovary. |
| 34 | `EXT_RIGHT_PARAMET_C_NAME` | VARCHAR |  | CAP synoptic form item: Extent - Right Parametrium. |
| 35 | `EXTENT_VAGINA_C_NAME` | VARCHAR |  | CAP synoptic form item: Extent - Vagina. |
| 36 | `PERIT_ASCITIC_FLD_C_NAME` | VARCHAR | org | CAP synoptic form item: Peritoneal Ascitic Fluid. |
| 37 | `PERIT_ASC_FLD_ATYP` | VARCHAR |  | CAP synoptic form item: Peritoneal Ascitic Fluid Atypical and / or suspicious. |
| 38 | `PERIT_ASC_FLD_UNSAT` | VARCHAR |  | CAP synoptic form item: Peritoneal Ascitic Fluid Unsatisfactory / nondiagnostic. |
| 39 | `ANC_STDIES_SPFY_TYP` | VARCHAR |  | CAP synoptic form item: Ancillary Studies Specify Types. |
| 40 | `PRIMARY_TUMOR_C_NAME` | VARCHAR | org | CAP synoptic form item: Primary Tumor (pT). |
| 41 | `REGIONL_LYMPH_ND_C_NAME` | VARCHAR | org | CAP synoptic form item: Regional Lymph Nodes (pN). |
| 42 | `DISTNT_METASTASIS_C_NAME` | VARCHAR | org | CAP synoptic form item: Distant Metastasis. |
| 43 | `DSTNT_METASTATIS_ST` | VARCHAR |  | CAP synoptic form item: Distant Metastasis Sites. |
| 44 | `HYPERPLASIA_C_NAME` | VARCHAR | org | CAP synoptic form item: Hyperplasia. |
| 45 | `ATYPICAL_HYPERPLS_C_NAME` | VARCHAR | org | CAP synoptic form item: Atypical Hyperplasia. |
| 46 | `ADDL_PATH_FIND_SPFY` | VARCHAR |  | CAP synoptic form item: Specify additional pathologic findings. |
| 47 | `MIXED_CARC_SPFY` | VARCHAR |  | CAP synoptic form item: Mixed carcinoma (specify types and percentages). |
| 48 | `MYOMETRL_INV_CANNT` | VARCHAR |  | CAP synoptic form item: Myometrial Invasion - Specify Why it Cannot Be Determined. |
| 49 | `ENDO_ADENOCARCINOMA` | VARCHAR |  | CAP synoptic form item: Endometrioid adenocarcinoma, variant. |
| 50 | `PELVIC_NUM_EXAMINED` | NUMERIC |  | CAP synoptic form item: Pelvic lymph nodes - Number Examined. |
| 51 | `PELVIC_NUM_INVOLVED` | NUMERIC |  | CAP synoptic form item: Pelvic lymph nodes - Number Involved. |
| 52 | `AORTIC_NUM_EXAMINED` | NUMERIC |  | CAP synoptic form item: Para-aortic lymph nodes - Number Examined. |
| 53 | `AORTIC_NUM_INVOLVED` | NUMERIC |  | CAP synoptic form item: Para-aortic lymph nodes - Number Involved. |
| 54 | `SPEC_PROC_HYS_C_NAME` | VARCHAR | org | CAP synoptic form item: Specimen Procedure - Hysterectomy. |
| 55 | `LATER_DIST_INV_CARC` | NUMERIC |  | CAP synoptic form item: Distance of Invasive Carcinoma from Closest Lateral Margin. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

