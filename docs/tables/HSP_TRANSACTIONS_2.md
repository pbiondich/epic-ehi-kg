# HSP_TRANSACTIONS_2

> This table contains hospital account transaction information from the Hospital Permanent Transactions (HTR) master file.

**Overflow of:** [HSP_TRANSACTIONS](HSP_TRANSACTIONS.md)  
**Primary key:** `TX_ID`  
**Columns:** 56  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction. |
| 2 | `REL_ACCL_INS_BKT_ID` | NUMERIC |  | This column stores the unique identifier for the insurance bucket on the accelerated self-pay adjustment transaction in the self-pay bucket. |
| 3 | `IMPLIED_QTY` | NUMERIC |  | The implied quantity for the order at the time this charge was dropped. This represents the quantity used to calculate the billing quantity on a pharmacy charge. |
| 4 | `IMPLIED_QTY_UNIT_C_NAME` | VARCHAR | org | This column stores the implied unit for the order at the time a charge was dropped. This represents the unit of the quantity used to calculate the billing quantity on a pharmacy charge. |
| 5 | `IMPLIED_UNIT_TYPE_C_NAME` | VARCHAR |  | The implied unit type for the order at the time a charge was dropped. This is where the unit was taken from (i.e. dispense unit, package unit, entire package). |
| 6 | `LATEST_MED_ORD_DAT` | NUMERIC |  | This column stores the most recent Order contact date (DAT) for the medication Order. |
| 7 | `SYS_RECLASS_RSN_C_NAME` | VARCHAR |  | Stores the reclassification reason for a transaction reposted for system reasons. |
| 8 | `CHRG_AMT_SRC_FLG_C_NAME` | VARCHAR |  | The charge amount source flag category number for the charge transaction. |
| 9 | `ORIG_ACCT_COMB_ID` | NUMERIC |  | This column stores the first account that a hospital billing transaction attempted to post to prior to combine accounts or combined account redirection. Resets upon transfer. |
| 10 | `PLB_PROV_ID` | VARCHAR |  | Stores PLB (Provider Level Adjustment) provider ID |
| 11 | `PLB_FP_DATE` | DATETIME |  | Stores PLB (Provider Level Adjustment) fiscal period date. |
| 12 | `PLB_REASON_CODE_C_NAME` | VARCHAR | org | Stores PLB (Provider Level Adjustment) reason code. |
| 13 | `PLB_REFERENCE_NUM` | VARCHAR |  | Stores PLB (Provider Level Adjustment) reference code. |
| 14 | `PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 15 | `RSH_MOD_TYPE_C_NAME` | VARCHAR | org | This column stores the charge's research billing modifier type. Having a value set here should mean that the charge should file to the patient account in order to bill to insurance, instead of filing to the study account. Thus, in most cases, the presence of data in this column should mean that RSH_CHG_ROUTE_C is also set to Yes, because the RSH_CHG_ROUTE_C column actually controls whether the study-related charge files to the patient or to the study budget. |
| 16 | `RSH_CHG_ROUTE_C_NAME` | VARCHAR |  | This column indicates whether a research-related charge should route to the patient account or the study account. In most cases, if the charge has a research billing modifier type, it will also file to the patient in order to be billed to insurance. However, the flag that actually determines when a charge will file to the patient account is its charge route value; the value in this column indicates the final determination whether the charge will file to the patient or to the study budget. |
| 17 | `ELEC_PMT_AUTH_CODE` | VARCHAR |  | Authorization code sent back by the merchant |
| 18 | `TREATMENT_PLAN_CSN` | NUMERIC |  | The contact serial number of the treatment plan that generated this charge and order. |
| 19 | `SUP_INV_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 20 | `SUP_WASTED_QTY` | INTEGER |  | Wasted quantity |
| 21 | `TREATMENT_DAY_CSN` | NUMERIC |  | This column stores the contact serial number of the treatment day that generated this charge's order. This contact serial number can be linked to TRG_UPDATE_INFO.CONTACT_SERIAL_NUM for additional information on the treatment day. This treatment day is contained within the treatment plan specified in HSP_TRANSACTIONS_2.TREATMENT_PLAN_contact serial number (CSN). |
| 22 | `OTHER_ADJ_AMOUNT` | NUMERIC |  | Stores the other adjustment amount associated with this payment. |
| 23 | `OTHER_ADJ_REF_NUM` | VARCHAR |  | Stores the other adjustment reference number associated with this payment. |
| 24 | `OTHER_ADJ_COMMENT` | VARCHAR |  | Stores the other adjustment comment associated with this payment. |
| 25 | `PMT_DRG_CODE` | VARCHAR |  | This column stores the diagnosis-related group (DRG) code received on the remittance image. |
| 26 | `RATE_CNTR_ID` | NUMERIC |  | The rate center stored in a charge transaction. If a user has chosen to override the default rate center in the procedure master file, the user-entered override rate center will display here. |
| 27 | `RATE_CNTR_ID_COST_CENTER_NAME` | VARCHAR |  | The name of the cost center. |
| 28 | `DFLT_RATE_CNTR_ID` | NUMERIC |  | This column stores the unique identifier for the default rate center from the procedure master file for a charge transaction. |
| 29 | `DFLT_RATE_CNTR_ID_COST_CENTER_NAME` | VARCHAR |  | The name of the cost center. |
| 30 | `DX_PRIM_CODE_SET_C_NAME` | VARCHAR | org | The primary diagnosis code set configured in the facility for the service date of the transaction. |
| 31 | `DX_ALT_CODE_SET_C_NAME` | VARCHAR |  | The alternate diagnosis code set configured in the facility for the service date of the transaction. |
| 32 | `COMPOUND_DRUG_LINK_NUM` | VARCHAR |  | The link number for compound medication. The link number is used to group charge lines for components from the same compound drug on claim. |
| 33 | `LATEST_MED_ORD_DTE` | NUMERIC |  | This column stores the most recent order date (DTE) for the medication order. This column can be used to link to the CONTACT_DATE_REAL column in many order tables to find the correct contact. |
| 34 | `FIRST_TX_POST_DATE` | DATETIME |  | This column stores the post date of the first transaction across hospital billing and professional billing in a chain of transfers, reposts, and reversals. |
| 35 | `ELEC_PMT_RESP_STS_C_NAME` | VARCHAR |  | Response message status from the gateway. This item is only stored for non-accepted responses. |
| 36 | `ELEC_PMT_RESP_MSG` | VARCHAR |  | Response message from gateway if transaction was not successful. We don't store a message (if any is sent) for accepted transactions. |
| 37 | `ACCT_FIN_CLASS_C_NAME` | VARCHAR | org | Holds the financial class of the account when the transaction filed. This is set for all transaction types. |
| 38 | `PRIMARY_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 39 | `DISCOUNT_PERCENT` | INTEGER |  | Stores the discount percentage applied to the self-pay balance. |
| 40 | `DISCOUNT_PROGRAM_ID` | NUMERIC |  | Stores the financial assistance program that the hospital account qualified for which caused the financial assistance adjustment to be applied. |
| 41 | `DISCOUNT_PROGRAM_ID_PROGRAM_NAME` | VARCHAR |  | The name of the financial assistance program record. |
| 42 | `DISCOUNT_COMMENT` | VARCHAR |  | Stores the additional details on why the discount is posted on the hospital account. |
| 43 | `PRIMARY_COVERAGE_ID` | NUMERIC |  | Holds the primary coverage of the account when the transaction filed. This is set for all transaction types. |
| 44 | `HAR_FIRST_POST_DATE` | DATETIME |  | This column stores the post date of the first hospital billing transaction on the hospital account in a chain of reposts and reversals. |
| 45 | `POST_SOURCE_C_NAME` | VARCHAR |  | This column stores the source from which the payment is posted in the system. This is calculated based on the transaction source on the hospital billing transaction. |
| 46 | `SERVICE_SPEC_C_NAME` | VARCHAR | org | The service specialty of the transaction. This may be different from the service provider's specialty for providers working outside their specialty. If this field has no value, the transaction specialty is the same as the service provider's first-listed specialty. |
| 47 | `BILLING_SPEC_C_NAME` | VARCHAR |  | The billing specialty of the transaction. This may be different from the billing provider's specialty for providers working outside their specialty. If this field has no value, the transaction specialty is the same as the billing provider's first-listed specialty. |
| 48 | `ORIG_BUNDPMT_ETR_ID` | NUMERIC |  | This column stores the unique identifier for the professional billing transaction for the original bundled payment. |
| 49 | `ORIG_BUNDPMT_HTR_ID` | NUMERIC |  | This column stores the unique identifier for the hospital billing transaction for the original bundled payment. |
| 50 | `REFERENCE_AMT` | NUMERIC |  | Holds the reference amount that is calculated based on the financial class for the charge. This is set by the system and is applicable only to charges. |
| 51 | `REFERENCE_AMT_SRC_C_NAME` | VARCHAR |  | Holds the source of the reference amount that is used in the calculation of the reference amount. This is set by the system and is applicable only to charges. |
| 52 | `SRCHG_CLP_ID` | NUMERIC |  | This column stores the unique identifier for the claim print record containing the values contributing to the surcharge adjustment. |
| 53 | `ADJUSTMENT_CAT_C_NAME` | VARCHAR | org | The adjustment category of the adjustment procedure at the time of posting. |
| 54 | `WRITE_OFF_RSN_C_NAME` | VARCHAR |  | The mapped write-off reason for the adjustment. |
| 55 | `SCHED_PMT_ID` | NUMERIC | FK→ | Stores the scheduled payment record that resulted in this payment. |
| 56 | `PARENT_SCHED_PMT_ID` | NUMERIC |  | Stores the parent scheduled payment record that resulted in this payment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SCHED_PMT_ID` | [BILL_SCHED_PMT](BILL_SCHED_PMT.md) | sole_pk | high |

