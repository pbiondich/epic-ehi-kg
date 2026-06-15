# TRANSPLANT_INFO

> This table contains information regarding the transplant episode. Only episodes whose Episode Type Class (I HBD 130) is 4 - Transplant will be included.

**Primary key:** `SUMMARY_BLOCK_ID`  
**Columns:** 76  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID of the episode of care record. |
| 2 | `TX_REV_DT` | DATETIME |  | Date on which the patient's information was presented at a multi-disciplinary committee meeting to determine whether to list the patient for transplant. |
| 3 | `TX_EPSD_TYPE_C_NAME` | VARCHAR |  | Indicates whether the patient is a donor or a recipient for the transplant. |
| 4 | `TX_NUM` | INTEGER |  | Stores the transplant number |
| 5 | `TX_HIST_LOCATION` | VARCHAR |  | This item stores the location where a historic transplant occurred |
| 6 | `TX_SURG_DT` | DATETIME |  | Date on which the transplant surgery took place. |
| 7 | `TX_IS_HISTORIC_YN` | VARCHAR |  | flag indicating a historic transplant episode |
| 8 | `TX_EPSD_NOTE_HNO_ID` | VARCHAR |  | The transplant episode note record ID. |
| 9 | `TX_HIST_COUNTY_C_NAME` | VARCHAR | org | This item stores the county where a historic transplant occurred |
| 10 | `TX_WAITLIST_DT` | DATETIME |  | Date on which the patient was placed on the waitlist |
| 11 | `TX_DNR_POS_C_NAME` | VARCHAR | org | The category number for the possibilities being investigated to find a live transplant donor. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 12 | `TX_DISCHARGE_DT` | DATETIME |  | Date on which the patient was discharged after the transplant surgery. |
| 13 | `TX_CURRENT_STAGE_C_NAME` | VARCHAR |  | Phase of the transplant episode. |
| 14 | `TX_CURRENT_STAGE_DT` | DATETIME |  | Effective date for the current phase, status, and reason of the transplant episode. |
| 15 | `TX_CURRENT_STATUS_C_NAME` | VARCHAR | org | Status of the current phase of the transplant episode. |
| 16 | `TX_CURRENT_REASON_C_NAME` | VARCHAR | org | Reason for the transplant episode's current phase and status. |
| 17 | `TXP_EXTERNAL_CITY` | VARCHAR |  | City where the external transplant procedure was performed. |
| 18 | `ADMISSION_DT` | DATETIME |  | Date on which the patient was admitted for the transplant procedure. |
| 19 | `BW_UNACCEPT_AG_C_NAME` | VARCHAR | org | List the patient's BW unacceptable antigen |
| 20 | `TXP_NEXT_REVIEW_DT` | DATETIME |  | Date on which the transplant episode and the patient chart should be reviewed. |
| 21 | `TXP_ADMIT_CSN` | NUMERIC |  | The contact serial number (CSN) for the hospital admission when the transplant surgery was performed. |
| 22 | `IN_TPN_DEPENDENT_YN` | VARCHAR |  | Indicates whether the patient is dependent on total parenteral nutrition (TPN). |
| 23 | `IN_IV_DEPENDENT_YN` | VARCHAR |  | Indicates whether the patient is dependent on intravenous fluids. |
| 24 | `IN_ORAL_FEEDING_YN` | VARCHAR |  | Indicates whether the patient is receiving oral nutrition. |
| 25 | `IN_TUBE_FEEDING_YN` | VARCHAR |  | Indicates whether the patient is receiving nutrition through a gastric tube. |
| 26 | `LISTED_ELSEWHERE` | VARCHAR |  | Non-United Network for Organ Sharing (UNOS) center where the patient is listed. |
| 27 | `TIME_TO_CENTER` | NUMERIC |  | The patient's travel time in hours to the transplant center. |
| 28 | `EXHAUST_VASC_HEM_YN` | VARCHAR |  | Indicates whether the patient has exhausted vascular access for hemodialysis. |
| 29 | `EXHAUST_PERITON_YN` | VARCHAR |  | Indicates whether the patient has exhausted peritoneal access. |
| 30 | `EXHAUST_IN_VASC_YN` | VARCHAR |  | Indicates whether the patient has exhausted vascular access to the intestine. |
| 31 | `LOSS_VASC_SITES_YN` | VARCHAR |  | Indicates whether the patient has lost two or more vascular access sites for the intestine. |
| 32 | `FLUID_ELEC_LOSS_YN` | VARCHAR |  | Indicates whether the patient has unmanageable fluid-electrolyte losses. |
| 33 | `NONRECON_GITRACT_YN` | VARCHAR |  | Indicates whether the patient has a non-reconstructable GI tract. |
| 34 | `TXP_REFERRAL_DT` | DATETIME |  | Date on which the patient was referred to transplant-related specialty care. |
| 35 | `TX_HIST_PHONE` | VARCHAR |  | Phone number of the facility where the historic transplant took place. |
| 36 | `TX_HIST_FAX` | VARCHAR |  | Fax for the facility where the historic transplant took place. |
| 37 | `TX_HIST_COORD` | VARCHAR |  | The coordinator for the historic transplant. |
| 38 | `TX_HIST_CENTER_C_NAME` | VARCHAR | org | United Network for Organ Sharing (UNOS) center where the historical transplant occurred. |
| 39 | `TX_EVAL_DT` | DATETIME |  | Date on which transplant evaluation began for the patient. |
| 40 | `TX_DNR_WILLING_YN` | VARCHAR |  | Is the organ donor willing to donate organ to anyone? |
| 41 | `TXP_CALC_RFL_DATE` | DATETIME |  | Computed referral date for a transplant episode. The following fields are checked, in this order, to obtain the referral date: 1. Transplant Referral Date (I HSB 30113). 2. From the transplant status history, the first time the episode reached the Pre-Evaluation phase in the system (I HSB 30056). 3. From the transplant status history, the first time the episode reached the Evaluation phase in the system (I HSB 30056). 4. Episode Start Date (I HSB 70). |
| 42 | `TXP_CALC_EVAL_DATE` | DATETIME |  | Computed evaluation date for a transplant episode. The following fields are checked, in this order, to obtain the evaluation date: 1. Transplant Evaluation Date (I HSB 30007). 2. From the transplant status history, the first time the episode reached the Evaluation phase in the system (I HSB 30056). |
| 43 | `TXP_CALC_CR_DATE` | DATETIME |  | Computed committee review date for a transplant episode. The following fields are checked, in this order, to obtain the committee review date: 1. Transplant Committee Review Date (I HSB 30025). 2. The earliest review date from Committee Review encounters linked to the episode (I EPT 98025). |
| 44 | `TXP_CALC_ADMIT_DATE` | DATETIME |  | Computed admission date for a transplant episode. The following fields are checked, in this order, to obtain the admission date: 1. Transplant Admission Date (I HSB 30048). 2. The admission date from the encounter linked to the episode as the admission encounter (I EPT 18850), as stored in item TX ADMISSION CONTACT SERIAL NUMBER (I HSB 30185). |
| 45 | `TXP_CALC_DISCHRG_DT` | DATETIME |  | Computed discharge date for a transplant episode. The following fields are checked, in this order, to obtain the discharge date: 1. Transplant Discharge Date (I HSB 30006). 2. The discharge date from the encounter linked to the episode as the admission encounter (I EPT 18855), as stored in item TX ADMISSION CONTACT SERIAL NUMBER (I HSB 30185). |
| 46 | `TXPORT_MTHD_C_NAME` | VARCHAR | org | The method of transportation to the transplant center. |
| 47 | `UNOS_ACCEPT` | VARCHAR |  | The United Network for Organ Sharing (UNOS) waitlist acceptance code. |
| 48 | `DONOR_MIN_WT` | NUMERIC |  | The minimum acceptable donor weight. |
| 49 | `DONOR_MAX_WT` | NUMERIC |  | The maximum acceptable donor weight |
| 50 | `TX_CENTER_WL_DT` | DATETIME |  | Date on which the patient was added to the center waitlist. |
| 51 | `EPISODE_STATUS_C_NAME` | VARCHAR |  | The status of the episode. Use this column to filter deleted episodes by using "<>3" comparison. |
| 52 | `TXP_REF_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 53 | `TXP_SURGEON_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 54 | `TXP_CALC_EVAL_END_DT` | DATETIME |  | Computed evaluation end date for a transplant episode. The following fields are checked, in this order, to obtain the evaluation date: 1. Transplant Evaluation End Date (I HSB 30081). 2. If the episode is declined for transplant, use the status date 3. if the patient is waitlisted or above, use the center waitlist date(I HSB 30074), if empty, use waitlist date(I HSB 30061) 4. if patient died during referral/evaluation then return patient death date(I EPT 115) |
| 55 | `UNOS_LIVER_SCORE` | VARCHAR |  | The most recent United Network for Organ Sharing (UNOS) liver score. |
| 56 | `UNOS_LIVER_SCORE_DT` | DATETIME |  | The date of the most recent United Network for Organ Sharing (UNOS) liver score update. |
| 57 | `UNOS_LIVER_IS_PELD_YN` | VARCHAR |  | Indicates whether the most recent United Network for Organ Sharing (UNOS) liver score is a PELD score |
| 58 | `UNOS_LIVER_IS_STATUS_YN` | VARCHAR |  | Indicates whether the most recent United Network for Organ Sharing (UNOS) liver score is a liver status. |
| 59 | `UNOS_HEART_STATUS` | VARCHAR |  | The most recent United Network for Organ Sharing (UNOS) heart status. |
| 60 | `UNOS_HEART_STATUS_DT` | DATETIME |  | The date of the most recent United Network for Organ Sharing (UNOS) heart status. |
| 61 | `UNOS_LAS` | NUMERIC |  | The most recent United Network for Organ Sharing (UNOS) lung allocation score. |
| 62 | `UNOS_LAS_DT` | DATETIME |  | The date of the most recent United Network for Organ Sharing (UNOS) lung allocation score. |
| 63 | `UNOS_CPRA` | INTEGER |  | The most recent United Network for Organ Sharing (UNOS) Calculated Panel Reactive Antibodies (CPRA) score. |
| 64 | `UNOS_CPRA_DT` | DATETIME |  | The most recent United Network for Organ Sharing (UNOS) Calculated Panel Reactive Antibodies (CPRA) score update date. |
| 65 | `TXP_EVAL_END_DT` | DATETIME |  | Date on which the transplant evaluation was completed for the patient. |
| 66 | `UNOS_IN_STATUS` | VARCHAR |  | The most recent United Network for Organ Sharing (UNOS) intestine status. |
| 67 | `UNOS_IN_STATUS_DT` | DATETIME |  | The date of the most recent United Network for Organ Sharing (UNOS) intestine status. |
| 68 | `TXP_CENTER_C_NAME` | VARCHAR |  | The transplant center that owns the patient episode. |
| 69 | `TXP_SURG_DTTM` | DATETIME (UTC) |  | Contains the earliest clamp time from organs associated with the transplant episode. If there are no clamp times for any associated organs, this will be null. |
| 70 | `HEIGHT_AT_TXP` | NUMERIC |  | The donor or recipient's height at transplant, in cm. |
| 71 | `WEIGHT_AT_TXP` | NUMERIC |  | The donor or recipient's weight at transplant, in kg. |
| 72 | `TOBACCO_USE_AT_TXP_C_NAME` | VARCHAR |  | The donor or recipient's tobacco usage at transplant. |
| 73 | `ALCOHOL_USE_AT_TXP_C_NAME` | VARCHAR |  | The donor or recipient's alcohol usage at transplant. |
| 74 | `DRUG_USE_AT_TXP_C_NAME` | VARCHAR |  | The donor or recipient's drug use at transplant. |
| 75 | `UNOS_CAS` | NUMERIC |  | Most recent lung composite allocation score |
| 76 | `UNOS_CAS_DATE` | DATETIME |  | The date of the most recent CAS subscore. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

