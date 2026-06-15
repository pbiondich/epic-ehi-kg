# ORDER_MED

> The ORDER_MED table enables you to report on medications ordered in EpicCare (prescriptions). We have also included patient and contact identification information for each record.

**Overflow family:** [ORDER_MED_2](ORDER_MED_2.md), [ORDER_MED_3](ORDER_MED_3.md), [ORDER_MED_4](ORDER_MED_4.md), [ORDER_MED_5](ORDER_MED_5.md), [ORDER_MED_6](ORDER_MED_6.md), [ORDER_MED_7](ORDER_MED_7.md), [ORDER_MED_8](ORDER_MED_8.md)  
**Primary key:** `ORDER_MED_ID`  
**Columns:** 116  
**Org-specific columns:** 10  
**Joined by:** 37 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK | The unique ID of the order record associated with this medication order. This is an internal unique identifier for ORD master file records in this table and cannot be used to link to CLARITY_MEDICATION. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this line. This column is frequently used to link to the PATIENT table. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number (CSN) for the patient contact associated with this medication order. This number is unique across patients and encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 5 | `ORDERING_DATE` | DATETIME |  | The date when the medication order was placed. |
| 6 | `ORDER_CLASS_C_NAME` | VARCHAR | org | The category number for the order class. This value is used to define how clinical systems process the order. |
| 7 | `PHARMACY_ID` | NUMERIC | FK→ | The unique ID of the pharmacy record that is associated with this medication order. This column is frequently used to link to the RX_PHR table. This field is only populated if the clinical system user selects a specific pharmacy from the list, otherwise the field is null. This field is only populated by the ambulatory clinical system, not the pharmacy system. |
| 8 | `PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 9 | `ORD_CREATR_USER_ID` | VARCHAR |  | The EMP ID (.1) of the user who signed the order (for a non-signed and held order) or the last person who performed a sign and hold or release action for a signed and held order. |
| 10 | `ORD_CREATR_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 12 | `DESCRIPTION` | VARCHAR |  | The description of the order. This information is found in the Order field of clinical system’s Order Detail window. |
| 13 | `DOSAGE` | VARCHAR |  | The dispensation amount for the prescription entered by the user in the orders activity. This amount is stored as a string in the orders database. |
| 14 | `QUANTITY` | VARCHAR |  | The quantity of the prescription being dispensed as entered by the user. |
| 15 | `REFILLS` | VARCHAR |  | The number of refills allowed for this prescription as entered by the user. |
| 16 | `START_DATE` | DATETIME |  | The date when the medication order started. The date appears in calendar format. |
| 17 | `END_DATE` | DATETIME |  | The date when the medication order is to end. |
| 18 | `DISP_AS_WRITTEN_YN` | VARCHAR |  | Indicates whether or not the prescription should be dispensed as written for this medication. |
| 19 | `RSN_FOR_DISCON_C_NAME` | VARCHAR | org | The category number for the reason a prescription has been discontinued. This column contains data only in prescription orders that have been discontinued. |
| 20 | `MED_PRESC_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 21 | `NONFRM_XCPT_CD_C_NAME` | VARCHAR | org | The category number for medication's exception code. This code explains the reason a non-formulary medication was ordered. |
| 22 | `PANEL_MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 23 | `UPDATE_DATE` | DATETIME (Local) |  | The date and time when this row was created or last updated in Clarity. |
| 24 | `ORDER_INST` | DATETIME (Local) |  | The date and time the order was placed. The date appears in calendar format. |
| 25 | `DISPLAY_NAME` | VARCHAR |  | The name of the medication as it appears on the medication record itself. |
| 26 | `AS_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 27 | `HV_HOSPITALIST_YN` | VARCHAR |  | Indicates whether this is a hospitalist order. A Y indicates a hospitalist order. |
| 28 | `ORDER_PRIORITY_C_NAME` | VARCHAR | org | The category number for the priority assigned to an order. |
| 29 | `MED_ROUTE_C_NAME` | VARCHAR | org | The category number for the route of administration of a medication. |
| 30 | `DISCON_USER_ID` | VARCHAR |  | The unique ID of the user who discontinued the order. |
| 31 | `DISCON_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 32 | `DISCON_TIME` | DATETIME (UTC) |  | The date and time when the medication order was discontinued. The date appears in calendar format. |
| 33 | `CHNG_ORDER_MED_ID` | NUMERIC |  | The unique ID of the changed or reordered medication order that this order replaced. This column is frequently used to link back to the ORDER_MED table. |
| 34 | `PEND_APPR_USER_ID` | VARCHAR |  | The unique ID of the user who approved a pended order. |
| 35 | `PEND_APPR_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 36 | `PEND_REF_REAS_C_NAME` | VARCHAR | org | The category number for the reason a pended medication was refused. |
| 37 | `HV_DISCR_FREQ_ID` | VARCHAR |  | The unique ID of the discrete frequency record associated with this medication order. This column is frequently used to link to the IP_FREQUENCY table. |
| 38 | `HV_DISCR_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 39 | `HV_DISCRETE_DOSE` | VARCHAR |  | The discrete dose for a medication as entered by the user in the orders activity. |
| 40 | `HV_DOSE_UNIT_C_NAME` | VARCHAR | org | The category number for the dosage unit of a medication. |
| 41 | `HV_IS_SELF_ADM_YN` | VARCHAR |  | Indicates whether this medication was self-administered. A Y indicates that the order was self-administered. |
| 42 | `ORDER_START_TIME` | DATETIME (Local) |  | The date and time when the medication order is to start. The date appears in calendar format. |
| 43 | `ORDER_END_TIME` | DATETIME (Local) |  | The date and time when the medication order is scheduled to end. The date appears in calendar format. |
| 44 | `NON_FORMULARY_YN` | VARCHAR |  | Indicates whether this medication is not on the formulary. A Y indicates a non-formulary medication. |
| 45 | `ORDER_STATUS_C_NAME` | VARCHAR |  | The category number for the current status of an order. |
| 46 | `AUTHRZING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 47 | `ORD_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 48 | `MIN_DISCRETE_DOSE` | NUMERIC |  | The minimum ordered dose amount for the medication as specified by the user in the orders activity. |
| 49 | `MAX_DISCRETE_DOSE` | NUMERIC |  | The maximum ordered dose amount for the medication as specified by the user in the orders activity. |
| 50 | `DOSE_UNIT_C_NAME` | VARCHAR |  | The category number for the dose unit of a medication. |
| 51 | `IS_PENDING_ORD_YN` | VARCHAR |  | Indicates whether the order has a pending status. A Y indicates that the order does have a pending status. |
| 52 | `BULK_DISP_YN` | VARCHAR |  | Indicates whether this is a bulk dispense order. A Y indicates this is a bulk dispense order. |
| 53 | `PROVIDER_TYPE_C_NAME` | VARCHAR | org | The medication provider type category number for the order. This item distinguishes between authorizing and documenting provider types for historical and non-historical medications. If the medication was ordered as historical, the provider is considered the documenting provider and is reflected as such in this item. If the medication was not ordered as historical, the provider is considered the authorizing provider is reflected in this item as such. |
| 54 | `MODIFY_TRACK_C_NAME` | VARCHAR |  | The category number for the flag that both indicates and distinguishes whether an order was reordered or modified. |
| 55 | `SPECIFIED_FIRST_TM` | DATETIME (Local) |  | If the order was placed with a Specified frequency (the frequency's Type (I EFQ 50) item has a value of 1) and the user specified a first occurrence time, the time specified is stored in this column. |
| 56 | `SCHED_START_TM` | DATETIME (Local) |  | The date and time at which an order was scheduled to begin. The date appears in calendar format. |
| 57 | `ACT_ORDER_C_NAME` | VARCHAR |  | The category number indicating additional information about an order's status--Active, Completed, Discontinued, or Cancelled. An active order is any order that has not been completed, discontinued, cancelled, pended, or signed and held. |
| 58 | `EXP_AFT_START_DATE` | DATETIME |  | The number of days after the start date that the medication order will expire based on the setting in the medication record. The date appears in calendar format. |
| 59 | `EXP_BEF_END_DATE` | DATETIME |  | The number of days before the end date that the medication order will expire based on the setting in the medication record. The date appears in calendar format. |
| 60 | `MED_COMMENTS` | VARCHAR |  | Comments for a medication order, as entered by the ordering user when entering the order. |
| 61 | `USER_SEL_MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 62 | `USER_SEL_ERX_DAT` | DATETIME |  | The date that the medication record was actually selected by the user. This item is populated only if Intelligent Medication Selection (IMS) replaced the original user-selected medication with another medication record. |
| 63 | `REQ_RNVERIFY_YN` | VARCHAR |  | Indicates whether this medication order requires RN verification before it is administered. A Y indicates that it does require RN verification. |
| 64 | `MDL_ID` | NUMERIC |  | The unique ID of the medication problem list record that is associated with this medication order. This column is frequently used to link to the MDL_MD_PRBLM_LIST table. |
| 65 | `LASTDOSE` | VARCHAR |  | Comments for the last administered dose of a medication entered in the medication documentation navigator section. |
| 66 | `INFORMANT_C_NAME` | VARCHAR | org | The category number for the informant of a prior to admission (PTA) medication. The informant is the person who reports a PTA medication being taken by the patient. |
| 67 | `AMB_MED_DISP_NAME` | VARCHAR |  | The name of the ambulatory medication. |
| 68 | `WEIGHT_BASED_YN` | VARCHAR |  | Indicates whether the dose for this medication order is based on the patient's weight. |
| 69 | `WEIGHT_REVIEW_YN` | VARCHAR |  | Indicates whether or not the patient's weight needs to be reviewed for this medication order due to the patient's weight change. |
| 70 | `ORD_TM_WEIGHT` | NUMERIC |  | The patient's last reviewed weight at the time the medication was ordered. |
| 71 | `ORDER_TIME_WT_INST` | DATETIME (Local) |  | The date and time when a new weight is recorded for a patient for a weight based medication review. |
| 72 | `REVIEW_WEIGHT` | NUMERIC |  | The patient's last non-reviewed weight at the time the medication was ordered. |
| 73 | `REVIEW_WEIGHT_INST` | DATETIME (Local) |  | The instant when the patient's last non-reviewed weight was entered prior to when the medication was ordered. |
| 74 | `REFILLS_REMAINING` | NUMERIC |  | The number of refills remaining in the medication. |
| 75 | `MED_REFILL_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 76 | `OLD_ORDER_ID` | NUMERIC |  | The unique ID of the order record that points to the parent medication for refills. |
| 77 | `OLD_ORDER_DAT` | VARCHAR |  | The internal contact date of the parent medication in integer format. Used to identify the parent medication and will only be populated for child orders. This does not link to CONTACT_DATE_REAL. |
| 78 | `RESUME_STATUS_C_NAME` | VARCHAR |  | The category number that indicates an outpatient medication order's status before it was suspended as a result on inpatient admission. |
| 79 | `USER_ID_OF_PROV` | VARCHAR |  | The unique ID of the user record that is linked to the provider ID in the AUTHRZING_PROV_ID column. |
| 80 | `ORDERING_MODE_C_NAME` | VARCHAR |  | The category number for the ordering mode of the order (i.e. Outpatient, Inpatient). Note that Outpatient orders can be placed from an Inpatient encounter as discharge orders / take-home prescriptions. This column might be blank for Outpatient orders placed prior to the creation of the IP module. |
| 81 | `PEND_APPROVE_FLAG_C_NAME` | VARCHAR |  | The pending medication approval status category number for the order. |
| 82 | `NF_POST_VERIF_YN` | VARCHAR |  | Indicates whether a medication order has been verified by the pharmacist as non-formulary. A Y indicates that the pharmacist verified the medication order as non-formulary. An administrator can use this column to report on how many orders that were placed as non-formulary were also verified as such. To find which orders were placed as non-formulary, use the NON_FORMULARY_YN column. |
| 83 | `EXT_ELG_SOURCE_ID` | VARCHAR |  | External eligibility source ID |
| 84 | `EXT_ELG_MEMBER_ID` | VARCHAR |  | External eligibility member ID |
| 85 | `EXT_FORMULARY_ID` | VARCHAR |  | External formulary ID |
| 86 | `EXT_COVERAGE_ID` | VARCHAR |  | External coverage ID |
| 87 | `EXT_COPAY_ID` | VARCHAR |  | This column contains the external copay ID for an order. |
| 88 | `EXT_PHARMACY_TYPE_C_NAME` | VARCHAR | org | External pharmacy type |
| 89 | `EXT_FORMULARY_STAT` | VARCHAR |  | External Formulary Status |
| 90 | `EXT_COV_AGE_LMT_YN` | VARCHAR |  | External coverage age limits |
| 91 | `EXT_COV_EXCLUS_YN` | VARCHAR |  | External coverage product coverage exclusion |
| 92 | `EXT_COV_SEX_LMT_YN` | VARCHAR |  | External coverage gender limits |
| 93 | `EXT_COV_MED_NCST_YN` | VARCHAR |  | External coverage medical necessity |
| 94 | `EXT_COV_PRI_AUTH_YN` | VARCHAR |  | External coverage prior authorization |
| 95 | `EXT_COV_QNTY_LMT_YN` | VARCHAR |  | External coverage quantity limits |
| 96 | `EXT_COV_LNK_DRUG_YN` | VARCHAR |  | External coverage resource link drug |
| 97 | `EXT_COV_LNK_SMRY_YN` | VARCHAR |  | External coverage resource link summary |
| 98 | `EXT_COV_STEP_MED_YN` | VARCHAR |  | External coverage step medication |
| 99 | `EXT_COV_STEP_THR_YN` | VARCHAR |  | External coverage step therapy |
| 100 | `USR_SEL_IMS_YN` | VARCHAR |  | This item stores whether the product to use with IMS was selected by the user or chosen automatically. Yes means the user chose the product, No means the product was selected automatically. |
| 101 | `INDICATION_COMMENTS` | VARCHAR |  | The comment entered for the indications of use for this order. |
| 102 | `DOSE_ADJ_TYPE_C_NAME` | VARCHAR |  | The type of dose adjustment that was triggered by the order (i.e. maximum or minimum dose). |
| 103 | `DOSE_ADJ_OVERRID_YN` | VARCHAR |  | This item indicates whether the dose adjustment (i.e. maximum or minimum dose) was overridden. |
| 104 | `MAX_DOSE` | NUMERIC |  | The maximum allowed dose for this medication order. |
| 105 | `MAX_DOSE_UNIT_C_NAME` | VARCHAR |  | The unit for the maximum allowed dose for this medication order. |
| 106 | `PRN_COMMENT` | VARCHAR |  | The user-entered comments for why the as needed (PRN) medication should be administered. |
| 107 | `INST_OF_UPDATE_TM` | DATETIME (Local) |  | The day and time the order record was last updated. |
| 108 | `PEND_ACTION_C_NAME` | VARCHAR |  | The manner in which the medication was reordered, such as reorder from order review or reorder from the medications activity. |
| 109 | `MED_DIS_DISP_QTY` | NUMERIC |  | This item stores the discrete dispense quantity when discrete dispense is enabled. |
| 110 | `MED_DIS_DISP_UNIT_C_NAME` | VARCHAR |  | This item stores the discrete dispense unit when discrete dispense is enabled. |
| 111 | `END_BEFORE_CMP_INST` | DATETIME (Local) |  | The default end date and time of a completed order. When an order is completed, we will store the system calculated end date and time (which may differ from the actual completion time) in this column in the event the completion is reversed and the defaults need to be restored. |
| 112 | `BSA_BASED_YN` | VARCHAR |  | Indicates whether the dose for this medication order is based on the patient's body surface area (BSA). |
| 113 | `BSA_REVIEW_YN` | VARCHAR |  | Flags orders that need to be reviewed because of a BSA change. |
| 114 | `ORD_TM_BSA` | NUMERIC |  | The patient's last reviewed BSA at the time this order was placed. |
| 115 | `REVIEW_BSA` | NUMERIC |  | The patient's last non-reviewed body surface areas (BSA) at the time the medication was ordered. |
| 116 | `LAST_DOSE_TIME` | VARCHAR |  | Store the time that a PTA med was last taken. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `PHARMACY_ID` | [RX_PHR](RX_PHR.md) | sole_pk | high |

## Joined in — referenced by (37)

| From | Column | Confidence |
|------|--------|------------|
| [AUDIT_ORD_RXNOADD](AUDIT_ORD_RXNOADD.md) | `ORDER_MED_ID` | high |
| [EXTERNAL_TREATMENT](EXTERNAL_TREATMENT.md) | `ORDER_MED_ID` | high |
| [HH_MED_ORD_EVENTS](HH_MED_ORD_EVENTS.md) | `ORDER_MED_ID` | high |
| [IB_MESSAGES](IB_MESSAGES.md) | `ORDER_MED_ID` | high |
| [MAR_ADMIN_ALERT](MAR_ADMIN_ALERT.md) | `ORDER_MED_ID` | high |
| [MAR_ADMIN_ALT_EDIT](MAR_ADMIN_ALT_EDIT.md) | `ORDER_MED_ID` | high |
| [MAR_ADMIN_EDITD](MAR_ADMIN_EDITD.md) | `ORDER_MED_ID` | high |
| [MAR_ADMIN_INFO](MAR_ADMIN_INFO.md) | `ORDER_MED_ID` | high |
| [MAR_FSD_LINK](MAR_FSD_LINK.md) | `ORDER_MED_ID` | high |
| [MTP_AUTO_EVAL_MEDS](MTP_AUTO_EVAL_MEDS.md) | `ORDER_MED_ID` | high |
| [ORDER_DDX](ORDER_DDX.md) | `ORDER_MED_ID` | high |
| [ORDER_DISP_COMMENT](ORDER_DISP_COMMENT.md) | `ORDER_MED_ID` | high |
| [ORDER_DISP_INFO](ORDER_DISP_INFO.md) | `ORDER_MED_ID` | high |
| [ORDER_DISP_INFO_3](ORDER_DISP_INFO_3.md) | `ORDER_MED_ID` | high |
| [ORDER_DISP_INFO_4](ORDER_DISP_INFO_4.md) | `ORDER_MED_ID` | high |
| [ORDER_DISP_MEDS](ORDER_DISP_MEDS.md) | `ORDER_MED_ID` | high |
| [ORDER_DX_MED](ORDER_DX_MED.md) | `ORDER_MED_ID` | high |
| [ORDER_MEDINFO](ORDER_MEDINFO.md) | `ORDER_MED_ID` | high |
| [ORDER_MEDMIXINFO](ORDER_MEDMIXINFO.md) | `ORDER_MED_ID` | high |
| [ORDER_MED_ALTCSN](ORDER_MED_ALTCSN.md) | `ORDER_MED_ID` | high |
| [ORDER_RXVER_NOADSN](ORDER_RXVER_NOADSN.md) | `ORDER_MED_ID` | high |
| [ORDER_RX_RPT_HX](ORDER_RX_RPT_HX.md) | `ORDER_MED_ID` | high |
| [ORDER_SIGNED_MED](ORDER_SIGNED_MED.md) | `ORDER_MED_ID` | high |
| [ORD_MAR_RN_VERFY](ORD_MAR_RN_VERFY.md) | `ORDER_MED_ID` | high |
| [ORD_MED_ADMININSTR](ORD_MED_ADMININSTR.md) | `ORDER_MED_ID` | high |
| [ORD_MED_PRNREASONS](ORD_MED_PRNREASONS.md) | `ORDER_MED_ID` | high |
| [ORD_PROVISIONAL_VERIFY](ORD_PROVISIONAL_VERIFY.md) | `ORDER_MED_ID` | high |
| [PAT_LIFEDOSE_HX](PAT_LIFEDOSE_HX.md) | `ORDER_MED_ID` | high |
| [POC_MEDICATIONS](POC_MEDICATIONS.md) | `ORDER_MED_ID` | high |
| [RX_DISP_LOT](RX_DISP_LOT.md) | `ORDER_MED_ID` | high |
| [RX_DISP_LOT_EXP_DATE](RX_DISP_LOT_EXP_DATE.md) | `ORDER_MED_ID` | high |
| [RX_DISP_LOT_QTY](RX_DISP_LOT_QTY.md) | `ORDER_MED_ID` | high |
| [RX_DISP_LOT_UNIT](RX_DISP_LOT_UNIT.md) | `ORDER_MED_ID` | high |
| [SEP1_AUTOPOP_ANTIBIO](SEP1_AUTOPOP_ANTIBIO.md) | `ORDER_MED_ID` | high |
| [SEP1_AUTOPOP_CRYS_FLUID](SEP1_AUTOPOP_CRYS_FLUID.md) | `ORDER_MED_ID` | high |
| [SEP1_AUTOPOP_VSPR](SEP1_AUTOPOP_VSPR.md) | `ORDER_MED_ID` | high |
| [V_EHI_AUDIT_ORD_RXITEMS](V_EHI_AUDIT_ORD_RXITEMS.md) | `ORDER_MED_ID` | high |

