# AP_CLM_RX

> This table contains information from pharmacy claims. Each record represents one pharmacy claim in the managed care system's AP Claims module.

**Overflow family:** [AP_CLM_RX_2](AP_CLM_RX_2.md)  
**Primary key:** `CLAIM_ID`  
**Columns:** 53  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record |
| 2 | `RX_BATCH_NUM` | VARCHAR |  | National Council for Prescription Drug Programs (NCPDP) file batch number |
| 3 | `RX_SUBMISSION_NUM` | INTEGER |  | NCPDP file submission number. |
| 4 | `RECORD_STATUS_EXT_CODE_LST_ID` | NUMERIC |  | Identifies the status of the pharmacy claim (paid, reversed, canceled, etc.). The record status code can be retrieved by joining this column to the EXT_CODE_LST_ID column in table FCL_EXTRNL_CDE_LST. |
| 5 | `RECORD_STATUS_EXT_CODE_LST_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 6 | `REJECT_OVRIDE_EXT_CODE_LST_ID` | NUMERIC |  | Indicates reason for paying a pharmacy claim when override is used. The reject override code can be retrieved by joining this column to the EXT_CODE_LST_ID column in table FCL_EXTRNL_CDE_LST. |
| 7 | `REJECT_OVRIDE_EXT_CODE_LST_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 8 | `PHARMACY_ID` | NUMERIC | FK→ | Pharmacy associated to the claim. |
| 9 | `PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 10 | `PRESC_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 11 | `PRESC_PROV_TAXONOMY` | VARCHAR |  | Stores the prescribing provider's taxonomy code for pharmacy claims. |
| 12 | `TTL_INGRED_COST_PAID` | NUMERIC |  | Drug ingredient cost paid. |
| 13 | `TTL_DISPENSING_FEE_PAID` | NUMERIC |  | Dispensing fee paid. |
| 14 | `TTL_REG_TAX_AMT_PAID` | NUMERIC |  | Flat sales tax amount paid. |
| 15 | `TTL_PCT_TAX_AMT_PAID` | NUMERIC |  | Percentage tax amount paid. |
| 16 | `TTL_INCENTIVE_AMT_PAID` | NUMERIC |  | Incentive amount paid. |
| 17 | `TTL_PROF_SVC_FEE_PAID` | NUMERIC |  | Professional service fee paid. |
| 18 | `OTHER_AMT_RECOGNIZED` | NUMERIC |  | Total amount recognized by the processor of any payment from another source. |
| 19 | `ALTERNATE_CLM_IDENT` | VARCHAR |  | Alternate Claim ID |
| 20 | `REF_CLAIM_IDENT` | VARCHAR |  | Reference claim ID for the original claim |
| 21 | `WORKFLOW_C_NAME` | VARCHAR | org | Claim workflow type (AP claim, paid claim, estimate claim, etc.) |
| 22 | `COVERAGE_ID` | NUMERIC | FK→ | Coverage used to pay the claim |
| 23 | `PAYER_SEQ_NUMBER_C_NAME` | VARCHAR |  | Sequence number of the payer of the claim. |
| 24 | `OWN_BUSINESS_SEGMENT_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 25 | `CLM_SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 26 | `CLM_STATUS_C_NAME` | VARCHAR |  | Claim status |
| 27 | `STATUS_SET_DATE` | DATETIME |  | Date when claim status was updated |
| 28 | `RECEIVED_DATE` | DATETIME |  | The date the claim was received |
| 29 | `ADJUD_DTTM` | DATETIME (Local) |  | Adjudication date and time |
| 30 | `SERVICE_START_DATE` | DATETIME |  | Service start date for the claim |
| 31 | `SERVICE_END_DATE` | DATETIME |  | Service end date for the claim |
| 32 | `TTL_DEDUCTIBLE` | NUMERIC |  | Total deductible |
| 33 | `TTL_COPAY` | NUMERIC |  | Total copay |
| 34 | `TTL_COINS` | NUMERIC |  | Total coinsurance |
| 35 | `TTL_PAT_AMT` | NUMERIC |  | Total patient amount |
| 36 | `TTL_PRIM_INS_AMT` | NUMERIC |  | Total prior insurance amount |
| 37 | `TTL_BILLED` | NUMERIC |  | Total billed amount |
| 38 | `TTL_ALLOWED_AMT` | NUMERIC |  | Total allowed amount |
| 39 | `TTL_NET_PAYABLE` | NUMERIC |  | Total net payable |
| 40 | `ORIG_OF_REV_CLAIM_ID` | NUMERIC |  | If this claim is a reversal claim, this column contains the ID of the claim reversed by this claim. |
| 41 | `ADJUST_BY_CLAIM_ID` | NUMERIC |  | If this claim has been adjusted, this column contains the ID of the claim which adjusts this claim. |
| 42 | `ORIG_OF_ADJUST_CLAIM_ID` | NUMERIC |  | If this claim adjusts another claim, this column contains the ID of the claim adjusted by this claim. |
| 43 | `TTL_PRIM_PAT_DEDUCTIBLE` | NUMERIC |  | Total prior patient deductible |
| 44 | `TTL_PRIM_PAT_COPAY` | NUMERIC |  | Total prior patient copay |
| 45 | `TTL_PRIM_PAT_COINS` | NUMERIC |  | Total prior patient coinsurance |
| 46 | `UNBALANCED_AMOUNTS_YN` | VARCHAR |  | Identifies whether the adjustment claim was received with credit/debit information that reflect the adjusted amount as opposed to new claim amounts. |
| 47 | `INVALID_CLM_YN` | VARCHAR |  | If the system determined we cannot trust the claim's data for reporting or clinical purposes, this column will store Y (invalid). Otherwise it will be N (valid) or NULL (has not been evaluated by the system). This column's value can be overridden by AP_CLM_RX.OVERRIDE_INVALID_CLM_YN. |
| 48 | `OVERRIDE_INVALID_CLM_YN` | VARCHAR |  | Overrides the INVALID_CLM_YN column and determines if we cannot trust the claim's data for reporting or clinical purposes. This column will store Y if overridden to invalid, N if overridden to valid, or NULL if validity has not been overridden and the value in AP_CLM_RX.INVALID_CLM_YN will be used. |
| 49 | `IS_INVLD_ADJ_SEQ_RX_YN` | VARCHAR |  | Indicates whether a claim is part of an adjustment sequence that is not valid. An adjustment sequence can be invalid for a number of reasons, such as the sequence ending in a cancellation or the sequence having gaps. |
| 50 | `TOT_NOT_COVERED_AMT` | NUMERIC |  | Total not covered amount |
| 51 | `MEDICARE_DRUG_CVG_CODE_C_NAME` | VARCHAR |  | Code to distinguish if a claim was paid under Medicare Part B or Part D. |
| 52 | `REC_OWN_BUSSEG_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 53 | `CMS_NATURAL_KEY` | VARCHAR |  | The claim natural key for a CMS claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PHARMACY_ID` | [RX_PHR](RX_PHR.md) | sole_pk | high |

