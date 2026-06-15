# UNOS_CLIN_INFO_2

> Additional information reported to the United Network for Organ Sharing (UNOS) for each of the registry records or forms.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 98

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `UNOS_SEC_DX_C_NAME` | VARCHAR |  | Transplant patient's secondary diagnosis. |
| 3 | `UNOS_SEC_DX_OTH` | VARCHAR |  | Free text description of transplant patient's the secondary diagnosis. |
| 4 | `UNOS_PULM_EMB_C_NAME` | VARCHAR |  | Indicates whether the candidate was diagnosed with a pulmonary embolism within the past six months. |
| 5 | `UNOS_VARICES_BLD_C_NAME` | VARCHAR |  | Indicates whether the candidate was experiencing bleeding from varices present in the esophagus and/or stomach within two weeks prior to listing. |
| 6 | `UNOS_LVR_SURG_PX_C_NAME` | VARCHAR |  | The surgical procedure type used for liver transplant. |
| 7 | `UNOS_LVR_PROC_TYP_C_NAME` | VARCHAR |  | The procedure used for liver transplant. |
| 8 | `UNOS_LVR_SPLT_TYP_C_NAME` | VARCHAR |  | The split type used for liver transplant. |
| 9 | `UNOS_LVR_5_PRBC_C_NAME` | VARCHAR |  | Indicates whether the recipient received five or more units of packed red blood cells within 48 hours prior to transplantation due to spontaneous hypertensive bleeding. |
| 10 | `UNOS_LVR_BCTRL_PT_C_NAME` | VARCHAR |  | Indicates whether the recipient was experiencing bacterial peritonitis. |
| 11 | `UNOS_LVR_ABDO_SUR_C_NAME` | VARCHAR |  | Indicates whether the recipient had abdominal surgery prior to transplant. |
| 12 | `UNOS_LVR_PVT_C_NAME` | VARCHAR |  | Indicates whether the recipient experienced portal vein thrombosis prior to transplant. |
| 13 | `UNOS_LVR_TIPSS_C_NAME` | VARCHAR |  | Indicates whether the recipient required TIPSS (transjugular intrahepatic portosystemic shunt) prior to transplant. |
| 14 | `UNOS_LVR_TUM_TYP_C_NAME` | VARCHAR |  | The type of incidental tumor found at the time of transplant. |
| 15 | `UNOS_WARM_ISCH_TM` | NUMERIC |  | The total warm ischemia time for the liver, in minutes. |
| 16 | `UNOS_WARM_ISCH_ST_C_NAME` | VARCHAR |  | If the total warm ischemia time is unavailable for the liver, this indicates why the information is unavailable. |
| 17 | `UNOS_COLD_ISCH_TM` | NUMERIC |  | The total cold ischemia time for the liver, in hours. If a pump is used, this includes pump time. |
| 18 | `UNOS_COLD_ISCH_ST_C_NAME` | VARCHAR |  | If the total cold ischemia time is unavailable for the liver, this indicates why the information is unavailable. |
| 19 | `UNOS_LF_SPT_ECMO_C_NAME` | VARCHAR |  | Indicates whether the patient was on an extracorporeal membrane oxygenation machine for life support at the time of UNOS registration |
| 20 | `UNOS_LF_SPT_AORP_C_NAME` | VARCHAR |  | Indicates whether the patient was on an intra-aortic balloon pump device for life support at the time of UNOS registration |
| 21 | `UNOS_LF_SPT_PRINF_C_NAME` | VARCHAR |  | Indicates whether the patient is on a prostacyclin infusion for life support at the time of UNOS registration |
| 22 | `UNOS_LF_SPT_PRINH_C_NAME` | VARCHAR |  | Indicates whether the patient is on a prostacyclin inhalation machine for life support at the time of UNOS registration |
| 23 | `UNOS_LF_SPT_INHNO_C_NAME` | VARCHAR |  | Indicates whether the patient is receiving inhaled nitric oxide for life support at the time of UNOS registration |
| 24 | `UNOS_LF_SPT_VAD_C_NAME` | VARCHAR |  | Indicates whether the patient is using a ventricular assist device at the time of UNOS registration |
| 25 | `UNOS_LF_SPT_VADB1_C_NAME` | VARCHAR |  | Indicates the brand of the first ventricular assist device used by the patient at the time of UNOS registration |
| 26 | `UNOS_LF_SPT_VADB2_C_NAME` | VARCHAR |  | Indicates the brand of a second ventricular assist device used by the patient at the time of UNOS registration |
| 27 | `UNOS_LF_SPT_VAD1S` | VARCHAR |  | The brand name of the first ventricular assist device being used if the brand is not in the UNOS-defined table |
| 28 | `UNOS_LF_SPT_VAD2S` | VARCHAR |  | The brand name of the second ventricular assist device being used if the brand is not in the UNOS-defined table |
| 29 | `UNOS_ANG_THOR_C_NAME` | VARCHAR |  | Indicates the thoracic transplant patient's angina status at the time of UNOS registration |
| 30 | `UNOS_SDEATH_C_NAME` | VARCHAR |  | Indicates whether the patient is at risk of sudden death at the time of UNOS registration |
| 31 | `UNOS_AMIOD_C_NAME` | VARCHAR |  | Indicates whether the patient is on an amiodarone medication at the time of UNOS registration |
| 32 | `UNOS_DEFIB_IMP_C_NAME` | VARCHAR |  | Indicates whether the patient has an implantable defibrillator at the time of UNOS registration |
| 33 | `UNOS_IV_INFECT_C_NAME` | VARCHAR |  | Indicates whether the patient had an infection requiring IV drug therapy within the 2 weeks prior to the time of UNOS registration |
| 34 | `UNOS_EX_O2` | NUMERIC |  | The amount of oxygen consumed during exercise (ml/min/kg) at the time of UNOS registration |
| 35 | `UNOS_EX_O2_ST_C_NAME` | VARCHAR |  | The reason there is no value for exercise oxygen consumption at the time of UNOS registration |
| 36 | `UNOS_FVC` | NUMERIC |  | The patient's forced vital capacity (% predicted) at the time of UNOS registration |
| 37 | `UNOS_FVC_ST_C_NAME` | VARCHAR |  | The reason there is no value for forced vital capacity at the time of UNOS registration |
| 38 | `UNOS_PCO2` | NUMERIC |  | The patient's partial pressure of carbon dioxide (mm/Hg) at the time of UNOS registration |
| 39 | `UNOS_PCO2_ST_C_NAME` | VARCHAR |  | The reason there is no value for carbon dioxide partial pressure at the time of UNOS registration |
| 40 | `UNOS_PUL_SEPS_IV_C_NAME` | VARCHAR |  | Indicates whether the patient experienced at least two pulmonary sepsis episodes treated by IV medications at the time of UNOS registration |
| 41 | `UNOS_CORT_DEP_C_NAME` | VARCHAR |  | Indicates whether the patient is dependent on at least 5 mg/day of corticosteroids at the time of UNOS registration |
| 42 | `UNOS_SIX_MIN_WALK` | NUMERIC |  | The number of feet the patient is able to walk in 6 minutes at the time of UNOS registration |
| 43 | `UNOS_PNRES_LNG_BC_C_NAME` | VARCHAR |  | Indicates whether the patient suffers from a pan-resistant bacterial lung at the time of UNOS registration |
| 44 | `UNOS_CARD_SURG_C_NAME` | VARCHAR |  | Indicates whether the patient has undergone any non-transplant cardiac surgery prior to UNOS registration |
| 45 | `UNOS_CARD_SURG_S` | VARCHAR |  | Description of a cardiac surgery the patient has undergone prior to UNOS registration that is not on the UNOS-defined category list |
| 46 | `UNOS_LUNG_SURG_C_NAME` | VARCHAR |  | Indicates whether the patient has undergone any non-transplant lung surgery prior to UNOS registration |
| 47 | `UNOS_LUNG_SURG_S` | VARCHAR |  | Description of a lung surgery the patient has undergone prior to UNOS registration that is not on the UNOS-defined category list |
| 48 | `UNOS_IV_INOTROPES_C_NAME` | VARCHAR |  | Indicates whether the patient is on intravenous inotropes for life support at the time of UNOS registration |
| 49 | `UNOS_THOR_SURG_C_NAME` | VARCHAR |  | Indicates whether the pediatric the patient has undergone any non-transplant thoracic surgery prior to UNOS registration |
| 50 | `UNOS_STERNO_C_NAME` | VARCHAR |  | The number of sternotomies the patient has undergone prior to UNOS registration |
| 51 | `UNOS_THORAC_C_NAME` | VARCHAR |  | The number of thoracotomies the patient has undergone prior to UNOS registration |
| 52 | `UNOS_CONGEN_CARD_C_NAME` | VARCHAR |  | Indicates whether the patient has undergone surgery for a congenital cardiac condition prior to UNOS registration |
| 53 | `UNOS_PALLIA_SURG_C_NAME` | VARCHAR |  | Indicates whether the patient has undergone palliative surgery prior to UNOS registration |
| 54 | `UNOS_CORR_SURG_C_NAME` | VARCHAR |  | Indicates whether the patient has undergone corrective surgery prior to UNOS registration |
| 55 | `UNOS_SING_VENT_C_NAME` | VARCHAR |  | Indicates whether the patient has undergone surgery for a single ventricular prior to UNOS registration |
| 56 | `UNOS_FEV1FVC` | NUMERIC |  | The ratio of forced expiratory volume in one second to forced vital capacity at the time of UNOS registration |
| 57 | `UNOS_FEV1FVC_ST_C_NAME` | VARCHAR |  | The reason there is no value for the ratio of forced expiratory volume in one second to forced vital capacity at the time of UNOS registration |
| 58 | `UNOS_ANTI_ARRYTH_C_NAME` | VARCHAR |  | Indicates whether the patient is on an antiarrythmic agent at the time of UNOS registration |
| 59 | `UNOS_CRDO` | NUMERIC |  | The cardiac output of the patient (L/min) at the time of UNOS registration |
| 60 | `UNOS_CRDO_ST_C_NAME` | VARCHAR |  | The reason there is no value for cardiac output at the time of UNOS registration |
| 61 | `UNOS_CRDO_INOVAS_YN` | VARCHAR |  | Indicates whether the patient was on inotropes or vasodilators that affected the cardiac output reading |
| 62 | `UNOS_PCW_AVG` | NUMERIC |  | The average pulmonary capillary wedge pressure (mm/Hg) at the time of UNOS registration |
| 63 | `UNOS_PCW_AVG_ST_C_NAME` | VARCHAR |  | The reason there is no value for the average pulmonary capillary wedge pressure at the time of UNOS registration |
| 64 | `UNOS_PCW_AVG_INV_YN` | VARCHAR |  | Indicates whether the patient was on inotropes or vasodilators that affected the average pulmonary capillary wedge pressure reading |
| 65 | `UNOS_PA_SYS` | NUMERIC |  | The systolic blood pressure of the patient's pulmonary artery (mm/Hg) at the time of UNOS registration |
| 66 | `UNOS_PA_SYS_ST_C_NAME` | VARCHAR |  | The reason there is no value for the pulmonary artery systolic blood pressure at the time of UNOS registration |
| 67 | `UNOS_PA_SYS_INOV_YN` | VARCHAR |  | Indicates whether the patient was on inotropes or vasodilators that affected the pulmonary artery systolic blood pressure reading |
| 68 | `UNOS_PA_DIA` | NUMERIC |  | The diastolic blood pressure of the patient's pulmonary artery (mm/Hg) at the time of UNOS registration |
| 69 | `UNOS_PA_DIA_ST_C_NAME` | VARCHAR |  | The reason there is no value for the pulmonary artery diastolic blood pressure at the time of UNOS registration |
| 70 | `UNOS_PA_DIA_INOV_YN` | VARCHAR |  | Indicates whether the patient was on inotropes or vasodilators that affected the pulmonary artery diastolic blood pressure reading |
| 71 | `UNOS_PA_AVG` | NUMERIC |  | The average blood pressure of the patient's pulmonary artery (mm/Hg) at the time of UNOS registration |
| 72 | `UNOS_PA_AVG_ST_C_NAME` | VARCHAR |  | The reason there is no value for the average pulmonary artery blood pressure at the time of UNOS registration |
| 73 | `UNOS_PA_AVG_INVS_YN` | VARCHAR |  | Indicates whether the patient was on inotropes or vasodilators that affected the average pulmonary artery blood pressure reading |
| 74 | `UNOS_LF_SPT_PGLAN_C_NAME` | VARCHAR |  | Indicates whether the patient was on an prostaglandins for life support at the time of UNOS registration |
| 75 | `UNOS_TITER_A_C_NAME` | VARCHAR |  | The current A titer value If the recipient's ABO blood-type is B or O. |
| 76 | `UNOS_TITER_B_C_NAME` | VARCHAR |  | The current B titer value If the recipient's ABO blood-type is A or O. |
| 77 | `HX_OF_HCC_YN` | VARCHAR |  | Indicates whether the patient ever had a diagnosis of HCC. |
| 78 | `NEOADJUVANT_YN` | VARCHAR |  | Indicates whether the patient received neoadjuvant therapy. |
| 79 | `CMV_STATUS_C_NAME` | VARCHAR |  | Stores the patient's CMV status. |
| 80 | `UNOS_HBV_SURFACE_C_NAME` | VARCHAR |  | The patient's HBV surface antibody total results. |
| 81 | `UNOS_OPO` | VARCHAR |  | The OPO that recovered the organ. |
| 82 | `UNOS_RIGHT_RESIST` | NUMERIC |  | The final resistance at the time of transplant for the right kidney. |
| 83 | `UNOS_R_F_TXP_RSTN_C_NAME` | VARCHAR |  | If the final resistance level is unavailable, this indicates why the information is unavailable. |
| 84 | `UNOS_R_FIN_FLOW_RT` | NUMERIC |  | If a pump was used, the final flow rate for the right kidney. |
| 85 | `UNOS_R_FN_FLOW_RT_C_NAME` | VARCHAR |  | If the final flow rate is unavailable, this indicates why the information is unavailable. |
| 86 | `UNOS_DIFF_CHOLANG_C_NAME` | VARCHAR |  | Indicates if the organ failed due to diffuse cholangiopathy. |
| 87 | `ER_URGENT_C_NAME` | VARCHAR |  | Indicates if the patient was admitted to the ER or Urgent care during the follow-up period related to the transplant. |
| 88 | `CREAT_DT` | DATETIME |  | Stores the date the patient's most recent creatinine test was drawn. |
| 89 | `SYS_BP_DT` | DATETIME |  | The date that the patient's systolic blood pressure was read. |
| 90 | `DIA_BP_DT` | DATETIME |  | The date that the patient's diastolic blood pressure was read. |
| 91 | `CNTRY_RESIDENCE_C_NAME` | VARCHAR |  | The patient's country of permanent residence. |
| 92 | `YR_OF_ENTRY_ST_C_NAME` | VARCHAR |  | Reason the year of entry to the US is missing. |
| 93 | `INSURANCE_LOSS_C_NAME` | VARCHAR |  | Indicates if the patient has lost insurance coverage due to the donation. |
| 94 | `UNOS_HEIGHT_DATE` | DATETIME |  | The date the patient's height was measured. |
| 95 | `UNOS_WEIGHT_DATE` | DATETIME |  | The date the patient's weight was measured. |
| 96 | `UNOS_HEP_B_C_NAME` | VARCHAR |  | Indicate if the patient receive a hepatitis B vaccine. |
| 97 | `UNOS_NO_HEPB_RSN_C_NAME` | VARCHAR |  | Indicates the reason the patient has not received a hepatitis B vaccine. |
| 98 | `UNOS_NO_HEPB_RSN_OTHR` | VARCHAR |  | Indicates the free-text reason the patient has not received a hepatitis B vaccine. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

