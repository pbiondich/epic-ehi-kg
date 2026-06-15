# AP_CLAIM_3

> The AP_CLAIM_3 table contains one record for each claim in Tapestry's Accounts Payable module.

**Overflow of:** [AP_CLAIM](AP_CLAIM.md)  
**Primary key:** `CLAIM_ID`  
**Columns:** 70  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim record. |
| 2 | `TOT_PRIM_PAT_NOTCOV` | NUMERIC |  | Displays the amount the primary payors adjudicated as the not covered patient portion. This is applicable only if the claim has been submitted to your facility as the non primary payor (secondary, tertiary, 4th, etc.) |
| 3 | `TOT_PRIM_PAT_DED` | NUMERIC |  | Displays the amount the primary payors adjudicated as the deductible patient portion. This is applicable only if the claim has been submitted to your facility as the non primary payor (secondary, tertiary, 4th, etc.) |
| 4 | `TOT_PRIM_PAT_COPAY` | NUMERIC |  | Displays the amount the primary payors adjudicated as the copay patient portion. This is applicable only if the claim has been submitted to your facility as the non primary payor (secondary, tertiary, 4th, etc.) |
| 5 | `TOT_PRIM_PAT_COINS` | NUMERIC |  | Displays the amount the primary payors adjudicated as the co-insurance patient portion. This is applicable only if the claim has been submitted to your facility as the non primary payor (secondary, tertiary, 4th, etc.) |
| 6 | `SUBMITTER_CREAT_DATE` | DATETIME |  | Date that the original submitter created the claim file from their business application system. This date is received in the Beginning of Hierarchical Transaction (BHT) segment on an incoming ANSI 837 file. |
| 7 | `INTERCHANGE_DATE` | DATETIME |  | Date of interchange. This date is received in the Interchange Control Header (ISA) segment on an incoming ANSI 837 file. |
| 8 | `FUNC_GROUP_DATE` | DATETIME |  | Functional group creation date. This date is received in the Function Group Header (GS) segment on an incoming ANSI 837 file. |
| 9 | `TOTAL_RESP_AMOUNT` | NUMERIC |  | The total responsible amount on the claim from Coordination of Benefits (COB) calculations. |
| 10 | `TOTAL_ADJ_PAT_OOP` | NUMERIC |  | Amount that the patient out of pocket would have been on a capitated secondary claim had the claim not been capitated according to the contract. |
| 11 | `TERMED_CVG_YN` | VARCHAR |  | Flag used to determine if the coverage used to pay the claim was termed at the time. |
| 12 | `IS_INPATIENT_YN` | VARCHAR |  | Defines if claim is inpatient/outpatient. |
| 13 | `DRG_CODE` | VARCHAR |  | Contains the Diagnosis Related Group (DRG) code on the claim. |
| 14 | `DRG_ID_TYPE_ID` | NUMERIC |  | Contains the Diagnosis Related Group (DRG) ID type used for the claims. |
| 15 | `DRG_ID_TYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 16 | `PERM_ORIG_OF_REV_CLAIM_ID` | NUMERIC |  | Stores the unique identifier of the original claim for reversal claims. The value will always persist, even if the claim is voided. If the claim is not a reversal claim, no value will be stored. |
| 17 | `PERM_ORIG_OF_CORR_CLAIM_ID` | NUMERIC |  | Stores the unique identifier of the original claim for corrected claims. The value will always persist, even if the claim is voided. If the claim is not a corrected claim, no value will be stored. |
| 18 | `PERM_ORIG_OF_ADJST_CLAIM_ID` | NUMERIC |  | Stores the unique identifier of the original claim for adjustment claims. The value will always persist, even if the claim is voided. If the claim is not an adjustment claim, no value will be stored. |
| 19 | `INVOICE_AMT_REM` | NUMERIC |  | The amount of the claim the system needs to generate invoice for. |
| 20 | `ADJST_ACTION_TYPE_C_NAME` | VARCHAR | org | Stores the category identifier indicating why the claim was adjusted. |
| 21 | `CLAIM_EFFECTIVE_DATE` | DATETIME |  | Stores the effective date of the claim at the time of adjudication. This date is calculated during adjudication based on other days (e.g. service date) and is used to price the claim when a single claim-level date is required, such as to find the correct vendor contract contact. |
| 22 | `VENDOR_TAXONOMY` | VARCHAR |  | Stores the vendor taxonomy code submitted in a claim. |
| 23 | `PROVIDER_TAXONOMY` | VARCHAR |  | Stores the provider taxonomy code submitted in a claim. It is the rendering provider taxonomy for CMS claims and attending provider taxonomy for UB claims. |
| 24 | `ADJST_REASON_C_NAME` | VARCHAR | org | The adjustment reason category ID. Entered by a user when adjusting a claim. |
| 25 | `AMBU_PICK_UP_COUNTY_C_NAME` | VARCHAR | org | Stores the unique identifier for the county associated with the ambulance pick-up location. Join this column to ZC_COUNTY_2 to translate to the county name. |
| 26 | `AMBU_PICK_UP_DISTRICT_C_NAME` | VARCHAR | org | Stores the unique identifier for the district associated with the ambulance pick-up location. Join this column to ZC_DISTRICT to translate to the district name. |
| 27 | `AMBU_PICK_UP_HOUSE_NUM` | VARCHAR |  | Stores the house number associated with the ambulance pick-up location. |
| 28 | `AMBU_DROP_OFF_COUNTY_C_NAME` | VARCHAR |  | Stores the unique identifier for the county associated with the ambulance drop-off location. Join this column to ZC_COUNTY_2 to translate to the county name. |
| 29 | `AMBU_DROP_OFF_DISTRICT_C_NAME` | VARCHAR |  | Stores the unique identifier for the district associated with the ambulance drop-off location. Join this column to ZC_DISTRICT to translate to the district name. |
| 30 | `AMBU_DROP_OFF_HOUSE_NUM` | VARCHAR |  | Stores the unique identifier for the house number associated with the ambulance drop-off location. |
| 31 | `SUPERVISING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 32 | `CLAIM_SVC_CLASS_CTX_C_NAME` | VARCHAR |  | Represents the high-level clinical classification context for the services billed on this claim. |
| 33 | `CLAIM_SVC_CLASS_C_NAME` | VARCHAR |  | Represents the clinical classification for the services billed on this claim. |
| 34 | `IS_SUBROGATION_DEMAND_CLAIM_YN` | VARCHAR |  | Flag whether the claim is a subrogation demand claim from another payer. |
| 35 | `TOT_SUBROGATION_DEMAND_AMT` | NUMERIC |  | This item stores the total subrogation demand amount from another payer. |
| 36 | `TOT_SUBROGATION_ADJ_AMT` | NUMERIC |  | This item stores the total amount on the claim that was not paid due to subrogation demand being less than net payable. |
| 37 | `CONTRACT_SEL_MTHD_C_NAME` | VARCHAR |  | This selection method was used to select the contract used to price the claim from the configured Vendor Contract and Comparison Contracts. |
| 38 | `IS_CLINICALLY_VALID_YN` | VARCHAR |  | Stores whether a claim is considered valid for the purpose of clinical data derivation |
| 39 | `PRIM_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 40 | `BCDA_GROUP_IDENT` | VARCHAR |  | Claim group identifier provided by BCDA (Beneficiary Claims Data API) |
| 41 | `CLIA_NUMBER` | VARCHAR |  | Identification of a Clinical Laboratory Improvement Amendment (CLIA) certified facility that performed CLIA covered laboratory services. |
| 42 | `CLIN_FILTER_UTC_DTTM` | DATETIME (UTC) |  | Last UTC instant data derivation clinical filters (I CLM 18625) were updated or calculated without changes for this claim. |
| 43 | `CLIN_FILTER_DTTM` | DATETIME (Local) |  | Last local instant data derivation clinical filters (I CLM 18625) were updated or calculated without changes for this claim. Calculated using EPIC_UTC_TO_LOCAL on I CLM 18626. |
| 44 | `TOT_PI_REDUCT_AMT` | NUMERIC |  | Total Payer Initiated Billed Amount Reduction from EDC Analyzer. |
| 45 | `MOST_RECENT_INCOMING_CEV_ID` | NUMERIC |  | The most recent incoming Claim External Value (CEV) record ID. |
| 46 | `PAT_REL_TO_COVERED_MEM_C_NAME` | VARCHAR |  | The patient's relation to the covered (insured) member that the claim is paid under. If the patient is the member, this is not set. If it is set, this value defines the relation to the covered member for the patient who received the services. |
| 47 | `CLIN_FILTER_TXP_YN` | VARCHAR |  | Tracks whether this claim is considered as having transplant services for the purposes of clinical derivation from claims. |
| 48 | `KLCTCEV_RECORD_ID` | NUMERIC |  | Holds the CEV ID containing the KLCT metadata for a reversal claim. |
| 49 | `SOURCE_ORG_ID` | NUMERIC |  | The source organization of the external record. |
| 50 | `SOURCE_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 51 | `LOOP_OR_SPLIT_YN` | VARCHAR |  | Indicates whether a claim is part of an adjustment sequence that contains a split claim or an adjustment sequence loop. This CLM does not have to be in the split or loop istelf, just a part of the adjustment sequence. |
| 52 | `IS_INVLD_ADJ_SEQ_YN` | VARCHAR |  | Indicates whether a claim is part of an adjustment sequence that is not valid. An adjustment sequence can be invalid for a number of reasons, such as the sequence ending in a cancellation or the sequence having gaps. |
| 53 | `CLAIM_PAID_DATE` | DATETIME |  | The date that the claim was paid, which is determined by the date the claim reaches the AP Status EOB Generated |
| 54 | `CLAIM_NAT_KEY_HASH` | VARCHAR |  | The hashed value of the mapped claim natural key. |
| 55 | `CLAIM_NAT_KEY_ORDER` | VARCHAR |  | The ordering value for the claim natural key. |
| 56 | `CLM_ADJ_TYPE_C_NAME` | VARCHAR |  | The Claim Adjustment Type Code |
| 57 | `NAT_KEY_FINAL_YN` | VARCHAR |  | Indicates whether a claim is the final action of an adjustment sequence that is tracking adjustments via natural keys. Natural key adjustments are tracked using superitem CLM 18690. A claim is the final action of its natural key if it has the maximum order value (item 18692) for a given natural key (item 18691). If there is a tie, the claim with the largest claim header id (item 18681) is deemed the final action. |
| 58 | `TTL_APL_U_AND_C_AMT` | NUMERIC |  | The total of the usual and customary amounts from all lines on the claim. |
| 59 | `TTL_APL_CNTRCT_AMT` | NUMERIC |  | The total of the contractual amounts from all lines on the claim. |
| 60 | `SUBMITTER_C_NAME` | VARCHAR |  | The person or entity that submitted the claim. |
| 61 | `SUBMITTER_AUTHORIZED_REP_GUID` | VARCHAR |  | The GUID of the authorized representative who submitted the claim. |
| 62 | `TOTAL_DENIED_AMOUNT` | NUMERIC |  | This tracks the total denied amount across all claim services. It is currently only used for display purposes in the claim workspace. |
| 63 | `TOTAL_DENIED_TO_PAT` | NUMERIC |  | This tracks the total amount denied to the patient across all claim services. It is currently only used for display purposes in the claim workspace. |
| 64 | `REC_OWN_BUS_SEGMENT_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 65 | `REGION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 66 | `MEDICAL_GROUP_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 67 | `PRICER_MSG_ID` | NUMERIC | shared | The most recent Epic Pricer message record that was used to price the claim. |
| 68 | `OUT_NET_ADJUD_OV_C_NAME` | VARCHAR | org | The reason for overriding a claim's adjudication network level to Out of Network. |
| 69 | `RECV_CLAIM_RECON_ID` | VARCHAR |  | This claim reconciliation record (CRD) for the claim. |
| 70 | `CMS_NATURAL_KEY` | VARCHAR |  | The claim natural key for a CMS claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

