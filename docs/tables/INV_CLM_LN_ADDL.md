# INV_CLM_LN_ADDL

> This table holds additional line-level information about the invoice (INV) specific to a given invoice including any line-level overrides.

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 62  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The invoice record ID. |
| 2 | `LINE` | INTEGER | PK | The line number. |
| 3 | `INVOICE_NUM` | VARCHAR |  | The invoice number related to this claim line. |
| 4 | `CLM_LN` | INTEGER |  | The invoice claim line number. |
| 5 | `PROC_OR_REV_CODE` | VARCHAR |  | This is the procedure revenue code |
| 6 | `REV_CODE_DESCRIPT` | VARCHAR |  | This is the revenue code description |
| 7 | `POS_CODE` | VARCHAR |  | The place of service type for this claim line |
| 8 | `CLAIM_STATUS_C_NAME` | VARCHAR |  | The claim line status. |
| 9 | `CLAIM_PAID_AMT` | NUMERIC |  | The claim line paid amount. |
| 10 | `UB_CPT_CODE` | VARCHAR |  | This is the Common Procedure Terminology (CPT) code for this institutional claim line. |
| 11 | `EOB_ALLOWED_AMOUNT` | NUMERIC |  | The service line's explanation of benefits adjustment amount. |
| 12 | `EOB_ADJUSTMENT_AMT` | NUMERIC |  | The service line's explanation of benefits allowed amount. |
| 13 | `EOB_NON_COVRD_AMT` | NUMERIC |  | The service line's explanation of benefits non-covered amount. |
| 14 | `EOB_COINSURANCE` | NUMERIC |  | The service line's explanation of benefits coinsurance amount. |
| 15 | `EOB_DEDUCTIBLE` | NUMERIC |  | The service line's explanation of benefits deductible. |
| 16 | `EOB_ICN` | VARCHAR |  | The explanation of benefits internal control number for the claim line. |
| 17 | `EOB_INV_LVL_YN` | VARCHAR |  | Identifies if this explanation of benefits is for the invoice level. |
| 18 | `EOB_COPAY` | NUMERIC |  | The service line's explanation of benefits copay amount. |
| 19 | `EOB_COB` | NUMERIC |  | The explanation of benefits coordination of benefits amount. |
| 20 | `CLAIM_DENIED_CODE` | VARCHAR |  | Claim denied code for this claim line on this invoice. |
| 21 | `REMIT_CODE_ID` | VARCHAR | FK→ | Remittance code for this claim line on this invoice. |
| 22 | `TEXT_MESSAGE` | VARCHAR |  | Message associated with the remittance code for this line on this invoice. |
| 23 | `TRANSACTION_LIST` | VARCHAR |  | The charges associated with the invoice. May hold a comma delimited list of professional transactions if the charges were bundled. |
| 24 | `FROM_SVC_DATE` | DATETIME |  | The date when the service was first performed. |
| 25 | `TO_SVC_DATE` | DATETIME |  | The date when the service was last performed. |
| 26 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 27 | `MODIFIER_ONE` | VARCHAR |  | The first modifier associated with the invoice. This is the external modifier, as it was printed on the claim. |
| 28 | `MODIFIER_TWO` | VARCHAR |  | The second modifier associated with the invoice. This is the external modifier, as it was printed on the claim. |
| 29 | `MODIFIER_THREE` | VARCHAR |  | The third modifier associated with the invoice. This is the external modifier, as it was printed on the claim. |
| 30 | `MODIFIER_FOUR` | VARCHAR |  | The fourth modifier associated with the invoice. This is the external modifier, as it was printed on the claim. |
| 31 | `QUANTITY` | NUMERIC |  | The number of units associated with the invoice. |
| 32 | `CHARGE_AMOUNT` | NUMERIC |  | The charge amount associated with the claim line. |
| 33 | `NONCVD_AMOUNT` | NUMERIC |  | The non-covered amount associated with the invoice. |
| 34 | `TYPE_OF_SERVICE_C_NAME` | VARCHAR | org | The type of service category value for the claim. |
| 35 | `DIAGNOSIS_MAP` | VARCHAR |  | Holds a comma-delimited list of pointers to the claim level diagnosis. The first number listed represents the primary diagnosis for the charge. |
| 36 | `SPECIAL_GRP_TYPE_C_NAME` | VARCHAR | org | The claim grouping type category value for the associated claim grouping rule. Only populated if a claim grouping rule was applied to the invoice. |
| 37 | `GROUP_TX_LIST` | VARCHAR |  | This holds a list of transaction IDs for bundled charges. |
| 38 | `UB_MIN_SVC_DATE` | DATETIME |  | The earliest date any charges were performed for an institutional claim. |
| 39 | `UB_MAX_SVC_DATE` | DATETIME |  | The latest date any charges were performed for an institutional claim. |
| 40 | `OT_REIMB_AMT` | NUMERIC |  | Stores reimbursement amount. |
| 41 | `CONTRACT_ID` | NUMERIC | shared | Stores reimbursement contract. |
| 42 | `CONTRACT_ID_CONTRACT_NAME` | VARCHAR |  | The name of the Vendor-Network contract. |
| 43 | `CALC_METHOD_C_NAME` | VARCHAR |  | The reimbursement contract method. |
| 44 | `PROC_CODE_RATE` | VARCHAR |  | Procedure code rate. |
| 45 | `PROC_CODE_RATE_DESC` | VARCHAR |  | The procedure code rate. |
| 46 | `REMITTANCE_RMC1_ID` | VARCHAR |  | First remittance code ID. |
| 47 | `REMITTANCE_RMC1_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 48 | `REMITTANCE_RMC2_ID` | VARCHAR |  | Second remittance code ID. |
| 49 | `REMITTANCE_RMC2_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 50 | `REMITTANCE_RMC3_ID` | VARCHAR |  | Third remittance code ID. |
| 51 | `REMITTANCE_RMC3_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 52 | `REMITTANCE_RMC4_ID` | VARCHAR |  | Fourth remittance code ID. |
| 53 | `REMITTANCE_RMC4_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 54 | `CLM_LN_CREAT_DATE` | DATETIME |  | Stores the date the claim line is created. |
| 55 | `INV_NUM_GRP100LN` | INTEGER |  | The invoice line number. |
| 56 | `CLM_LN_PAID_DATE` | DATETIME |  | Stores the most recent date the invoice line is paid. |
| 57 | `IS_CODE_ONLY` | VARCHAR |  | Identifies show only lines. |
| 58 | `LN_AUTH_NUM` | VARCHAR |  | This item stores the line level authorization number. |
| 59 | `LN_REF_NUM` | VARCHAR |  | This item stores the line level referral number. |
| 60 | `FQHC_BILLOUT_MOD_ID` | VARCHAR |  | The modifier added to a bill out line for grouped claim lines. |
| 61 | `FQHC_BILLOUT_MOD_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |
| 62 | `CALCULATED_REIMB_AMOUNT` | NUMERIC |  | Stores the system calculated reimbursement amount. This may differ from items 395 and 398 if the expected reimbursement amount was manually overridden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |
| `REMIT_CODE_ID` | [CLARITY_RMC](CLARITY_RMC.md) | sole_pk | high |

