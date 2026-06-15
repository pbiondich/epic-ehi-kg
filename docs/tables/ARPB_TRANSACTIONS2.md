# ARPB_TRANSACTIONS2

> This table contains information about professional billing transactions.

**Primary key:** `TX_ID`  
**Columns:** 57  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `EB_PMT_TOTAL_AMT` | NUMERIC |  | Displays the enterprise payment total amount. |
| 3 | `FIN_DIV_ID` | NUMERIC |  | The Financial Division for this transaction. Taken from the ETR listed or from the associated Bill Area, as found in ARPB_TRANSACTIONS |
| 4 | `FIN_DIV_ID_BILL_AREA_NAME` | VARCHAR |  | The record name of this bill area, financial subdivision, or financial division. |
| 5 | `FIN_SUBDIV_ID` | NUMERIC |  | The Financial Subdivision for this transaction. Taken from the ETR listed or from the associated Bill Area, as found in ARPB_TRANSACTIONS |
| 6 | `FIN_SUBDIV_ID_BILL_AREA_NAME` | VARCHAR |  | The record name of this bill area, financial subdivision, or financial division. |
| 7 | `RESEARCH_STUDY_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 8 | `RSH_MOD_TYPE_C_NAME` | VARCHAR | org | The research billing modifier type for a research study related charge. |
| 9 | `RSH_ORIG_ACCOUNT_ID` | NUMERIC |  | Stores the original patient account for charges billed to the guarantor account related to a research study. |
| 10 | `OUTSTANDING_FLAG_C_NAME` | VARCHAR |  | The type of balance category ID for the transaction |
| 11 | `VST_DO_NOT_BIL_I_YN` | VARCHAR |  | This item indicates whether the visit has been marked as do not bill insurance. |
| 12 | `TREATMENT_PLAN_CSN` | NUMERIC |  | The contact serial number of the treatment plan that generated the order, which generated this charge. |
| 13 | `TX_ENTERED_INSTANT_DTTM` | DATETIME (UTC) |  | The transaction entered instant (date and time in UTC) for manually posted payments. The transaction filing instant (date and time in UTC) for electronically posted payments. |
| 14 | `CVG_PLAN_ON_PMT_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 15 | `REVERSED_PMT_TX_ID` | NUMERIC |  | For the negation payment generated during a payment reversal, this item stores the transaction ID of the original payment. |
| 16 | `PMT_REVERSAL_TX_ID` | NUMERIC |  | This virtual item returns the reversal transaction ID for a reversed payment. |
| 17 | `STMT_HOLD_DT` | DATETIME |  | The most recent date on which the transaction was held from the Professional Billing statement processing. |
| 18 | `STMT_HOLD_REASON_C_NAME` | VARCHAR | org | The reason why the transaction was held in PB statement processing. |
| 19 | `REPOST_REASON_C_NAME` | VARCHAR | org | If this transaction was reposted from another, this contains the category value of the reason the transaction was reposted. |
| 20 | `SUSP_NRP_INDICATOR_YN` | VARCHAR |  | This item indicates whether NRP is currently suspended. |
| 21 | `SUSP_NRP_INST_DTTM` | DATETIME (Local) |  | This item stores the instant (date and time) when the next responsible party action was suspended. |
| 22 | `SUSP_NRP_USER_ID` | VARCHAR |  | This item stores the suspended next responsible party user for the transaction. |
| 23 | `SUSP_NRP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 24 | `OUTST_CLM_STAT_C_NAME` | VARCHAR | org | The status of an outstanding claim that is attached to a transaction. |
| 25 | `POS_TYPE_C_NAME` | VARCHAR | org | Place of service type for a charge transaction. |
| 26 | `INACTIVE_TYPE_C_NAME` | VARCHAR |  | This column returns the type of an inactive transaction. Inactive transactions are those involved in a void or reversal. This item subcategorizes the transaction's role in the void or reversal. This will be for both the actual voided/reversed credit and the associated negation payment or debit adjustment. |
| 27 | `VOIDED_INS_AMT` | NUMERIC |  | The total amount owed from insurance at the time a charge was voided. This includes previously applied payments and adjustments. |
| 28 | `PROV_NETWORK_STAT_C_NAME` | VARCHAR |  | Basic indicator of whether a provider was in or out of network on the service date of a transaction |
| 29 | `NETWORK_LEVEL_C_NAME` | VARCHAR | org | The provider's level of network involvement category ID for the transaction. |
| 30 | `SPEC_CHG_TYPE_C_NAME` | VARCHAR |  | The special type category ID for the charge. |
| 31 | `ORIG_BUNDPMT_ETR_ID` | NUMERIC |  | The original bundled payment transaction ID. |
| 32 | `ORIG_BUNDPMT_HTR_ID` | NUMERIC |  | The original bundled payment hospital transaction ID. |
| 33 | `REFERENCE_AMT` | NUMERIC |  | Holds the reference amount that is calculated based on the financial class for the charge. This is set by the system and is applicable only to charges. |
| 34 | `REFERENCE_AMT_SRC_C_NAME` | VARCHAR |  | Holds the source of the reference amount that is used in the calculation of the reference amount. This is set by the system and is applicable only to charges. |
| 35 | `CLM_RMV_RSN_C_NAME` | VARCHAR |  | Stores the reason charge was removed from the claim queue. |
| 36 | `ADJUSTMENT_CAT_C_NAME` | VARCHAR | org | Stores the adjustment category of the associated adjustment code when the credit adjustment is posted. |
| 37 | `WRITE_OFF_RSN_C_NAME` | VARCHAR |  | The reason a credit adjustment was posted. This is determined programmatically when possible (e.g. contractual adjustments, self-pay discounts). Otherwise, this is the write-off reason associated with the adjustment category for this adjustment. |
| 38 | `SCHED_PMT_ID` | NUMERIC | FK→ | Stores the scheduled payment record that resulted in this payment. |
| 39 | `TAX_CHARGE_TX_ID` | NUMERIC |  | Stores the source transaction for a tax charge |
| 40 | `PATIENT_ESTIMATE_ID` | NUMERIC |  | This column contains the Patient Estimate (PES) record ID for a dental estimate that is finalized and is linked to this charge. If the charge was triggered from dental and if there is a dental estimate associated with the encounter (in a status of "Finalized"), that estimate's record ID will be stored in ETR item 1801 and extracted in this column. The item and column are not updated if and when the original finalized estimate is replaced. |
| 41 | `PATIENT_WISDOM_PROC_ID` | NUMERIC |  | Patient dental procedure that was respected by the temporary transaction that filed into this transaction. |
| 42 | `RFL_OVRIDE_SRC_C_NAME` | VARCHAR |  | This item stores the referral override source. The options are 1-User or 2-System. |
| 43 | `RFL_OVRIDE_USER_ID` | VARCHAR |  | This item stores the user who overrode the referral associated with this charge. |
| 44 | `RFL_OVRIDE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 45 | `PARENT_SCHED_PMT_ID` | NUMERIC |  | Stores the parent scheduled payment record that resulted in this payment. |
| 46 | `MANUAL_PRICE_OVRIDE_YN` | VARCHAR |  | Permanent transaction indicator used during repost/correct/retro to determine if the charge's price was originally overridden. |
| 47 | `IS_PRE_SERVICE_PMT_YN` | VARCHAR |  | Indicates whether or not this is a pre-service payment, such as a copay. This item is only populated for self-pay payments. A payment is considered pre-service if it is a visit prepay, a copay payment (such as during check-in), a Visit Auto Pay payment, or a payment made on a visit account added to a pre-service payment plan based on an estimate. |
| 48 | `FIRST_HTR_TX_ID` | NUMERIC |  | Stores the hospital transaction ID of the first transaction in a chain of transactions. Note that this chain will include transactions from both Hospital Billing and Professional Billing, so this item will return the very first transaction. For a given transaction, either column ARPB_TRANSACTIONS2.FIRST_HTR_ID, or column ARPB_TRANSACTIONS2.FIRST_ETR_ID will be populated. This is different from column ARPB_TRANSACTIONS2.FIRST_TX_ID, which only chains back to the point that the transaction was transferred from Hospital Billing. |
| 49 | `FIRST_ETR_TX_ID` | NUMERIC |  | Stores the transaction ID of the first transaction in a chain of transactions. Note that this chain will include transactions from both Hospital Billing and Professional Billing, so this item will return the very first transaction. For a given transaction, either column ARPB_TRANSACTIONS2.FIRST_HTR_ID, or column ARPB_TRANSACTIONS2.FIRST_ETR_ID will be populated. This is different from column ARPB_TRANSACTIONS2.FIRST_TX_ID, which only chains back to the point that the transaction was transferred from Hospital Billing. |
| 50 | `POSTING_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 51 | `EXP_REIMB_SYS_AMT` | NUMERIC |  | The item stores the original reimbursement amount calculated by contract if the original reimbursement amount is overridden. |
| 52 | `EXP_REIMB_SRC_C_NAME` | VARCHAR |  | The item stores how the reimbursement amount was calculated for the charge. |
| 53 | `RECORD_STATUS_C_NAME` | VARCHAR |  | This column displays the transaction record status. |
| 54 | `RESEARCH_ENROLL_ID` | NUMERIC |  | The unique ID of the research study association linked to this charge. |
| 55 | `STMT_HOLD_RSN_TEXT` | VARCHAR |  | The free text information related to the reason why the transaction was held in Professional Billing statement processing. |
| 56 | `E_PMT_RECEIPT_MSG` | VARCHAR |  | Saves the receipt message received from the gateway for an electronic payment transaction. |
| 57 | `PARENT_TX_ID` | NUMERIC |  | This column contains the charge ID that created this transaction during transaction filing. This is used for anesthesia supplemental charges, charge quantity splitting, and charge shadowing. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SCHED_PMT_ID` | [BILL_SCHED_PMT](BILL_SCHED_PMT.md) | sole_pk | high |

