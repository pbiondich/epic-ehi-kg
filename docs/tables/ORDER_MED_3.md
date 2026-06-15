# ORDER_MED_3

> This table enables you to report on medications ordered. This table should be used with ORDER_MED.

**Overflow of:** [ORDER_MED](ORDER_MED.md)  
**Primary key:** `ORDER_ID`  
**Columns:** 71  
**Org-specific columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `ORIG_RX_DOSAGE` | VARCHAR |  | Original prescription column; contains the medication order dosage. |
| 3 | `ORIG_RX_QUANTITY` | VARCHAR |  | Original prescription column; contains the medication order quantity. |
| 4 | `ORIG_RX_REFILLS` | VARCHAR |  | Original prescription column; contains the medication refills. |
| 5 | `ORIG_RX_DIRECTIONS` | VARCHAR |  | Original prescription column; contains the medication directions. |
| 6 | `ORIG_RX_PRE_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 7 | `ORIG_RX_COMMENTS` | VARCHAR |  | Original prescription column; contains the medication comments. |
| 8 | `PRESCRIP_EXP_DATE` | DATETIME |  | Contains the expiration date for the prescription. |
| 9 | `ORD_AUC` | NUMERIC |  | Item to store the area under curve value for medications using this value in dose calculation. |
| 10 | `ORD_SEL_TARGETAUC_C_NAME` | VARCHAR | org | Selected type of the Target AUC in the order composer. |
| 11 | `ORIG_RX_PHRM_ID` | NUMERIC |  | Original prescription column; contains the pharmacy |
| 12 | `ORIG_RX_PHRM_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 13 | `ORD_PHASE_OF_CARE_C_NAME` | VARCHAR | org | This item will store the phase of care for which this order was created. Example: Pre-Op, Intra-Op, PACU. |
| 14 | `ORIGINAL_MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 15 | `INTERACT_COMMENT` | VARCHAR |  | Interaction override comment. |
| 16 | `COPY_POINTER_ID` | NUMERIC |  | This object tracks order (ORD) record links created when using the inpatient or ambulatory order mover utilities to move an ORD record. This item is populated on the source ORD record and points to the target ORD record(s) created. |
| 17 | `CONDITION_FLAG` | INTEGER |  | This column contains the Condition Flag for an order. |
| 18 | `PRINT_LOCAL_COPY_YN` | VARCHAR |  | Indicates whether to print a copy of this order. 'Y' indicates to print a copy of this order. 'N' indicates not to print a copy of this order. |
| 19 | `ORX_ID` | NUMERIC |  | This column contains the record ID from the Order Lookup Index (ORX). The ORX contains records for all active medication records and procedure records. This may be populated if an order originates from an Order Panel. |
| 20 | `ORX_ID_ORDER_LOOKUP_NAME` | VARCHAR |  | The name (.2 item) for the order panel record. |
| 21 | `SELECTED_FOR_OPC_YN` | VARCHAR |  | Indicates whether the order has been selected for resulting in the Orderable/Performable/Chargeable navigator. |
| 22 | `MEDS_RESYME_REASO_C_NAME` | VARCHAR | org | This item stores the reason to resume the medication. |
| 23 | `MEDS_DC_REASON_C_NAME` | VARCHAR | org | This item is populated in discharge navigator to save discontinue reason at the time of discharge. The value entered will be copied to I ORD 7074. |
| 24 | `IP_INCLUDE_NOW_C_NAME` | VARCHAR |  | This is when to start the medication administration. |
| 25 | `IP_INCL_NOW_SCH_C_NAME` | VARCHAR |  | Result of Scheduling Include Now Instant for Order |
| 26 | `LAST_SCHED_DATE` | DATETIME |  | The last scheduled date of the order. |
| 27 | `MEDS_ACTION_VERB_C_NAME` | VARCHAR | org | Action verb which is used in patient sig of the order. |
| 28 | `MED_SOURCE_C_NAME` | VARCHAR | org | Source of externally ordered medication. |
| 29 | `CRCL_FORMULA_ID` | NUMERIC |  | The creatinine clearance CrCl programming point that will be used for AUC calculations for order whose dose calculation programming point does not specify a CrCl programming point. |
| 30 | `CRCL_FORMULA_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |
| 31 | `AFTER_ORDER_ID` | NUMERIC |  | This column contains the After Order ID for an order. |
| 32 | `BEFORE_ORDER_ID` | NUMERIC |  | This column contains the Before Order ID for an order. |
| 33 | `DIET_COMMENTS` | VARCHAR |  | This column contains the Diet Comments entered for an order. |
| 34 | `END_DT_BEF_FILL_DT` | DATETIME |  | Stores the order's end date before it was changed due to the order being (re)filled. This is needed so that if the fills are ever cancelled, we know what to set the end date back to. |
| 35 | `PREV_POC_C_NAME` | VARCHAR |  | This column contains the previous phase of care (I ORD 61040). The phase of care for an order is stored in I ORD 61010. If the phase of care is not needed when the sign and held order is released, the phase of care stored in I ORD 61010 is moved to I ORD 61040 for tracking purposes. The phase of care stored in I ORD 61040 can still be used in the MAR activity to allow for continued phase of care grouping. The list of phases of care not needed when sign and held orders are released is stored in I LSD 61050. |
| 36 | `ORDER_TIME` | DATETIME (Local) |  | The date and time when the medication order was placed. |
| 37 | `IS_HELD_ORDER_C_NAME` | VARCHAR |  | This item stores 1 if the order is signed and held and active |
| 38 | `TXT_ORDPROV_NAME` | VARCHAR |  | The name of the ordering provider, for providers that do not yet exist in the Provider (SER) master file. |
| 39 | `TXT_ORDPROV_DEA` | VARCHAR |  | The DEA number of the ordering provider, for providers that do not yet exist in the Provider (SER) master file. A DEA number is given to providers by the Drug Enforcement Administration and allows them to prescribe controlled substances. |
| 40 | `TXT_ORDPROV_NPI` | VARCHAR |  | The National Provider Identifier (NPI) of the ordering provider, for providers that do not yet exist in the Provider (SER) master file. |
| 41 | `TXT_ORDPROV_PHONE` | VARCHAR |  | The phone number of the ordering provider, for providers that do not yet exist in the Provider (SER) master file. |
| 42 | `TXT_ORDPROV_FAX` | VARCHAR |  | The fax number of the ordering provider, for providers that do not yet exist in the Provider (SER) master file. |
| 43 | `TXT_ORDPROV_STREET` | VARCHAR |  | The street address of the ordering provider, for providers that do not yet exist in the Provider (SER) master file. |
| 44 | `TXT_ORDPROV_CITY` | VARCHAR |  | The city of the ordering provider, for providers that do not yet exist in the Provider (SER) master file. |
| 45 | `TXT_ORDPROV_STATE_C_NAME` | VARCHAR | org | The state of the ordering provider, for providers that do not yet exist in the Provider (SER) master file. |
| 46 | `TXT_ORDPROV_ZIP` | VARCHAR |  | The zip code of the ordering provider, for providers that do not yet exist in the Provider (SER) master file. |
| 47 | `RX_SERIAL_NUMBER` | VARCHAR |  | Stores the prescription serial number commonly found on triplicate prescription forms. Triplicate prescription forms are used for controlled substances and require multiple copies of the prescription form. |
| 48 | `NOCHRG_EXT_RSLT_YN` | VARCHAR |  | This column returns whether the order is an external result that should not drop charges. A value of 1 returns Y. A value of 0 returns N. A null value will return null but is treated the same as 0 when dropping charges. |
| 49 | `WT_MAX_DOSE` | NUMERIC |  | This column returns the saved weight-based or body surface area (BSA)-based maximum dose for the order (ORD). |
| 50 | `WT_MAX_DOSE_UNIT_C_NAME` | VARCHAR | org | This column returns the saved unit for the weight-based or body surface area (BSA)-based maximum dose for the order (ORD). |
| 51 | `MAX_DOSE_SOURCE_C_NAME` | VARCHAR |  | This column returns the source of max dose information that was used in the order (ORD). |
| 52 | `SRC_RX_MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 53 | `SRC_RX_QUANTITY` | VARCHAR |  | The quantity of the originally prescribed medication as returned by the pharmacy in a refill request. |
| 54 | `SRC_RX_DIS_DISP_QTY` | NUMERIC |  | The discrete dispense quantity of the originally prescribed medication as returned by the pharmacy in a refill request. |
| 55 | `SRC_RX_DISP_UNIT_C_NAME` | VARCHAR |  | The discrete dispense unit of the originally prescribed medication as returned by the pharmacy in a refill request. |
| 56 | `SRC_RX_REFILLS` | VARCHAR |  | The number of refills of the originally prescribed medication as returned by the pharmacy in a refill request. |
| 57 | `SRC_RX_DIRECTIONS` | VARCHAR |  | The directions (patient sig) of the originally prescribed medication as returned by the pharmacy in a refill request. |
| 58 | `SRC_RX_START_DATE` | DATETIME |  | The start date of the originally prescribed medication as returned by the pharmacy in a refill request. |
| 59 | `SRC_RX_END_DATE` | DATETIME |  | The end date of the originally prescribed medication as returned by the pharmacy in a refill request. |
| 60 | `SRC_RX_DAW_YN` | VARCHAR |  | The Dispense as Written (DAW) flag of the originally prescribed medication as returned by the pharmacy in a refill request. |
| 61 | `SRC_RX_PRES_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 62 | `SRC_RX_COMMENTS` | VARCHAR |  | The comments associated with the originally prescribed medication as returned by the pharmacy in a refill request. |
| 63 | `PAT_SIG_REPLY_C_NAME` | VARCHAR |  | This column contains the user's response to the sig-related questions for previous sig reorder workflows. The sig is the description of how a medication is supposed to be administered which includes the dose and frequency. |
| 64 | `SIG_REVIEW_USER_ID` | VARCHAR |  | Holds the user ID of the user who reviewed the patient sig for accuracy. The sig is the description of how a medication is supposed to be administered which includes the dose and frequency. |
| 65 | `SIG_REVIEW_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 66 | `SIG_REVIEW_INS_DTTM` | DATETIME (Local) |  | Holds the instant that the user took action on the patient sig in previous sig workflows. The sig is the description of how a medication is supposed to be administered which includes the dose and frequency. |
| 67 | `SRC_RX_WRITTEN_DATE` | DATETIME |  | The written date of the originally prescribed medication as returned by the pharmacy in a refill request. |
| 68 | `DOSE_RND_ACK_RSN_C_NAME` | VARCHAR | org | The category number for the acknowledgement reason given by the user to override a dose rounding warning on this order. |
| 69 | `SRC_RX_DESC` | VARCHAR |  | The description of the originally prescribed medication as returned by the pharmacy in a refill request. |
| 70 | `EPRES_DEST_C_NAME` | VARCHAR |  | Indicates the destination of e-prescribing order. It will be set by an interface or the ambulatory pharmacy system. The item may not be populated for the old order records. |
| 71 | `CTRL_MED_YN` | VARCHAR |  | Indicates whether the medication was controlled when the order was signed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [ORDER_MED](ORDER_MED.md).

