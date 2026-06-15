# AP_CLAIM_PROC

> This table summarizes data for AP Claims service lines, with each service line given one row. To link this table’s service line information back to a claim header, join this table to AP_CLAIM_PROC_IDS on the TX_ID column. If you need to report on claim service lines specific to Cost Sharing Reduction (CSR), join this table instead to AP_CLAIM_PROC_IDS_CSR on the TX_ID column. If you care about neither distinguishing CSR-related service lines nor the ordering of service lines on a claim, you can join back to the claim header on this table's CLAIM_ID column.

**Overflow family:** [AP_CLAIM_PROC_2](AP_CLAIM_PROC_2.md), [AP_CLAIM_PROC_3](AP_CLAIM_PROC_3.md), [AP_CLAIM_PROC_4](AP_CLAIM_PROC_4.md), [AP_CLAIM_PROC_5](AP_CLAIM_PROC_5.md)  
**Primary key:** `TX_ID`  
**Columns:** 96  
**Org-specific columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the AP Claim procedure transaction. |
| 2 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 3 | `SVC_FROM_DATE` | DATETIME |  | The beginning service date for the procedure on the accounts payable claim record. |
| 4 | `SVC_TO_DATE` | DATETIME |  | The ending service date for the procedure on the accounts payable claim record. |
| 5 | `MODIFIERS` | VARCHAR |  | A list of modifiers used with the procedure on the accounts payable claim record. |
| 6 | `BILLED_AMT` | NUMERIC |  | The amount billed for the procedure on the accounts payable claim record. |
| 7 | `ALLOWED_AMT` | NUMERIC |  | The allowed amount calculated for the procedure on the accounts payable claim record. |
| 8 | `NET_PAYABLE` | NUMERIC |  | The net payable amount for the procedure on the accounts payable claim record. |
| 9 | `POS_TYPE_C_NAME` | VARCHAR | org | The category value associated with the place of service type of the procedure on the accounts payable claim record. |
| 10 | `OVERRIDE_ALLD_AMT` | NUMERIC |  | The override allowed amount for the procedure on the accounts payable claim record. |
| 11 | `OVERRIDE_REASON_C_NAME` | VARCHAR | org | The category value associated with the reason for the override. |
| 12 | `TYPE_OF_SERVICE_C_NAME` | VARCHAR | org | The category ID of the type of service associated with the procedure on the accounts payable claim record. |
| 13 | `PRIM_INS_AMOUNT` | NUMERIC |  | For non-primary claims (e.g. secondary), the sum of the insurance amounts paid by previous payors. |
| 14 | `PRIM_PAT_PORTION` | NUMERIC |  | For non-primary claims (e.g. secondary), the sum of all patient portion amounts specified by previous payors. |
| 15 | `PROC_INSURANCE_AMT` | NUMERIC |  | The calculated insurance amount for the procedure on the accounts payable claim record. |
| 16 | `NET_INSURANCE_AMT` | NUMERIC |  | The net insurance amount for this procedure on the accounts payable claim record. |
| 17 | `WITHHOLD_METHOD_C_NAME` | VARCHAR |  | The category value representing the method of withholding an amount for this procedure. |
| 18 | `WITHHOLD_RATE` | NUMERIC |  | The rate to be withheld for this procedure. |
| 19 | `COMP_WITHHOLDING` | NUMERIC |  | The computed withholding amount for the procedure on the accounts payable claim record. |
| 20 | `COMP_ADJUSTMENT` | NUMERIC |  | The computed adjustment amount for the procedure on the accounts payable claim record. |
| 21 | `ACTUAL_ADJUSTMENT` | NUMERIC |  | The actual adjustment taken for this procedure on the accounts payable claim record. |
| 22 | `ADJUST_REASON_C_NAME` | VARCHAR | org | The category value of the reason for the adjustment to this procedure on the accounts payable claim record. |
| 23 | `ADJ_BILLED_AMT` | NUMERIC |  | The adjusted billed amount after refund for the procedure on the accounts payable claim record. |
| 24 | `ADJ_ALLOWED_AMT` | NUMERIC |  | The adjusted allowed amount after refund for the procedure on the accounts payable claim record. |
| 25 | `ADJ_PAT_PORTION` | NUMERIC |  | The adjusted patient portion after refund for the procedure on the accounts payable claim record. |
| 26 | `ADJ_INS_AMT` | NUMERIC |  | The adjusted insurance amount after refund for the procedure on the accounts payable claim record. |
| 27 | `ADJ_ADJUSTMENT` | NUMERIC |  | The adjusted adjustment amount after refund for the procedure on the accounts payable claim record. |
| 28 | `ADJ_NET_INS` | NUMERIC |  | The adjusted net insurance amount after refund for the procedure on the accounts payable claim record. |
| 29 | `ADJ_WITHHOLDING` | NUMERIC |  | The adjusted withholding amount after refund for the procedure on the accounts payable claim record. |
| 30 | `ADJ_NET_PAYABLE` | NUMERIC |  | The adjusted net payable amount after refund for the procedure on the accounts payable claim record. |
| 31 | `PAT_PORTION` | NUMERIC |  | The patient portion for the procedure on the accounts payable claim record. |
| 32 | `REVENUE_CODE_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 33 | `QUANTITY` | NUMERIC |  | The quantity (number of units, procedures, etc.) billed on this service line. |
| 34 | `REFUND_REVERSAL_ID` | NUMERIC |  | The unique ID of the reversal procedure transaction for refund. |
| 35 | `REFUND_ADJT_ID` | NUMERIC |  | The unique ID of the adjustment procedure transaction for refund. |
| 36 | `EOB_COMMENT` | VARCHAR |  | The claim code (explanation of benefit code) comment on the procedure. |
| 37 | `UC_VALUE` | NUMERIC |  | The usual and customary amount for the procedure. |
| 38 | `CONTRACT_ALLOWED` | NUMERIC |  | The contractual allowed amount for the procedure. |
| 39 | `OVRD_DISALW_RSN_C_NAME` | VARCHAR | org | The category ID of the reason for overriding the disallowed amount on the procedure. |
| 40 | `OVRD_DISALW_AMT` | NUMERIC |  | The override disallowed amount for the procedure. |
| 41 | `DISALW_AMT` | NUMERIC |  | The disallowed amount for the procedure. |
| 42 | `OVRD_NOT_CVD` | NUMERIC |  | The override not covered amount for the procedure. |
| 43 | `OVRD_DEDUCTIBLE` | NUMERIC |  | The override deductible amount for the procedure. |
| 44 | `OVRD_COINS` | NUMERIC |  | The override coinsurance amount for the procedure. |
| 45 | `OVRD_COPAY` | NUMERIC |  | The override copay amount for the procedure. |
| 46 | `NON_CVD_AMT` | NUMERIC |  | The non-covered amount for the procedure. |
| 47 | `DEDUCTIBLE` | NUMERIC |  | The deductible amount for the procedure. |
| 48 | `COPAYMENT` | NUMERIC |  | The copayment amount for the procedure. |
| 49 | `COINSURANCE` | NUMERIC |  | The coinsurance amount for the procedure. |
| 50 | `PATIENT_TOT` | NUMERIC |  | The total patient portion for the procedure. |
| 51 | `OVRD_PAT_RSN_C_NAME` | VARCHAR | org | The category ID of the reason for overriding the patient portion on the procedure. |
| 52 | `OVRD_PAT_PORT` | NUMERIC |  | The override patient portion amount for the procedure. |
| 53 | `PRICING_ATTR_C_NAME` | VARCHAR | org | The category ID of the pricing attribute for the procedure (used in conjunction with the vendor contract). |
| 54 | `PENALTY_BEF_BEN` | NUMERIC |  | The before benefits provider penalty amount for the procedure. |
| 55 | `PENALTY_AFT_BEN` | NUMERIC |  | The after benefits provider penalty amount for the procedure. |
| 56 | `EXCEEDED_BEN_AMT` | NUMERIC |  | The amount on the procedure that exceeds benefits. |
| 57 | `COB_SAVING_AMT` | NUMERIC |  | The Coordination of Benefits (COB) savings amount for the procedure. |
| 58 | `PAT_OUT_OF_POCKET` | NUMERIC |  | The total patient out-of-pocket amount for the procedure. |
| 59 | `SUB_PEN_ADJ_STR` | VARCHAR |  | The submission penalty adjudication string for the procedure. |
| 60 | `ALLOWED_CODE_C_NAME` | VARCHAR |  | The allowed code for the procedure (e.g., claim denied, procedure denied, contracted rate payment). |
| 61 | `WITHHOLDING` | NUMERIC |  | The withholding amount for the procedure. |
| 62 | `TX_TYPE_C_NAME` | VARCHAR |  | The category ID that indicates the type of procedure. Only AP claim types should appear in this table (e.g. AP claim, AP claim refund, AP claim DRG). |
| 63 | `DRG_ID` | VARCHAR | FK→ | The unique ID of Diagnosis Related Group (DRG) code for the procedure. |
| 64 | `DRG_ID_DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |
| 65 | `PAT_PORT_CODE_C_NAME` | VARCHAR |  | The category ID of the type of patient payment for the procedure (e.g., coinsurance, copay, not covered). |
| 66 | `DISCOUNT` | NUMERIC |  | The discount amount for the procedure. |
| 67 | `SECONDARY_DISC_AMT` | NUMERIC |  | The amount of additional discount on a secondary claim. |
| 68 | `PRIMARY_FACTORS` | NUMERIC |  | The amount on a non-primary (e.g. secondary) claim that was paid/handled by the primary payor. |
| 69 | `SEC_PROV_RESP` | NUMERIC |  | The secondary denied amount if the service is denied to provider responsibility. |
| 70 | `UNCVRD_EOB_CODE_ID_EOB_CODE_NAME` | VARCHAR |  | The name of the processing code. |
| 71 | `DISC_EOB_CODE_ID_EOB_CODE_NAME` | VARCHAR |  | The name of the processing code. |
| 72 | `PRICE_USING_C_NAME` | VARCHAR |  | The category ID of the method used to price the service (e.g. Revenue code, HCPCS code, DRG code). This is set only for UB claims. |
| 73 | `STATUS_C_NAME` | VARCHAR |  | The category ID of the procedure's status. |
| 74 | `CVG_ID` | VARCHAR | FK→ | The ID of the coverage used to pay the procedure on the claim. |
| 75 | `APC_CODE_ID` | VARCHAR |  | The unique ID of the Ambulatory Payment Classification (APC) code that mapped to the procedure. |
| 76 | `APC_PRICE` | NUMERIC |  | The Ambulatory Payment Classification (APC) price for the procedure. |
| 77 | `OVRD_EXCD_BEN_AMT` | NUMERIC |  | The override exceeded benefit amount for the procedure. |
| 78 | `COB_SAVINGS_PAYOUT` | NUMERIC |  | The Coordination of Benefits (COB) savings member payout. |
| 79 | `PAT_PAY_ADJ_STR` | VARCHAR |  | The patient payment adjudication string. |
| 80 | `ALWD_AMT_ADJ_STR` | VARCHAR |  | The allowed amount adjudication string. |
| 81 | `CMG_MATCHED_ID` | VARCHAR |  | Stores the matched component group for referral bed days for this service. |
| 82 | `CMG_MATCHED_ID_COMPONENT_GRP_NAME` | VARCHAR |  | The name of the component group |
| 83 | `NPR_BDTABLE_LINE` | NUMERIC |  | The line number of the bed days mapping table in the Tapestry Profile (I NPR 41040) on which the procedure matched. |
| 84 | `REL_WT_BED_DAY` | NUMERIC |  | Relative weight of the bed day type mapped to this service. |
| 85 | `RFL_MATCHED_ID` | NUMERIC |  | Referral matched for service. |
| 86 | `TOD_MATCHED_ID` | NUMERIC |  | Bed day type matched for service. |
| 87 | `TOD_MATCHED_ID_BED_DAY_TYPE_NAME` | VARCHAR |  | The name of the bed day type record (i.e. ICU or non-authorized.) |
| 88 | `WEIGHT_BED_DAYS` | NUMERIC |  | Weight of bed days for service. |
| 89 | `UBC_REVENUE_CODE_ID` | NUMERIC |  | The unique identifier of the revenue code/procedure associated with the accounts payable claim record. |
| 90 | `UBC_REVENUE_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 91 | `CLAIM_ID` | NUMERIC | FK→ | The claim to which this service associated. For most claim services, this column is equivalent to joining this table's TX_ID column to AP_CLAIM_PROC_IDS.TX_ID and retrieving AP_CLAIM_PROC_IDS.CLAIM_ID. For services related to Cost Sharing Reduction (CSR), this column is equivalent to joining this table's TX_ID column to AP_CLAIM_PROC_IDS_CSR.TX_ID and retrieving AP_CLAIM_PROC_IDS_CSR.CLAIM_ID. To retrieve the ordering of service lines on a claim, join to AP_CLAIM_PROC_IDS or AP_CLAIM_PROC_IDS_CSR as appropriate and retrieve the LINE column. |
| 92 | `PEN_AFT_BEN_COMPUTED` | NUMERIC |  | The after benefits provider penalty amount for the procedure, as computed by the system. |
| 93 | `PEN_AFT_BEN_OVRIDE` | NUMERIC |  | The after benefits provider penalty amount for the procedure, as overridden by the user. |
| 94 | `PEN_AFT_BEN_OVRIDE_RSN_C_NAME` | VARCHAR | org | The reason given for setting the provider penalty after benefits override, if any. This should be translated using ZC_PEN_AFT_BEN_OVRIDE_RSN. |
| 95 | `POS_TYPE_SRC_C_NAME` | VARCHAR |  | Source of the procedure's Place of Service type |
| 96 | `OVERRIDE_UC_VALUE` | NUMERIC |  | The amount that overrides the usual and customary amount for the procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |
| `DRG_ID` | [CLARITY_DRG](CLARITY_DRG.md) | sole_pk | high |

