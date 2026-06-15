# HSP_TRANSACTIONS

> This table contains hospital account transaction information from the Hospital Permanent Transactions (HTR) master file.

**Overflow family:** [HSP_TRANSACTIONS_2](HSP_TRANSACTIONS_2.md), [HSP_TRANSACTIONS_3](HSP_TRANSACTIONS_3.md)  
**Primary key:** `TX_ID`  
**Columns:** 131  
**Org-specific columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction. |
| 2 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the hospital account associated with the hospital billing transaction. |
| 3 | `ACCT_CLASS_HA_C_NAME` | VARCHAR | org | Holds the account class of the account when the transaction filed. This is set for all transaction types. |
| 4 | `ACTION_STRING` | VARCHAR |  | A comma-delimited list of one or more numbers stored in a payment transaction that correspond to actions entered in payment posting. Actions are 1 -- Not Allowed Adjustment, 2 -- Next Responsible Party, 3 -- Claim Denied. |
| 5 | `ALLOWED_AMOUNT` | NUMERIC |  | An allowed amount stored in a payment transaction. |
| 6 | `BILLED_AMOUNT` | NUMERIC |  | A billed amount stored in a payment transaction. |
| 7 | `BILLING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `BUCKET_ID` | NUMERIC | shared | This column stores the unique identifier for the liability bucket on which the transaction is currently active. This field is only populated for payment and adjustment transactions, not charges. |
| 9 | `COINSURANCE_AMOUNT` | NUMERIC |  | A coinsurance amount stored in a payment transaction. Coinsurance amounts are informational only. |
| 10 | `COPAY_AMOUNT` | NUMERIC |  | A copay amount stored in a payment transaction. Coinsurance amounts are informational only. |
| 11 | `DEDUCTIBLE_AMOUNT` | NUMERIC |  | A deductible amount stored in a payment transaction. Coinsurance amounts are informational only. |
| 12 | `DEPARTMENT_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 13 | `DFLT_FEE_SCHED_ID` | NUMERIC |  | This column stores the unique identifier for the default fee schedule for the service area with which a charge transaction is associated. |
| 14 | `DFLT_FEE_SCHED_ID_FEE_SCHEDULE_NAME` | VARCHAR |  | The name of each fee schedule. |
| 15 | `DFLT_PROC_DESC` | VARCHAR |  | This column stores the original description of the procedure stored in the procedure record's Name History (I EAP 6), which appears in Procedure Editor as Name. This item is only populated if the description for the procedure was overridden in charge entry. |
| 16 | `DFLT_UB_REV_CD_ID` | NUMERIC |  | The default revenue code from the procedure master file for a charge transaction. |
| 17 | `DFLT_UB_REV_CD_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 18 | `FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 19 | `FIN_CLASS_C_NAME` | VARCHAR | org | This column stores the category ID of the financial class stored in a hospital billing transaction. For charges, the financial class comes from the hospital account that the charge is associated with. For payments, the financial class comes from the payer specified during payment posting. If no payer is specified during payment posting, the financial class is self-pay. If the adjustment is entered in adjustment posting, the financial class is from the payer specified in adjustment posting. If the adjustment is created from a bucket action, the financial class comes from the financial class on the bucket. If no payer is specified during adjustment posting or the adjustment bucket action is made on an undistributed bucket, the financial class is self-pay. Adjustment refund bucket actions can specify the payer, in which case the specified payer's financial class is used. |
| 20 | `INST_BILL_COMMENT` | VARCHAR |  | A comment stored in a charge transaction. If a hospital account's guarantor is of a type that is considered institutional, then certain pieces of institutional billing-related information can be stored in charges filed on that hospital account. |
| 21 | `INST_BILL_DOB` | DATETIME |  | A date of birth stored in a charge transaction. If a hospital account's guarantor is of a type that is considered institutional, then certain pieces of institutional billing-related information can be stored in charges filed on that hospital account. A date of birth is one such piece of information. |
| 22 | `INST_BILL_EMP_NUM` | VARCHAR |  | An employee number stored in a charge transaction. If a hospital account's guarantor is of a type that is considered institutional, then certain pieces of institutional billing-related information can be stored in charges filed on that hospital account. An employee number is one such piece of information. |
| 23 | `INST_BILL_PAT_NAME` | VARCHAR |  | A patient name stored in a charge transaction. If a hospital account's guarantor is of a type that is considered institutional, then certain pieces of institutional billing-related information can be stored in charges filed on that hospital account. A patient name is one such piece of information. |
| 24 | `INST_BILL_SEX_C_NAME` | VARCHAR | org | A patient sex stored in a charge transaction. If a hospital account's guarantor is of a type that is considered institutional, then certain pieces of institutional billing-related information can be stored in charges filed on that hospital account. A patient sex is one such piece of information. |
| 25 | `INT_CONTROL_NUMBER` | VARCHAR |  | The internal control number stored in a payment transaction. |
| 26 | `IS_SYSTEM_ADJ_YN` | VARCHAR |  | Denotes whether the adjustment is a system adjustment, as opposed to a contractual write-off, charity care write-off, refund, or other adjustments. A system adjustment moves liability between buckets or between collection statuses on a hospital account to properly adjust the GL and are not just adjustments posted by the system. |
| 27 | `IS_HOSPITALIST_YN` | VARCHAR |  | Denotes whether a charge has a billing provider who is designated in ADT as a hospitalist. |
| 28 | `IS_LATE_CHARGE_YN` | VARCHAR |  | Denotes whether a charge is a late charge. |
| 29 | `IS_RECOUPMENT_YN` | VARCHAR |  | Denotes whether a payment is a recoupment. |
| 30 | `MODIFIERS` | VARCHAR |  | A comma-delimited list of one or more modifiers associated with a charge transaction. |
| 31 | `OLD_HSP_ACCOUNT_ID` | NUMERIC |  | This column stores the unique identifier for the hospital account associated with the old hospital billing transaction that was transferred to a different hospital account, causing this new transaction to be created. |
| 32 | `ORDER_ID` | NUMERIC | shared | This column stores the unique identifier for the clinical system order that triggered a hospital billing transaction. |
| 33 | `ORIG_PRICE` | NUMERIC |  | Denotes the price that was determined for a charge based on fee schedules. |
| 34 | `ORIG_REPOST_TX_ID` | NUMERIC |  | This column stores the unique identifier for the original transaction of a hospital billing transaction automatically reposted due to a change in financial class, account class, or primary payer. |
| 35 | `ORIG_REV_TX_ID` | NUMERIC |  | In a reversal transaction, this column denotes the ID number of the original transaction that was reversed. |
| 36 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | For a charge dropped via ADT's bed charge billing function or a payment collected at the point-of-service, the contact serial number of the patient contact that triggered the bed charge or led to the collection of the payment. |
| 37 | `PAYMENT_FROM` | VARCHAR |  | For self pay payments, a text string indicating from whom the payment was received. |
| 38 | `PAYMENT_SRC_HA_C_NAME` | VARCHAR | org | The payment source stored in a payment transaction, i.e. cash, check, or credit card. |
| 39 | `PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 40 | `PERFORMING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 41 | `PREV_CREDITS_ACT` | NUMERIC |  | For adjustment transactions that move liability from one bucket to another, the total monetary amount of previous credits on the former bucket. |
| 42 | `PRIM_FEE_SCHED_ID` | NUMERIC |  | This column stores the unique identifier for the primary fee schedule used to price a charge transaction. |
| 43 | `PRIM_FEE_SCHED_ID_FEE_SCHEDULE_NAME` | VARCHAR |  | The name of each fee schedule. |
| 44 | `PROCEDURE_DESC` | VARCHAR |  | This column stores the value manually entered for the procedure description at the time of charge entry. If no value was manually entered, then the procedure record's Name History (I EAP 6) is populated here. |
| 45 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 46 | `QUANTITY` | NUMERIC |  | For charge transactions, the quantity. |
| 47 | `REFERENCE_NUM` | VARCHAR |  | The payment posting reference number associated with a transaction. |
| 48 | `UB_REV_CODE_ID` | NUMERIC | FK→ | The revenue code associated with a charge transaction. This could come from the procedure master file or from a user-entered override. |
| 49 | `UB_REV_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 50 | `REVENUE_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 51 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 52 | `SERVICE_DATE` | DATETIME |  | The service date of a charge, the deposit date of a payment, or the creation date of an adjustment. |
| 53 | `START_DATE_TIME` | DATETIME (UTC) |  | For charge transactions that result from timed procedures, the start date and time stored in the transaction. |
| 54 | `STOP_DATE_TIME` | DATETIME (UTC) |  | For charge transactions that result from timed procedures, the end date and time stored in the transaction. |
| 55 | `TEMP_TX_ID` | NUMERIC |  | The ID number of the temporary transaction (HTT record) associated with the transaction in question. |
| 56 | `TOTAL_CHARGES_ACT` | NUMERIC |  | For adjustment transactions that move liability from one bucket to another, the total monetary amount of charges on the latter bucket. |
| 57 | `TX_AMOUNT` | NUMERIC |  | The monetary amount of a transaction. |
| 58 | `TX_COMMENT` | VARCHAR |  | A comment associated with a transaction. |
| 59 | `TX_FILED_TIME` | DATETIME (Local) |  | The date and time when a transaction was filed on a hospital account. |
| 60 | `TX_NUM_IN_HOSPACCT` | INTEGER |  | A number denoting in what order the transaction filed on the hospital account. For example, if the transaction in question was the third transaction to file on the account, this column would contain the number 3. |
| 61 | `TX_POST_DATE` | DATETIME |  | The date on which the transaction was posted. |
| 62 | `TX_SOURCE_HA_C_NAME` | VARCHAR |  | The source of the transaction, i.e. unit charge entry, payment posting, electronic remittance, |
| 63 | `TX_TYPE_HA_C_NAME` | VARCHAR |  | The transaction type, i.e. charge, payment, debit adjustment, or credit adjustment. |
| 64 | `TYPE_OF_SVC_HA_C_NAME` | VARCHAR | org | The type of service associated with a transaction. |
| 65 | `USER_ID` | VARCHAR | FK→ | This column stores the unique identifier for the user who posted the hospital billing transaction. |
| 66 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 67 | `XFER_LIAB_ADJ_YN` | VARCHAR |  | Y/N flag denoting if the transaction transfers the liability adjustment. |
| 68 | `CHG_CRED_ORIG_ID` | NUMERIC |  | This column stores the unique identifier for the transaction of a late charge credit. |
| 69 | `LATE_CRCTN_ORIG_ID` | NUMERIC |  | This column stores the unique identifier for the original charge for a late charge correction transaction. |
| 70 | `ALLOWANCE_ADJ_YN` | VARCHAR |  | Y/N flag indicating if there is an allowance adjustment. |
| 71 | `PLACE_OF_SVC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 72 | `NON_COVERED_YN` | VARCHAR |  | Indicates whether the transaction is expected to be a non-covered charge. |
| 73 | `BEN_BKT_CVG_ID` | NUMERIC |  | This column stores the unique identifier for the benefit bucket associated with the hospital billing transaction. |
| 74 | `BEN_BKT_INC_STR` | VARCHAR |  | The increment string for the benefit bucket associated with the transaction. |
| 75 | `QUICK_PMT_TYPE_C_NAME` | VARCHAR | org | The quick payment type category ID for the transaction. |
| 76 | `NON_COVERED_AMT` | NUMERIC |  | The non-covered amount associated with the transaction. |
| 77 | `IS_REFUND_ADJ_YN` | VARCHAR |  | Denotes whether this is a Refund Adjustment. |
| 78 | `INVOICE_NUM` | VARCHAR |  | The invoice number for the transaction. |
| 79 | `COLLECTION_AGENCY` | NUMERIC |  | This column stores the unique identifier for the collection agency that the hospital billing transaction has been sent to for collections. |
| 80 | `COLLECTION_AGENCY_COLL_AGENCY_NAME` | VARCHAR |  | The name of the collection agency. |
| 81 | `PRIMARY_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 82 | `HCPCS_CODE` | VARCHAR |  | The override CPT™ or HCPCS code either entered manually during charge entry or coming from the clinical application. Often, pharmacy and supply charges will have a code sent from the clinical system to override the code stored on the procedure. When reporting, you will often want to display this column if it is populated, otherwise display CPT_CODE. |
| 83 | `NDC_ID` | VARCHAR | FK→ | This column stores the unique identifier for the historical National Drug Code for the corresponding charge. This column will only be set for certain charges posted prior to being on the Epic Summer 2009 release. For current NDC code information, use NDC_CODE_RG_ID column in the HSP_TX_NDC_CODES table. |
| 84 | `NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 85 | `HIPPS_CODE` | VARCHAR |  | HIPPS Code for this transaction. |
| 86 | `HIPPS_CODE_TYPE_C_NAME` | VARCHAR |  | HIPPS Code type for this transaction. i.e. 1-Skilled Nursing Facility 2-Home Health PPS 99-other |
| 87 | `HIPPS_CODE_DESC` | VARCHAR |  | HIPPS Code description for this transaction. |
| 88 | `RFND_SND_TO_C_NAME` | VARCHAR |  | This column specifies where to send the refund should there be a credit balance on the hospital billing transaction: 1-Coverage, 2-Guarantor, 3-Patient, 4-Custom Payee, 5-Address Override, 6-Payor, or 7-Plan. |
| 89 | `RFND_GUAR_ID` | NUMERIC |  | This column stores the unique identifier for the guarantor associated with the refund code on the hospital billing transaction. |
| 90 | `RFND_COVERAGE_ID` | NUMERIC |  | This column stores the unique identifier for the coverage associated with the refund code on the hospital billing transaction. |
| 91 | `REFUND_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 92 | `RECONCILIATION_NUM` | VARCHAR |  | Reconciliation number from a remittance run. |
| 93 | `RFND_CUST_PAYEE_C_NAME` | VARCHAR | org | The custom payee for the refund (no system-released values). |
| 94 | `CE_SRC_DEP_ID` | VARCHAR |  | This column stores the unique identifier for the source deployment of the transaction. This identifies the location where the hospital billing transaction originated. This will have a value of null unless the transaction's deployment of origination and the home deployment are different. |
| 95 | `CE_POST_DT` | DATETIME |  | The post date for the transaction. This will have a value of null unless the transaction's deployment of origination and the home deployment are different. |
| 96 | `CE_FILED_TIME` | DATETIME |  | The date and time that the transaction was filed. This will have a value of null unless the transaction's deployment of origination and the home deployment are different. |
| 97 | `CE_HM_OFF_TXTYP_C_NAME` | VARCHAR |  | The type of transaction that took place. This will have a value of null unless the transaction's deployment of origination and the home deployment are different. Some example values for this field are as follows: 1 - charge, 2 - payment, 3 - debit adjustment, 4 - credit adjustment. |
| 98 | `POS_SESSIONID` | VARCHAR |  | This column stores the unique identifier for the Point of Sale session. |
| 99 | `POS_TXID` | VARCHAR |  | This column stores the unique identifier for the Point of Sale transaction. |
| 100 | `POS_TX_LINE` | NUMERIC |  | The Point of Sale transaction line number. |
| 101 | `ORIG_ETR_ID` | NUMERIC |  | This column stores the unique identifier for the Professional Billing transaction that was the transfer source for this Hospital Billing transaction. |
| 102 | `EXTERN_AR_FLAG_YN` | VARCHAR |  | External A/R Flag. This flag determines if an transaction's A/R is to be counted as belonging to an external agency (i.e., as bad debt). This flag is copied from the hospital account level flag. This flag is only used if external agency A/R has been enabled. |
| 103 | `ERX_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 104 | `SUP_ID` | VARCHAR |  | This column stores the unique identifier for the hospital billing transaction. |
| 105 | `SUP_ID_SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |
| 106 | `BAD_DEBT_FLAG_YN` | VARCHAR |  | Bad Debt Flag. This flag determines if a transaction's amount is to be counted as belonging to a bad debt agency. This flag is copied from the hospital account level flag. This flag is only used if account-based bad debt is used. This flag will be set to 'Y' if the account is in bad debt, 'N' otherwise. |
| 107 | `PMT_RECEIPT_NO` | VARCHAR |  | Stores the receipt number for a receipt printed during payment posting. |
| 108 | `RFND_AP_DATE` | DATETIME |  | Stores the date on which the A/P system approved and processed the transaction. |
| 109 | `RFND_AP_STATUS_C_NAME` | VARCHAR |  | Stores the action taken by the A/P system when it processed the transaction. |
| 110 | `OPTIME_LOG_ID` | VARCHAR |  | This column stores the unique identifier for the OpTime log associated with the hospital billing transaction. |
| 111 | `INI_FILE_ATTEMPT_DT` | DATETIME |  | Item to represent the date when the first attempt to file the transaction was made. |
| 112 | `RELATED_HTR_ID` | NUMERIC |  | This column stores the unique identifier of the related hospital billing (HB) transaction for this HB transaction. This will map to a HB transaction that is associated with the related hospital account. |
| 113 | `IMD_ID` | VARCHAR |  | This column stores the unique identifier for the image associated with this hospital billing transaction. |
| 114 | `DURATION_MINUTES` | INTEGER |  | This column contains the duration of service in minutes. |
| 115 | `EB_PMT_HAR_RES_YN` | VARCHAR |  | Indicates whether hospital account restrictions are used. |
| 116 | `PMT_HAR_DIS_FROM_DT` | DATETIME |  | The hospital account restriction discharge from date. |
| 117 | `PMT_HAR_DIS_TO_DT` | DATETIME |  | The hospital account restriction discharge to date. |
| 118 | `OVERRIDE_XOVER_YN` | VARCHAR |  | Indicates whether this payment contained override crossover information. |
| 119 | `RESEARCH_STUDY_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 120 | `RSH_CHG_ORIG_HAR_ID` | NUMERIC |  | This column stores the unique identifier for the original hospital account for a research charge. |
| 121 | `PAYMENT_NOT_ALLOWED` | NUMERIC |  | This column contains the not-allowed amount on the payment transaction. |
| 122 | `EB_PMT_TOTAL_AMOUNT` | VARCHAR |  | This column contains the original payment amount. Original payment amount is the amount of the payment prior to getting split in split cases and if the payment is not split, then the original payment amount is the full payment of the transaction. |
| 123 | `EB_PMT_POST_TYPE_C_NAME` | VARCHAR | org | The type category number of the post type used to post the enterprise payment. |
| 124 | `EB_PREPMT_POST_TP_C_NAME` | VARCHAR | org | The type category number for the pre-payment post type associated with this transaction. |
| 125 | `PANEL_DT` | DATETIME |  | The contact date of the panel procedure that is associated with this transaction. |
| 126 | `MEA_ID_C_NAME` | VARCHAR | org | Measurement reference ID code. |
| 127 | `PANEL_DAT` | FLOAT |  | The contact date of the panel procedure that is associated with this transaction, in decimal format. Used to link with the CLARITY_EAP_OT table. |
| 128 | `ELEC_PMT_APRVL_CODE` | VARCHAR |  | This column stores the unique identifier for the hospital billing transaction sent back by the merchant. |
| 129 | `ELEC_PMT_INST_TIME` | DATETIME (UTC) |  | Instant of when the payment was approved |
| 130 | `IMPLANT_ID` | VARCHAR | shared | This column stores the unique identifier for the implant record associated with this procedure. |
| 131 | `LINKED_HTR_ID` | NUMERIC |  | This item links two hospital billing transactions in the system. These transactions will be reversed and transferred at the same time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |
| `NDC_ID` | [RX_NDC](RX_NDC.md) | sole_pk | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `UB_REV_CODE_ID` | [CL_UB_REV_CODE](CL_UB_REV_CODE.md) | sole_pk | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

