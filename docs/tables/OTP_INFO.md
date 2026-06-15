# OTP_INFO

> This table stores basic information about a treatment plan order, such as its status, display name, which medication or procedure it represents, etc.

**Overflow family:** [OTP_INFO_1](OTP_INFO_1.md), [OTP_INFO_2](OTP_INFO_2.md), [OTP_INFO_3](OTP_INFO_3.md), [OTP_INFO_4](OTP_INFO_4.md), [OTP_INFO_5](OTP_INFO_5.md)  
**Primary key:** `OTP_ID`  
**Columns:** 86  
**Org-specific columns:** 20  
**Joined by:** 66 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK | The unique identifier for the patient order template record. |
| 2 | `ORDER_TYPE_C_NAME` | VARCHAR | org | The order type of the order template in this row. |
| 3 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `ORDER_DESC` | VARCHAR |  | The description of the order linked to the order template in this row. |
| 5 | `DISPLAY_NAME` | VARCHAR |  | The display name of the order template in this row. |
| 6 | `PRESEL_DISPLAY_NAME` | VARCHAR |  | The pre-selection display name for the order template in this row. |
| 7 | `ORDER_CLASS_C_NAME` | VARCHAR | org | The order class of the order template in this row. |
| 8 | `RESULTING_AGENCY_ID` | NUMERIC |  | The resulting agency ID of the order template in this row. |
| 9 | `RESULTING_AGENCY_ID_LLB_NAME` | VARCHAR |  | Interface laboratory name. |
| 10 | `OTP_STATUS_C_NAME` | VARCHAR |  | The status of the order template in this row. May be empty, or In Process (being released), or Converted (actually released). |
| 11 | `PRIORITY_C_NAME` | VARCHAR | org | The priority of the order template in this row. |
| 12 | `ORDERING_QUANTITY` | NUMERIC |  | The ordering quantity of the order template in this row. |
| 13 | `DX_FOLLOW_UP_C_NAME` | VARCHAR | org | The diagnostic followup of the order template in this row. |
| 14 | `CHECK_OUT_COMMENT` | VARCHAR |  | The check-out comments for the order template in this row. |
| 15 | `SPECIMEN_TYPE_C_NAME` | VARCHAR | org | The specimen type for the order template in this row. |
| 16 | `SPECIMEN_SOURCE_C_NAME` | VARCHAR | org | The specimen source for the order template in this row. |
| 17 | `ORD_SIGN_CONTEXT_C_NAME` | VARCHAR | org | The context of revalidation for the order template in this row. |
| 18 | `ORDER_ID` | NUMERIC | shared | The unique identifier of the order record linked to the order template in this row. |
| 19 | `STANDING_ORDER_C_NAME` | VARCHAR |  | The standing status of the order template in this row, for example Standing or Once (Future). |
| 20 | `STANDING_EXP_DATE` | VARCHAR |  | The Recurring expiration date of the order template in this row. |
| 21 | `FUT_EXPECT_COMP_DT` | VARCHAR |  | The Once (Future) expected completion date of the order template in this row. |
| 22 | `FUT_APPROX_DT_YN` | VARCHAR |  | Indicates whether this patient order template has an approximate target date (Pre-May 26: approximate future expected date) |
| 23 | `STAND_INTERVAL` | VARCHAR |  | The Standing/Recurring interval for the order template in this row. |
| 24 | `DISCRETE_INTERVAL_C_NAME` | VARCHAR | org | The discrete interval selection for the order template in this row. |
| 25 | `STAND_OCCUR` | NUMERIC |  | The Standing/Recurring occurrences for the order template in this row. |
| 26 | `STAND_ORIG_OCCUR` | NUMERIC |  | The original number of Standing/Recurring occurrences for the order template in this row. |
| 27 | `PERFORMING_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 28 | `REFG_PROV_ID` | VARCHAR |  | The ID of the referring provider for the order template in this row. |
| 29 | `REFG_PROV_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 30 | `SER_ADDRESSID` | VARCHAR |  | Stores the referring provider address ID for referral orders. The format is provider external ID - Address line number. For example, if provider external ID = 123 and Address line = 4, the value would be 123-4. If the referring provider has no address, this will store the provider external ID only. |
| 31 | `REFD_TO_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 32 | `REFD_TO_FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 33 | `REFD_TO_SPECLTY_C_NAME` | VARCHAR | org | The referred-to specialty for the order template in this row. |
| 34 | `DEPT_REF_TO_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 35 | `DEPT_SPEC_REF_TO_C_NAME` | VARCHAR | org | The referred-to department specialty for the order template in this row. |
| 36 | `RFL_PRIORITY_C_NAME` | VARCHAR | org | The referral priority for the order template in this row. |
| 37 | `RFL_TYPE_C_NAME` | VARCHAR | org | The referral type for the order template in this row. This links to ZC_RFL_TYPE. |
| 38 | `RSN_FOR_RFL_C_NAME` | VARCHAR | org | The reason for referral for the order template in this row. |
| 39 | `RFL_NUM_VIS` | NUMERIC |  | The referral number of visits for the order template in this row. |
| 40 | `RFL_EXPIRE_DT` | VARCHAR |  | The referral expiration date for the order template in this row. |
| 41 | `PRN_COMMENT` | VARCHAR |  | The user-entered comments for why the PRN medication should be administered. |
| 42 | `MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 43 | `MED_CONTACT_DAT` | NUMERIC |  | The contact date of the linked medication for the order template in this row. |
| 44 | `MED_ROUTE_C_NAME` | VARCHAR | org | The route of the linked medication for the order template in this row. |
| 45 | `MED_QUANTITY` | VARCHAR |  | The quantity of the linked medication for the order template in this row. |
| 46 | `MED_REFILLS` | VARCHAR |  | The refill information for the linked medication for the order template in this row. |
| 47 | `MED_DIRECTN_LONG` | VARCHAR |  | The long version of the instructions for the medication linked to the order template in this row. |
| 48 | `MED_START_DATE` | VARCHAR |  | The start date of the medication linked to the order template in this row. |
| 49 | `START_TIME` | DATETIME (Local) |  | The start time of the medication linked to the order template in this row. |
| 50 | `MED_END_TIME` | DATETIME (Local) |  | The end time of the medication linked to the order template in this row. |
| 51 | `MED_END_DATE` | VARCHAR |  | The end date of the medication linked to the order template in this row. |
| 52 | `DISP_AS_WRITTEN_YN` | VARCHAR |  | The Y/N flag to dispense as written for the medication linked to the order template in this row. |
| 53 | `MED_DFL_DSCR_FRQ_YN` | VARCHAR |  | The Y/N flag to indicate if this order template applied to a patient should default discrete frequency info for after-visit (take-home prescription) orders. |
| 54 | `MED_DFL_DSCR_DOS_YN` | VARCHAR |  | The Y/N flag to indicate if this order template applied to a patient should default discrete dose info for after-visit (take-home prescription) orders. |
| 55 | `MED_NF_CODE_C_NAME` | VARCHAR | org | The non-formulary code for the medication linked to the order template in this row. |
| 56 | `MED_COMMENTS` | VARCHAR |  | The medication comments for the medication linked to the order template in this row. |
| 57 | `MED_NUM_OF_DOSES` | NUMERIC |  | The number of doses for the medication linked to the order template in this row. |
| 58 | `MED_TYPE_C_NAME` | VARCHAR |  | The type of medication linked to the order template in this row. |
| 59 | `MODIFIED_MIXTURE_YN` | VARCHAR |  | The Y/N flag for whether the order template in this row is a modified mixture. |
| 60 | `MED_INFUSION_TYPE_C_NAME` | VARCHAR | org | The infusion type for the medication linked to the order template in this row. |
| 61 | `MED_INFUSION_RATE` | VARCHAR |  | The infusion rate for the medication linked to the order template in this row. |
| 62 | `MED_RATE_UNIT_C_NAME` | VARCHAR | org | The units to use with the rate for the medication linked to the order template in this row. |
| 63 | `MED_INFUSE_DURATION` | VARCHAR |  | The duration for the medication linked to the order template in this row. |
| 64 | `MED_DURATION_UNIT_C_NAME` | VARCHAR |  | The units to use with the duration of the medication linked to the order template in this row. |
| 65 | `TPN_SITE_C_NAME` | VARCHAR | org | The infusion site of the medication linked to the order template in this row. |
| 66 | `MED_VOLUME` | VARCHAR |  | The volume of the medication linked to the order template in this row. |
| 67 | `MED_VOLUME_UNIT_C_NAME` | VARCHAR |  | The units to use with the volume of the medication linked to the order template in this row. |
| 68 | `CALCULATE_VOLUME_YN` | VARCHAR |  | The Y/N flag for whether or not the volume should be calculated for the medication linked to the order template in this row. |
| 69 | `MIXTURE_CONC_C_NAME` | VARCHAR | org | The concentration of a mixture (for fixed ratio mixtures) for the medication linked to the order template in this row. |
| 70 | `DISCRETE_FREQ_ID` | VARCHAR |  | The discrete frequency for the medication linked to the order template in this row. |
| 71 | `DISCRETE_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 72 | `DISCRETE_DOSE_MIN` | VARCHAR |  | The minimum discrete dose for a medication whose dose was entered as a range, or the discrete dose amount for a medication whose dose was not entered as a range. |
| 73 | `DOSE_UNIT_C_NAME` | VARCHAR |  | The dose unit category for the medication linked to the order template in this row. |
| 74 | `ORDER_TIME_PRIOR_C_NAME` | VARCHAR | org | The discrete order time priority for the medication linked to the order template in this row. |
| 75 | `ENC_CSN` | NUMERIC |  | The contact serial number (CSN) of the encounter linked to the order template in this row. |
| 76 | `ORDER_FREQ` | VARCHAR |  | The frequency of the medication being ordered in this order template. |
| 77 | `OTP_TPL_ID` | NUMERIC |  | The ID of the treatment plan that contains this order template. |
| 78 | `OTP_TRG_ID` | NUMERIC |  | The ID of the treatment day that contains this order template. |
| 79 | `DISCRETE_DOSE_MAX` | VARCHAR |  | The maximum discrete dose for a medication whose dose was entered as a range. |
| 80 | `MAX_DOSE` | NUMERIC |  | This column stores the suggested maximum dose amount for the patient order template record. |
| 81 | `MAX_DOSE_UNIT_C_NAME` | VARCHAR |  | This column stores the suggested maximum dose unit for the patient order template record. |
| 82 | `OVRD_IMS_PROD_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 83 | `INDICATION_COMMENTS` | VARCHAR |  | User's comments for the corresponding Indications of Use (stored in OTP_INDICATIONS table) |
| 84 | `MED_DISP_QTY` | NUMERIC |  | This item stores the medication dispense quantity when discrete dispense is enabled. |
| 85 | `MED_DISP_UNIT_C_NAME` | VARCHAR |  | This item stores the medication dispense unit when discrete dispense is enabled. |
| 86 | `MAX_BSA` | NUMERIC |  | The maximum Body Surface Area (BSA) for an order, if the selected BSA is greater than this BSA than the selected BSA will be capped at this value. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (66)

| From | Column | Confidence |
|------|--------|------------|
| [CL_OTP_FST_LST_SCH](CL_OTP_FST_LST_SCH.md) | `OTP_ID` | medium |
| [DOSING_RULE_OVERRIDES](DOSING_RULE_OVERRIDES.md) | `OTP_ID` | medium |
| [EDITED_SIG_WARNING_ACK](EDITED_SIG_WARNING_ACK.md) | `OTP_ID` | medium |
| [IMAGING_CDS_ORDER_TEMPLT](IMAGING_CDS_ORDER_TEMPLT.md) | `OTP_ID` | medium |
| [MLSIG_PAT_TEMPLT_LEVEL_1](MLSIG_PAT_TEMPLT_LEVEL_1.md) | `OTP_ID` | medium |
| [MLSIG_PAT_TEMPLT_LEVEL_2](MLSIG_PAT_TEMPLT_LEVEL_2.md) | `OTP_ID` | medium |
| [ORDER_DEVIATION_ACTION](ORDER_DEVIATION_ACTION.md) | `OTP_ID` | medium |
| [ORDER_DEVIATION_INFO](ORDER_DEVIATION_INFO.md) | `OTP_ID` | medium |
| [OTP_ADDL_COMMENTS](OTP_ADDL_COMMENTS.md) | `OTP_ID` | medium |
| [OTP_ADDL_WISHES_DISPENSE](OTP_ADDL_WISHES_DISPENSE.md) | `OTP_ID` | medium |
| [OTP_ADDL_WISHES_MED](OTP_ADDL_WISHES_MED.md) | `OTP_ID` | medium |
| [OTP_ADMIN_INSTRS](OTP_ADMIN_INSTRS.md) | `OTP_ID` | medium |
| [OTP_ALERT_CSN](OTP_ALERT_CSN.md) | `OTP_ID` | medium |
| [OTP_ASSOC_WOUND](OTP_ASSOC_WOUND.md) | `OTP_ID` | medium |
| [OTP_BLOOD_SPEC_REQTS](OTP_BLOOD_SPEC_REQTS.md) | `OTP_ID` | medium |
| [OTP_CC](OTP_CC.md) | `OTP_ID` | medium |
| [OTP_COMPONENT_SEL](OTP_COMPONENT_SEL.md) | `OTP_ID` | medium |
| [OTP_COND_QUESNS](OTP_COND_QUESNS.md) | `OTP_ID` | medium |
| [OTP_DISPLAY_NAME_HX](OTP_DISPLAY_NAME_HX.md) | `OTP_ID` | medium |
| [OTP_DOSE_CHANGE](OTP_DOSE_CHANGE.md) | `OTP_ID` | medium |
| [OTP_DOSE_PARAMS](OTP_DOSE_PARAMS.md) | `OTP_ID` | medium |
| [OTP_DOSE_SUGG_OVRD](OTP_DOSE_SUGG_OVRD.md) | `OTP_ID` | medium |
| [OTP_DUAL_SIGN_INFO](OTP_DUAL_SIGN_INFO.md) | `OTP_ID` | medium |
| [OTP_DX_ASSOC](OTP_DX_ASSOC.md) | `OTP_ID` | medium |
| [OTP_EXCUSED_ACTIVITY](OTP_EXCUSED_ACTIVITY.md) | `OTP_ID` | medium |
| [OTP_INDICATIONS](OTP_INDICATIONS.md) | `OTP_ID` | medium |
| [OTP_INGRED](OTP_INGRED.md) | `OTP_ID` | medium |
| [OTP_INGRED_CALC_DOSE](OTP_INGRED_CALC_DOSE.md) | `OTP_ID` | medium |
| [OTP_INGRED_CALC_UNITS](OTP_INGRED_CALC_UNITS.md) | `OTP_ID` | medium |
| [OTP_INGRED_DOSE](OTP_INGRED_DOSE.md) | `OTP_ID` | medium |
| [OTP_INGRED_DOSE_UNITS](OTP_INGRED_DOSE_UNITS.md) | `OTP_ID` | medium |
| [OTP_NON_PREF_PROV_COMMENT](OTP_NON_PREF_PROV_COMMENT.md) | `OTP_ID` | medium |
| [OTP_NORWAY_PRECAUTIONS](OTP_NORWAY_PRECAUTIONS.md) | `OTP_ID` | medium |
| [OTP_OPIMS_OVERRIDE](OTP_OPIMS_OVERRIDE.md) | `OTP_ID` | medium |
| [OTP_OPIMS_OVERRIDE_DOSE](OTP_OPIMS_OVERRIDE_DOSE.md) | `OTP_ID` | medium |
| [OTP_OPIMS_OVERRIDE_ERX](OTP_OPIMS_OVERRIDE_ERX.md) | `OTP_ID` | medium |
| [OTP_OPIMS_OVERRIDE_UNITS](OTP_OPIMS_OVERRIDE_UNITS.md) | `OTP_ID` | medium |
| [OTP_ORDER_CMTS](OTP_ORDER_CMTS.md) | `OTP_ID` | medium |
| [OTP_ORDER_INSTRUCTION](OTP_ORDER_INSTRUCTION.md) | `OTP_ID` | medium |
| [OTP_ORDER_MODIFIER](OTP_ORDER_MODIFIER.md) | `OTP_ID` | medium |
| [OTP_ORDER_SPEC_QST](OTP_ORDER_SPEC_QST.md) | `OTP_ID` | medium |
| [OTP_PREP_INFO](OTP_PREP_INFO.md) | `OTP_ID` | medium |
| [OTP_PRESCRIPT_DETAILS_EXT](OTP_PRESCRIPT_DETAILS_EXT.md) | `OTP_ID` | medium |
| [OTP_PRN_REASONS](OTP_PRN_REASONS.md) | `OTP_ID` | medium |
| [OTP_REVIEW_HISTORY](OTP_REVIEW_HISTORY.md) | `OTP_ID` | medium |
| [OTP_RX_DOSEHX_CMNT](OTP_RX_DOSEHX_CMNT.md) | `OTP_ID` | medium |
| [OTP_RX_DOSEHX_DOSE](OTP_RX_DOSEHX_DOSE.md) | `OTP_ID` | medium |
| [OTP_RX_DOSEHX_DTTM](OTP_RX_DOSEHX_DTTM.md) | `OTP_ID` | medium |
| [OTP_RX_DOSEHX_PCT](OTP_RX_DOSEHX_PCT.md) | `OTP_ID` | medium |
| [OTP_RX_DOSEHX_RSN](OTP_RX_DOSEHX_RSN.md) | `OTP_ID` | medium |
| [OTP_RX_DOSEHX_SEL](OTP_RX_DOSEHX_SEL.md) | `OTP_ID` | medium |
| [OTP_RX_DOSEHX_TYPE](OTP_RX_DOSEHX_TYPE.md) | `OTP_ID` | medium |
| [OTP_RX_DOSEHX_UNIT](OTP_RX_DOSEHX_UNIT.md) | `OTP_ID` | medium |
| [OTP_RX_DOSEHX_USER](OTP_RX_DOSEHX_USER.md) | `OTP_ID` | medium |
| [OTP_RX_MIXTURE](OTP_RX_MIXTURE.md) | `OTP_ID` | medium |
| [OTP_SCHED_INSTRS](OTP_SCHED_INSTRS.md) | `OTP_ID` | medium |
| [OTP_SIGN_INFO](OTP_SIGN_INFO.md) | `OTP_ID` | medium |
| [OTP_SLV_APPL_REASON](OTP_SLV_APPL_REASON.md) | `OTP_ID` | medium |
| [OTP_SPECIAL_DOSING_INFO](OTP_SPECIAL_DOSING_INFO.md) | `OTP_ID` | medium |
| [OTP_STATUS](OTP_STATUS.md) | `OTP_ID` | medium |
| [OTP_TIMES_OF_DAY_IN_SIG](OTP_TIMES_OF_DAY_IN_SIG.md) | `OTP_ID` | medium |
| [OTP_VERB_SIGN_INFO](OTP_VERB_SIGN_INFO.md) | `OTP_ID` | medium |
| [RT_OTP_SITE_AND_TECHNQ](RT_OTP_SITE_AND_TECHNQ.md) | `OTP_ID` | medium |
| [RT_OTP_SITE_QUALIFIERS](RT_OTP_SITE_QUALIFIERS.md) | `OTP_ID` | medium |
| [SOURCE_ORDER_EDITED_SIG](SOURCE_ORDER_EDITED_SIG.md) | `OTP_ID` | medium |
| [V_EHI_AUDIT_OTP](V_EHI_AUDIT_OTP.md) | `OTP_ID` | medium |

