# UNOS_CLIN_INFO_4

> Additional information reported to the United Network for Organ Sharing (UNOS) for each of the registry records or forms.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 105

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `C_PEPTIDE` | NUMERIC |  | The patient's most recent C-peptide lab value |
| 3 | `C_PEPTIDE_ST_C_NAME` | VARCHAR |  | The status item for the C-peptide result |
| 4 | `HBA1C` | NUMERIC |  | The patient's HbA1c |
| 5 | `HBA1C_ST_C_NAME` | VARCHAR |  | The HbA1c status for the patient |
| 6 | `PAT_ON_INSULIN_C_NAME` | VARCHAR |  | Whether the patient is on insulin |
| 7 | `INSULIN_RES_DT_C_NAME` | VARCHAR |  | The status for the insulin resumed date |
| 8 | `INSULIN_DOSE` | INTEGER |  | The patient's insulin dosage |
| 9 | `INSULIN_DOSE_DT_ST_C_NAME` | VARCHAR |  | The insulin dosage status |
| 10 | `BLOOD_SUGAR_CTL_C_NAME` | VARCHAR |  | Indicates if the patient is using blood sugar control |
| 11 | `ORAL_BLD_SGR_MED_C_NAME` | VARCHAR |  | Indicates whether the patient is on oral medications for blood sugar control |
| 12 | `ORAL_MED_RSM_DT` | DATETIME |  | The date the patient resumed oral medication for blood sugar control |
| 13 | `ORAL_MED_RSM_DT_S_C_NAME` | VARCHAR |  | The reason there is no blood sugar resumed date |
| 14 | `ON_DIABETIC_DIET_C_NAME` | VARCHAR |  | Indicates whether the patient is on a diabetic diet |
| 15 | `INSULIN_DUR` | INTEGER |  | The insulin duration |
| 16 | `INSULIN_DUR_ST_C_NAME` | VARCHAR |  | The insulin duration status |
| 17 | `UNOS_PFT1_DATE` | DATETIME |  | The date of the transplant patient's first set of pulmonary function tests during the follow-up period. |
| 18 | `UNOS_PFT1_DATE_ST_C_NAME` | VARCHAR |  | The reason the Pulmonary Function Test (1): Date test performed field is blank. |
| 19 | `UNOS_PFT1_FEV1` | NUMERIC |  | The transplant patient's FEV1 in L for the first set of pulmonary function tests during the follow-up period. |
| 20 | `UNOS_PFT1_FEV1_ST_C_NAME` | VARCHAR |  | The reason the Pulmonary Function Test (1): FEV1 field is blank. |
| 21 | `UNOS_PFT1_FVC` | NUMERIC |  | The transplant patient's FVC in L for the first set of pulmonary function tests during the follow-up period. |
| 22 | `UNOS_PFT1_FVC_ST_C_NAME` | VARCHAR |  | The reason the Pulmonary Function Test (1): FVC field is blank. |
| 23 | `UNOS_PFT1_FEF2575` | NUMERIC |  | The transplant patient's FEF 25-75 in L/sec for the first set of pulmonary function tests during the follow-up period. |
| 24 | `UNOS_PFT1_FEF_ST_C_NAME` | VARCHAR |  | The reason the Pulmonary Function Test (1): FEF 25-75 field is blank. |
| 25 | `UNOS_PFT2_DATE` | DATETIME |  | The date of the transplant patient's second set of pulmonary function tests during the follow-up period. |
| 26 | `UNOS_PFT2_DATE_ST_C_NAME` | VARCHAR |  | The reason the Pulmonary Function Test (2): Date test performed field is blank. |
| 27 | `UNOS_PFT2_FEV1` | NUMERIC |  | The transplant patient's FEV1 in L for the second set of pulmonary function tests during the follow-up period. |
| 28 | `UNOS_PFT2_FEV1_ST_C_NAME` | VARCHAR |  | The reason the Pulmonary Function Test (2): FEV1 field is blank. |
| 29 | `UNOS_PFT2_FVC` | NUMERIC |  | The transplant patient's FVC in L for the second set of pulmonary function tests during the follow-up period. |
| 30 | `UNOS_PFT2_FVC_ST_C_NAME` | VARCHAR |  | The reason the Pulmonary Function Test (2): FVC field is blank. |
| 31 | `UNOS_PFT2_FEF2575` | NUMERIC |  | The transplant patient's FEF 25-75 in L/sec for the second set of pulmonary function tests during the follow-up period. |
| 32 | `UNOS_PFT2_FEF_ST_C_NAME` | VARCHAR |  | The reason the Pulmonary Function Test (2): FEF 25-75 field is blank. |
| 33 | `UNOS_PFT3_DATE` | DATETIME |  | The date of the transplant patient's third set of pulmonary function tests during the follow-up period. |
| 34 | `UNOS_PFT3_DATE_ST_C_NAME` | VARCHAR |  | The reason the Pulmonary Function Test (3): Date test performed field is blank. |
| 35 | `UNOS_PFT3_FEV1` | NUMERIC |  | The transplant patient's FEV1 in L for the third set of pulmonary function tests during the follow-up period. |
| 36 | `UNOS_PFT3_FEV1_ST_C_NAME` | VARCHAR |  | The reason the Pulmonary Function Test (3): FEV1 field is blank. |
| 37 | `UNOS_PFT3_FVC` | NUMERIC |  | The transplant patient's FVC in L for the third set of pulmonary function tests during the follow-up period. |
| 38 | `UNOS_PFT3_FVC_ST_C_NAME` | VARCHAR |  | The reason the Pulmonary Function Test (3): FVC field is blank. |
| 39 | `UNOS_PFT3_FEF2575` | NUMERIC |  | The transplant patient's FEF 25-75 in L/sec for the third set of pulmonary function tests during the follow-up period. |
| 40 | `UNOS_PFT3_FEF_ST_C_NAME` | VARCHAR |  | The reason the Pulmonary Function Test (3): FEF 25-75 field is blank. |
| 41 | `UNOS_SUPPO2_YN` | VARCHAR |  | Whether the transplant patient required supplemental oxygen during the follow-up period. |
| 42 | `UNOS_FIO2_REST` | INTEGER |  | The transplant patient's percentage of inspired oxygen required at rest during the follow-up period. |
| 43 | `UNOS_FIO2_REST_ST_C_NAME` | VARCHAR |  | The reason the FiO2 at rest field is blank. |
| 44 | `UNOS_O2FLOW_REST` | NUMERIC |  | The transplant patient's oxygen flow required at rest in L/min during the follow-up period. |
| 45 | `UNOS_O2FLOW_REST_ST_C_NAME` | VARCHAR |  | The reason the Flow at rest field is blank. |
| 46 | `UNOS_FIO2_EXERCISE` | INTEGER |  | The transplant patient's percentage of inspired oxygen required with exercise during the follow-up period. |
| 47 | `UNOS_FIO2_EXERCISE_ST_C_NAME` | VARCHAR |  | The reason the FiO2 with exercise field is blank. |
| 48 | `UNOS_O2FLOW_EXERCISE` | NUMERIC |  | The transplant patient's oxygen flow required with exercise in L/min during the follow-up period. |
| 49 | `UNOS_O2FLOW_EXERCISE_ST_C_NAME` | VARCHAR |  | The reason the Flow with exercise field is blank. |
| 50 | `UNOS_EPSD_VT_C_NAME` | VARCHAR |  | Indicates whether the transplant patient had ventilatory support. |
| 51 | `UNOS_EPSD_VT_TIME_C_NAME` | VARCHAR |  | The timeframe of the transplant patient’s ventilatory support. |
| 52 | `UNOS_TRACH_C_NAME` | VARCHAR |  | Indicates whether the transplant patient had a tracheostomy. |
| 53 | `UNOS_HR_PROC_C_NAME` | VARCHAR |  | The heart procedure used for the transplant. |
| 54 | `UNOS_HRHL_ISCH` | INTEGER |  | The heart total ischemia time in minutes. |
| 55 | `UNOS_HRHL_ISCH_ST_C_NAME` | VARCHAR |  | The reason why the heart total ischemia time field is empty. |
| 56 | `UNOS_LLU_ISCH` | INTEGER |  | The left lung total ischemia time in minutes. Submitted to UNOS for field name lu_isch. |
| 57 | `UNOS_LLU_ISCH_ST_C_NAME` | VARCHAR |  | The reason why the left lung total ischemia time field is empty. Submitted to UNOS for field name lu_isch_i. |
| 58 | `UNOS_RLU_ISCH` | INTEGER |  | The right lung total ischemia time in minutes. Submitted to UNOS for field name lu2_isch. |
| 59 | `UNOS_RLU_ISCH_ST_C_NAME` | VARCHAR |  | The reason why the right lung total ischemia time field is empty. Submitted to UNOS for field name lu2_isch_i. |
| 60 | `UNOS_PST_STROKE_C_NAME` | VARCHAR |  | Indicates whether the transplant patient had a stroke post-transplant but prior to discharge. |
| 61 | `UNOS_PST_DIALYSIS_C_NAME` | VARCHAR |  | Indicates whether the transplant patient had dialysis post-transplant but prior to discharge. |
| 62 | `UNOS_PST_VENT_C_NAME` | VARCHAR |  | Indicates whether the transplant patient had ventilator support post-transplant but prior to discharge. |
| 63 | `UNOS_PST_REINTUB_C_NAME` | VARCHAR |  | Indicates whether the transplant patient was reintubated post-transplant but prior to discharge. |
| 64 | `UNOS_PST_AIR_DEHI_C_NAME` | VARCHAR |  | Indicates whether the transplant patient had airway dehiscence post-transplant but prior to discharge. |
| 65 | `UNOS_PRE_A_TITER_C_NAME` | VARCHAR |  | The transplant patient's most recent pre-transplant anti-A titer. This field only applies if the recipient's ABO blood type is B or O. |
| 66 | `UNOS_PRE_TITER_A_DT` | DATETIME |  | The date of the transplant patient's most recent pre-transplant anti-A titer. |
| 67 | `UNOS_PRE_B_TITER_C_NAME` | VARCHAR |  | The transplant patient's most recent pre-transplant anti-B titer. This field only applies if the recipient's ABO blood type is A or O. |
| 68 | `UNOS_PRE_TITER_B_DT` | DATETIME |  | The date of the transplant patient's most recent pre-transplant anti-B titer. |
| 69 | `UNOS_CARDIAC_INDEX` | INTEGER |  | The transplant patient's most recent cardiac index in L/min/m^2 during the reporting period. |
| 70 | `UNOS_INTUB_72HR_C_NAME` | VARCHAR |  | Indicates whether the transplant patient was intubated at 72 hours after transplant. |
| 71 | `UNOS_PAO2_72HR` | INTEGER |  | The transplant patient's PaO2 in mm/Hg at 72 hours after transplant. |
| 72 | `UNOS_FIO2_72HR` | INTEGER |  | The transplant patient's percentage of inspired oxygen required at 72 hours after transplant. |
| 73 | `UNOS_EMCO_72HR_C_NAME` | VARCHAR |  | Indicates whether extracorporeal membrane oxygenation was used on the transplant patient at 72 hours after transplant. |
| 74 | `UNOS_NO_72HR_C_NAME` | VARCHAR |  | Indicates whether the transplant patient inhaled nitric oxide at 72 hours after transplant. |
| 75 | `UNOS_PAO2_72HR_ST_C_NAME` | VARCHAR |  | The reason the PaO2 at 72 hours field is blank. |
| 76 | `UNOS_FIO2_72HR_ST_C_NAME` | VARCHAR |  | The reason the FiO2 at 72 hours field is blank. |
| 77 | `UNOS_LU_PERFUSED_YN` | VARCHAR |  | Indicates whether the transplant organs were perfused prior to transplant. |
| 78 | `UNOS_PERFSN_LOC_C_NAME` | VARCHAR |  | The location at which the transplant organs were perfused prior to transplant. |
| 79 | `UNOS_PERFSN_PERF_C_NAME` | VARCHAR |  | Who performed the perfusion on the transplant organs prior to transplant. |
| 80 | `UNOS_TIME_ON_PERFSN` | INTEGER |  | The total time in minutes the transplant organs were on perfusion prior to transplant. |
| 81 | `UNOS_TIME_PERF_ST_C_NAME` | VARCHAR |  | The reason why the total time on perfusion field is blank. |
| 82 | `UNOS_LLU_RCD_C_NAME` | VARCHAR |  | How the left lung was received at the transplant center. |
| 83 | `UNOS_RLU_RCD_C_NAME` | VARCHAR |  | How the right lung was received at the transplant center. |
| 84 | `SURG_NAME` | VARCHAR |  | The name of the surgeon who last saw the transplant patient. |
| 85 | `SURG_NPI` | VARCHAR |  | The National Provider Identifier (NPI) of the surgeon who last saw the transplant patient. |
| 86 | `UNOS_STEROID_C_NAME` | VARCHAR |  | Indicates whether the transplant patient has a chronic steroid prescription. |
| 87 | `UNOS_TRNSFSNS_C_NAME` | VARCHAR |  | Indicates whether the transplant patient has undergone transfusions between listing and transplant. |
| 88 | `UNOS_HL_PROC_TYP_C_NAME` | VARCHAR |  | The heart or lung procedure type used for the transplant. |
| 89 | `UNOS_PA_PRIM_DX_C_NAME` | VARCHAR |  | UNOS pancreas primary diagnosis |
| 90 | `UNOS_PA_PRIM_DX_SP` | VARCHAR |  | UNOS pancreas primary diagnosis, specify |
| 91 | `UNOS_PA_GR_PLCMNT_C_NAME` | VARCHAR |  | UNOS pancreas graft placement |
| 92 | `UNOS_PA_OP_TECH_C_NAME` | VARCHAR |  | UNOS pancreas operative technique |
| 93 | `UNOS_PA_DUCT_MGMT_C_NAME` | VARCHAR |  | UNOS pancreas duct management |
| 94 | `UNOS_PA_DUCT_MGM_SP` | VARCHAR |  | UNOS pancreas duct management, specify |
| 95 | `UNOS_PA_VNS_MGMT_C_NAME` | VARCHAR |  | UNOS pancreas venous vascular management |
| 96 | `UNOS_PA_ART_RCN_C_NAME` | VARCHAR |  | UNOS pancreas arterial reconstruction |
| 97 | `UNOS_PA_ART_RCN_SP` | VARCHAR |  | UNOS pancreas arterial reconstruction, specify |
| 98 | `UNOS_PA_VNS_EXT_YN` | VARCHAR |  | UNOS pancreas venous extension graft |
| 99 | `UNOS_PA_TOT_PRES` | NUMERIC |  | UNOS pancreas total preservation time (hours) |
| 100 | `UNOS_PA_TOT_PR_ST_C_NAME` | VARCHAR |  | UNOS pancreas total preservation time status |
| 101 | `UNOS_PA_HYP_REJ_C_NAME` | VARCHAR |  | UNOS pancreas contributory cause of graft failure: hyperacute rejection |
| 102 | `UNOS_WT_POST_TX` | NUMERIC |  | The patient's post-transplant weight |
| 103 | `UNOS_WT_POST_ST_C_NAME` | VARCHAR |  | The patient's post-transplant weight status |
| 104 | `UNOS_INSLN_POST_TX` | NUMERIC |  | UNOS average total insulin dosage per day post-transplant |
| 105 | `UNOS_INS_PST_ST_C_NAME` | VARCHAR |  | UNOS average total insulin dosage per day post-transplant status |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

