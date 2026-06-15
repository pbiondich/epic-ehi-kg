# AP_CLAIM

> The AP_CLAIM table contains one record for each claim in the managed care system's AP Claims module.

**Overflow family:** [AP_CLAIM_2](AP_CLAIM_2.md), [AP_CLAIM_3](AP_CLAIM_3.md), [AP_CLAIM_4](AP_CLAIM_4.md)  
**Primary key:** `CLAIM_ID`  
**Columns:** 133  
**Org-specific columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier of the accounts payable claim record. |
| 2 | `ORIG_CLAIM_NUM` | VARCHAR |  | Stores the original claim number after it is changed. |
| 3 | `STATUS_C_NAME` | VARCHAR |  | Stores the unique category identifier of the claims processing status, such as whether it is pending, clean, denied, or void. |
| 4 | `AP_STS_C_NAME` | VARCHAR |  | Stores the unique category identifier of the claim's AP status or NULL if the claim has not been sent to AP. |
| 5 | `DATE_RECEIVED` | DATETIME |  | The date the accounts payable claim was received. |
| 6 | `ADMISSION_DATE` | DATETIME |  | The date on which the member was admitted to the place of service. |
| 7 | `ADMISSION_HOUR` | NUMERIC |  | The hour at which the member was admitted to the place of service. |
| 8 | `ENTRY_DATE` | DATETIME |  | The date the accounts payable claim was entered into Epic. |
| 9 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 10 | `NUM_PROC` | INTEGER |  | The number of procedures on the accounts payable claim record. |
| 11 | `TOT_BILLED_AMT` | NUMERIC |  | The total billed amount on the claim. |
| 12 | `TOT_PAT_PORTION` | NUMERIC |  | The total patient portion on the claim. |
| 13 | `TOT_NET_PAYABLE` | NUMERIC |  | The total net payable amount on the claim. |
| 14 | `COVERAGE_ID` | NUMERIC | FK→ | Stores the identifier of the coverage used to process the claim. |
| 15 | `SERV_DATE` | DATETIME |  | Stores the service start date for the first service line on the claim. |
| 16 | `ASSOC_SPEC_C_NAME` | VARCHAR | org | The category value corresponding to the specialty associated with the accounts payable claim record. |
| 17 | `PAT_STATUS_C_NAME` | VARCHAR | org | The category value representing the member's discharge disposition/status as of the service end date. |
| 18 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 19 | `ADMISSION_SOURCE_C_NAME` | VARCHAR | org | The category value representing the origin or source of admission. |
| 20 | `EXTERNAL_CLAIM_ID` | VARCHAR |  | The external claim identification number. Note: This is not used for linking purposes. |
| 21 | `PAY_BY_DATE` | DATETIME |  | The date by which the accounts payable claim should be paid. |
| 22 | `NETWORK_ID` | VARCHAR | FK→ | The unique ID of the network associated with this accounts payable claim record. |
| 23 | `NETWORK_ID_NETWORK_NAME` | VARCHAR |  | The name of the network. |
| 24 | `METH_TO_PAY_CLM_C_NAME` | VARCHAR | org | Stores the category identifier of the method used to pay the claim, such as whether it was paid as primary or secondary. |
| 25 | `TOT_PRIM_INS_AMT` | NUMERIC |  | The amount already paid towards the billed amount on the claim by primary payors. This is applicable only if the claim has been submitted to your facility as the secondary payor. |
| 26 | `TOT_PRIM_PAT_PORT` | NUMERIC |  | Displays the amount the primary payors adjudicated as the patient portion. This is applicable only if the claim has been submitted to your facility as the secondary payor. |
| 27 | `TOT_ADJUSTMENT` | NUMERIC |  | The total adjustment amount associated with the accounts payable claims record. |
| 28 | `ADMISSION_TYPE_C_NAME` | VARCHAR | org | The category value representing the type of admission. |
| 29 | `TOT_INSURANCE_AMT` | NUMERIC |  | The total insurance amount associated with the accounts payable claim record. |
| 30 | `ADMISSION_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 31 | `TOT_NET_INSURANCE` | NUMERIC |  | The total net insurance amount remaining after deducting all applicable adjustments and other payments from the total insurance amount. |
| 32 | `E_CODE_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 33 | `TYPE_OF_BILL` | VARCHAR |  | The type of bill associated with the accounts payable claim record. |
| 34 | `RCVD_BY_CARRIER_DT` | DATETIME |  | The date the accounts payable claim was received by the carrier. |
| 35 | `HCFA_UNCLEAN_YN` | VARCHAR |  | An indication of whether the CMS claim contained errors. |
| 36 | `ORIG_REV_CLM_ID` | NUMERIC |  | The ID number of the original claim related to a reversed claim. |
| 37 | `ADJST_CLM_ID` | NUMERIC |  | The ID number of an adjustment claim. |
| 38 | `ORIG_ADJST_CLM_ID` | NUMERIC |  | If a claim is an adjustment claim, this represents the ID number of the original claim being adjusted. |
| 39 | `REF_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 40 | `TOT_U_AND_C_AMT` | NUMERIC |  | The total usual and customary amount for the claim. |
| 41 | `TOT_DISALLOW_AMT` | NUMERIC |  | The total disallowed amount for the claim. |
| 42 | `TOT_NOT_COVD_AMT` | NUMERIC |  | The total not covered amount for the claim. |
| 43 | `TOT_DEDUCTIBLE` | NUMERIC |  | The total deductible for the claim. |
| 44 | `TOT_COPAY` | NUMERIC |  | The total copay for the claim. |
| 45 | `TOT_COINS` | NUMERIC |  | The total coinsurance amount for the claim. |
| 46 | `TOT_PAT_TOTAL` | NUMERIC |  | The total patient portion for the claim. |
| 47 | `TOT_BBEN_PNLTY` | NUMERIC |  | The total before benefit penalty amount for the claim. |
| 48 | `TOT_EXD_BEN_AMT` | NUMERIC |  | The total exceeded benefit amount for the claim. |
| 49 | `IN_OUT_NET_C_NAME` | VARCHAR | org | Indicates the network level of the claim, as computed during adjudication. |
| 50 | `RKP_ID` | VARCHAR | FK→ | The unique ID of the risk panel associated with the claim. |
| 51 | `RKP_ID_RISK_PANEL_NAME` | VARCHAR |  | The name of the risk panel. |
| 52 | `CLM_LOB_ID` | VARCHAR |  | Stores the unique identifier of the line of business associated with the claim. This is the LOB determined at adjudication. |
| 53 | `CLM_LOB_ID_LOB_NAME` | VARCHAR |  | The name of the line of business record. |
| 54 | `WORKFLOW_C_NAME` | VARCHAR | org | Stores the unique category identifier of the workflow this claim was created as part of. Standard AP Claims processed through Tapestry will store 0 or NULL in this column. |
| 55 | `SENSITIVITY_C_NAME` | VARCHAR | org | Stores the unique category identifier of the sensitivity applied to the claim, if any. This value is used to restrict access within Hyperspace. The values in AP_CLAIM_ANALYTICS_SENS are distinct and intended for use with reporting. |
| 56 | `SERVICE_START_DATE` | DATETIME |  | The earliest service start date among all services on the claim. |
| 57 | `SERVICE_END_DATE` | DATETIME |  | The service end date for the claim. |
| 58 | `TOT_COB_SAVING` | NUMERIC |  | The total Coordination of Benefits (COB) savings amount for the claim. |
| 59 | `TOT_PAT_OUT_PCKT` | NUMERIC |  | The total patient out-of-pocket amount for the claim. |
| 60 | `SHADOW_RECON_AMT` | NUMERIC |  | The shadow reconciliation threshold amount for the claim. |
| 61 | `DRG_ID` | VARCHAR | FK→ | The unique ID of the Diagnosis Related Group (DRG) associated with the claim. |
| 62 | `DRG_ID_DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |
| 63 | `TIF_NUM` | VARCHAR |  | The tax increment financing (TIF) number for the claim. |
| 64 | `LIFEMAX_AMT_IN` | NUMERIC |  | The amount applied to the patient's in-network lifetime maximum buckets for this claim. |
| 65 | `LIFEMAX_AMT_OUT` | NUMERIC |  | The amount applied to the patient's out-of-network lifetime maximum buckets for this claim. |
| 66 | `CLAIM_FORMAT_C_NAME` | VARCHAR |  | Indicates the format of the claim (CMS, UB, Rx). |
| 67 | `OTHER_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 68 | `OPERATING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 69 | `ADJ_TIME` | DATETIME (Local) |  | The adjudication date and time of the claim. |
| 70 | `ATTEND_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 71 | `TOT_COB_SV_PAYOUT` | NUMERIC |  | The total amount of Coordination of Benefits (COB) savings member payout. |
| 72 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 73 | `TOT_SEC_DIS` | NUMERIC |  | The total amount of secondary discount from all the services added up. |
| 74 | `TOT_PRIM_FAC` | NUMERIC |  | The total primary factor amounts from all the services added up. |
| 75 | `TOT_CODE_EDIT_SAV` | NUMERIC |  | The total amount of code edit savings for this claim. |
| 76 | `INTEREST_AMT_OVRD` | NUMERIC |  | This stores the override interest amount for the claim. |
| 77 | `RTF_EOB_NOTE_ID` | VARCHAR |  | Contains the most recently generated rich text explanation of benefits report. |
| 78 | `INFO_CVG_ID` | NUMERIC |  | The ID of the additional coverage record associated with the accounts payable claim record for informational and reporting purposes. |
| 79 | `CLM_PRIM_INS_AMT` | NUMERIC |  | Claim-level primary insurance amount to allocate between procedures |
| 80 | `CLM_PRIM_PAT_AMT` | NUMERIC |  | Claim-level primary patient amount to allocate between procedures |
| 81 | `STATUS_DATE` | DATETIME |  | The status date of the claim. |
| 82 | `PEND_TYPE_C_NAME` | VARCHAR |  | The category value of the pend type for this claim |
| 83 | `CL_DEN_PEND_EXAM_ID` | VARCHAR |  | The unique ID of the claims examiner who applied a status of clean, deny, or pend to this claim. |
| 84 | `CL_DEN_PEND_EXAM_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 85 | `CL_DEN_PEND_DTTM` | DATETIME (Local) |  | The date that a status of clean, deny, or pend was applied to this claim. |
| 86 | `VOID_EXAMINER_ID` | VARCHAR |  | The ID of the user who voided this claim. |
| 87 | `VOID_EXAMINER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 88 | `VOID_CHNG_DATETIME` | DATETIME (Local) |  | The date the claim was voided. |
| 89 | `ACCIDENT_DT` | DATETIME |  | The date of accident associated with the claim. |
| 90 | `ER_ENTRY_DATETIME` | DATETIME (Local) |  | The date and time of entry to emergency room. |
| 91 | `IN_NET_ADJUD_OVRD_C_NAME` | VARCHAR | org | Category value corresponding to the in network adjudication override reason. |
| 92 | `DRG_PRICING_YN` | VARCHAR |  | Indicates whether Diagnosis Related Groups (DRG) were used to price this claim. 'Y' indicates that DRG pricing was used, 'N' indicates that it was not. |
| 93 | `WORKFLOW_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 94 | `TOT_BILLED_ENT` | NUMERIC |  | The total billed entered for this claim. |
| 95 | `TOT_ALLOWED_AMT` | NUMERIC |  | The total allowed amount for this claim. |
| 96 | `TOT_WITHHOLDING` | NUMERIC |  | The total withholding for this claim. |
| 97 | `TOT_DISCOUNT` | NUMERIC |  | Total discount amount for this claim. |
| 98 | `ADJ_NET_PAID` | NUMERIC |  | Adjusted net paid for this claim. |
| 99 | `ADJ_PAT_PORTION` | NUMERIC |  | Adjusted patient portion for this claim. |
| 100 | `MEM_PRIMARY_NET_ID` | VARCHAR |  | The ID of the member's primary network. |
| 101 | `MEM_PRIMARY_NET_ID_NETWORK_NAME` | VARCHAR |  | The name of the network. |
| 102 | `LIFEMAX_ETR_DATA` | VARCHAR |  | The lifetime max transactions data for this claim. |
| 103 | `INBASKET_MESSAGE_ID` | VARCHAR |  | The ID of the in basket message associated with this claim. |
| 104 | `STMT_COV_FROM_DATE` | DATETIME |  | Start date for statement covers. |
| 105 | `STMT_COV_TO_DATE` | DATETIME |  | End date for statement covers. For claims processed through Epic for adjudication, this column is only populated for UB claims. |
| 106 | `MSP_YN` | VARCHAR |  | Indicates whether Medicare is listed as a secondary payor on the claim record. 'Y' indicates that Medicare is a secondary payor, 'N' indicates that it is not. |
| 107 | `CLM_REPRICER_ID` | NUMERIC |  | The ID of the 3rd party claim pricer |
| 108 | `CLM_REPRICER_ID_RUL_NAME` | VARCHAR |  | The name of the third-party pricing entity, grouper, or rule. |
| 109 | `COVERED_DAYS` | NUMERIC |  | The number of covered days on the claim. |
| 110 | `NONCOVERED_DAYS` | NUMERIC |  | The number of noncovered days on the claim. |
| 111 | `COINS_DAYS` | NUMERIC |  | The number of coinsurance days on the claim. |
| 112 | `LIFETIME_RESRV_DAYS` | NUMERIC |  | The number of lifetime reserve days for inpatient claims. |
| 113 | `ILL_INJ_LMP_DATE` | DATETIME |  | Date of injury/illness. |
| 114 | `INTEREST_TO_DT` | DATETIME |  | The to date for interest calculation for the claim. Used when the associated check which was returned is voided. |
| 115 | `DISCHRG_HR_UB92_FMT` | VARCHAR |  | The discharge hour listed on UB claims. |
| 116 | `ADJUSTMENT_USER_ID` | VARCHAR |  | The ID of the user who created the adjustment for this claim. |
| 117 | `ADJUSTMENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 118 | `ADJST_CREATE_DATE` | DATETIME |  | The date the adjustment claim was created. |
| 119 | `REFUNDED_FLAG_YN` | VARCHAR |  | Flag indicating if the claim has been refunded. |
| 120 | `EMPY_RELATED_YN` | VARCHAR |  | Indicates whether patient's condition is related to employment. |
| 121 | `AUTO_ACDNT_STATE_C_NAME` | VARCHAR | org | Specifies the state where the auto accident occurred. |
| 122 | `DISABILITY_FROM_DT` | DATETIME |  | The date the disability started. |
| 123 | `DISABILITY_TO_DT` | DATETIME |  | The date the disability ended. |
| 124 | `DISCHARGE_DATE` | DATETIME |  | The date patient was discharged. For claims processed through Epic for adjudication, this column is only populated for CMS claims. |
| 125 | `OUTSIDE_LAB_YN` | VARCHAR |  | Indicate if lab services outside the provider's office are involved. |
| 126 | `OUTSIDE_LAB_CHARGE` | NUMERIC |  | The cost of services performed at the outside lab. |
| 127 | `RELATED_CONDITION_C_NAME` | VARCHAR | org | Information regarding related condition. |
| 128 | `WGT_BED_DAYS` | NUMERIC |  | Total weight of bed days. |
| 129 | `TOT_CONV_DAYS_RFL` | NUMERIC |  | To store the total converted bed days on the only attached referral with bed days information in it. |
| 130 | `BENEFIT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 131 | `PLAN_GROUP_ID` | VARCHAR |  | Stores the unique identifier of the plan group for the coverage used to pay the claim, as of adjudication. |
| 132 | `PLAN_GROUP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |
| 133 | `ENTRY_INSTANT_DTTM` | DATETIME (Local) |  | The instant when the accounts payable claim record was created. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `DRG_ID` | [CLARITY_DRG](CLARITY_DRG.md) | sole_pk | high |
| `NETWORK_ID` | [CLARITY_NETWORK](CLARITY_NETWORK.md) | sole_pk | high |
| `RKP_ID` | [CLARITY_RKP](CLARITY_RKP.md) | sole_pk | high |

