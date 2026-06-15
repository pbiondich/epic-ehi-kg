# UNOS_CLIN_INFO_3

> Additional information reported to the United Network for Organ Sharing (UNOS) for each of the registry records or forms.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 96

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `DNR_VIR_TESTED_YN` | VARCHAR |  | Indicates whether the donor was tested for HIV, CMV, HBV, HCV or EBV prior to the donation. |
| 3 | `VIR_CMV_TESTED_YN` | VARCHAR |  | Indicates the presence of CMV. |
| 4 | `VIR_CMV_DISEASE_C_NAME` | VARCHAR |  | Indicates whether the patient had any CMV related clinical disease. |
| 5 | `VIR_CMV_NUC_ACID_C_NAME` | VARCHAR |  | The patient's CMV nucleic acid test results. |
| 6 | `VIR_CMV_CULTURE_C_NAME` | VARCHAR |  | The patient's CMV culture test results. |
| 7 | `VIR_CMV_PREUNET_C_NAME` | VARCHAR |  | The patient's pre-UNet CMV data. |
| 8 | `VIR_HIV_TESTED_YN` | VARCHAR |  | Indicates the presence of any of several retroviruses indicative of AIDS. |
| 9 | `VIR_HIV_SCREEN_C_NAME` | VARCHAR |  | The patient's HIV screening test results. |
| 10 | `VIR_HIV_CONFIRM_C_NAME` | VARCHAR |  | The patient's HIV confirmation test results. |
| 11 | `VIR_HIV_DISEASE_C_NAME` | VARCHAR |  | Indicates whether the patient had any HIV related clinical disease. |
| 12 | `VIR_HIV_ANTIB_C_NAME` | VARCHAR |  | The patient's HIV antibody test results. |
| 13 | `VIR_HIV_RNA_C_NAME` | VARCHAR |  | The patient's HIV RNA test results. |
| 14 | `VIR_HBV_TESTED_YN` | VARCHAR |  | Indicates the presence of HBV or serum hepatitis. |
| 15 | `VIR_HBV_DISEASE_C_NAME` | VARCHAR |  | Indicates whether the patient had any HBV related clinical disease. |
| 16 | `VIR_HBV_LVR_HISTO_C_NAME` | VARCHAR |  | The patient's HBV liver histology test results. |
| 17 | `VIR_HBV_DNA_C_NAME` | VARCHAR |  | The patient's HBV DNA test results. |
| 18 | `VIR_HBV_HDV_C_NAME` | VARCHAR |  | The patient's HBV HDV (Delta virus) test results. |
| 19 | `VIR_HCV_TESTED_YN` | VARCHAR |  | Indicates the presence of HCV. |
| 20 | `VIR_HCV_DISEASE_C_NAME` | VARCHAR |  | Indicates whether the patient had any HCV related clinical disease. |
| 21 | `VIR_HCV_LVR_HISTO_C_NAME` | VARCHAR |  | The patient's HCV liver histology test results. |
| 22 | `VIR_HCV_ANTIB_C_NAME` | VARCHAR |  | The patient's HCV antibody test results. |
| 23 | `VIR_HCV_RIBA_C_NAME` | VARCHAR |  | The patient's HCV RIBA test results. |
| 24 | `VIR_HCV_RNA_C_NAME` | VARCHAR |  | The patient's HCV RNA test results. |
| 25 | `VIR_EBV_TESTED_YN` | VARCHAR |  | Indicates the presence of EBV or EB virus. |
| 26 | `VIR_EBV_DISEASE_C_NAME` | VARCHAR |  | Indicates whether the patient had any EBV related clinical disease. |
| 27 | `VIR_EBV_IGG_C_NAME` | VARCHAR |  | The patient's EBV IgG test results. |
| 28 | `VIR_EBV_IGM_C_NAME` | VARCHAR |  | The patient's EBV IgM test results. |
| 29 | `VIR_EBV_DNA_C_NAME` | VARCHAR |  | The patient's EBV DNA test results. |
| 30 | `UNOS_CANCER_HX_C_NAME` | VARCHAR |  | Indicates whether the donor had a history of cancer prior to the donation. |
| 31 | `UNOS_CANCER_HX_SP` | VARCHAR |  | The name of the cancer of which the donor had a history prior to the donation. |
| 32 | `CANCER_FREE_INTERVL` | INTEGER |  | If the donor had a history of cancer, the number of years the donor was cancer-free prior to donation. |
| 33 | `CANCER_FREE_ST_C_NAME` | VARCHAR |  | Specifies the reason why the number of years the donor was free of the cancer is not available. |
| 34 | `UNOS_HX_HYPERTNSN_C_NAME` | VARCHAR |  | Indicates whether the donor had a history of hypertension prior to donation. |
| 35 | `UNOS_HX_HYPT_DIET_C_NAME` | VARCHAR |  | If the donor had a history of hypertension, indicates whether diet was used as a treatment method. |
| 36 | `UNOS_HX_HYPT_DIUR_C_NAME` | VARCHAR |  | If the donor had a history of hypertension, indicates whether diuretics were used as a treatment method. |
| 37 | `UNOS_HX_HYPT_MED_C_NAME` | VARCHAR |  | If the donor had a history of hypertension, indicates whether medication was used as a treatment method. |
| 38 | `PREOP_BP_SYSTOLIC` | INTEGER |  | The living donor's systolic blood pressure prior to donation. |
| 39 | `PREOP_BP_SYST_ST_C_NAME` | VARCHAR |  | Specifies why the living donor's systolic blood pressure prior to donation is not available. |
| 40 | `PREOP_BP_DIASTOLIC` | INTEGER |  | The living donor's diastolic blood pressure prior to donation. |
| 41 | `PREOP_BP_DIAS_ST_C_NAME` | VARCHAR |  | Specifies why the living donor's diastolic blood pressure prior to donation is not available. |
| 42 | `PREOP_URINE_RATIO` | NUMERIC |  | The donor's urinalysis protein-creatinine ratio prior to donation. |
| 43 | `PREOP_URINE_PRTN_C_NAME` | VARCHAR |  | The living donor's urinalysis urine protein prior to donation. |
| 44 | `UNOS_KI_GLOMERO_C_NAME` | VARCHAR |  | The living donor's glomerulosclerosis if the living donor had a kidney biopsy prior to donation. |
| 45 | `UNOS_KI_PROC_TYPE_C_NAME` | VARCHAR |  | The kidney intended procedure type. |
| 46 | `CNV_LAPAROS_OPEN_YN` | VARCHAR |  | Indicates whether there was a conversion from laparoscopic to open procedure if laparoscopic was selected for intended procedure type. |
| 47 | `CIGARETTE_HX_YN` | VARCHAR |  | Indicates whether the donor has a history of cigarette use. |
| 48 | `UNOS_CGR_PCK_YR_C_NAME` | VARCHAR |  | The number of packs of cigarettes the donor smoked per day multiplied by the number of years if the donor has a history of cigarette use. |
| 49 | `UNOS_ABSTINENCE_C_NAME` | VARCHAR |  | The number of months the donor has abstained from cigarettes if the donor has a history of cigarette use. |
| 50 | `UNOS_OTH_TOBACCO_C_NAME` | VARCHAR |  | Indicates whether the donor has a history of other tobacco use. |
| 51 | `UNOS_DNR_DEATH_C_NAME` | VARCHAR |  | The cause of death if the living donor died. |
| 52 | `NONAUTOLOG_BLOOD_YN` | VARCHAR |  | Indicates whether non-autologous blood was administered to the donor. |
| 53 | `PRBC_UNIT_NUM` | INTEGER |  | The number of units the donor received for PRBC if non-autologous blood was administered to the donor. |
| 54 | `PLATELETS_UNIT_NUM` | INTEGER |  | The number of units the donor received for platelets if non-autologous blood was administered to the donor. |
| 55 | `FFP_UNIT_NUM` | INTEGER |  | The number of units the donor received for FFP if non-autologous blood was administered to the donor. |
| 56 | `KI_VSC_COMP_C_NAME` | VARCHAR |  | Indicates whether the donor experienced vascular complications requiring intervention during the first 6 weeks after the donation. |
| 57 | `KI_VSC_COMP_OTH` | VARCHAR |  | Free text description of the kidney vascular complication(s) if the donor experienced vascular complications requiring intervention during the first 6 weeks after the donation. |
| 58 | `KI_OTH_COMP_C_NAME` | VARCHAR |  | Indicates whether the donor experienced other complication requiring intervention during the first 6 weeks after the donation. |
| 59 | `KI_OTH_COMP_SP` | VARCHAR |  | Free text description of the kidney other complication(s) if the donor experienced vascular complications requiring intervention during the first 6 weeks after the donation. |
| 60 | `KI_REOP_C_NAME` | VARCHAR |  | Indicates whether the donor required reoperation the first 6 weeks after the donation. |
| 61 | `KI_REOP_BLEEDING_YN` | VARCHAR |  | Indicates whether bleeding is the reason for reoperation during first six weeks. |
| 62 | `KI_REOP_BLEEDING_DT` | DATETIME |  | The reoperation date if bleeding is the reason for reoperation during first six weeks. |
| 63 | `KI_REOP_HERN_REP_YN` | VARCHAR |  | Indicates whether hernia repair is the reason for reoperation during first six weeks. |
| 64 | `KI_REOP_HERN_REP_DT` | DATETIME |  | The reoperation date if hernia repair is the reason for reoperation during first six weeks. |
| 65 | `KI_REOP_BOW_OBST_YN` | VARCHAR |  | Indicates whether bowel obstruction is the reason for reoperation during first six weeks. |
| 66 | `KI_REOP_BOW_OBST_DT` | DATETIME |  | The reoperation date if bowel obstruction is the reason for reoperation during first six weeks. |
| 67 | `KI_REOP_VSC_YN` | VARCHAR |  | Indicates whether vascular is the reason for reoperation during first six weeks. |
| 68 | `KI_REOP_VSC_DT` | DATETIME |  | The reoperation date if vascular is the reason for reoperation during first six weeks. |
| 69 | `KI_REOP_OTH_YN` | VARCHAR |  | Indicates whether there is a specific reason for reoperation during first six weeks. |
| 70 | `KI_REOP_OTH_SP` | VARCHAR |  | Free text description of the reason for reoperation during first six weeks. |
| 71 | `KI_REOP_OTH_DT` | DATETIME |  | The reoperation date if there is a specific reason for reoperation during first six weeks. |
| 72 | `READMISSION_C_NAME` | VARCHAR |  | Indicates whether the donor required any readmission after the initial discharge during the first 6 weeks after the donation. |
| 73 | `READMISSION_SP` | VARCHAR |  | Free text description of the reason why the donor required readmission after the initial discharge during the first 6 weeks after the donation. |
| 74 | `READMISSION_DT` | DATETIME |  | The date of the first readmission. |
| 75 | `KI_OTH_PROC_C_NAME` | VARCHAR |  | Indicates whether the donor required other interventional procedures after the initial discharge during the first 6 weeks after the donation. |
| 76 | `KI_OTH_PROC_SP` | VARCHAR |  | Free text description of the procedure(s) if the donor required other interventional procedures after the initial discharge during the first 6 weeks after the donation. |
| 77 | `KI_OTH_PROC_DT` | DATETIME |  | The date of procedure if the donor required other interventional procedures after the initial discharge during the first 6 weeks after the donation. |
| 78 | `POSTOP_BP_SYSTOLIC` | INTEGER |  | The donor's systolic blood pressure within 6 weeks after the donation. |
| 79 | `POSTOP_BP_SYST_ST_C_NAME` | VARCHAR |  | The reason why the donor's systolic blood pressure is not available. |
| 80 | `POSTOP_BP_DIASTOLIC` | INTEGER |  | The donor's diastolic blood pressure within 6 weeks after the donation. |
| 81 | `POSTOP_BP_DIAS_ST_C_NAME` | VARCHAR |  | The reason why the donor's diastolic blood pressure is not available. |
| 82 | `POSTOP_URINE_RATIO` | NUMERIC |  | The donor's urinalysis protein-creatinine ratio within 6 weeks after the donation. |
| 83 | `POSTOP_URINE_PRTN_C_NAME` | VARCHAR |  | The donor's urinalysis urine protein within 6 weeks after the donation. |
| 84 | `DNR_HYPERTNSN_MED_C_NAME` | VARCHAR |  | Indicates whether donor developed hypertension requiring medication within 6 weeks after the donation. |
| 85 | `ORGAN_RECOVERY_DT` | DATETIME |  | Date of donor organ recovery. |
| 86 | `UNOS_CATSCAN_C_NAME` | VARCHAR |  | Indicates whether a CAT scan was performed for the patient. |
| 87 | `UNOS_CATSCAN_SP` | VARCHAR |  | The patient's CAT scan result. |
| 88 | `UNOS_MRI_C_NAME` | VARCHAR |  | Indicates whether an MRI was performed for the patient. |
| 89 | `UNOS_MRI_SP` | VARCHAR |  | The patient's MRI result. |
| 90 | `UNOS_ULTRASND_C_NAME` | VARCHAR |  | Indicates whether an ultrasound was performed for the patient. |
| 91 | `UNOS_ULTRASND_SP` | VARCHAR |  | The patient's ultrasound result. |
| 92 | `READMISSION_DT_ST_C_NAME` | VARCHAR |  | The reason why the first readmission date is not available. |
| 93 | `KI_COMP_C_NAME` | VARCHAR |  | Indicates whether the donor experienced kidney complications. |
| 94 | `KI_COMP_SP` | VARCHAR |  | Free text description of the type of kidney complications. |
| 95 | `UNOS_DNR_DEATH_SP` | VARCHAR |  | Free text description of the cause of death if the living donor died. |
| 96 | `UNOS_RECOVR_ORG_C_NAME` | VARCHAR |  | The organ recovered from the donor that is being addressed by this form. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

