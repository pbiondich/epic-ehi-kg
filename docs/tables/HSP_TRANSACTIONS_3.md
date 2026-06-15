# HSP_TRANSACTIONS_3

> This table contains hospital account transaction information from the Hospital Permanent Transactions (HTR) master file.

**Overflow of:** [HSP_TRANSACTIONS](HSP_TRANSACTIONS.md)  
**Primary key:** `TX_ID`  
**Columns:** 47  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction. |
| 2 | `CONTEST_RSN_C_NAME` | VARCHAR | org | Stores the contested reason. This is set only for charges. |
| 3 | `CONTEST_RESOLUTION_RSN_C_NAME` | VARCHAR | org | Stores the contested resolution reason. This is set only for charges. |
| 4 | `REVERSAL_RSN_C_NAME` | VARCHAR | org | Holds the reversal reason. This is set for all transaction types. |
| 5 | `TAX_RATE_DEF_CSN` | NUMERIC |  | This column stores the tax rate definition contact serial number (CSN) used in the tax calculation. |
| 6 | `IS_PRE_SERVICE_PMT_YN` | VARCHAR |  | Indicates whether or not this is a pre-service payment, such as a copay. This item is only populated for self-pay payments. A payment is considered pre-service if it is a visit prepay, a copay payment (such as during check-in), a Visit Auto Pay payment, or a payment made on a visit account added to a pre-service payment plan based on an estimate. |
| 7 | `FIRST_HTR_TX_ID` | NUMERIC |  | This column stores the unique identifier for the first hospital billing transaction in a chain of transactions. Note that this chain will include transactions from both hospital billing and professional billing, so this item will return the very first transaction. For a given transaction, either column HSP_TRANSACTIONS_3.FIRST_HTR_ID, or column HSP_TRANSACTIONS_3.FIRST_ETR_ID will be populated. This is different from column HSP_TRANSACTIONS_2.FIRST_TX_ID, which only chains back to the point that the transaction was transferred from professional billing. |
| 8 | `FIRST_ETR_TX_ID` | NUMERIC |  | This column stores the unique identifier for the first professional billing transaction (ETR record) in a chain of transactions. Note that this chain will include transactions from both hospital billing and professional billing, so this item will return the very first transaction. For a given transaction, either column HSP_TRANSACTIONS_3.FIRST_HTR_ID, or column HSP_TRANSACTIONS_3.FIRST_ETR_ID will be populated. This is different from column HSP_TRANSACTIONS_2.FIRST_TX_ID, which only chains back to the point that the transaction was transferred from professional billing. |
| 9 | `NO_PAY_CLAIM_TYPE_C_NAME` | VARCHAR |  | If this charge was posted to drive no-pay claims to be generated, this charge is intended to file and bill immediately. These claims will have different types/purposes. This item defines the type of claim that should be generated for the bucket that hold this charge. |
| 10 | `ORIG_PMT_SPLIT_TX_ID` | NUMERIC |  | This column stores the original unique identifier for the hospital billing transaction when payments are distributed or split. |
| 11 | `SVC_AUTH_ID` | NUMERIC |  | This item stores the social care service decision level authorization record associated with this charge. |
| 12 | `POSTING_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 13 | `TAX_EFFECTIVE_DATE` | DATETIME |  | This column stores the date used in the hospital billing system definitions that determine when this tax line went into effect. |
| 14 | `TAXABLE_AMOUNT` | NUMERIC |  | This item stores the amount that the tax is applied to |
| 15 | `TAX_PERCENT` | NUMERIC |  | Percent used to calculate the tax amount |
| 16 | `TAX_AMOUNT` | NUMERIC |  | This item stores the amount used for the tax |
| 17 | `DIGITAL_WALLET_C_NAME` | VARCHAR |  | Holds the digital wallet used for an electronic payment. Stored on payments made from a digital wallet and on reversals. This item is not stored on refund transactions. |
| 18 | `ADV_BILL_DB_TX_ID` | NUMERIC |  | This column stores the unique identifier for the hospital billing transaction for this advance bill debit transfer adjustment. |
| 19 | `ADV_BILL_ESTIMATE_ID` | NUMERIC |  | This column stores the unique identifier for the estimate used in posting this advance bill adjustment. |
| 20 | `IS_ADV_BILL_TRANS_YN` | VARCHAR |  | Indicates if this transaction an advance bill transfer system adjustment. Includes both credit and debit adjustments. |
| 21 | `SAVED_PMT_DIGITAL_WALLET_C_NAME` | VARCHAR |  | Holds the digital wallet of the saved payment method used to make the payment |
| 22 | `RESEARCH_ENROLL_ID` | NUMERIC |  | The unique ID of the research study association linked to this transaction. |
| 23 | `CLAIM_PRINT_ID` | NUMERIC | shared | The payment's claim print ID with a matching invoice number. |
| 24 | `INS_WRITE_OFF_AMT` | NUMERIC |  | This item stores the insurance write off amount from the payment based on remittance codes that are mapped to an insurance write-off action. |
| 25 | `IS_SCANNED_CHECK_YN` | VARCHAR |  | Indicates if a transaction was made using a scanned check. |
| 26 | `E_PMT_RECEIPT_MSG` | VARCHAR |  | Saves the receipt message received from the gateway for an electronic payment transaction. |
| 27 | `PAT_PMT_COLL_WKFL_C_NAME` | VARCHAR |  | This column contains the workflow category ID performed to collect a patient payment from the point of view of the user. For example, MyChart eCheck-in vs. MyChart One-Touch. |
| 28 | `MYC_SIGNIN_METHOD_C_NAME` | VARCHAR |  | This column denotes how the patient or guarantor logged in to MyChart to either post the payment or create an agreement that will post a payment via Auto Pay. Only populated for agreements made via MyChart. |
| 29 | `POSTING_MYPT_ID` | VARCHAR |  | This column contains either the MyChart account that created the agreement that resulted in the self-pay payment (if applicable) or the MyChart account that posted the self-pay payment. |
| 30 | `POSTING_MYC_STATUS_C_NAME` | VARCHAR | org | This column contains either the status of the MyChart account that created the agreement that resulted in the self-pay payment (if applicable) or the status of the MyChart account that posted the self-pay payment. An active MyChart account status is defined as whether a MyChart user could log into the account with a user name and password. Accounts that are not yet active, deactivated, or are proxy accounts are considered inactive. |
| 31 | `EB_TX_SOURCE_C_NAME` | VARCHAR |  | This column stores the enterprise posting module for the transaction. This is calculated based on the hospital billing transaction source for the transaction. For reversals, the module will always match the module of the reversed parent transaction. |
| 32 | `LINKED_PARENT_TX_ID` | NUMERIC |  | Stores the parent HTR ID in a linked child HTR. |
| 33 | `RELATED_ETR_TX_ID` | NUMERIC |  | Applies only if you have enabled Consolidated Self-Pay Balances functionality. Stores the professional transaction ID of the related transaction. This will only be populated on transactions that were mirrored from professional billing. |
| 34 | `PMT_PLAN_AGRMT_SCHED_PMT_ID` | NUMERIC |  | The unique ID of the transaction's target guarantor's active payment plan agreement record at the time of filing. |
| 35 | `IS_EST_PRE_SERVICE_PLAN_PMT_YN` | VARCHAR |  | Indicates whether this payment was made on an estimated balance on a payment plan at time of filing ('Y'). 'N' or NULL indicates that the transaction is not a payment, the payment is not on a balance on a payment plan, or the balance was not estimated at the time of filing. |
| 36 | `IS_PRE_SERVICE_PLAN_PMT_YN` | VARCHAR |  | Indicates whether this payment was made toward a hospital account on a payment plan that was added by an estimate ('Y'). 'N' or NULL indicates that the transaction is not a payment or the payment was not made toward a hospital account on a payment plan that was added by an estimate. |
| 37 | `EST_VARIANCE_WO_ESTIMATE_ID` | NUMERIC |  | If this transaction is part of an automatic estimate variance write-off, this item stores the estimate that this is a write off towards. |
| 38 | `AR_CLASSIFICATION_C_NAME` | VARCHAR |  | This column stores the AR classification of this transaction. |
| 39 | `DISCOUNT_FIN_ASST_TRACKER_ID` | NUMERIC |  | The unique identifier of the financial assistance tracker that generated this discount transaction. |
| 40 | `DISCOUNT_DAILY_PAY_AMT` | NUMERIC |  | This item stores the daily pay amount applied to the self-pay balance. |
| 41 | `DISCOUNT_NUM_OF_DAYS` | INTEGER |  | This item stores the number of billable days a patient is responsible for. |
| 42 | `PMT_DISCOUNT_PROMOTION_ID` | NUMERIC |  | The Promotion Record for the payment-based discount. This is set both on the payment and the discount adjustment. |
| 43 | `PMT_DISCOUNT_PROMOTION_ID_PROMOTION_NAME` | VARCHAR |  | The promotion record name. |
| 44 | `IS_PREPAY_PMT_YN` | VARCHAR |  | Indicates whether this is a prepay payment. This includes visit prepay payments and copay payments, such as during check in. This column is only populated for self-pay payments. |
| 45 | `PMT_DISCOUNT_ORIG_PMT_TX_ID` | NUMERIC |  | The original payment transaction that resulted in a discount offer being applied. This is only stored on discount offer adjustments. |
| 46 | `REV_SPEC_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 47 | `REV_SUBSPEC_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

