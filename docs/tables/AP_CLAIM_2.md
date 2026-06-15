# AP_CLAIM_2

> The AP_CLAIM_2 table contains one record for each claim in Tapestry's Accounts Payable module.

**Overflow of:** [AP_CLAIM](AP_CLAIM.md)  
**Primary key:** `CLAIM_ID`  
**Columns:** 66  
**Org-specific columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim record. |
| 2 | `E_CODE_POA_C_NAME` | VARCHAR |  | Present on Admission (POA) indicator for the external cause of injury diagnosis code. |
| 3 | `READY_FOR_AP_MGR_ID_MEM_GRP_NAME` | VARCHAR |  | The name of the member group |
| 4 | `TOT_REFD_RECVD` | NUMERIC |  | The total refund received for the claim. |
| 5 | `TOTAL_COB_AMOUNT` | NUMERIC |  | Contains the calculated Coordination of Benefits (COB) amount for all services on the claim. |
| 6 | `EPSDT_YN` | VARCHAR |  | Stores if an Early and Periodic Screening, Diagnosis, and Treatment (EPSDT) referral was given to the patient on the claim. |
| 7 | `RENDERING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `TOTAL_MOB_AMOUNT` | NUMERIC |  | Stores the total Maintenance of Benefits (MOB) amount for all services on the claim. |
| 9 | `PMT_INFO_MAP_LN` | INTEGER |  | Stores the line that the Tapestry Profile responsibility map matched on. |
| 10 | `PMT_INFO_GRPR_ID` | VARCHAR |  | Stores the grouper rule that the Tapestry Profile responsibility map matched on. |
| 11 | `PMT_INFO_GRPR_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 12 | `PMT_INFO_RULE_ID` | VARCHAR |  | Stores the rule that the Tapestry Profile responsibility map matched on. |
| 13 | `PMT_INFO_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 14 | `PMT_INFO_SPLIT_ID` | NUMERIC |  | Stores the split definition record that was determined by the Tapestry Profile responsibility map. |
| 15 | `PMT_INFO_SPLIT_ID_SPLIT_DEF_NAME` | VARCHAR |  | The name of the split definition record. |
| 16 | `SPECIALTY_SOURCE_C_NAME` | VARCHAR |  | Source of associated specialty. |
| 17 | `CASE_MGMT_CREAT_ID` | VARCHAR |  | ID of the case trigger message associated with the claim. |
| 18 | `CVG_FILTER_EPP_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 19 | `PMT_INFO_STOP_COND` | INTEGER |  | Stores the procedure line that triggered a stopping condition during pricing. |
| 20 | `NO_MEM_GRP_YN` | VARCHAR |  | Identifies that the claim does not have a member group. |
| 21 | `INTEREST_TOTAL` | NUMERIC |  | Stores the total interest for the claim, from the constituent service lines. |
| 22 | `PROV_ACPT_ASGN_C_NAME` | VARCHAR |  | Stores the provider accept assignment code. |
| 23 | `BEN_ASGN_IND_C_NAME` | VARCHAR |  | Stores the benefits assignment indicator. |
| 24 | `OVRD_SUB_POLICY_YN` | VARCHAR |  | If this item is set, the submission policy tables at the profile and on the vendor contract are ignored. The Claim filing window (days) setting on the vendor contract is also ignored. |
| 25 | `OVRD_SUB_POL_RSN_C_NAME` | VARCHAR | org | This item provides an explanation as to why the override submission policy item is set. |
| 26 | `CLM_TRAIT_1_C_NAME` | VARCHAR | org | The first custom claim trait, used to classify and group claims. |
| 27 | `CLM_TRAIT_2_C_NAME` | VARCHAR | org | The second custom claim trait, used to classify and group claims. |
| 28 | `CLM_TRAIT_3_C_NAME` | VARCHAR | org | The third custom claim trait, used to classify and group claims. |
| 29 | `CLM_TRAIT_4_C_NAME` | VARCHAR | org | The fourth custom claim trait, used to classify and group claims. |
| 30 | `CLM_TRAIT_5_C_NAME` | VARCHAR | org | The fifth custom claim trait, used to classify and group claims. |
| 31 | `TP_INFO_837_SEND_ID` | NUMERIC |  | The trading partner (NTP record) that sent the ANSI 837 claim file that was used to submit this claim. |
| 32 | `TP_INFO_837_SEND_ID_TRADING_PARTNR_NAME` | VARCHAR |  | The name of the trading partner record. |
| 33 | `TP_INFO_837_RCVR_ID` | NUMERIC |  | The trading partner (NTP record) that received the ANSI 837 claim file that was used to submit this claim. |
| 34 | `TP_INFO_837_RCVR_ID_TRADING_PARTNR_NAME` | VARCHAR |  | The name of the trading partner record. |
| 35 | `APPLIANCE_PLACE_DT` | DATETIME |  | This is the date orthodontic appliances were placed. |
| 36 | `DNTL_SVC_FROM_DT` | DATETIME |  | This is the dental service span from date. |
| 37 | `DNTL_SVC_TO_DT` | DATETIME |  | This is the dental service span to date. |
| 38 | `ORTHO_SVCS_YN` | VARCHAR |  | This is to determine if orthodontic services were performed. |
| 39 | `ORTHO_TOT_MONTHS` | INTEGER |  | This is the total months of orthodontic treatment. |
| 40 | `ORTHO_MNTHS_REMAIN` | INTEGER |  | This is the months of orthodontic treatment remaining |
| 41 | `ASSIST_SURGEON_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 42 | `DENTAL_INFO_YN` | VARCHAR |  | This is to determine if the claim has dental information. |
| 43 | `LMP_DATE` | DATETIME |  | The date of the patient's last menstrual period. |
| 44 | `CHIR_FRST_TRT_DT` | DATETIME |  | First treatment date listed on the patient's claim. |
| 45 | `FROM_OCR_YN` | VARCHAR |  | Flags whether the claim was originally paper or scanned into the system through an EDI batch load. |
| 46 | `CLM_PRICER_IDENT_C_NAME` | VARCHAR | org | When a matching repricer organization is found, the identification is stored on the claim. |
| 47 | `TOTAL_HRA_AMOUNT` | NUMERIC |  | Stores the total reimbursement amount for all services on the claim. |
| 48 | `ORIG_ACT_ADJ_CLM_ID` | NUMERIC |  | The original claim ID of the actual adjustment claim. |
| 49 | `REF_CLM` | VARCHAR |  | Contains the reference claim ID in the ANSI 837 file from Loop 2300, Segment REF02 with identifier F8. This is often used in combination with the claim frequency code. When the claim frequency code indicates the claim needs to be adjusted or voided, the reference claim ID is used to help identify the claim. |
| 50 | `MGR_ASSOC_EXT_VAL_C_NAME` | VARCHAR | org | Stores the association extension value returned by the association extension on the member group. |
| 51 | `AMBU_TRAN_REASON_C_NAME` | VARCHAR | org | Transport Reason code for ANSI claims. |
| 52 | `AMBU_TRAN_DIST` | NUMERIC |  | Transport distance for the CRC segment in the 2300 loop on ANSI claims. |
| 53 | `AMBU_TXPORT_WT` | NUMERIC |  | Weight of the patient at the time of transport in an ambulance. |
| 54 | `AMBU_COND_YN` | VARCHAR |  | Indicates a yes or a no condition response code in the related item. |
| 55 | `AMBU_PICK_UP_CITY` | VARCHAR |  | Stores the city of the ambulance pick-up location. |
| 56 | `AMBU_PICK_UP_ST_C_NAME` | VARCHAR | org | Stores the state of the ambulance pick-up location. |
| 57 | `AMBU_PICK_UP_ZIP` | VARCHAR |  | Stores the ZIP code of the ambulance pick-up location. |
| 58 | `AMBU_DROP_OFF_CITY` | VARCHAR |  | Stores the city of the ambulance drop-off location. |
| 59 | `AMBU_DROP_OFF_ST_C_NAME` | VARCHAR |  | Stores the state of the ambulance drop-off location. |
| 60 | `AMBU_DROP_OFF_ZIP` | VARCHAR |  | Stores the ZIP code of the ambulance drop-off location. |
| 61 | `AMBU_DROP_OFF_NM` | VARCHAR |  | Stores the last name or organization name of the ambulance drop-off location. |
| 62 | `PAYEE_C_NAME` | VARCHAR |  | Payee of the claim. |
| 63 | `ESRD_ONSET_DATE` | DATETIME |  | This item stores the onset date of End Stage Renal Disease. This date is sent on CMS 2728 form in Field 24. |
| 64 | `PAYOR_SEQ_NUMBER_C_NAME` | VARCHAR |  | Sequence number of the payor of the claim. |
| 65 | `CLM_FREQ_CODE_C_NAME` | VARCHAR | org | Contains the claim frequency type code from the ANSI 837 file. The value comes from Loop 2300, Segment CLM05, Piece 3. |
| 66 | `DENY_CLM_SRC_C_NAME` | VARCHAR |  | Tracks the source of an attempt to deny a claim that can't be immediately denied, but has not yet reached a status of fully paid to be able to be reversed and adjusted. When claims with this item set are removed from a batch or become fully paid, they can be denied or reversed, adjusted and denied. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

