# AP_CLM_RX_DTL

> This table contains information for a single NDC code on a pharmacy claim.

**Overflow family:** [AP_CLM_RX_DTL_2](AP_CLM_RX_DTL_2.md)  
**Primary key:** `TX_ID`  
**Columns:** 40  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record |
| 2 | `NDC_ID` | VARCHAR | FK→ | National Drug Code (NDC) |
| 3 | `NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 4 | `PRESC_REF_NUM` | VARCHAR |  | Prescription reference number. |
| 5 | `NDC_UNIT_EXT_CODE_LST_ID` | NUMERIC |  | Units (ml, units, etc.). The unit code can be retrieved by joining this column to the EXT_COSE_LST_ID column in FCL_EXTRNL_CDE_LST table. |
| 6 | `NDC_UNIT_EXT_CODE_LST_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 7 | `FILL_NUMBER` | INTEGER |  | Indicates whether the prescription is an original (0) or a refill (1,2,...). |
| 8 | `DAYS_SUPPLY` | INTEGER |  | Estimated number of days the prescription will last. |
| 9 | `DAW_CODE_EXT_CODE_LST_ID` | NUMERIC |  | Code indicating whether or not the prescriber's instructions regarding generic substitution were followed. The Dispense As Written (DAW) code can be retrieved by joining this column to the EXT_COSE_LST_ID column in FCL_EXTRNL_CDE_LST table. |
| 10 | `DAW_CODE_EXT_CODE_LST_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 11 | `INGRED_COST_PAID` | NUMERIC |  | Drug ingredient cost paid. |
| 12 | `DISPENSING_FEE_PAID` | NUMERIC |  | Dispensing fee paid. |
| 13 | `REG_TAX_AMT_PAID` | NUMERIC |  | Flat sales tax amount paid. |
| 14 | `PCT_TAX_AMT_PAID` | NUMERIC |  | Percentage tax amount paid. |
| 15 | `INCENTIVE_AMT_PAID` | NUMERIC |  | Incentive amount paid. |
| 16 | `PROF_SVC_FEE_PAID` | NUMERIC |  | Professional service fee paid. |
| 17 | `OTHER_AMT_RECOGNIZED` | NUMERIC |  | Total amount recognized by the processor of any payment from another source. |
| 18 | `QUANTITY` | NUMERIC |  | Quantity dispensed |
| 19 | `FILL_DATE` | DATETIME |  | Identifies date the prescription was filled. |
| 20 | `OWNING_SAPBS_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 21 | `POS_TYPE_C_NAME` | VARCHAR | org | Place of service type |
| 22 | `PRIM_INS_AMT` | NUMERIC |  | Sum of all the insurance amount paid by previous payers. |
| 23 | `BILLED_AMT` | NUMERIC |  | Billed amount |
| 24 | `ALLOWED_AMT` | NUMERIC |  | Allowed amount |
| 25 | `PRIM_PAT_DEDUCTIBLE` | NUMERIC |  | Store prior patient deductible |
| 26 | `PRIM_PAT_COPAY` | NUMERIC |  | Store prior patient copay |
| 27 | `PRIM_PAT_COINS` | NUMERIC |  | Store prior patient co-insurance |
| 28 | `DEDUCTIBLE` | NUMERIC |  | Deductible amount |
| 29 | `COPAY` | NUMERIC |  | Copay amount |
| 30 | `COINSURANCE` | NUMERIC |  | Coinsurance amount |
| 31 | `PAT_TOTAL` | NUMERIC |  | Patient total amount |
| 32 | `NET_PAYABLE` | NUMERIC |  | Net payable |
| 33 | `CLAIM_ID` | NUMERIC | FK→ | The accounts payable claim to which this service line is associated. |
| 34 | `RX_POINTER_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 35 | `FILL_STATUS_C_NAME` | VARCHAR |  | Stores information on whether the prescription was completely or partially filled. |
| 36 | `POS_TYPE_SRC_C_NAME` | VARCHAR |  | Source of the Place of Service type |
| 37 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Chronicles special item. This is the soft-delete flag that will be set to the appropriate record status option when the record is soft-deleted. |
| 38 | `PRESC_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 39 | `SERV_PHARMACY_ID` | NUMERIC |  | The unique ID associated with the service pharmacy record for this row. This column is frequently used to link to the RX_PHR table. |
| 40 | `SERV_PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |
| `NDC_ID` | [RX_NDC](RX_NDC.md) | sole_pk | high |

