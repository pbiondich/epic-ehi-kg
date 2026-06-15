# AP_CLAIM_PROC_4

> This table summarizes data for AP Claims service lines, with each service line given one row. To link this table’s service line information back to a claim header, join this table to AP_CLAIM_PROC_IDS on the TX_ID column. If you need to report on claim service lines specific to Cost Sharing Reduction (CSR), join this table instead to AP_CLAIM_PROC_IDS_CSR on the TX_ID column.

**Overflow of:** [AP_CLAIM_PROC](AP_CLAIM_PROC.md)  
**Primary key:** `TX_ID`  
**Columns:** 98  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `REPRICED_ALLOWED_AMT` | NUMERIC |  | The allowed amount for the procedure that was received from the most recent repricer. |
| 3 | `REPRICED_DISALLOWED_AMT` | NUMERIC |  | The disallowed amount for the procedure that was received from the most recent repricer. |
| 4 | `UPN_CODE` | VARCHAR |  | UPN (Universal Product Number) code for the procedure on a claim. |
| 5 | `UPN_QTY` | INTEGER |  | Quantity of UPN code for the procedure on a claim. |
| 6 | `UPN_DESC` | VARCHAR |  | Description of the UPN code for the procedure on a claim. |
| 7 | `UPN_QUAL_C_NAME` | VARCHAR |  | Qualifier code of the UPN code for the procedure on a claim. |
| 8 | `UPN_UNIT_C_NAME` | VARCHAR |  | Unit of measurement for UPN code for the procedure on a claim. |
| 9 | `PAID_CLM_FILE_NOT_CVD_AMT` | NUMERIC |  | The not covered amount from the claim's source file. This is only populated for externally-paid claims loaded from claims files. |
| 10 | `PAID_CLM_FILE_DEDUCT_AMT` | NUMERIC |  | The deductible amount from the claim's source file. This is only populated for externally-paid claims loaded from claims files. |
| 11 | `PAID_CLM_FILE_COINS_AMT` | NUMERIC |  | The coinsurance amount from the claim's source file. This is only populated for externally-paid claims loaded from claims files. |
| 12 | `PAID_CLM_FILE_COPAY_AMT` | NUMERIC |  | The copay amount from the claim's source file. This is only populated for externally-paid claims loaded from claims files. |
| 13 | `PAID_CLM_FILE_INS_AMT` | NUMERIC |  | The insurance amount from the claim's source file. This is only populated for externally-paid claims loaded from claims files. |
| 14 | `PAT_ID` | VARCHAR | FK→ | Patient associated with the transaction. |
| 15 | `RECORD_STATUS_C_NAME` | VARCHAR |  | This column displays the transaction record status. |
| 16 | `QUAL_AMT` | NUMERIC |  | Amount used for computing benefits for limiting patient portion. |
| 17 | `QUAL_AMT_FEE_SCHEDULE_MAP_ID` | NUMERIC |  | Fee schedule map used for limiting patient portion. |
| 18 | `QUAL_AMT_FEE_SCHEDULE_MAP_ID_FEE_SCHEDULE_MAP_NAME` | VARCHAR |  | The name for the fee schedule map record. |
| 19 | `QUAL_AMT_FEE_SCHEDULE_ID` | NUMERIC |  | Fee schedule used for limiting patient portion. |
| 20 | `QUAL_AMT_FEE_SCHEDULE_ID_FEE_SCHEDULE_NAME` | VARCHAR |  | The name of each fee schedule. |
| 21 | `QUAL_AMT_NETWORK_LEVELS_C_NAME` | VARCHAR | org | Network level used for limiting patient portion. |
| 22 | `QUAL_AMT_SKIP_YN` | VARCHAR |  | Whether to skip this service for limiting the patient portion. |
| 23 | `QUAL_AMT_NETWORK_ID` | VARCHAR |  | Network ID used for limiting patient portion. |
| 24 | `QUAL_AMT_NETWORK_ID_NETWORK_NAME` | VARCHAR |  | The name of the network. |
| 25 | `QUAL_AMT_OVERRIDE` | NUMERIC |  | Override for the qualifying amount for computing benefits for limiting patient portion. |
| 26 | `INVOICE_EXTERNAL_AMOUNT` | NUMERIC |  | The service line price that is manually entered by an end user based on an invoice or externally calculated amount. |
| 27 | `SUB_PEN_ADJ_DATE_TYPE_C` | INTEGER |  | The date type used when calculating timely filing (submission penalty). |
| 28 | `OVERRIDE_CONTRACTUAL_VALUE` | NUMERIC |  | The override contractual allowed amount. This is only used in Adjudication review for display and calculations in pricing card. |
| 29 | `HIPPS_PROC_CODE` | VARCHAR |  | Service-line HIPPS Code. |
| 30 | `HIPPS_CODE_PC_TYPE_C_NAME` | VARCHAR |  | Service-line HIPPS Code Type. This qualifies the HIPPS Code to a Prospective Payment System (PPS). |
| 31 | `PRICER_MSG_ID` | NUMERIC | shared | The most recent Epic Pricer message record that was used to price the service. |
| 32 | `PRICER_DISTRIBUTION_AMT` | NUMERIC |  | For HIPPS-based pricing, Epic Pricer will return a claim-level allowed amount. This amount is then distributed to Room & Board service lines, based on the billed amount. |
| 33 | `ALWD_AMT_STOP_LOSS_CNCT_DATE` | DATETIME |  | This column stores the contact date associated with the stop loss term record (NSL) that was used in determining the allowed amount of this service line. |
| 34 | `ALWD_AMT_ADJ_CMP_CNCT_DATE` | DATETIME |  | The contact date of the component record used to calculate the allowed amount of the service line on the AP Claim. |
| 35 | `ALWD_AMT_TIERED_CMP_INDEX_ID` | VARCHAR |  | The CMP & CMG Index (CMI) record of the tiered component used to calculate the allowed amount of the service line on the AP Claim. |
| 36 | `ALWD_AMT_TIERED_CMP_INDEX_ID_COMPONENT_INDEX_NAME` | VARCHAR |  | The name of the component index record |
| 37 | `ALWD_AMT_TIERED_PX_LN` | INTEGER |  | The line of the matched tiered procedure used to calculate the allowed amount of the service line on the AP Claim. |
| 38 | `SUB_PEN_ADJ_PCT_USED` | NUMERIC |  | The reimbursement percentage used to calculate timely filing (submission penalty). |
| 39 | `SUB_PEN_ADJ_CNTRCT_OR_PRFL` | VARCHAR |  | Whether vendor contracts ("Contract") or the Tapestry Profile ("Profile") was used to calculate timely filing (submission penalty). |
| 40 | `SUB_PEN_ADJ_LAG_DAYS` | INTEGER |  | The difference in days between date received and date serviced for calculating timely filing (submission penalty). |
| 41 | `SUB_PEN_ADJ_DISCNT_AMT` | NUMERIC |  | The discounted amount used in calculating timely filing (submission penalty). |
| 42 | `SUB_PEN_ADJ_RULE_ID` | VARCHAR |  | The rule ID used if timely filing (submission penalty) setting was used and a rule was matched. |
| 43 | `SUB_PEN_ADJ_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 44 | `SUB_PEN_ADJ_TMLY_FILE_YN` | VARCHAR |  | Set to "Y" if timely filing (submission penalty) setting was used but no rule matched. Otherwise, set to "N". |
| 45 | `ALWD_AMT_ADJ_CMG_LN` | INTEGER |  | The line of the component group used to calculate the allowed amount of the service line on the AP Claim. |
| 46 | `ADDL_ADJ_AMT` | NUMERIC |  | Stores the total additional adjustments that apply to the allowed amount on a service. |
| 47 | `ORIGINAL_DOWNCODED_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 48 | `ORIGINAL_DOWNCODED_QUAL_AMT` | NUMERIC |  | Qualifying payment amount for the original code before it went through EDC downcoding. |
| 49 | `AUTH_REQ_YN` | VARCHAR |  | Whether a service required authorization when it was last adjudicated. |
| 50 | `SUGGESTED_AUTH_FOUND_YN` | VARCHAR |  | Whether a service found a suggested authorization when it was last adjudicated. |
| 51 | `IS_CONTRACT_CAPITATED_YN` | VARCHAR |  | Whether the contract line matched to this service during adjudication has a service type of capitated. |
| 52 | `COMPUTED_PRIOR_INS_AMT` | NUMERIC |  | Prior insurance amount computed based on the claim-level prior insurance amount and allocated to this service. |
| 53 | `COMPUTED_PRIOR_PAT_PORTION` | NUMERIC |  | Prior patient portion computed based on the claim-level prior patient portion and allocated to this service. |
| 54 | `ORIG_CD_WORKFLOW_C_NAME` | VARCHAR |  | Workflow that changed the original code. |
| 55 | `PAID_CLM_FILE_WITHHOLD_AMT` | NUMERIC |  | The withholding amount from the file for an externally paid claim. |
| 56 | `PAID_CLM_FILE_COB_AMT` | NUMERIC |  | The COB amount from the file for an externally paid claim. |
| 57 | `PAID_CLM_FILE_ADJ_AMT` | NUMERIC |  | The adjustment amount from the file for an externally paid claim. |
| 58 | `PAID_CLM_FILE_VEN_PENALTY_AMT` | NUMERIC |  | The vendor penalty amount from the file for an externally paid claim. |
| 59 | `PAID_CLM_FILE_DISCOUNT_AMT` | NUMERIC |  | The discount from the file for an externally paid claim. |
| 60 | `PAID_CLM_FILE_HRA_AMT` | NUMERIC |  | The HRA amount from the file for an externally paid claim. |
| 61 | `SECONDARY_NOT_COVERED_AMT` | NUMERIC |  | Patient responsibility for not-covered amounts on secondary claims. |
| 62 | `SECONDARY_DEDUCTIBLE` | NUMERIC |  | Deductible amount for secondary claims. |
| 63 | `SECONDARY_COINSURANCE` | NUMERIC |  | Coinsurance amount for secondary claims. |
| 64 | `SECONDARY_COPAY` | NUMERIC |  | Copay amount for secondary claims. |
| 65 | `SECONDARY_EXCEED_BENEFITS_AMT` | NUMERIC |  | Exceeded benefits amount for secondary claims. |
| 66 | `SECONDARY_DISALLOWED_AMT` | NUMERIC |  | Disallowed amount for secondary claims. |
| 67 | `BEN_TEMPLT_ID` | NUMERIC | FK→ | The unique identifier for the benefits template used to adjudicate the procedure line. |
| 68 | `BEN_TEMPLT_ID_TEMPLATE_NAME` | VARCHAR |  | The name of the benefits template record. |
| 69 | `BENEFITS_DEFINITION_PROFILE_ID` | NUMERIC |  | The unique identifier for the benefit definitions used to adjudicate the procedure line. |
| 70 | `BENEFITS_DEFINITION_PROFILE_ID_PROFILE_NAME` | VARCHAR |  | The name of the configuration profile record. |
| 71 | `BENEFIT_GROUP_COMPON_INDEX_ID` | VARCHAR |  | The benefit grouping component/group that the procedure line matched to during patient payment adjudication. |
| 72 | `BENEFIT_GROUP_COMPON_INDEX_ID_COMPONENT_INDEX_NAME` | VARCHAR |  | The name of the component index record |
| 73 | `BENEFIT_GROUP_COMPON_LINE` | INTEGER |  | The benefit grouping component group line that the procedure line matched to during patient payment adjudication. |
| 74 | `SERVICE_COMPON_INDEX_ID` | VARCHAR |  | The service component/group that the procedure line matched to during patient payment adjudication. |
| 75 | `SERVICE_COMPON_INDEX_ID_COMPONENT_INDEX_NAME` | VARCHAR |  | The name of the component index record |
| 76 | `SERVICE_GROUP_COMPON_LINE` | INTEGER |  | The service component group line that the procedure line matched to during patient payment adjudication. |
| 77 | `ALTERNATE_NETWORK_RULE_ID` | VARCHAR |  | The ID of the alternate network criteria rule that the procedure line matched to during patient payment adjudication. |
| 78 | `ALTERNATE_NETWORK_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 79 | `BENEFIT_GROUP_CMP_CNCT_DT_REAL` | FLOAT |  | The date real contact of the benefit grouping component that the procedure line matched to during patient payment adjudication. |
| 80 | `SERVICE_COMPON_CONTACT_DT_REAL` | FLOAT |  | The date real contact of the service component that the procedure line matched to during patient payment adjudication. |
| 81 | `BENEFIT_GROUP_BEN_VAR_ID` | NUMERIC |  | The ID of the benefit grouping definition that the procedure line matched to during patient payment adjudication. |
| 82 | `BENEFIT_GROUP_BEN_VAR_ID_BEN_VAR_NAME` | VARCHAR |  | The name of the benefit variable. |
| 83 | `SERVICE_BEN_VAR_ID` | NUMERIC |  | The ID of the service definition that the procedure line matched to during patient payment adjudication. |
| 84 | `SERVICE_BEN_VAR_ID_BEN_VAR_NAME` | VARCHAR |  | The name of the benefit variable. |
| 85 | `BENEFIT_TIER_RULE_ID` | VARCHAR |  | The ID of the benefits tier rule record the service matches to. |
| 86 | `BENEFIT_TIER_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 87 | `BEN_GRP_DEF_OVR_BEN_VAR_ID` | NUMERIC |  | Stores the ID of the overridden benefit grouping definition to use for the service line in benefits calculations. |
| 88 | `BEN_GRP_DEF_OVR_BEN_VAR_ID_BEN_VAR_NAME` | VARCHAR |  | The name of the benefit variable. |
| 89 | `SVC_DEF_OVR_BEN_VAR_ID` | NUMERIC |  | Stores the ID of the override service definition to use for the service line in benefits calculations. |
| 90 | `SVC_DEF_OVR_BEN_VAR_ID_BEN_VAR_NAME` | VARCHAR |  | The name of the benefit variable. |
| 91 | `BEN_GRP_OVR_RSN_C_NAME` | VARCHAR | org | The override reason for the benefit grouping keyword if it is overridden. |
| 92 | `COPAY_WAIVE_BEN_VAR_ID` | NUMERIC |  | The ID of the copay waive group used when adjudicating this service |
| 93 | `COPAY_WAIVE_BEN_VAR_ID_BEN_VAR_NAME` | VARCHAR |  | The name of the benefit variable. |
| 94 | `COMPUTED_NETWORK_LEVEL_C_NAME` | VARCHAR | org | Contains the network level of a service, as computed during adjudication. |
| 95 | `ADJUD_NETWORK_ID` | VARCHAR |  | The provider network record matched to the service during adjudication. |
| 96 | `ADJUD_NETWORK_ID_NETWORK_NAME` | VARCHAR |  | The name of the network. |
| 97 | `BEN_EXCEPTION_CLASSIFIER_ID` | VARCHAR |  | The ID of the benefit referral classifier that qualified this service as a benefit exception. |
| 98 | `BEN_EXCEPTION_CLASSIFIER_ID_CLASSIFIER_NAME` | VARCHAR |  | The title of the classifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BEN_TEMPLT_ID` | [BENEFITS_TEMPLATE](BENEFITS_TEMPLATE.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

