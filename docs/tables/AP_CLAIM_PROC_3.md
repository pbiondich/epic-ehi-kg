# AP_CLAIM_PROC_3

> This table summarizes data for AP Claims service lines, with each service line given one row. To link this table’s service line information back to a claim header, join this table to AP_CLAIM_PROC_IDS on the TX_ID column. If you need to report on claim service lines specific to Cost Sharing Reduction (CSR), join this table instead to AP_CLAIM_PROC_IDS_CSR on the TX_ID column.

**Overflow of:** [AP_CLAIM_PROC](AP_CLAIM_PROC.md)  
**Primary key:** `TX_ID`  
**Columns:** 90  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the AP Claim procedure transaction. |
| 2 | `ALWD_AMT_ADJ_RCR_TABLE_NAME` | VARCHAR |  | The name of the referral rules table record. |
| 3 | `ALWD_AMT_ADJ_FSC` | NUMERIC |  | The fee schedule that was used in determining the allowed amount of the service line on the AP Claim, if Regional Usual and Customary pricing was used. |
| 4 | `ALWD_AMT_ADJ_FSC_FEE_SCHEDULE_NAME` | VARCHAR |  | The name of each fee schedule. |
| 5 | `ALWD_AMT_ADJ_UC_HMU` | VARCHAR |  | The conversion factor table that was used in determining the allowed amount of the service line on the AP Claim, if Regional Usual and Customary pricing was used. |
| 6 | `ALWD_AMT_ADJ_UC_HMU_TABLE_NAME` | VARCHAR |  | The name for the conversion factor table. |
| 7 | `ALWD_AMT_ADJ_UC_ZIP` | INTEGER |  | The ZIP Code that was used in determining the allowed amount of the service line on the AP Claim, if Regional Usual and Customary pricing was used. |
| 8 | `ALWD_AMT_ADJ_RCR_LN` | INTEGER |  | The line number of the referral rules table used in determining the allowed amount of the service line on the AP Claim. Join ALWD_AMT_ADJ_RCR and ALWD_AMT_ADJ_RCR_LN to REFERRAL_RCR_LINE.TABLE_ID and REFERRAL_RCR_LINE.LINE for information on the matched line. |
| 9 | `ALWD_AMT_ADJ_CFR_RQ` | VARCHAR |  | The benefit referral classifier from the referral rules table that is used to determine the referral requirement for the allowed amount of the service line on the AP Claim. |
| 10 | `ALWD_AMT_ADJ_CFR_RQ_CLASSIFIER_NAME` | VARCHAR |  | The title of the classifier record. |
| 11 | `ALWD_AMT_ADJ_USE_UC` | INTEGER |  | Determines whether the Usual and Customary value in the contract was used. Join this column to ZC_IS_UC_APPLIED on INTERNAL_ID in order to translate values. |
| 12 | `PROC_QTY_OVRRIDEN_C_NAME` | VARCHAR |  | Flag to indicate if the Procedure Quantity was manually overridden by the user. |
| 13 | `PMT_INFO_RESP_ID` | NUMERIC |  | The responsibility class from the split definition table that was assigned to the service line on the AP Claim. |
| 14 | `PMT_INFO_RESP_ID_RECORD_NAME` | VARCHAR |  | The name of the responsibility class record. |
| 15 | `PMT_INFO_SPLIT_DATE` | DATETIME |  | The effective date of the split definition table used in determining the responsibility class of the service line on the AP Claim. |
| 16 | `PMT_INFO_SPLIT_LINE` | INTEGER |  | The line of the split definition table used in determining the responsibility class of the service line on the AP Claim. |
| 17 | `PMT_INFO_CPNT_ID` | VARCHAR |  | The component or component group of the split definition table used in determining the responsibility class of the service line on the AP Claim. |
| 18 | `PMT_INFO_CPNT_ID_COMPONENT_INDEX_NAME` | VARCHAR |  | The name of the component index record |
| 19 | `SERVICE_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 20 | `START_TIME` | DATETIME (Local) |  | The start time of the procedure. |
| 21 | `STOP_TIME` | DATETIME (Local) |  | The stop time of the procedure. |
| 22 | `SERVICE_TIME` | NUMERIC |  | The elapsed time of the procedure in minutes. |
| 23 | `PMT_RESP_OVER_ID` | NUMERIC |  | The override responsibility class that was assigned to the service line on the AP Claim. |
| 24 | `PMT_RESP_OVER_ID_RECORD_NAME` | VARCHAR |  | The name of the responsibility class record. |
| 25 | `VEN_CNTRCT_RFL_LST` | VARCHAR |  | The list of referrals satisfying the vendor contract authorization requirements. This column will be deprecated in a future release. Reporting content should use Clarity table AP_CLM_PX_VEN_CNTRCT_RFL going forward, which contains one row per linked referral record. |
| 26 | `OPR_AUTH_RFL_LST` | VARCHAR |  | The list of referrals satisfying the operational authorization requirements. This column will be deprecated in a future release. Reporting content should use Clarity table AP_CLM_PX_OPR_AUTH_RFL going forward, which contains one row per linked referral record. |
| 27 | `BEN_REQ_RFL_LST` | VARCHAR |  | The list of referrals satisfying the benefits authorization requirements. This column will be deprecated in a future release. Reporting content should use Clarity table AP_CLM_PX_BEN_AUTH_RFL going forward, which contains one row per linked referral record. |
| 28 | `OPR_AUTH_CMP_CMG_ID` | VARCHAR |  | The unique identifier of the component or component group matched on the operational authorization table for this procedure. The operational authorization table is found in the Tapestry Profile. |
| 29 | `OPR_AUTH_CMP_CMG_ID_COMPONENT_INDEX_NAME` | VARCHAR |  | The name of the component index record |
| 30 | `OPR_AUTH_NET_C_NAME` | VARCHAR | org | The column stores the network status value as found by matching on the operational authorization table. The operational authorization table is found in the Tapestry Profile. The stored values can be translated using the ZC_NETWORK_LEVELS table. |
| 31 | `OPR_AUTH_EFF_DATE` | DATETIME |  | The effective date column value of the matched row on the operational authorization table. The operational authorization table is found in the Tapestry Profile. |
| 32 | `OPR_AUTH_TERM_DATE` | DATETIME |  | The termination date column value of the matched row on the operational authorization table. The operational authorization table is found in the Tapestry Profile. |
| 33 | `OPR_AUTH_REQ_C_NAME` | VARCHAR |  | This column stores whether or not authorization is required as found by matching on the operational authorization table. The operational authorization table is found in the Tapestry Profile. The stored values can be translated using the ZC_AUTH_REC table. |
| 34 | `OPR_AUTH_CFR_ID` | VARCHAR |  | The column stores the unique identifier of the referral classifier as found by matching on the operational authorization table. The operational authorization table is found in the Tapestry Profile. |
| 35 | `OPR_AUTH_CFR_ID_CLASSIFIER_NAME` | VARCHAR |  | The title of the classifier record. |
| 36 | `HR_AMOUNT` | NUMERIC |  | The healthcare reimbursement amount for the procedure. |
| 37 | `OVERRIDE_HR_AMOUNT` | NUMERIC |  | The override healthcare reimbursement amount. |
| 38 | `PMT_ORIG_RESP_ID` | NUMERIC |  | The responsibility class that was originally matched before it got overridden by the system. |
| 39 | `PMT_ORIG_RESP_ID_RECORD_NAME` | VARCHAR |  | The name of the responsibility class record. |
| 40 | `ALWD_AMT_ADJ_UC_FSM` | NUMERIC |  | The fee schedule map that was used in determining the allowed amount of the service line on the AP Claim, if Regional Usual and Customary pricing was used. |
| 41 | `ALWD_AMT_ADJ_UC_FSM_FEE_SCHEDULE_MAP_NAME` | VARCHAR |  | The name for the fee schedule map record. |
| 42 | `NETWORK_STATUS_C_NAME` | VARCHAR | org | Network status at the service level |
| 43 | `OVRD_STOP_LOSS_YN` | VARCHAR |  | If set to 1-Yes, then the contractual stop loss threshold will not be evaluated when this service is adjudicated, and stop loss will therefore not be applied to this service. If set to 0-No, then stop loss will be applied to this service if applicable to the claim. If left blank, then the claim-level override (CLM 18132) will be used. |
| 44 | `PRIM_PAT_NOTCOV` | NUMERIC |  | For non-primary claims (e.g. secondary), the patient not covered amount adjudicated by the primary insurance company. |
| 45 | `PRIM_PAT_DED` | NUMERIC |  | For non-primary claims (e.g. secondary), the patient deductible amount adjudicated by the primary insurance company. |
| 46 | `PRIM_PAT_COPAY` | NUMERIC |  | For non-primary claims (e.g. secondary), the patient copay amount adjudicated by the primary insurance company. |
| 47 | `PRIM_PAT_COINS` | NUMERIC |  | For non-primary claims (e.g. secondary), the patient co-insurance amount adjudicated by the primary insurance company. |
| 48 | `ORIGINAL_TX_ID` | NUMERIC |  | Holds the original service line ID for claim line splitting. |
| 49 | `ALWD_AMT_ADJ_DSLW_DSC_YN` | VARCHAR |  | This column stores a Y/N flag if the amount of this service line will route to patient responsibility as a disallowed amount. If Y, the discount amount on a service priced by the line was routed to patient responsibility as a disallowed amount. If N, means the system left the discount amount as provider responsibility. |
| 50 | `ALWD_AMT_ADJ_NSL` | NUMERIC |  | This column stores the ID stop loss term record (NSL) that was used in determining the allowed amount of this service line. |
| 51 | `ALWD_AMT_ADJ_NSL_RECORD_NAME` | VARCHAR |  | The name of the stop loss term record. |
| 52 | `ALWD_AMT_ADJ_UBC` | NUMERIC |  | This column stores the ID of the revenue record (UBC) used in determining the allowed amount of this service line. |
| 53 | `ALWD_AMT_ADJ_UBC_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 54 | `RESPONSIBLE_AMOUNT` | NUMERIC |  | Stores the responsible amount for this service line, as calculated by custom COB logic. If the payment method (AP_CLAIM.METH_TO_PAY_CLM_C) for the claim this service line is associated with is 1 (Primary Coverage), this column will be null. |
| 55 | `NDC_PRICE` | NUMERIC |  | Holds the National Drug Code (NDC) price for the service. |
| 56 | `NDC_FEE_SCHEDULE_ID` | NUMERIC |  | Holds the ID of the National Drug Code (NDC) fee schedule used. |
| 57 | `NDC_FEE_SCHEDULE_ID_FEE_SCHEDULE_NAME` | VARCHAR |  | The name of each fee schedule. |
| 58 | `NDC_PRICING_METHOD_C_NAME` | VARCHAR |  | Holds the category ID of the contract-level National Drug Code (NDC) pricing method for the service. |
| 59 | `NDC_PRICING_METHOD_ALLOWED_C_NAME` | VARCHAR |  | Holds the category ID of the National Drug Code (NDC) pricing method applied to the service allowed amount. |
| 60 | `NDC_HANDLING_FEE` | NUMERIC |  | Holds the National Drug Code (NDC) handling fee used to price the service. |
| 61 | `NDC_BASE_RATE` | NUMERIC |  | The National Drug Code (NDC) base rate used to price the service. |
| 62 | `NDC_UNIT_PRICE` | NUMERIC |  | Holds the National Drug Code (NDC) unit price used to price the service. |
| 63 | `NDC_PERCENT_OF_UNIT` | NUMERIC |  | Holds the National Drug Code (NDC) percent of unit charge used to price the service. |
| 64 | `NDC_PERCENT_OF_FEE` | NUMERIC |  | Holds the National Drug Code (NDC) percent of fee schedule used to price the service. |
| 65 | `NDC_CLAIM_THRESHOLD` | NUMERIC |  | Holds the National Drug Code (NDC) claim-level threshold used to price the service. |
| 66 | `NDC_SERVICE_THRESHOLD` | NUMERIC |  | Holds the National Drug Code (NDC) service-level threshold used to price the service. |
| 67 | `NDC_SERVICE_THRESHOLD_TYPE` | NUMERIC |  | Holds the National Drug Code (NDC) service-level threshold type. |
| 68 | `NDC_CLAIM_THRESHOLD_MET_YN_NAME` | VARCHAR |  | A flag that stores whether or not the National Drug Code (NDC) claim-level threshold was met. If set to 0-No, the threshold was not met. If set to 1-Yes, the threshold was met. |
| 69 | `NDC_SERVICE_THRESHOLD_MET_YN_NAME` | VARCHAR |  | A flag that stores whether or not the National Drug Code (NDC) claim-level threshold was met. If set to 0-No, the threshold was not met. If set to 1-Yes, the threshold was met. |
| 70 | `NDC_PAYMENT_MECHANISM_PRICE` | NUMERIC |  | Holds the contractual payment mechanism price that the National Drug Code (NDC) price was compared with or added to during adjudication. |
| 71 | `ADJ_TO_PAT_OOP` | NUMERIC |  | Amount that the patient out of pocket would have been on a capitated secondary service had the service not been capitated according to the contract. This amount gets displayed on the 835 in the CAS*CO*45 segment. |
| 72 | `REDISTRIBUTED_TO_TX_ID` | NUMERIC |  | Specifies the line to which this line's primary factors (primary insurance and primary patient portion) were redistributed for the purposes of secondary claim adjudication, if applicable. |
| 73 | `REPRESENTATIVE_LINE_YN` | VARCHAR |  | Specifies whether this line is used as a representative line for one or more other service lines for the purposes of secondary claim adjudication. |
| 74 | `OVERRIDE_RENTAL_RECORD_ID` | NUMERIC |  | Contains the rental record which this service should use when pricing by durable medical equipment (DME) rental. |
| 75 | `DME_RENTAL_ID` | NUMERIC |  | Contains the rental linked to this service. |
| 76 | `SYS_ADJUST_REASON_C_NAME` | VARCHAR | org | The category value of the system calculated reason for the adjustment to this procedure on the accounts payable claim record. |
| 77 | `DME_PRICING_RECORD_ID` | NUMERIC |  | Holds the Durable Medical Equipment (DME) pricing record used during adjudication of the claim. |
| 78 | `DME_PRICING_RECORD_ID_RECORD_NAME` | VARCHAR |  | The name of the pricing record. |
| 79 | `MOOP_MET_C_NAME` | VARCHAR |  | Maximum Out-Of-Pockets (MOOPs) apply to this service. |
| 80 | `DEDUCTIBLE_MET_C_NAME` | VARCHAR |  | Displays whether the deductible limit was met, not met, or didn't apply to this service. 11 - Yes indicates that the deductible was met by this service or before the service was adjudicated. 12 - No indicates that a deductible applies to the service, but the limit was not met as of the time the service was adjudicated. 13 - N/A indicates that no deductibles apply to this service. |
| 81 | `NOT_COVERED_YN` | VARCHAR |  | Stores Yes if the service is not covered, No if the service is covered, or NULL if the service was adjudicated prior to this calculation being available. |
| 82 | `SUBROGATION_DEMAND_AMT` | NUMERIC |  | This item stores the subrogation demand amount from another payer for a service. |
| 83 | `SUBROGATION_ADJ_AMT` | NUMERIC |  | This item stores the amount for a service that was not paid due to subrogation demand being less than net payable. |
| 84 | `LN_ITEM_CTRL_NUM` | VARCHAR |  | The line item control number from the submitted EDI claim. This is the ID of the service line in the submitter's system. |
| 85 | `CLIA_NUMBER` | VARCHAR |  | Identification of a Clinical Laboratory Improvement Amendment (CLIA) certified facility that contrasts with the claim level. |
| 86 | `REFERRING_CLIA_FACILITY_IDENT` | VARCHAR |  | Identification of a Clinical Laboratory Improvement Amendment (CLIA) certified facility that was referred to for qualifying tests. |
| 87 | `HAS_UNMAPPED_CODE_YN` | VARCHAR |  | Indicates if there were procedure codes on the incoming claim that could not be mapped to internal records. |
| 88 | `PI_REDUCT_AMT` | NUMERIC |  | Payer Initiated Billed Amount Reduction from Emergency Department Claim (EDC) Analyzer as a result of down coding. |
| 89 | `PI_REDUCT_OVRIDE_AMT` | NUMERIC |  | Override amount for Payer Initiated Reduction |
| 90 | `ALWD_AMT_ADJ_UC_ZIP_FULL` | VARCHAR |  | The ZIP Code that was used in determining the allowed amount of the service line on the AP Claim, if Regional Usual and Customary pricing was used. This column can support both 5 and 9 digit zip codes. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

