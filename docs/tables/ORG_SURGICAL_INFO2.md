# ORG_SURGICAL_INFO2

> Contains organ and surgical level information related to transplant.

**Primary key:** `ORG_RECORD_ID`  
**Columns:** 76  
**Org-specific columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORG_RECORD_ID` | NUMERIC | PK shared | The unique identifier for the organ record. |
| 2 | `STERNOTOMY_APPRCH_C_NAME` | VARCHAR | org | Indicate whether the sternotomy performed was routine or a reoperation related to lung transplant surgery |
| 3 | `PFO_IDENTIFIED_YN` | VARCHAR |  | Indicate whether a patent foramen ovale (PFO) was identified during heart transplant surgery. |
| 4 | `CHEST_CLOSED_YN` | VARCHAR |  | Indicates whether the sternum/chest cavity was closed or left open after the cardiothoracic transplant surgery. |
| 5 | `RETURN_TO_CPB_YN` | VARCHAR |  | Indicate whether the patient returned to cardiopulmonary bypass after the cardiothoracic transplant surgery. |
| 6 | `CHEST_OPEN_REASON_C_NAME` | VARCHAR | org | Indicates the reason why the transplant recipient's chest was left open after the transplant surgery. |
| 7 | `ORGAN_DAMAGE_YN` | VARCHAR |  | Indicate whether there was any damage to the donor organ. |
| 8 | `ORGAN_DAMAGE_SPEC` | VARCHAR |  | Indicates the damage to the donor organ. |
| 9 | `PLAQUE_DNR_AORTA_C_NAME` | VARCHAR | org | Indicates the plaque present on the donor's aorta. |
| 10 | `PLAQUE_DNR_RENART_C_NAME` | VARCHAR | org | Indicates the plaque present on the donor's renal artery. |
| 11 | `ATHERO_RECIP_RENA_C_NAME` | VARCHAR | org | Indicates the type of atherosclerosis present on the recipient's renal artery. |
| 12 | `ATHERO_RECIP_AORT_C_NAME` | VARCHAR | org | Indicates the type of atherosclerosis present on the recipient's aorta. |
| 13 | `RECIP_ARTERIAL_OTH` | VARCHAR |  | Indicates the other arterial site for the transplant recipient. |
| 14 | `INCISION_SITE_OTH` | VARCHAR |  | Indicates the other surgical incision site for the transplant recipient. |
| 15 | `DONOR_PAO2_MAX_NUM` | NUMERIC |  | Indicate the maximum value for the donor's oxygen saturation (PaO2) in mmHg. |
| 16 | `DONOR_PRESSURE_CLOS` | VARCHAR |  | Indicate the donor's airway pressure in cm H2O when the donor's chest is closed |
| 17 | `DONOR_PRESSURE_OPEN` | VARCHAR |  | Indicate the donor's airway pressure in cm H2O when the donor's chest is open. |
| 18 | `SURGICAL_POSITION_C_NAME` | VARCHAR | org | Indicate the surgical position of the recipient. |
| 19 | `EX_VIVO_PERFUSION_YN` | VARCHAR |  | Indicate whether ex-vivo perfusion was performed. |
| 20 | `INCISION_TYPE_C_NAME` | VARCHAR | org | Indicate the surgical incision type used on the recipient. |
| 21 | `ANTERIOR_PERICARD_C_NAME` | VARCHAR | org | Indicates whether an anterior pericardiotomy procedure was performed during the lung transplant surgery. |
| 22 | `PLEURAL_ADHESIONS_C_NAME` | VARCHAR | org | Indicate whether any pleural adhesions were found during the lung transplant surgery. |
| 23 | `ADHESION_SITE_C_NAME` | VARCHAR | org | Indicates on which lung the pleural adhesions were found. |
| 24 | `LUNG_IMPLANT_METH_C_NAME` | VARCHAR | org | Indicate the method of pneumonectomy and implant used during the lung transplant surgery. |
| 25 | `LUNG_IMPLANT_ORDER_C_NAME` | VARCHAR | org | Indicates the order of the pneumonectomy and implant for en-bloc or bilateral sequential lung transplant surgery: Left then right, or right then left. |
| 26 | `BRONCH_ANAS_C_NAME` | VARCHAR | org | Indicates the technique used for bronchial anastomosis during the lung transplant surgery. |
| 27 | `DIAPH_PLICATION_C_NAME` | VARCHAR | org | Indicate whether a diaphragm plication was performed, with or without sutures, during the lung transplant surgery. |
| 28 | `COMPLETION_BRONCH_C_NAME` | VARCHAR | org | Indicates the findings of a fiberoptic bronchoscopy procedure that was performed during the lung transplant. |
| 29 | `CPB_TIME_NUM` | INTEGER |  | Indicate the number of minutes the patient was on cardiopulmonary bypass for circulatory support during the surgery. |
| 30 | `FIO2_NUM` | NUMERIC |  | Indicate the percent oxygen measured post-lung transplant, entered as a decimal between 0 and 1. |
| 31 | `PA_PRESSURE_OPEN` | VARCHAR |  | Indicates the recipient's pulmonary artery pressure in mmHg when the recipient's chest is open after the lung transplant surgery. |
| 32 | `PA_PRESSURE_CLOS` | VARCHAR |  | Indicates the recipient's pulmonary artery pressure in mmHg when the recipient's chest is closed after the lung transplant surgery. |
| 33 | `CLOSURE_TECHNIQUE_C_NAME` | VARCHAR | org | Indicate the technique used to close the recipient's body after the transplant surgery. |
| 34 | `LUNG_DRAIN_SITE_C_NAME` | VARCHAR | org | Indicates the drainage site for excess fluids during the lung transplant surgery. |
| 35 | `HEMOSTASIS_QUAL_C_NAME` | VARCHAR | org | Indicate the quality of the recipient's blood clotting after the transplant surgery. |
| 36 | `DNR_CXR_HORIZ_NUM` | NUMERIC |  | Indicate the measurement across the donor's chest prior to the lung transplant. |
| 37 | `DNR_CXR_L_VERT_NUM` | NUMERIC |  | Indicate the measurement across the left vertical portion of the donor's chest prior to the lung transplant. |
| 38 | `DNR_CXR_R_VERT_NUM` | NUMERIC |  | Indicate the measurement across the right vertical portion of the donor's chest prior to the lung transplant. |
| 39 | `VASCULAR_ACCESS_C_NAME` | VARCHAR | org | Indicates the site of vascular access for the transplant, as separate from anastomosis sites. |
| 40 | `HEPATECTOMY_ST_TM_DTTM` | DATETIME (UTC) |  | Indicate the hepatectomy start time. |
| 41 | `VENOUS_RECON_C_NAME` | VARCHAR | org | Indicates the venous reconstruction technique used during the surgery. |
| 42 | `VENOUS_RECON_OTHER` | VARCHAR |  | Indicates the other venous site type for the recipient. |
| 43 | `RECIP_AORTIC_TM_DTTM` | DATETIME (UTC) |  | Indicate the clamp on time of the recipient's aorta |
| 44 | `PROX_BOWEL_NAT_C_NAME` | VARCHAR | org | Indicate where the donor organ was connected in the donor's body for the intestinal transplant surgery. |
| 45 | `PROX_BOWEL_TXP_C_NAME` | VARCHAR |  | Indicate where the donor organ was connected in the recipient's body during the intestinal transplant surgery. |
| 46 | `DIST_BOWEL_NAT_C_NAME` | VARCHAR |  | Indicate where the donor organ was connected in the donor's body during the intestinal transplant surgery. |
| 47 | `DIST_BOWEL_TXP_C_NAME` | VARCHAR |  | Indicate where the donor organ was connected in the recipient's body for the intestinal transplant surgery. |
| 48 | `PERISTALSIS_IN_OR_YN` | VARCHAR |  | Indicates whether there was peristalsis in the operating room during the transplant surgery. |
| 49 | `PERF_SUPPORT_OTHER` | VARCHAR |  | Indicates the other type of perfusion support used on the recipient during the surgery. |
| 50 | `DEVICE_EXPLANT_OTH` | VARCHAR |  | Indicates other device explanted. |
| 51 | `PREOP_MCS_OTH` | VARCHAR |  | Indicates the other pre-op mechanical circulatory support devices in the transplant recipient. |
| 52 | `POSTOP_MCS_OTH` | VARCHAR |  | Indicates the other post-op mechanical circulatory support devices in the transplant recipient. |
| 53 | `TRACH_ANAS_C_NAME` | VARCHAR | org | Indicates the technique used for tracheal anastomosis during the transplant surgery. |
| 54 | `ART_GRAFT_TYPE_C_NAME` | VARCHAR | org | Indicates the type of arterial graft performed during the transplant surgery. |
| 55 | `BILE_DUCT_STENT_OTH` | VARCHAR |  | Indicates the free text technique for the recipient's bile duct stent. |
| 56 | `ART_INFLOW_OTH` | VARCHAR |  | Indicates the free text technique for the recipient's arterial inflow. |
| 57 | `SUTURE_BRAND_C_NAME` | VARCHAR | org | Indicates the brand name of the suture used during the transplant surgery. |
| 58 | `SUTURE_SIZE_C_NAME` | VARCHAR | org | Indicates the suture size in USP designation measurement used during the transplant surgery. |
| 59 | `NATV_PV_ANAST_C_NAME` | VARCHAR | org | Indicates the native portal vein anastomosis type used during the transplant surgery. |
| 60 | `ART_RECON_SUTURE_C_NAME` | VARCHAR | org | Indicates the type of arterial reconstruction suture technique used during the transplant surgery. |
| 61 | `DIST_ENTEROSTOMY_C_NAME` | VARCHAR | org | Indicates the type of distal enterostomy performed during the transplant surgery. |
| 62 | `ARTERIAL_TYP_OTHR` | VARCHAR |  | Indicates the specific site of arterial vascular access used during the transplant surgery. |
| 63 | `VENOUS_TYP_OTHR` | VARCHAR |  | Indicates the specific site of venous vascular access used during the transplant surgery. |
| 64 | `CHEST_OP_RSN_OTHR` | VARCHAR |  | Indicates the specific reason why the transplant recipient's chest was left open after the transplant surgery. |
| 65 | `RSN_CPB_OTHR` | VARCHAR |  | Indicates the specific reason why the patient needed to return to cardiopulmonary bypass support after the cardiothoracic transplant surgery. |
| 66 | `PROCURE_DAMAGE_YN` | VARCHAR |  | Indicates whether the organ was damaged during procurement. |
| 67 | `PROCURE_DAMAGE_CMT` | VARCHAR |  | Indicates the specific damage to the organ during procurement. |
| 68 | `RECIP_SUP_VC_COMP_DTTM` | DATETIME (UTC) |  | Indicates the superior vena cava completion time for the transplant recipient. |
| 69 | `RECIP_INF_VC_COMP_DTTM` | DATETIME (UTC) |  | Indicates the inferior vena cava completion time for the transplant recipient. |
| 70 | `BILE_DUCT_COMP_DTTM` | DATETIME (UTC) |  | Indicates the bile duct completion time for the transplant recipient. |
| 71 | `VC_BYPASS_ST_DTTM` | DATETIME (UTC) |  | Indicates the vena cava bypass start time for the transplant recipient. |
| 72 | `VC_BYPASS_END_DTTM` | DATETIME (UTC) |  | Indicates the vena cava bypass end time for the transplant recipient. |
| 73 | `PRESER_SOL_LOT_NUM` | VARCHAR |  | Indicates the lot number of preservation solution for the donor organ. |
| 74 | `PRESER_SOL_EXP_DATE` | DATETIME |  | Indicates the expiration date of preservation solution for the donor organ. |
| 75 | `ORG_PERFUSION_LOCATION_C_NAME` | VARCHAR | org | Indicate where the organ perfusion occurred. |
| 76 | `ORG_PERFUSION_BY_C_NAME` | VARCHAR | org | Indicate who performed the organ perfusion. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

