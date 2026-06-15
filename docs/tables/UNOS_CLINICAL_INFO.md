# UNOS_CLINICAL_INFO

> Additional information reported to the United Network for Organ Sharing (UNOS) for each of the registry records or forms.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 257  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique ID of the registry record. |
| 2 | `UNOS_ORGAN_C_NAME` | VARCHAR |  | The type of organ transplanted. |
| 3 | `UNOS_CARE_PROV_BY_C_NAME` | VARCHAR |  | The place or type of provider responsible for the patient's follow-up care. |
| 4 | `UNOS_CARE_PROV_OTH` | VARCHAR |  | If different from common answers, the specified place or type of provider responsible for the patient's follow-up care. This clarifies the answer in the UNOS_CARE_PROV_BY_C column. |
| 5 | `UNOS_WAS_HOSP_C_NAME` | VARCHAR |  | Specifies whether the patient was hospitalized during the follow-up period. |
| 6 | `UNOS_NBR_HOSP_ADMIT` | INTEGER |  | Specifies the number of hospitalizations during the follow-up period. |
| 7 | `UNOS_HOSP_STAT_C_NAME` | VARCHAR |  | If the number of hospitalizations is unspecified, this field indicates why. |
| 8 | `UNOS_CLIN_RSCH_YN` | VARCHAR |  | Specifies whether the patient participated in any clinical research protocols for immunosuppressive medications. |
| 9 | `UNOS_CLIN_RSCH_SPEC` | VARCHAR |  | If the patient participated in any protocols for immunosuppressive medications, this specifies which ones. |
| 10 | `UNOS_DISEASE_RCR_C_NAME` | VARCHAR |  | Indicates the presence or absense of disease recurrence. |
| 11 | `UNOS_IMM_NONCOMP_C_NAME` | VARCHAR |  | Indicates whether there was evidence of patient non-compliance with immunosuppressive medications that could have compromised the patient's recovery. |
| 12 | `UNOS_MAINT_MEDS_C_NAME` | VARCHAR |  | Specifies whether maintenance immunosuppressive medications were given during the follow-up period. |
| 13 | `UNOS_IMM_DISC_YN` | VARCHAR |  | Indicates whether the physician discontinued all immunosuppressive medications. |
| 14 | `UNOS_CREATININE` | NUMERIC |  | The patient's most recent serum creatinine. |
| 15 | `UNOS_CREAT_ST_C_NAME` | VARCHAR |  | The reason why the most recent serum creatinine is unspecified. |
| 16 | `UNOS_ACUTE_REJ_C_NAME` | VARCHAR |  | Indicates whether there were any acute rejections during the last follow-up period. |
| 17 | `UNOS_BX_CONFIRM_C_NAME` | VARCHAR |  | Indicates whether a biopsy was done to confirm acute rejection. |
| 18 | `UNOS_MALG_POSTTXP_C_NAME` | VARCHAR |  | Indicates whether any post-transplant malignancies were found during the follow-up period. |
| 19 | `UNOS_MALG_DNR_REL_C_NAME` | VARCHAR |  | Indicates whether discovered post-transplant malignancies were related to the donor. |
| 20 | `UNOS_MALG_PRETXP_C_NAME` | VARCHAR |  | Indicates whether discovered post-transplant malignancies were recurrences of a pre-transplant tumor. |
| 21 | `UNOS_MALG_NOVO_T_C_NAME` | VARCHAR |  | Indicates whether discovered post-transplant malignancies were new solid tumors. |
| 22 | `UNOS_MALG_LYMPH_C_NAME` | VARCHAR |  | Indicates whether discovered post-transplant malignancies were new Lymphoproliferative disease and Lymphoma. |
| 23 | `UNOS_DIABETES_FP_C_NAME` | VARCHAR |  | Specifies whether the patient had an onset of diabetes during the follow-up period. |
| 24 | `UNOS_INSULIN_DEP_C_NAME` | VARCHAR |  | Indicates whether the patient is insulin dependent. |
| 25 | `UNOS_CAD_C_NAME` | VARCHAR |  | Indicates whether the patient was diagnosed with coronary artery disease during the follow-up period. |
| 26 | `UNOS_FRAC_PASTYR_C_NAME` | VARCHAR |  | Indicates whether the patient had any bone fractures either in the past year or since the last follow-up period. |
| 27 | `UNOS_FRAC_SPINE_YN` | VARCHAR |  | Indicates whether the patient had any spine compression fractures either in the past year or since the last follow-up period. |
| 28 | `UNOS_FRAC_SPINE_NUM` | INTEGER |  | The patient's number of spine compression fractures either in the past year or since the last follow-up period. |
| 29 | `UNOS_FRAC_EXTRM_YN` | VARCHAR |  | Indicates whether the patient had any extremity fractures either in the past year or since the last follow-up period. |
| 30 | `UNOS_FRAC_EXTRM_NUM` | INTEGER |  | The patient's number of extremity fractures either in the past year or since the last follow-up period. |
| 31 | `UNOS_FRAC_OTHER_YN` | VARCHAR |  | Indicates whether the patient had any other fractures either in the past year or since the last follow-up period. |
| 32 | `UNOS_FRAC_OTHER_NUM` | INTEGER |  | The patient's number of other fractures either in the past year or since the last follow-up period. |
| 33 | `UNOS_AVN_C_NAME` | VARCHAR |  | Indicates whether the patient was diagnosed with Avascular Necrosis (AVN) during the follow-up period. |
| 34 | `UNOS_PRI_DEATH_C_NAME` | VARCHAR |  | The patient's primary cause of death. |
| 35 | `UNOS_PRI_DEATH_OTH` | VARCHAR |  | Specifies the primary cause of death for the kidney graft recipient if that cause of death was not picked from a list. |
| 36 | `UNOS_SEC_DEATH_C_NAME` | VARCHAR |  | The patient's contributory cause of death. |
| 37 | `UNOS_SEC_DEATH_OTH1` | VARCHAR |  | The free-text description of the patient's contributory cause of death. |
| 38 | `UNOS_SEC_DEATH2_C_NAME` | VARCHAR |  | The patient's second contributory cause of death. |
| 39 | `UNOS_SEC_DEATH_OTH2` | VARCHAR |  | The free-text description of the patient's second contributory cause of death. |
| 40 | `UNOS_DIALYSIS_C_NAME` | VARCHAR |  | Indicates whether the patient has had dialysis since the last follow-up period. |
| 41 | `UNOS_DLYS_DT` | DATETIME |  | The date on which the patient resumed maintenance dialysis. |
| 42 | `UNOS_DLYS_PROV_ID` | VARCHAR |  | The provider number for the center at which the patient receives dialysis. |
| 43 | `UNOS_DLYS_PROV_NAME` | VARCHAR |  | The name of the center at which the patient receives dialysis. |
| 44 | `UNOS_BIO_ANTIV_C_NAME` | VARCHAR |  | Indicates whether the patient has had biological or anti-viral therapy in the last follow-up period. |
| 45 | `UNOS_BIO_ANTIV_OTH1` | VARCHAR |  | The patient's first other biological or anti-viral therapy during the last follow-up period. |
| 46 | `UNOS_BIO_ANTIV_OTH2` | VARCHAR |  | The patient's second other biological or anti-viral therapy during the last follow-up period. |
| 47 | `UNOS_OTHER_THERP_YN` | VARCHAR |  | Indicates whether the patient had any other therapies during the follow-up period. |
| 48 | `UNOS_GRWTH_THERP_C_NAME` | VARCHAR |  | Indicates whether the patient had growth hormone therapy. |
| 49 | `UNOS_BKV_TREAT_YN` | VARCHAR |  | Indicates whether the patient was treated for BK (Polyoma) Virus. |
| 50 | `UNOS_BKV_TREAT_OTH` | VARCHAR |  | The other specified treatments the patient had for BK (polyoma) viral infections. |
| 51 | `UNOS_URINE_PROT_C_NAME` | VARCHAR |  | Indicates whether urine protein was found by any method. |
| 52 | `UNOS_CMV_IGG_C_NAME` | VARCHAR |  | The last CMV IgG result for the patient. |
| 53 | `UNOS_CMV_IGM_C_NAME` | VARCHAR |  | The last CMV IgM result for the patient. |
| 54 | `UNOS_KI_FL_PRI_C_NAME` | VARCHAR |  | The reason for kidney failure. This column pulls data from Transplant Recipient Follow-up forms. |
| 55 | `UNOS_KI_FL_OTH` | VARCHAR |  | The free-text reason for primary graft failure. |
| 56 | `UNOS_KI_FL_ACUTE_C_NAME` | VARCHAR |  | Indicates whether acute rejection was a contributory cause of graft failure. |
| 57 | `UNOS_KI_FL_CHRON_C_NAME` | VARCHAR |  | Indicates whether chronic rejection was a contributory cause of graft failure. |
| 58 | `UNOS_KI_FL_INFECT_C_NAME` | VARCHAR |  | Indicates whether infection was a contributory cause of graft failure. |
| 59 | `UNOS_KI_FL_PT_NON_C_NAME` | VARCHAR |  | Indicates whether patient non-compliance was a contributory cause of graft failure. |
| 60 | `UNOS_KI_FL_RECUR_C_NAME` | VARCHAR |  | Indicates whether recurrent disease was a contributory cause of graft failure. |
| 61 | `UNOS_KI_FL_CNTB_OTH` | VARCHAR |  | A free-text contributory cause of graft failure. |
| 62 | `UNOS_KI_FL_THROMB_C_NAME` | VARCHAR |  | Indicates whether graft thrombosis was a contributory cause of graft failure. |
| 63 | `UNOS_KI_FL_BKV_C_NAME` | VARCHAR |  | Indicates whether BK (polyoma) virus was a contributory cause of graft failure. |
| 64 | `UNOS_KI_FL_UROLOG_C_NAME` | VARCHAR |  | Indicates whether urological complications were a contributory cause of graft failure. |
| 65 | `UNOS_LVR_FAIL_C_NAME` | VARCHAR |  | Indicates whether primary graft failure was a contributory cause for liver graft failure. |
| 66 | `UNOS_BILIARY_C_NAME` | VARCHAR |  | Indicates whether biliary tract complication was a contributory cause for liver graft failure. |
| 67 | `UNOS_HEP_DENOVO_C_NAME` | VARCHAR |  | Indicates whether DeNovo hepatitis was a contributory cause for liver graft failure. |
| 68 | `UNOS_VASC_THROMB_C_NAME` | VARCHAR |  | Indicates whether vascular thrombosis was a contributory cause for liver graft failure. |
| 69 | `UNOS_HEP_RECUR_C_NAME` | VARCHAR |  | Indicates whether recurrent hepatitis was a contributory cause for liver graft failure. |
| 70 | `UNOS_HEP_ARTTHRM_C_NAME` | VARCHAR |  | Indicates whether hepatic arterial thrombosis was a contributory cause for liver graft failure. |
| 71 | `UNOS_HEP_OBSTRUCT_C_NAME` | VARCHAR |  | Indicates whether hepatic outflow obstruction was a contributory cause for liver graft failure. |
| 72 | `UNOS_PORT_VNTHRM_C_NAME` | VARCHAR |  | Indicates whether portal vein thrombosis was a contributory cause for liver graft failure. |
| 73 | `UNOS_DIS_LAB_DT` | DATETIME |  | Indicates the patient's discharge lab date. |
| 74 | `UNOS_DIS_BILI` | NUMERIC |  | Indicates the patient's total bilirubin at discharge. |
| 75 | `UNOS_DIS_BILI_ST_C_NAME` | VARCHAR |  | Indicates the patient's discharge bilirubin status. |
| 76 | `UNOS_DIS_SGPT` | NUMERIC |  | Indicates the patient's SGPT ALT at discharge. |
| 77 | `UNOS_DIS_SGPT_ST_C_NAME` | VARCHAR |  | Indicates the patient's discharge SGPT ALT status. |
| 78 | `UNOS_DIS_ALBUM` | NUMERIC |  | Indicates the patient's serum albumin at discharge. |
| 79 | `UNOS_DIS_ALBUM_ST_C_NAME` | VARCHAR |  | Indicates the patient's discharge serum albumin status. |
| 80 | `UNOS_DIS_CREAT` | NUMERIC |  | Indicates the patient's serum creatinine at discharge. |
| 81 | `UNOS_DIS_CREAT_ST_C_NAME` | VARCHAR |  | Indicates the patient's discharge serum creatinine status. |
| 82 | `UNOS_DIS_INR` | NUMERIC |  | Indicates the patient's INR at discharge. |
| 83 | `UNOS_DIS_INR_ST_C_NAME` | VARCHAR |  | Indications the patient's discharge INR status. |
| 84 | `UNOS_LVR_REC_DIS_C_NAME` | VARCHAR |  | Indicates whether recurrent disease was a contributory cause for liver graft failure. |
| 85 | `UNOS_LVR_ACT_REJ_C_NAME` | VARCHAR |  | Indicates whether acute rejection was a contributory cause for liver graft failure. |
| 86 | `UNOS_LVR_CHN_REJ_C_NAME` | VARCHAR |  | Indicates whether chronic rejection was a contributory cause for liver graft failure. |
| 87 | `UNOS_LVR_INFECT_C_NAME` | VARCHAR |  | Indicates whether infection was a contributory cause for liver graft failure. |
| 88 | `UNOS_LVR_PAT_NCM_C_NAME` | VARCHAR |  | Indicates whether patient noncompliance was a contributory cause for liver graft failure. |
| 89 | `UNOS_LVR_OTHR_SPEC` | VARCHAR |  | The free text description of other specified contributory reasons for the patient's liver graft failure. |
| 90 | `UNOS_PAN_INS_RSM_DT` | DATETIME |  | Indicates the date the patient resumed insulin/medication. |
| 91 | `UNOS_PAN_FAIL_DT` | DATETIME |  | Indicates the patient's pancreas graft failure date. |
| 92 | `UNOS_PAN_GRF_RMV_C_NAME` | VARCHAR |  | Indicates whether the patient's pancreas graft was removed. |
| 93 | `UNOS_PAN_GRF_RMV_DT` | DATETIME |  | Indicates the patient's pancreas graft removal date. |
| 94 | `UNOS_PAN_PRM_FAIL_C_NAME` | VARCHAR |  | Indicates the patient's primary cause of pancreas graft failure. |
| 95 | `UNOS_PAN_OTHR_FAIL` | VARCHAR |  | The free text description of other specified primary reasons for the patient's pancreas graft failure. |
| 96 | `UNOS_PAN_GV_THRMB_C_NAME` | VARCHAR |  | Indicates whether graft/vascular thrombosis was a contributory cause of pancreas graft failure. |
| 97 | `UNOS_PAN_INFECT_C_NAME` | VARCHAR |  | Indicates whether infection was a contributory cause of pancreas graft failure. |
| 98 | `UNOS_PAN_BLEED_C_NAME` | VARCHAR |  | Indicates whether bleeding was a contributory cause of pancreas graft failure. |
| 99 | `UNOS_PAN_ANM_LK_C_NAME` | VARCHAR |  | Indicates whether anastomotic leak was a contributory cause of pancreas graft failure. |
| 100 | `UNOS_PAN_ACT_REJ_C_NAME` | VARCHAR |  | Indicates whether acute rejection was a contributory cause of pancreas graft failure. |
| 101 | `UNOS_PAN_CHN_REJ_C_NAME` | VARCHAR |  | Indicates whether chronic rejection was a contributory cause of pancreas graft failure. |
| 102 | `UNOS_PAN_BPSY_ISL_C_NAME` | VARCHAR |  | Indicates whether biopsy proven isletitis was a contributory cause of pancreas graft failure. |
| 103 | `UNOS_PAN_PAT_NCM_C_NAME` | VARCHAR |  | Indicates whether patient noncompliance was a contributory cause of pancreas graft failure. |
| 104 | `UNOS_PAN_N_PNCRTS_C_NAME` | VARCHAR |  | Indicates whether pancreatitis was a complication that did not lead to pancreas graft failure. |
| 105 | `UNOS_PAN_NON_LK_C_NAME` | VARCHAR |  | Indicates whether anastomotic leak was a complication that did not lead to pancreas graft failure. |
| 106 | `UNOS_PAN_NON_INF_C_NAME` | VARCHAR |  | Indicates whether abcess or local infection was a complication that did not lead to pancreas graft failure. |
| 107 | `UNOS_PAN_NON_OTHR` | VARCHAR |  | The free text description of other specified complications not leading to the patient's pancreas graft failure. |
| 108 | `UNOS_REC_LAB_DT` | DATETIME |  | Indicates the patient's most recent lab date. |
| 109 | `UNOS_BILIRUBIN` | NUMERIC |  | Indicates the patient's most recent total bilirubin. |
| 110 | `UNOS_BILIRUBIN_ST_C_NAME` | VARCHAR |  | Indicates the patient's total bilirubin status. |
| 111 | `UNOS_SGPT_ALT` | NUMERIC |  | Indicates the patient's most recent SGPT ALT. |
| 112 | `UNOS_SGPT_ALT_ST_C_NAME` | VARCHAR |  | Indicates the patient's SGPT ALT status. |
| 113 | `UNOS_SERUM_ALBUMIN` | NUMERIC |  | Indicates the patient's most recent serum albumin. |
| 114 | `UNOS_SERUM_ALB_ST_C_NAME` | VARCHAR |  | Indicates the patient's serum albumin status. |
| 115 | `UNOS_INR` | NUMERIC |  | Indicates the patient's most recent INR. |
| 116 | `UNOS_INR_ST_C_NAME` | VARCHAR |  | Indicates the patient's recent INR status. |
| 117 | `UNOS_PAN_OTHR_SPEC` | VARCHAR |  | The free text description of other specified contributory reasons for the patient's pancreas graft failure. |
| 118 | `UNOS_SERUM_AMYLASE` | NUMERIC |  | Indicates the patient's serum amylase value. |
| 119 | `UNOS_SERUM_AMY_ST_C_NAME` | VARCHAR |  | Indicates the patient's serum amylase status. |
| 120 | `UNOS_PAN_PANCRTS_C_NAME` | VARCHAR |  | Indicates whether pancreatitis was a contributory cause of pancreas graft failure. |
| 121 | `UNOS_BLDR_ENTDRN_DT` | DATETIME |  | Indicates the patient's enteric drainage date. |
| 122 | `UNOS_PAN_GRF_ST_C_NAME` | VARCHAR |  | Indicates the patient's current pancreas graft status. |
| 123 | `UNOS_BLDR_ENTDRN_C_NAME` | VARCHAR |  | Indicates whether conversion from bladder to enteric drain was performed. |
| 124 | `UNOS_SEC_ACT_REJ_C_NAME` | VARCHAR |  | Indicates whether the patient had any acute rejections during the last follow-up for the second organ in a multi-organ form. |
| 125 | `UNOS_SEC_ACT_ST_C_NAME` | VARCHAR |  | In a multi-organ form, indicates whether a biopsy was done to confirm acute rejection of the second organ. |
| 126 | `UNOS_RE_TXP_ORG_C_NAME` | VARCHAR |  | If a patient was retransplanted, inicates which organs were involved. |
| 127 | `UNOS_LVR_SC_DTH1_SP` | VARCHAR |  | Specifies the first contributory cause of death for the liver graft recipient. |
| 128 | `UNOS_LVR_SC_DTH1_C_NAME` | VARCHAR |  | Indicates the first contributory cause of death for the liver graft recipient. |
| 129 | `UNOS_LVR_SC_DTH2_C_NAME` | VARCHAR |  | Indicates the second contributory cause of death for the liver graft recipient. |
| 130 | `UNOS_LVR_SC_DTH2_SP` | VARCHAR |  | Specifies the second contributory cause of death for the liver graft recipient. |
| 131 | `UNOS_KPF_SC_DTH1_C_NAME` | VARCHAR |  | Indicates the first contributory cause of death for the kidney and pancreas graft recipient. |
| 132 | `UNOS_KPF_SC_DTH1_SP` | VARCHAR |  | Specifies the first contributory cause of death for the kidney and pancreas graft recipient. |
| 133 | `UNOS_KPF_SC_DTH2_C_NAME` | VARCHAR |  | Indicates the second contributory cause of death for the kidney and pancreas graft recipient. |
| 134 | `UNOS_KPF_SC_DTH2_SP` | VARCHAR |  | Specifies the second contributory cause of death for the kidney and pancreas graft recipient. |
| 135 | `UNOS_PAN_SC_DTH1_C_NAME` | VARCHAR |  | Indicates the first contributory cause of death for the pancreas graft recipient. |
| 136 | `UNOS_PAN_SC_DTH1_SP` | VARCHAR |  | Specifies the first contributory cause of death for the pancreas graft recipient. |
| 137 | `UNOS_DIS_LVR_DX_C_NAME` | VARCHAR | org | Indicates the pathology confirmed liver diagnosis at hospital discharge. |
| 138 | `UNOS_DIS_LVR_DX_SP` | VARCHAR |  | Specified pathology confirmed liver diagnosis at hospital discharge. |
| 139 | `UNOS_LVR_PM_DTH_C_NAME` | VARCHAR |  | Specifies the primary cause of death for the liver graft recipient if that cause of death was not picked from a list. |
| 140 | `UNOS_LVR_PM_DTH_SP` | VARCHAR |  | Specifies the primary cause of death for the liver graft recipient. |
| 141 | `UNOS_KPF_PM_DTH_C_NAME` | VARCHAR |  | Indicates the primary cause of death for the kidney and pancreas graft recipient. |
| 142 | `UNOS_KPF_PM_DTH_SP` | VARCHAR |  | Specifies the primary cause of death for the kidney and pancreas graft recipient if that cause of death was not picked from a list. |
| 143 | `UNOS_PAN_PM_DTH_C_NAME` | VARCHAR |  | Indicates the primary cause of death for the pancreas graft recipient. |
| 144 | `UNOS_PAN_PM_DTH_SP` | VARCHAR |  | Specifies the primary cause of death for the pancreas graft recipient if that cause of death was not picked from a list. |
| 145 | `UNOS_PAN_SC_DTH2_C_NAME` | VARCHAR |  | Indicates the second contributory cause of death for the pancreas graft recipient. |
| 146 | `UNOS_PAN_SC_DTH2_SP` | VARCHAR |  | Specifies the second contributory cause of death for the pancreas graft recipient. |
| 147 | `UNOS_PREV_ORG1_C_NAME` | VARCHAR |  | The organ transplanted at the most recent transplant. |
| 148 | `UNOS_PREV_TXP1_DT` | DATETIME |  | The date of the most recent transplant. |
| 149 | `UNOS_PREV_FAIL1_DT` | DATETIME |  | The graft failure date of the most recent transplant. |
| 150 | `UNOS_PREV_ORG2_C_NAME` | VARCHAR |  | The organ transplanted at the second most recent transplant. |
| 151 | `UNOS_PREV_TXP2_DT` | DATETIME |  | The date of the second most recent transplant. |
| 152 | `UNOS_PREV_FAIL2_DT` | DATETIME |  | The graft failure date of the second most recent transplant. |
| 153 | `UNOS_PREV_ORG3_C_NAME` | VARCHAR |  | The organ transplanted at the third most recent transplant. |
| 154 | `UNOS_PREV_TXP3_DT` | DATETIME |  | The date of the third most recent transplant. |
| 155 | `UNOS_PREV_FAIL3_DT` | DATETIME |  | The graft failure date of the third most recent transplant. |
| 156 | `UNOS_PREV_PAN_IST_C_NAME` | VARCHAR |  | Indicates whether the patient previously received a pancreas islet infusion. |
| 157 | `UNOS_ABO_BLD_GRP_C_NAME` | VARCHAR |  | The patient's blood type. |
| 158 | `UNOS_PRIM_DX_C_NAME` | VARCHAR |  | The patient's primary diagnosis. |
| 159 | `UNOS_PRIM_DX_SP` | VARCHAR |  | The primary diagnosis, if it is not one of the available options in column UNOS_PRI_DX_C. |
| 160 | `UNOS_DIAB_TYPE_C_NAME` | VARCHAR |  | Indicates whether the patient has a history of diabetes and if so, the type of diabetes. |
| 161 | `UNOS_DIAL_TYPE_C_NAME` | VARCHAR |  | Indicates whether the patient has a history of dialysis treatment. |
| 162 | `UNOS_PEPT_ULCR_C_NAME` | VARCHAR |  | Indicates whether the patient has a history of peptic ulcers. |
| 163 | `UNOS_ANGINA_C_NAME` | VARCHAR |  | Indicates whether the patient has a history of angina and coronary artery disease. |
| 164 | `UNOS_DRG_TRT_HYP_C_NAME` | VARCHAR |  | Indicates whether the patient has a history of high blood pressure or of being treated with medications to lower blood pressure. |
| 165 | `UNOS_SYM_CER_VASC_C_NAME` | VARCHAR |  | Indicates whether the patient has a history of transient ischemic attacks or stroke. |
| 166 | `UNOS_SYM_PER_VASC_C_NAME` | VARCHAR |  | Indicates whether the patient has a history of peripheral vascular disease, including intermittent claudication or diminished peripheral pulses. |
| 167 | `UNOS_DRG_TRT_COPD_C_NAME` | VARCHAR |  | Indicates whether the patient has a history of Chronic Obstructive Pulmonary Disease (COPD) or of being treated with medications to control COPD. |
| 168 | `UNOS_MALIG_HX_C_NAME` | VARCHAR |  | Indicates whether the patient has a history of malignant cancer. |
| 169 | `UNOS_MALIG_HX_SP` | VARCHAR |  | If the patient has a history of malignant cancer, free text indicating the specific type of tumor. |
| 170 | `UNOS_EXH_VAS_ACC_C_NAME` | VARCHAR |  | Indicates whether the available sites to obtain vascular access for hemodialysis have been exhausted. |
| 171 | `UNOS_EXH_PER_ACC_C_NAME` | VARCHAR |  | Indicates whether all sites to obtain peritoneal access have been exhausted. |
| 172 | `UNOS_AGE_DIAB_ONST` | NUMERIC |  | The patient's age at the time of diabetes onset. |
| 173 | `UNOS_AGE_DIAB_ST_C_NAME` | VARCHAR |  | If the patient's age at the time of diabetes onset is not available, the reason this information is not available. |
| 174 | `UNOS_PAT_IN_HOSP_C_NAME` | VARCHAR |  | Indicates whether the recipient was hospitalized during the 90 days prior to transplant admission. |
| 175 | `UNOS_HBV_C_AB_C_NAME` | VARCHAR |  | The patient's HBV core antibody serology results. |
| 176 | `UNOS_HBV_S_AG_C_NAME` | VARCHAR |  | The patient's HBV surface antigen serology results. |
| 177 | `UNOS_KID_BIOPSY_YN` | VARCHAR |  | Indicates whether a pre-implantation kidney biopsy was performed. |
| 178 | `UNOS_BLD_TRNFSN_C_NAME` | VARCHAR |  | Indicates whether any pre-transplant blood infusions were performed. |
| 179 | `UNOS_TOL_IND_TECH_C_NAME` | VARCHAR |  | Indicates whether any tolerance induction techniques were used. |
| 180 | `UNOS_PREV_PREG_C_NAME` | VARCHAR |  | The number of pregnancies the patient had prior to transplant. |
| 181 | `UNOS_PROC_TYPE_C_NAME` | VARCHAR |  | The procedure used for the transplant. |
| 182 | `UNOS_TCI_R_KID` | NUMERIC |  | The total cold ischemia time for the right kidney or both kidneys, in hours. If a pump is used, this includes pump time. |
| 183 | `UNOS_TCI_R_KID_ST_C_NAME` | VARCHAR |  | If the total cold ischemia time is unavailable for the right kidney or both kidneys, this indicates why the information is unavailable. |
| 184 | `UNOS_TWI_R_KID` | NUMERIC |  | The total warm ischemia time for the right kidney or both kidneys, in minutes. |
| 185 | `UNOS_TWI_R_KID_ST_C_NAME` | VARCHAR |  | If the total warm ischemia time is unavailable for the right kidney or both kidneys, this indicates why the information is unavailable. |
| 186 | `UNOS_TCI_L_KID` | NUMERIC |  | The total cold ischemia time for the left kidney, in hours. If a pump is used, this includes pump time. |
| 187 | `UNOS_TCI_L_KID_ST_C_NAME` | VARCHAR |  | If the total cold ischemia time is unavailable for the left kidney, this indicates why the information is unavailable. |
| 188 | `UNOS_TWI_L_KID` | NUMERIC |  | The total warm ischemia time for the left kidney, in minutes. |
| 189 | `UNOS_TWI_L_KID_ST_C_NAME` | VARCHAR |  | If the total warm ischemia time is unavailable for the left kidney, this indicates why the information is unavailable. |
| 190 | `UNOS_KID_REC_ON_C_NAME` | VARCHAR | org | Indicates whether the transplanted organs were received on ice or on a pump. |
| 191 | `UNOS_REC_ON_ICE_C_NAME` | VARCHAR |  | If the transplanted organs were received on ice, indicates whether the organs stayed on ice or were put on a pump. |
| 192 | `UNOS_REC_ON_PMP_C_NAME` | VARCHAR |  | If the transplanted organs were received on a pump, indicates whether the organs stayed on a pump or were put on ice. |
| 193 | `UNOS_FIN_TXP_RSTN` | NUMERIC |  | If a pump was used during eschemia time, indicates the final resistance. |
| 194 | `UNOS_FIN_TXP_RSTN_C_NAME` | VARCHAR |  | If the final resistance level is unavailable, this indicates why the information is unavailable. |
| 195 | `UNOS_FIN_FLOW_RATE` | NUMERIC |  | If a pump was used, the final flow rate. |
| 196 | `UNOS_FIN_FLOW_RT_C_NAME` | VARCHAR |  | If the final flow rate is unavailable, this indicates why the information is unavailable. |
| 197 | `UNOS_TXP_INC_TUM_C_NAME` | VARCHAR |  | Indicates whether an incidental tumor was found in an organ that was removed from the recipient at the time of transplant. |
| 198 | `UNOS_TXP_TUM_TYP_C_NAME` | VARCHAR |  | The type of incidental tumor found at the time of transplant. |
| 199 | `UNOS_TXP_TUM_TYP_SP` | VARCHAR |  | The free text type of tumor found at the time of transplant. |
| 200 | `UNOS_KID_URN_24H_YN` | VARCHAR |  | Indicates whether the kidney graft produced at least 40 ml of urine in the first 24 hours following the transplant. |
| 201 | `UNOS_PAT_DIAL_1W_YN` | VARCHAR |  | Indicates whether the recipient required any dialysis within the first 7 days following the transplant. |
| 202 | `UNOS_CREAT_DECLN_YN` | VARCHAR |  | Indicates whether the recipient's creatinine value declined by 25% or more in the first 24 hours on two separate samples. |
| 203 | `UNOS_HIV_SEROS_C_NAME` | VARCHAR |  | The patient's HIV serology results. |
| 204 | `UNOS_HCV_SEROS_C_NAME` | VARCHAR |  | The patient's HCV serology results. |
| 205 | `UNOS_EBV_SEROS_C_NAME` | VARCHAR |  | The patient's EBV serology results. |
| 206 | `UNOS_KID_RECIP_YN` | VARCHAR |  | Indicates whether the patient received a kidney. |
| 207 | `UNOS_PAN_RECIP_YN` | VARCHAR |  | Indicates whether the patient received a pancreas. |
| 208 | `UNOS_LVR_RECIP_YN` | VARCHAR |  | Indicates whether the patient received a liver. |
| 209 | `UNOS_INT_RECIP_YN` | VARCHAR |  | Indicates whether the patient received an intestine. |
| 210 | `UNOS_HRT_RECIP_YN` | VARCHAR |  | Indicates whether the patient received a heart. |
| 211 | `UNOS_LNG_RECIP_YN` | VARCHAR |  | Indicates whether the patient received a lung. |
| 212 | `UNOS_PIT_RECIP_YN` | VARCHAR |  | Indicates whether the patient received a pancreas islet. |
| 213 | `UNOS_BMW_RECIP_YN` | VARCHAR |  | Indicates whether the patient received bone marrow. |
| 214 | `UNOS_PRETXP_DIAL_C_NAME` | VARCHAR |  | Indicates whether the patient was on dialysis prior to transplant. |
| 215 | `UNOS_PRETXP_DIAL_DT` | DATETIME |  | The date the recipient first began pre-transplant dialysis. |
| 216 | `UNOS_PRETXP_DL_ST_C_NAME` | VARCHAR |  | The recipients's dialysis date status if the dialysis date field is not populated. |
| 217 | `UNOS_SRM_CREAT` | NUMERIC |  | The recipient's serum creatinine in mg/dl at the time of transplant. |
| 218 | `UNOS_SRM_CREAT_ST_C_NAME` | VARCHAR |  | If the recipient's serum creatinine at the time of transplant is unavailable, this indicates why the information is unavailable. |
| 219 | `UNOS_RESM_DIAL_YN` | VARCHAR |  | Indicates whether the recipient returned to maintenance dialysis. |
| 220 | `UNOS_SURG_COMP_C_NAME` | VARCHAR |  | Indicates whether surgical complication is the contributory cause of graft failure. |
| 221 | `UNOS_MALIG_C_NAME` | VARCHAR |  | Indicates whether the recipient had any malignancies between listing and transplant. |
| 222 | `UNOS_MALIG_TYPE_SP` | VARCHAR |  | The free text type of malignancy the recipient had between listing and transplant. |
| 223 | `UNOS_MED_ANTI_RE_YN` | VARCHAR |  | Indicates whether the patient is currently on any maintenance or anti-rejection medications. |
| 224 | `UNOS_MED_CND_C_NAME` | VARCHAR |  | Indicates the patient's condition and location prior to the transplant. |
| 225 | `UNOS_THF_PM_DTH_C_NAME` | VARCHAR |  | Indicates the primary cause of death for the thoracic graft recipient. |
| 226 | `UNOS_THF_PM_DTH_SP` | VARCHAR |  | Specifies the primary cause of death for the thoracic graft recipient, if that cause of death was not selected from a list. |
| 227 | `UNOS_THF_SC_DTH1_C_NAME` | VARCHAR |  | Indicates the first contributory cause of death for the thoracic graft recipient. |
| 228 | `UNOS_THF_SC_DTH1_SP` | VARCHAR |  | Specifies the first contributory cause of death for the thoracic graft recipient. |
| 229 | `UNOS_THF_SC_DTH2_C_NAME` | VARCHAR |  | Indicates the second contributory cause of death for the thoracic graft recipient. |
| 230 | `UNOS_THF_SC_DTH2_SP` | VARCHAR |  | Specifies the second contributory cause of death for the thoracic graft recipient. |
| 231 | `UNOS_HOSP_REJ_C_NAME` | VARCHAR |  | Indicates whether the recipient was hospitalized for rejection during this follow-up period. |
| 232 | `UNOS_HOSP_INF_C_NAME` | VARCHAR |  | Indicates whether the recipient was hospitalized for infection during this follow-up period. |
| 233 | `UNOS_THF_FAIL_C_NAME` | VARCHAR |  | Indicates the primary cause of graft failure for the thoracic graft recipient. |
| 234 | `UNOS_EJ_FRAC` | NUMERIC |  | Indicates the most recent ejection fraction available for the thoracic graft recipient. |
| 235 | `UNOS_EJ_FRAC_ST_C_NAME` | VARCHAR |  | The most recent ejection fraction status. |
| 236 | `UNOS_SH_FRAC` | NUMERIC |  | Indicates the most recent shortening fraction available for the thoracic graft recipient. |
| 237 | `UNOS_SH_FRAC_ST_C_NAME` | VARCHAR |  | The most recent shortening fraction status. |
| 238 | `UNOS_PACE_C_NAME` | VARCHAR |  | Indicates whether the recipient has had a permanent pacemaker inserted during the follow-up period. |
| 239 | `UNOS_CLIN_EVENT_C_NAME` | VARCHAR |  | Indicates whether the recipient has exhibited clinically significant events related to coronary artery disease. |
| 240 | `UNOS_FEV1` | NUMERIC |  | Indicates the most recent value available for forced expiratory volume at one second. |
| 241 | `UNOS_FEV1_ST_C_NAME` | VARCHAR |  | The status of the most recent value available for forced expiratory volume at one second. |
| 242 | `UNOS_O2_REQ` | NUMERIC |  | The recipient's oxygen requirement at rest at the time of follow-up. |
| 243 | `UNOS_O2_REQ_ST_C_NAME` | VARCHAR |  | The status of the recipient's oxygen requirement at rest at the time of follow-up. |
| 244 | `UNOS_BR_OBLIT_C_NAME` | VARCHAR |  | Indicates whether the recipient has been diagnosed with a bronchial obliterans syndrome during the follow-up period. |
| 245 | `UNOS_BR_STRIC_C_NAME` | VARCHAR |  | Indicates whether the recipient was diagnosed with a bronchial stricture during the follow-up period. |
| 246 | `UNOS_STENT_C_NAME` | VARCHAR |  | If the patient was diagnosed with a bronchial stricture, this indicates whether a stent was inserted. |
| 247 | `UNOS_BONE_DISEAS_C_NAME` | VARCHAR |  | Indicates whether the recipient has exhibited new signs and symptoms of bone disease during the follow-up period. |
| 248 | `UNOS_LVR_DISEASE_C_NAME` | VARCHAR |  | Indicates whether the recipient has exhibited new signs and symptoms of chronic liver disease during the follow-up period. |
| 249 | `UNOS_CATARACT_C_NAME` | VARCHAR |  | Indicates whether the recipient was newly diagnosed with cataracts during the follow-up period. |
| 250 | `UNOS_RENAL_DYS_C_NAME` | VARCHAR |  | Indicates whether the recipient was newly diagnosed with or developed signs and symptoms of renal dysfunction during the follow-up period. |
| 251 | `UNOS_CREAT25_C_NAME` | VARCHAR |  | Indicates whether the recipient's creatinine level was greater than 2.5 mg/dl during the follow-up period. |
| 252 | `UNOS_CHRON_DIAL_C_NAME` | VARCHAR |  | Indicates whether the recipient had chronic peritoneal or hemodialysis during the follow-up period. |
| 253 | `UNOS_RENAL_TXP_C_NAME` | VARCHAR |  | Indicates whether the recipient received a renal transplant during the follow-up period. |
| 254 | `UNOS_STROKE_C_NAME` | VARCHAR |  | Indicates whether the recipient experienced a stroke (CVA) during the follow-up period. |
| 255 | `UNOS_DRG_HYPLIP_C_NAME` | VARCHAR |  | Indicates whether the recipient had any medication newly prescribed for the purpose of lowering serum lipid levels. |
| 256 | `UNOS_TITER_A_DT` | DATETIME |  | The current A titer sample date. |
| 257 | `UNOS_TITER_B_DT` | DATETIME |  | The current B titer sample date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

