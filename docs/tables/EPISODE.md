# EPISODE

> This table contains high-level information on the episodes recorded in the clinical system for your patients. When a provider sees a patient several times for an ongoing condition, such as prenatal care, these encounters can be linked to a single Episode of Care. It does not contain episodes linked to an inpatient encounter.

**Overflow family:** [EPISODE_2](EPISODE_2.md)  
**Primary key:** `EPISODE_ID`  
**Columns:** 51  
**Org-specific columns:** 8  
**Joined by:** 57 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK | The unique ID of the episode of care record. |
| 2 | `NAME` | VARCHAR |  | The name of the episode. |
| 3 | `SUM_BLK_TYPE_ID_EPISODE_DEF_NAME` | VARCHAR |  | This column displays the name of the episode / block definition record. |
| 4 | `START_DATE` | DATETIME |  | The date the episode was initiated. |
| 5 | `END_DATE` | DATETIME |  | The date the episode was resolved in calendar format. This field is called "Resolved" on the clinical system screen. |
| 6 | `COMMENTS` | VARCHAR |  | Any free text comments about the episode. |
| 7 | `PREGRAVID_WEIGHT` | NUMERIC |  | This field contains the pre-pregnancy weight maintained before this episode. |
| 8 | `NUMBER_OF_BABIES` | INTEGER |  | Prior to delivery, this column is expected to contain the number of fetuses that the patient is carrying. This can be manually documented, such as in the Prenatal Vitals section, or the value can be automatically set by creating or removing fetal result tabs in the ultrasound activity. If your organization documents on the Delivery Summary then after the Delivery Summary is signed, this column is expected to contain the number of viable deliveries associated with the pregnancy. Specifically, this is the number of delivery records attached to the pregnancy. This expectation is based on Epic's recommendation that only viable deliveries should be documented on the Delivery Summary. Your organization may follow a different policy for when to create a delivery record. The behavior of this column containing the number of delivery records may be overridden at the profile level in system definitions, in which case it will continue to contain the number of fetuses that were being carried unless the number of deliveries is manually documented in its place. |
| 9 | `PRIMARY_LPL_ID` | NUMERIC |  | The primary problem linked to the episode. |
| 10 | `STATUS_C_NAME` | VARCHAR |  | The status category number for the episode. |
| 11 | `L_UPDATE_USER_ID` | VARCHAR |  | The ID of the last user that updated the episode of care record. |
| 12 | `L_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `PATERNITY_ACK_C_NAME` | VARCHAR | org | Whether a paternity acknowledgement has been signed by the biological father of the baby if the parents are not married. This column may not be applicable depending on the identity of the second parent and the two parents' relationship. |
| 14 | `SMOKE_3_MO_BEF` | INTEGER |  | The number of cigarettes/packs smoked per day 3 months before the pregnancy by the mother. |
| 15 | `SMOKE_3_MO_BEF_C_NAME` | VARCHAR | org | The unit of measurement for the quantity of cigarettes being smoked 3 months before the pregnancy by the mother. |
| 16 | `SMOKE_1ST_3_MO` | INTEGER |  | The number of cigarettes/packs smoked per day in the first 3 months of the pregnancy by the mother. |
| 17 | `SMOKE_1ST_3_MO_C_NAME` | VARCHAR |  | The unit of measurement for the quantity of cigarettes being smoked the first three months of the pregnancy by the mother. |
| 18 | `SMOKE_2ND_3_MO` | INTEGER |  | The number of cigarettes/packs smoked per day in the second 3 months of the pregnancy by the mother. |
| 19 | `SMOKE_2ND_3_MO_C_NAME` | VARCHAR |  | The unit of measurement for the quantity of cigarettes being smoked the second three months of the pregnancy by the mother. |
| 20 | `SMOKE_3RD_TRI` | INTEGER |  | The number of cigarettes/packs smoked per day in the third trimester of the pregnancy by the mother. |
| 21 | `SMOKE_3RD_TRI_C_NAME` | VARCHAR |  | The unit of measurement for the quantity of cigarettes being smoked the third trimester of the pregnancy by the mother. |
| 22 | `DRINK_3_MO_BEF` | INTEGER |  | The number of alcoholic drinks consumed per week 3 months before the pregnancy by the mother. |
| 23 | `DRINK_1ST_3_MO` | INTEGER |  | The number of alcoholic drinks consumed per week in the first three months of the pregnancy by the mother. |
| 24 | `DRINK_2ND_3_MO` | INTEGER |  | The number of alcoholic drinks consumed per week in the second three months of the pregnancy by the mother. |
| 25 | `DRINK_3RD_TRI` | INTEGER |  | The number of alcoholic drinks consumed per week in the third trimester of the pregnancy by the mother. |
| 26 | `IN_CITY_LIMITS_YN` | VARCHAR |  | Whether the address of the mother is inside the city limits. |
| 27 | `WIC_FOODS_YN` | VARCHAR |  | Did the mother receive WIC foods during this pregnancy? |
| 28 | `TOTAL_PNC` | INTEGER |  | Override value to be used in situations where not all prenatal care was given at the same Epic provider and so not all prenatal care visits are in the system. |
| 29 | `MONTH_1ST_PNC` | INTEGER |  | Override value to be used in situations where not all prenatal care was given at the same Epic provider and so first date of prenatal care is not in the system and the month of the pregnancy when prenatal care began cannot be calculated. |
| 30 | `LIVE_BIRTHS_LIVING` | INTEGER |  | Override value to be used in situations where not all prenatal care was given at the same Epic provider, and consequently, other pregnancy information is not available. The number of children born alive which are still living not including children born at this birth. |
| 31 | `LIVE_BIRTHS_DEAD` | INTEGER |  | Override value to be used in situations where not all prenatal care was given at the same Epic provider, and consequently, other pregnancy information is not available. The number of other children born alive which are now deceased not including any born alive and deceased at this birth. |
| 32 | `MOTHER_MARRIED_YN` | VARCHAR |  | Whether the mother is married at birth, conception, or any time in between. |
| 33 | `OB_PREGRAVID_BMI` | NUMERIC |  | The patient's pre-pregnancy BMI for this pregnancy episode. |
| 34 | `FIRST_PNT_LOC_C_NAME` | VARCHAR | org | This item stores who the patient's first prenatal care was with. |
| 35 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 36 | `OB_WRK_EDD_DT` | DATETIME |  | The estimated date of delivery for a pregnancy episode. |
| 37 | `EXPECTED_DEL_LOC_C_NAME` | VARCHAR | org | Location where the woman plans to deliver her baby. |
| 38 | `DEL_LOC_CHANGE_C_NAME` | VARCHAR | org | Why the delivery location changed from the expected delivery location (EXPECTED_DEL_LOC_C) for a pregnancy episode. |
| 39 | `OB_FEEDING_INTENTIONS_C_NAME` | VARCHAR | org | Mother's intended feeding method for the baby. |
| 40 | `INTENT_TREAT_C_NAME` | VARCHAR | org | The intended treatment for an implanted Mechanical Circulatory Device. |
| 41 | `INTENT_TREAT_OTHR` | VARCHAR |  | The free text intended treatment for an implanted Mechanical Circulatory Device. |
| 42 | `MCS_DISCHARGE_DT` | DATETIME |  | Date a Mechanical Circulatory Device patient is discharged. |
| 43 | `MCS_EVAL_DT` | DATETIME |  | The start date of the Mechanical Circulatory Device evaluation. |
| 44 | `MCS_REV_DT` | DATETIME |  | The date when the Mechanical Circulatory Device case was reviewed by the evaluation committee. |
| 45 | `MCS_ADMISSION_DT` | DATETIME |  | Date of the admission for the Mechanical Circulatory Device procedure. |
| 46 | `MCS_SURG_DT` | DATETIME |  | The date of the Mechanical Circulatory Device surgery. |
| 47 | `MCS_IS_HISTORIC_YN` | VARCHAR |  | Flag indicating a historic Mechanical Circulatory Device episode. This is intended to flag if the Device was implanted at another center than the Center that is currently following the patient. |
| 48 | `MCS_EVAL_END_DT` | DATETIME |  | The date on which the Mechanical Circulatory Device evaluation was completed. |
| 49 | `MCS_NEXT_REVIEW_DT` | DATETIME |  | The date on which both the Mechanical Circulatory Device episode and the patient chart should be reviewed. |
| 50 | `MCS_REFERRAL_DT` | DATETIME |  | The date the patient was referred for the Mechanical Circulatory Device. |
| 51 | `MCS_TXPORT_MTHD_C_NAME` | VARCHAR | org | The method of transportation to the implantation center. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (57)

| From | Column | Confidence |
|------|--------|------------|
| [ACCOUNT_3](ACCOUNT_3.md) | `EPISODE_ID` | high |
| [AI_INTRCT_INFO](AI_INTRCT_INFO.md) | `EPISODE_ID` | high |
| [ALL_EPISODE_CSN_LINKS](ALL_EPISODE_CSN_LINKS.md) | `EPISODE_ID` | high |
| [AP_CLAIMS_BUNDLE_LEDGER](AP_CLAIMS_BUNDLE_LEDGER.md) | `EPISODE_ID` | high |
| [BMT_DONOR_EPISODE_LINKS](BMT_DONOR_EPISODE_LINKS.md) | `EPISODE_ID` | high |
| [BMT_DONOR_SUITABILITY_AUD](BMT_DONOR_SUITABILITY_AUD.md) | `EPISODE_ID` | high |
| [BND_EPSD_BILLING_CMT](BND_EPSD_BILLING_CMT.md) | `EPISODE_ID` | high |
| [BND_EPSD_DIST_HX](BND_EPSD_DIST_HX.md) | `EPISODE_ID` | high |
| [BND_EPSD_EXCL_VISITS](BND_EPSD_EXCL_VISITS.md) | `EPISODE_ID` | high |
| [BND_EPSD_HX](BND_EPSD_HX.md) | `EPISODE_ID` | high |
| [BND_EPSD_INCL_VISITS](BND_EPSD_INCL_VISITS.md) | `EPISODE_ID` | high |
| [BND_EPSD_INFO](BND_EPSD_INFO.md) | `EPISODE_ID` | high |
| [BND_EPSD_INFO_TRANSFORM](BND_EPSD_INFO_TRANSFORM.md) | `EPISODE_ID` | high |
| [CHART_REVIEW_BOOKMARKS](CHART_REVIEW_BOOKMARKS.md) | `EPISODE_ID` | high |
| [CMGMT_EPISODE_CASE_TEAM](CMGMT_EPISODE_CASE_TEAM.md) | `EPISODE_ID` | high |
| [CMGMT_EPISODE_HX](CMGMT_EPISODE_HX.md) | `EPISODE_ID` | high |
| [CMGMT_EPISODE_TYPES](CMGMT_EPISODE_TYPES.md) | `EPISODE_ID` | high |
| [CMGMT_SUPPORT_TYPE_END](CMGMT_SUPPORT_TYPE_END.md) | `EPISODE_ID` | high |
| [CMGMT_SUPPORT_TYPE_POOL](CMGMT_SUPPORT_TYPE_POOL.md) | `EPISODE_ID` | high |
| [CMGMT_SUPPORT_TYPE_PROV](CMGMT_SUPPORT_TYPE_PROV.md) | `EPISODE_ID` | high |
| [CMGMT_SUPPORT_TYPE_START](CMGMT_SUPPORT_TYPE_START.md) | `EPISODE_ID` | high |
| [CMGMT_SUPPORT_TYPE_TYPE](CMGMT_SUPPORT_TYPE_TYPE.md) | `EPISODE_ID` | high |
| [COMP_ASMT_FLAGS](COMP_ASMT_FLAGS.md) | `EPISODE_ID` | high |
| [COMP_ASMT_REVIEW](COMP_ASMT_REVIEW.md) | `EPISODE_ID` | high |
| [DEVICE_TRACKING_DETAILS](DEVICE_TRACKING_DETAILS.md) | `EPISODE_ID` | high |
| [EPISODE_ALL](EPISODE_ALL.md) | `EPISODE_ID` | high |
| [EPSD_ASSOC_MEDS_HX_END_DT](EPSD_ASSOC_MEDS_HX_END_DT.md) | `EPISODE_ID` | high |
| [EPSD_ASSOC_MEDS_HX_MED](EPSD_ASSOC_MEDS_HX_MED.md) | `EPISODE_ID` | high |
| [EPSD_ASSOC_MEDS_HX_PRIM](EPSD_ASSOC_MEDS_HX_PRIM.md) | `EPISODE_ID` | high |
| [EPSD_ASSOC_MEDS_HX_ST_DT](EPSD_ASSOC_MEDS_HX_ST_DT.md) | `EPISODE_ID` | high |
| [HSB_TPL_LIST](HSB_TPL_LIST.md) | `EPISODE_ID` | high |
| [HSC_SPEC_INFO](HSC_SPEC_INFO.md) | `EPISODE_ID` | high |
| [HSP_ACCOUNT_4](HSP_ACCOUNT_4.md) | `EPISODE_ID` | high |
| [HSP_PRE_AR_BND_EPSD_HX](HSP_PRE_AR_BND_EPSD_HX.md) | `EPISODE_ID` | high |
| [IP_EPISODE_LINK](IP_EPISODE_LINK.md) | `EPISODE_ID` | high |
| [IP_WORKLIST](IP_WORKLIST.md) | `EPISODE_ID` | high |
| [LCA_COMM_ATTACH](LCA_COMM_ATTACH.md) | `EPISODE_ID` | high |
| [MED_THERAPY_PROB_INFO](MED_THERAPY_PROB_INFO.md) | `EPISODE_ID` | high |
| [NEPHROLOGY_INFO](NEPHROLOGY_INFO.md) | `EPISODE_ID` | high |
| [NEPH_MODALITY_EPISODE](NEPH_MODALITY_EPISODE.md) | `EPISODE_ID` | high |
| [NEPH_TREATMENT_DAYS](NEPH_TREATMENT_DAYS.md) | `EPISODE_ID` | high |
| [NEPH_TREATMENT_HISTORY](NEPH_TREATMENT_HISTORY.md) | `EPISODE_ID` | high |
| [NEPH_TREATMENT_HX_AUDIT](NEPH_TREATMENT_HX_AUDIT.md) | `EPISODE_ID` | high |
| [PAT_EPISODE](PAT_EPISODE.md) | `EPISODE_ID` | high |
| [PAT_REL_INFO_EPSD](PAT_REL_INFO_EPSD.md) | `EPISODE_ID` | high |
| [PEF_ADD_ED_TMSP](PEF_ADD_ED_TMSP.md) | `EPISODE_ID` | high |
| [PEF_FLO_DATA](PEF_FLO_DATA.md) | `EPISODE_ID` | high |
| [PEF_NTFY_INSTR](PEF_NTFY_INSTR.md) | `EPISODE_ID` | high |
| [POC_INFO](POC_INFO.md) | `EPISODE_ID` | high |
| [SMRTDTA_ELEM_EPISODE](SMRTDTA_ELEM_EPISODE.md) | `EPISODE_ID` | high |
| [SMRTDTA_ELEM_EPISODE_GRP](SMRTDTA_ELEM_EPISODE_GRP.md) | `EPISODE_ID` | high |
| [SOCIAL_CARE_EPISODE](SOCIAL_CARE_EPISODE.md) | `EPISODE_ID` | high |
| [TPL_HSB_EPT_LINK](TPL_HSB_EPT_LINK.md) | `EPISODE_ID` | high |
| [TRANSPLANT_DNRREL](TRANSPLANT_DNRREL.md) | `EPISODE_ID` | high |
| [TRANSPLANT_PRTCL](TRANSPLANT_PRTCL.md) | `EPISODE_ID` | high |
| [UCL_BUNDLED_EPISODE](UCL_BUNDLED_EPISODE.md) | `EPISODE_ID` | high |
| [V_EHI_HSB_LINKED_PATS](V_EHI_HSB_LINKED_PATS.md) | `EPISODE_ID` | high |

