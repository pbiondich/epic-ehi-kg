# ORG_SURGICAL_INFO

> Organ transplant surgical information.

**Primary key:** `ORG_RECORD_ID`  
**Columns:** 95  
**Org-specific columns:** 42

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORG_RECORD_ID` | NUMERIC | PK shared | The unique identifier for the organ record. |
| 2 | `PA_REVASCULARIZED_C_NAME` | VARCHAR | org | Was pancreas revascularized before or after other organ if simultaneously transplanted with another organ |
| 3 | `PA_SURG_INC_C_NAME` | VARCHAR | org | Specify the transplant surgical incision location. |
| 4 | `PA_GRAFT_PLACE_C_NAME` | VARCHAR | org | Pancreas transplant graft placement |
| 5 | `PA_OP_TECH_C_NAME` | VARCHAR | org | Pancreas transplant operative technique |
| 6 | `PA_DUCT_MANAGE_C_NAME` | VARCHAR | org | Pancreas transplant duct management |
| 7 | `PA_DUCT_OTHER` | VARCHAR |  | Pancreas transplant duct management. Used when "other" is specified for Pancreas Duct Management (I ORG 2004). |
| 8 | `PA_VENOUS_C_NAME` | VARCHAR | org | Pancreas transplant venous vascular management |
| 9 | `PA_ARTERIAL_C_NAME` | VARCHAR | org | Indicates the transplant arterial reconstruction method. |
| 10 | `PA_ARTERIAL_OTHER` | VARCHAR |  | Pancreas transplant arterial reconstruction method. Used when "other" is specified for Arterial Reconstruction (I ORG 2007). |
| 11 | `PA_VENOUS_GRAFT_YN` | VARCHAR |  | Pancreas transplant venous extension graft |
| 12 | `SURGICAL_PROC_C_NAME` | VARCHAR | org | Organ transplant surgical procedure |
| 13 | `SPLIT_TYPE_C_NAME` | VARCHAR | org | Organ transplant surgical split type |
| 14 | `VENOUS_DRAIN_C_NAME` | VARCHAR | org | Intestine transplant venous drainage |
| 15 | `VISCERA_DRAIN_C_NAME` | VARCHAR |  | Intestine transplant native viscera |
| 16 | `ANASTAMOSIS_TYPE_C_NAME` | VARCHAR | org | Liver anastomosis type |
| 17 | `BACK_TABLE_C_NAME` | VARCHAR | org | Indicates the type of back table used for the organ recipient. |
| 18 | `PRESERV_SOLUTN_C_NAME` | VARCHAR | org | Indicates the organ preservation solution used during transplant. |
| 19 | `EST_BLOOD_LOSS` | NUMERIC |  | Indicates the estimated blood loss (EBL) for the organ recipient in milliliters. |
| 20 | `ARTRY_SITE_C_NAME` | VARCHAR | org | Indicates the artery site used for the organ recipient. |
| 21 | `BIL_DRAIN_SITE_C_NAME` | VARCHAR | org | Indicates the biliary drainage site used for the organ recipient. |
| 22 | `URETER_STENT_YN` | VARCHAR |  | Indicates whether a ureteral stent was used during transplant. |
| 23 | `EXCRN_DRAIN_TYPE_C_NAME` | VARCHAR | org | Indicates the exocrine drainage method used during transplant. |
| 24 | `VENO_VENOUS_BYPS_YN` | VARCHAR |  | Indicates whether the Veno-Venous Bypass (VVBP) technique was used during transplant. |
| 25 | `VENOUS_OUTFLOW_C_NAME` | VARCHAR | org | Indicates the venous outflow technique used during transplant. |
| 26 | `PV_INFLOW_C_NAME` | VARCHAR | org | Indicates the portal vein inflow technique used during transplant. |
| 27 | `ARTRY_INFLOW_C_NAME` | VARCHAR | org | Indicates the arterial inflow technique used for the organ recipient. |
| 28 | `ARTRY_ANATOMY_C_NAME` | VARCHAR | org | Indicates the artery anatomy technique used for the organ recipient. |
| 29 | `DRAIN_NUM` | INTEGER |  | Indicates the number of drains used for the organ recipient. |
| 30 | `BIL_DCT_STNT_TY_C_NAME` | VARCHAR | org | Indicates the bile duct stent technique used for the organ recipient. |
| 31 | `PA_IMPLANT_SITE_C_NAME` | VARCHAR | org | Indicates the pancreas implant site for the organ recipient. |
| 32 | `PORT_VEIN_PTNCY_C_NAME` | VARCHAR | org | Indicates the portal vein patency during transplant. |
| 33 | `VEIN_TREATMENT_C_NAME` | VARCHAR | org | Indicates the vein treatment used during transplant. |
| 34 | `ALT_INFLOW_TYPE` | VARCHAR |  | Indicates the alternative inflow type used for the organ recipient. |
| 35 | `DNR_ARTRY_SITE_C_NAME` | VARCHAR | org | Indicates the artery site of the donor organ. |
| 36 | `DNR_VENOUS_SITE_C_NAME` | VARCHAR | org | Indicates the venous site used for the donor organ. |
| 37 | `DNR_BIL_DRN_SITE_C_NAME` | VARCHAR | org | Indicates the biliary drainage site used for the donor organ. |
| 38 | `DNR_ARTRY_RECNST_C_NAME` | VARCHAR | org | Indicates the artery reconstruction technique used for the donor organ. |
| 39 | `DNR_ARTRY_ANTMY_C_NAME` | VARCHAR |  | Indicates the arterial anatomy type used for the donor organ. |
| 40 | `DNR_ARTRY_INFLOW_C_NAME` | VARCHAR | org | Indicates the arterial inflow technique used for the donor organ. |
| 41 | `ORG_SPLIT_METHD_C_NAME` | VARCHAR | org | Indicates the split method performed during transplant. |
| 42 | `BIL_ANASTOMOS_TYP_C_NAME` | VARCHAR | org | Indicates the biliary anastomosis type. |
| 43 | `LVR_ANATOMY_TYPE_C_NAME` | VARCHAR | org | Indicates the liver anatomy type for the organ recipient. |
| 44 | `ARTRY_ANATOMY_OTH` | VARCHAR |  | Indicates the specific arterial anatomy type used for the organ recipient. |
| 45 | `DNR_ARTRY_ANTMY_OTH` | VARCHAR |  | Free text description of the specific arterial anatomy type used for the donor organ. |
| 46 | `KI_IMPLANT_SITE_C_NAME` | VARCHAR | org | Indicates the kidney implant site for the organ recipient. |
| 47 | `VENOUS_SITE_C_NAME` | VARCHAR | org | Indicates the venous site used for the organ recipient. |
| 48 | `URETER_RECNSTRCT_C_NAME` | VARCHAR | org | Indicates the ureteral reconstruction technique used during transplant. |
| 49 | `ASCITES` | INTEGER |  | Indicates the amount of ascites for the organ recipient in milliliters. |
| 50 | `PRESERV_SOLUTN_OTH` | VARCHAR |  | Free text description of the specific organ preservation solution used during transplant. |
| 51 | `ARTRY_RECONSTRCT_SP` | VARCHAR |  | Specifies the arterial reconstruction method for the donor's organ. |
| 52 | `URINE_PRODUCTION_YN` | VARCHAR |  | Was there urine production in the operating room? |
| 53 | `BILE_PRODUCTION_YN` | VARCHAR |  | Was there bile production in the operating room? |
| 54 | `LI_ARTERIAL_GX_C_NAME` | VARCHAR |  | Indicates if an arterial graft was performed. |
| 55 | `LI_PORTAL_GX_C_NAME` | VARCHAR |  | Indicates if a portal vein graft was performed. |
| 56 | `REPERFUSION_C_NAME` | VARCHAR | org | The quality of reperfusion. |
| 57 | `END_OP_QUALITY_C_NAME` | VARCHAR | org | The quality of the graft at the end of the operation. |
| 58 | `GRAFT_QUALITY_C_NAME` | VARCHAR | org | The quality of the graft. |
| 59 | `DOMINO_DONOR_YN` | VARCHAR |  | Indicates whether this was a domino donor surgery. |
| 60 | `ORGAN_IN_OPFLD_DTTM` | DATETIME (UTC) |  | The instant the organ was removed from ice or pump, whichever was later, in Standard Coordinated Universal Time (UTC). |
| 61 | `OGN_INROOM_INST_DTTM` | DATETIME (UTC) |  | The date and time the organ was in the operating room. |
| 62 | `DNR_CONV_LAPA_OPN_YN` | VARCHAR |  | Indicates if the laparoscopic procedure was converted to an open procedure. |
| 63 | `DNR_KI_PROC_TYPE_C_NAME` | VARCHAR |  | The intended procedure type for the kidney donor. |
| 64 | `DNR_ARTERY_LEN_CM` | NUMERIC |  | Indicates the arterial length of donor organ in centimeters. |
| 65 | `DNR_VENOUS_LEN_CM` | NUMERIC |  | Indicates the venous length of donor organ in centimeters. |
| 66 | `DNR_URETERAL_LEN_CM` | NUMERIC |  | Indicates the ureteral length of donor organ in centimeters. |
| 67 | `DNR_EBL_ML` | INTEGER |  | Indicates the donor's estimated blood loss in milliliters. |
| 68 | `DNR_KI_VENOUS_ANATOMY_C_NAME` | VARCHAR | org | Indicates the donor's venous anatomy during transplant. |
| 69 | `DNR_URETER_ANATOMY_C_NAME` | VARCHAR |  | Indicates the donor's ureteral anatomy during transplant. |
| 70 | `DNR_KI_FL_STRT_INST_DTTM` | DATETIME (UTC) |  | Time at which organ flushing began. |
| 71 | `DNR_KI_FL_END_INST_DTTM` | DATETIME (UTC) |  | Time at which organ flushing ended. |
| 72 | `DNR_KI_DEPRT_INST_DTTM` | DATETIME (UTC) |  | Time at which the organ was removed from the operating room. |
| 73 | `DNR_LAP_TO_OP_REA_C_NAME` | VARCHAR | org | The reason that the procedure was converted to open from laparoscopic. |
| 74 | `DNR_LAP_TO_OP_REA_O` | VARCHAR |  | Stores the reason why the donor nephrectomy was converted from laparoscopic to open if the selected reason is "Other". |
| 75 | `CNSL_STRT_INST_DTTM` | DATETIME (UTC) |  | Time when the surgeon started using the console. |
| 76 | `CNSL_END_INST_DTTM` | DATETIME (UTC) |  | Time at which the surgeon stopped using the console. |
| 77 | `TRANSECTION_STRT_TM_DTTM` | DATETIME (UTC) |  | The instant that the transection of a donor liver begins. |
| 78 | `TRANSECTION_END_TM_DTTM` | DATETIME (UTC) |  | The instant that the transection of a donor liver ends. |
| 79 | `ARTERIES_TO_LOBE` | INTEGER |  | The number of arteries connected to the liver lobe being transplanted. |
| 80 | `MID_HEP_VEN_INC_YN` | VARCHAR |  | Indicates whether the middle hepatic vein is included in the lobe of liver being transplanted. |
| 81 | `NUM_BILE_DUCTS` | INTEGER |  | The number of bile ducts in the lobe of the liver being transplanted. |
| 82 | `PORTAL_VEIN_FLUSH` | INTEGER |  | Stores the quantity of fluid (in CCs) used to flush the portal vein. |
| 83 | `ARTERY_FLUSH` | INTEGER |  | Stores the quantity of fluid (in CCs) used to flush the artery. |
| 84 | `HEP_VEN_ANAT_OTH` | VARCHAR |  | The anatomy of the hepatic vein in the part of the liver being transplanted (used when 'other' is selected for hepatic venous anatomy). |
| 85 | `BILE_DUCT_COM` | VARCHAR |  | Comments about the bile ducts in the liver being transplanted. |
| 86 | `HEPATIC_VEN_ANAT_C_NAME` | VARCHAR | org | The anatomy of the hepatic vein in the part of the liver being transplanted. |
| 87 | `PORT_VN_FLSH_YN` | VARCHAR |  | Indicates whether the organ was flushed prior to the transplant surgery. |
| 88 | `PORT_VN_FLSH_TEMP_C_NAME` | VARCHAR | org | Indicates the portal vein flush temperature during organ preparation prior to the transplant surgery. |
| 89 | `BACK_TBL_FLSH_OTHR` | VARCHAR |  | Indicates the specific back table flush solution used during organ preparation prior to transplant surgery. |
| 90 | `RECPNT_VCC_UTC_DTTM` | DATETIME (UTC) |  | Indicates the vena cava cross clamp time for the transplant recipient. |
| 91 | `DNR_ARTERIAL_DIA_CM` | NUMERIC |  | Indicates the arterial diameter of the donor organ in centimeters. |
| 92 | `DNR_ARTERIAL_DIS_CM` | NUMERIC |  | Indicates the arterial distance apart of the donor organ in centimeters. |
| 93 | `DNR_VENOUS_DIA_CM` | NUMERIC |  | Indicates the venous diameter of the donor organ in centimeters. |
| 94 | `DNR_VENOUS_DIS_CM` | NUMERIC |  | Indicates the venous distance apart of the donor organ in centimeters. |
| 95 | `VOL_PRESER_SOL_ML` | NUMERIC |  | Indicates the volume in milliliters of the organ preservation solution used during the transplant surgery. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

