# AP_CLAIM_PROC_2

> This table summarizes data for AP Claims service lines, with each service line given one row. To link this table’s service line information back to a claim header, join this table to AP_CLAIM_PROC_IDS on the TX_ID column. If you need to report on claim service lines specific to Cost Sharing Reduction (CSR), join this table instead to AP_CLAIM_PROC_IDS_CSR on the TX_ID column.

**Overflow of:** [AP_CLAIM_PROC](AP_CLAIM_PROC.md)  
**Primary key:** `TX_ID`  
**Columns:** 83  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the AP Claim procedure transaction. |
| 2 | `PAT_PAY_CMP_CMG` | VARCHAR |  | The component or component group used to determine the patient portion on service line of the AP claim. |
| 3 | `PAT_PAY_CMP_CMG_COMPONENT_INDEX_NAME` | VARCHAR |  | The name of the component index record |
| 4 | `PAT_PAY_CML_LN` | VARCHAR |  | The line of the adjudication table that was used to determine the patient portion of the service line on the AP Claim. |
| 5 | `PAT_PAY_NET` | VARCHAR |  | The network status of the service line on the AP claim. This column can be joined to column IN_OUT_NET_C in table ZC_IN_OUT_NET in order to translate the category value to the corresponding name or abbreviation. |
| 6 | `PAT_PAY_CMT` | NUMERIC |  | The benefit tier that was used to determine the patient portion of the service line on the AP Claim. |
| 7 | `PAT_PAY_CMT_COMPON_TIER_NAME` | VARCHAR |  | The name of the tier record. |
| 8 | `PAT_PAY_RFL` | NUMERIC |  | The referral attached to the AP claim. |
| 9 | `PAT_PAY_CMA` | NUMERIC |  | The adjudication formula used to determine the patient portion of the service on the AP claim. |
| 10 | `PAT_PAY_CMA_ADJUD_FORMULA_NAME` | VARCHAR |  | The name of the adjudication formula |
| 11 | `PAT_PAY_CMK` | NUMERIC |  | The benefit package used to determine the patient portion of the service line on the AP Claim. |
| 12 | `PAT_PAY_CMK_BENEFIT_PACKAGE_NM` | VARCHAR |  | The name of the benefit package. |
| 13 | `PAT_PAY_EPP_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 14 | `PAT_PAY_COPAY_CAT` | VARCHAR |  | The copay category used in adjudicating the service line of the AP claim. This column will be deprecated in a future release and replaced by the Clarity column AP_CLAIM_PROC_2.PAT_PAY_COPAY_SERVICE_TYPE_ID. |
| 15 | `PAT_PAY_DEP_SPEC` | INTEGER |  | The department specialty of the AP claim. This column will be deprecated in a future release and replaced by the Clarity column AP_CLAIM_PROC_2.PAT_PAY_SPECIALTY_DEP_C. |
| 16 | `PAT_PAY_PT_AMT` | VARCHAR |  | The patient portion for the service line on the AP claim. |
| 17 | `PAT_PAY_SRC` | VARCHAR |  | The source of the copay or coinsurance value for the service line on the AP claim. If equal to 1, the value comes from the benefit plan. If equal to a value other than 1, the value comes from a coverage-level override. This column will be deprecated in a future release and replaced by the Clarity column AP_CLAIM_PROC_2.PAT_PAY_COPAY_AMT_SRC_C. |
| 18 | `PAT_PAY_COPAY_FLAG` | VARCHAR |  | Stores 1 if the copay was collected at check-in. This column will be deprecated in a future release and replaced by the Clarity column AP_CLAIM_PROC_2.PAT_PAY_COPAY_COL_SRC_C. |
| 19 | `PAT_PAY_AUTH` | INTEGER |  | Indicates whether authorization is required for the service line on the AP Claim. |
| 20 | `PAT_PAY_CFR` | VARCHAR |  | The benefit referral classifier record that was used to determine the patient portion of the service line on the AP Claim. |
| 21 | `PAT_PAY_CFR_CLASSIFIER_NAME` | VARCHAR |  | The title of the classifier record. |
| 22 | `PAT_PAY_RFL_LST` | VARCHAR |  | The list of referrals associated with the service line on the AP Claim. This column will be deprecated in a future release and replaced by the Clarity table AP_CLM_PX_PAT_PAY_RFL. |
| 23 | `PAT_PAY_CML` | NUMERIC |  | The adjudication table used to determine the patient portion of the service line on the AP Claim. |
| 24 | `PAT_PAY_CML_ADJ_TABLE_NAME` | VARCHAR |  | The name of the adjudication table. |
| 25 | `PAT_PAY_LFTM_MAX_EX` | INTEGER |  | Stores 1 if the patient's lifetime maximum has been exceeded and null otherwise. |
| 26 | `PAT_PAY_QTY` | VARCHAR |  | The service line quantity used to adjudicate the AP Claim. |
| 27 | `ALWD_AMT_ADJ_CMP` | VARCHAR |  | The component or component group from the contract that was used to adjudicate the allowed amount of the service on the AP Claim. |
| 28 | `ALWD_AMT_ADJ_CMP_COMPONENT_INDEX_NAME` | VARCHAR |  | The name of the component index record |
| 29 | `ALWD_AMT_ADJ_NCC` | NUMERIC |  | The vendor contract record that was used to determine the allowed amount of the service line on the AP Claim. |
| 30 | `ALWD_AMT_ADJ_NCC_CONTRACT_NAME` | VARCHAR |  | The name of the Vendor-Network contract. |
| 31 | `ALWD_AMT_NCC_DAT` | DATETIME |  | The contact date of the vendor contract that was used to determine the allowed amount of the service line on the accounts payable claim record. |
| 32 | `ALWD_AMT_ADJ_NCC_LN` | VARCHAR |  | The line of the vendor contract that was used to determine the allowed amount of the service line on the AP Claim. |
| 33 | `ALWD_AMT_ADJ_EAP_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 34 | `ALWD_AMT_ADJ_ERX_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 35 | `ALWD_AMT_ADJ_DRG` | VARCHAR |  | The DRG record used to determine the allowed amount of the service line on the AP Claim. |
| 36 | `ALWD_AMT_ADJ_DRG_DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |
| 37 | `ALWD_AMT_ADJ_CMC_COMP_GRP_NAME` | VARCHAR |  | The name for the whole claim component group. |
| 38 | `ALWD_AMT_ADJ_CMC_LN` | VARCHAR |  | The service line from the AP Claim that matched the whole claim component group. |
| 39 | `SECTION_340B_YN` | VARCHAR |  | Stores Y or N that indicates whether or not the drug was dispensed under the Section 340B Program for NDCs. |
| 40 | `COB_AMOUNT` | NUMERIC |  | The calculated Coordination of Benefits (COB) amount for the service line. |
| 41 | `MOB_AMOUNT` | NUMERIC |  | The calculated Maintenance of Benefits (MOB) amount for the service line. |
| 42 | `SRC_TYPE_OF_SVC_C_NAME` | VARCHAR |  | The data source for the type of service. |
| 43 | `CLM_BEN_BKT_DATE` | DATETIME |  | The date the claim was applied to a benefit bucket. |
| 44 | `PRS_CRWN_INLAY_CD_C_NAME` | VARCHAR |  | This is the prosthesis, crown, or inlay code for the service. |
| 45 | `PRIOR_PLACEMENT_DT` | DATETIME |  | This stores the prior placement date (PPD) for a dental claim. The PPD is used for replacement procedures to note when the prosthesis being replaced was previously installed. |
| 46 | `APPLIANCE_PLACE_DT` | DATETIME |  | The date orthodontic appliances were placed. |
| 47 | `REPLACEMENT_DT` | DATETIME |  | Date when orthodontic appliance was replaced. |
| 48 | `AMBU_TXPORT_WT` | NUMERIC |  | The weight of the patient during ambulance transport. |
| 49 | `AMBU_TXPORT_RSN_C_NAME` | VARCHAR | org | The ambulance transport reason code. |
| 50 | `AMBU_TXPORT_DIST` | NUMERIC |  | The ambulance transport distance. |
| 51 | `AMBU_PAT_CNT` | INTEGER |  | The number of patients in the ambulance. |
| 52 | `AMBU_PICK_UP_CITY` | VARCHAR |  | The city of the ambulance pick-up location. |
| 53 | `AMBU_PICK_UP_STAT_C_NAME` | VARCHAR | org | The state of the ambulance pick-up location. |
| 54 | `AMBU_PICK_UP_ZIP` | VARCHAR |  | The zip code of the ambulance pick-up location. |
| 55 | `AMBU_DROP_OFF_CITY` | VARCHAR |  | The city of the ambulance drop-off location. |
| 56 | `AMBU_DROP_OFF_STA_C_NAME` | VARCHAR |  | The state of the ambulance drop-off location. |
| 57 | `AMBU_DROP_OFF_ZIP` | VARCHAR |  | The zip code of the ambulance drop-off location. |
| 58 | `AMBU_DROP_OFF_NAME` | VARCHAR |  | The name of the ambulance drop-off location. |
| 59 | `AMBU_PICK_UP_COUNTRY_C_NAME` | VARCHAR | org | Stores the unique identifier for the country associated with the ambulance pick-up location. Join this column to ZC_COUNTRY_2 to translate to the country name. |
| 60 | `AMBU_PICK_UP_COUNTY_C_NAME` | VARCHAR | org | Stores the unique identifier for the county associated with the ambulance pick-up location. Join this column ZC_COUNTY_2 to translate to the county name. |
| 61 | `AMBU_PICK_UP_DISTRICT_C_NAME` | VARCHAR | org | Stores the unique identifier for the district associated with the ambulance pick-up location. Join this column to ZC_DISTRICT to translate to the district name. |
| 62 | `AMBU_PICK_UP_HOUSE_NUM` | VARCHAR |  | Stores the house number associated with the ambulance pick-up location. |
| 63 | `AMBU_DROP_OFF_COUNTRY_C_NAME` | VARCHAR |  | Stores the unique identifier for the country associated with the ambulance drop-off location. Join this column to ZC_COUNTRY_2 to translate to the country name. |
| 64 | `AMBU_DROP_OFF_COUNTY_C_NAME` | VARCHAR |  | Stores the unique identifier for the county associated with the ambulance drop-off location. Join this column to ZC_COUNTY_2 to translate to the county name. |
| 65 | `AMBU_DROP_OFF_DISTRICT_C_NAME` | VARCHAR |  | Stores the unique identifier for the district associated with the ambulance drop-off location. Join this column to ZC_DISTRICT to translate to the district name. |
| 66 | `AMBU_DROP_OFF_HOUSE_NUM` | VARCHAR |  | Stores the house number associated with the ambulance drop-off location. |
| 67 | `CLAIM_LN_DTL_SVC_CLASS_C_NAME` | VARCHAR |  | Represents a clinical classification of the billed service. |
| 68 | `PAT_PAY_COPAY_SERVICE_TYPE_ID` | VARCHAR |  | The copay category used in adjudicating the service line. |
| 69 | `PAT_PAY_COPAY_SERVICE_TYPE_ID_SERVICE_TYPE_NAME` | VARCHAR |  | The name of this benefit service type. |
| 70 | `PAT_PAY_SPECIALTY_DEP_C` | VARCHAR |  | The specialty of the department where the service was rendered. |
| 71 | `PAT_PAY_COPAY_AMT_SRC_C` | INTEGER |  | The source of the copay amount as determined during adjudication. |
| 72 | `PAT_PAY_COPAY_COL_SRC_C` | INTEGER |  | The location where the copay was collected as determined during adjudication. |
| 73 | `PAT_PAY_PROC_SEQ_NUM` | INTEGER |  | The service's place in the adjudication order. |
| 74 | `PAT_PAY_COB_FROM_OTH_LINES_AMT` | NUMERIC |  | The coordination of benefits (COB) amount for this service that was transferred from other services on the same claim. |
| 75 | `PAT_PAY_COB_TO_OTH_LINES_AMT` | NUMERIC |  | The coordination of benefits (COB) amount for this service that was transferred to other services on the same claim. |
| 76 | `PAT_PAY_HRA_DEF_ID` | NUMERIC |  | The ID of the Health Reimbursement Arrangement (HRA) plan used to adjudicate the claim. |
| 77 | `PAT_PAY_HRA_DEF_ID_HRA_DEF_NAME` | VARCHAR |  | Record name. |
| 78 | `PAT_PAY_HRA_ACCUMULATE_BY_C` | INTEGER |  | The family type from the Health Reimbursement Arrangement (HRA) used when adjudicating the claim. |
| 79 | `PAT_PAY_ADJ_BEN_CHECK_TYPE_C` | INTEGER |  | The type of benefits check performed when calculating the patient portion. |
| 80 | `PAT_PAY_CHECKED_FOR_AUTH_FLAG` | INTEGER |  | Indicates whether authorizations were checked during adjudication. |
| 81 | `PAT_PAY_MATCHED_CMG_LINE` | INTEGER |  | The line of the component group that was matched during adjudication if the service was matched to a component group. |
| 82 | `PAT_PAY_CMP_CONTACT_DATE` | DATETIME |  | The contact date of the component that was matched during adjudication if the service was matched to a component. |
| 83 | `PAT_PAY_BEN_PLAN_CONTACT_DATE` | DATETIME |  | The contact date of the benefit plan that was used during adjudication. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

