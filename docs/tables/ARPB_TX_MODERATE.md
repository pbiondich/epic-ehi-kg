# ARPB_TX_MODERATE

> This table has one row per ETR record and contains additional information about Professional Billing transactions. This table can be considered an extension table of ARPB_TRANSACTIONS.

**Primary key:** `TX_ID`  
**Columns:** 68  
**Org-specific columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `ORIGINATING_TAR_ID` | NUMERIC |  | This item holds the originating temporary transaction ID for this transaction. If the transaction is a charge, then the originating temporary transaction ID will be the temporary transaction ID of the charge. If transaction is a payment, then the originating temporary transaction ID will be the payment temporary transaction ID unless the payment is from fast payment. In the fast payment case, the originating temporary transaction ID will be the charge temporary transaction ID. |
| 3 | `SOURCE_TAR_ID` | NUMERIC |  | This item holds the source temporary transaction ID for this transaction. The source temporary transaction ID will always be equal to the temporary transaction ID that generates the transaction. |
| 4 | `SRC_TAR_CHG_LINE` | INTEGER |  | Indicates the temporary transaction charge line this transaction originated from. |
| 5 | `PAT_AGING_DATE` | DATETIME |  | Aging date used for self-pay aged A/R |
| 6 | `INS_AGING_DATE` | DATETIME |  | Aging date used for insurance aged A/R |
| 7 | `HOSP_ACCT_ID` | NUMERIC |  | This item stores the hospital account record ID for the transaction. |
| 8 | `ORDER_ID` | NUMERIC | shared | The unique ID of the order record that triggered this transaction. This item is not always populated if you use the Charge Router. |
| 9 | `EXT_REF_NUM` | VARCHAR |  | External reference number. This is a customer item that can be populated as they see fit. Typically, this item is populated with data from an external system via an interface or transaction import. |
| 10 | `REFERENCE_NUM` | VARCHAR |  | This item stores the reference number (check number) for a payment transaction. |
| 11 | `PMT_RECEIPT_NUM` | VARCHAR |  | This item stores the receipt number for a payment transaction. |
| 12 | `PAT_TYPE_C_NAME` | VARCHAR | org | This item stores the patient type for the patient on this transaction. |
| 13 | `REFERRAL_PROV_ID` | VARCHAR |  | This stores this transaction's referral provider. Note that this field is linked to the referral source master file and not the provider master file. |
| 14 | `REFERRAL_PROV_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 15 | `INSURANCE_AMT_PAID` | NUMERIC |  | This item stores the insurance amount that has been paid on a charge transaction. |
| 16 | `WRITEOFF_EXCEPT_C_NAME` | VARCHAR |  | The Yes-No write-off category number for a charge transaction. The value indicates whether the charge transaction was adjudicated as a write-off in charge entry and thus the insurance portion write-off is suppressed. |
| 17 | `PAT_LOCATION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 18 | `ORIG_PRICE` | NUMERIC |  | This item stores the original price of the transaction if the price was changed during charge entry. |
| 19 | `EXP_REIMB_DYNAMIC` | NUMERIC |  | The expected reimbursement will be updated whenever reimbursement is calculated. This amount cannot exceed the charge amount. |
| 20 | `EXPECTED_REIMB` | NUMERIC |  | The expected reimbursement calculated at charge entry. This item is not updated by any change during claims. Also, this amount cannot exceed the charge amount. |
| 21 | `COVERAGE_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 22 | `CVG_PLAN_GROUP_ID` | VARCHAR |  | This item stores the employer group (PPG) ID that is associated with this transaction. |
| 23 | `CVG_PLAN_GROUP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |
| 24 | `MED_NEC_YN` | VARCHAR |  | This is the flag that is set in charge entry if medical necessity is needed for a transaction. |
| 25 | `TECHNICAL_CHG_FL_YN` | VARCHAR |  | This flag is set to yes if the transaction is a technical charge. This is only populated if using the split billing functionality. |
| 26 | `CNTR_DISCOUNT_AMT` | VARCHAR |  | This item stores the pricing contract discount amount for a transaction. |
| 27 | `UNDIST_TX_DATE` | DATETIME |  | This items stores the date that a transaction was undistributed (unmatched). |
| 28 | `UNDIST_CHG_USER_ID` | VARCHAR |  | This item stores the user that unmatched a transaction. |
| 29 | `UNDIST_CHG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 30 | `UNDIST_INSTANT` | DATETIME (Local) |  | This item stores the instant that a transaction was undistributed (unmatched). |
| 31 | `ORIGINAL_AMT_COPAY` | NUMERIC |  | This item stores the original copay amount for the transaction. |
| 32 | `BAD_DEBT_CHG_YN` | VARCHAR |  | Indicates whether the charges is written off to bad debt. |
| 33 | `AUTO_PAT_WO_C_NAME` | VARCHAR |  | This item stores if a transaction had its self-pay portion automatically written off. |
| 34 | `TX_USER_COMMENT` | VARCHAR |  | The comments entered by users when they perform an action like transfer, retro, void, and undistribute on a transaction in Transaction Inquiry are stored in this item. |
| 35 | `CONTESTED_YN` | VARCHAR |  | This item stores a flag to determine if a transaction is contested. |
| 36 | `CONTEST_REASON_C_NAME` | VARCHAR | org | This item stores the reason that a transaction is contested if the transaction is contested. |
| 37 | `MEA_IDENTIFIER_C_NAME` | VARCHAR | org | This item stores the measurement (MEA) identifiers that are entered in charge entry. |
| 38 | `CRC_CODE_C_NAME` | VARCHAR | org | This item stores the CRC code entered in charge entry. |
| 39 | `REIMB_CONTRACT_AMT` | NUMERIC |  | Stores the allowed amount as calculated by the reimbursement contract. This amount can exceed the charge amount. |
| 40 | `EXT_CUR_AGENCY_ID` | NUMERIC |  | The current collections agency. |
| 41 | `EXT_CUR_AGENCY_ID_COLL_AGENCY_NAME` | VARCHAR |  | The name of the collection agency. |
| 42 | `EXT_CURAGNCY_STAT_C_NAME` | VARCHAR |  | The current agency status category ID for the transaction. |
| 43 | `EXTERNAL_ID` | VARCHAR |  | This item stores the external transaction ID |
| 44 | `SURGICAL_LOG_ID` | VARCHAR |  | The unique ID associated with the surgical log record for this row. This column is frequently used to link to the OR_LOG table. This item is populated if charge is entered from OpTime. |
| 45 | `SUPPLY_ID` | VARCHAR | FK→ | The unique ID associated with the supply record for this row. This column is frequently used to link to the OR_SPLY table. |
| 46 | `SUPPLY_ID_SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |
| 47 | `IMPLANT_ID` | VARCHAR | shared | The unique ID associated with the implant record for this row. This column is frequently used to link to the OR_IMP table. |
| 48 | `EXT_AGNCY_SENT_DTTM` | DATETIME (Local) |  | The instant the charge was sent to its current agency. |
| 49 | `FIRST_SELFPAY_DATE` | DATETIME |  | This items stores the date when a charge first goes to self-pay. |
| 50 | `PROV_TYPE_C_NAME` | VARCHAR | org | The provider type for the transaction. |
| 51 | `CLAIM_ID` | NUMERIC | FK→ | The claim record for the transaction. |
| 52 | `IS_WK_COMP` | VARCHAR |  | Indicates whether the transaction is for worker's comp. |
| 53 | `EOB_UPDATED_DT` | DATETIME |  | Date in which the Explanation of Benefits for this transaction was last updated. |
| 54 | `RAD_THER_COMP_TX_ID` | NUMERIC |  | This item stores the ID for radiation therapy component transactions and rollup charges. |
| 55 | `RAD_THER_END_YN` | VARCHAR |  | Indicates whether Radiation Therapy is at the end of treatment for this transaction. |
| 56 | `START_TIME` | DATETIME (Local) |  | Start time of a timed procedure. |
| 57 | `STOP_TIME` | DATETIME (Local) |  | Stop time of a timed procedure. |
| 58 | `SERVICE_TIME` | DATETIME (Local) |  | Time when service is performed. |
| 59 | `PURCHASESERVICE_AMT` | NUMERIC |  | This is the amount paid for or to be paid to a third party for performing a service. This field is used to report this amount on claims and statements along with price being charged to the payor or guarantor for the service. This item should only be used if it is desired this purchased service information be reported on claims and statements. |
| 60 | `THIRD_PARTY_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 61 | `MNL_RETRO_REASON_C_NAME` | VARCHAR | org | The retroadjudication reason category ID for the transaction |
| 62 | `TYPE_OF_SERVICE_C_NAME` | VARCHAR | org | The type of service category number associated with the transaction. |
| 63 | `DX_PRIM_CODESET_C_NAME` | VARCHAR | org | This item stores the primary diagnosis codeset for the transaction. |
| 64 | `DX_ALT_CODESET_C_NAME` | VARCHAR |  | This item stores the alternate diagnosis codeset for the transaction. |
| 65 | `START_DATE` | DATETIME |  | The date on which a service is started. |
| 66 | `STOP_DATE` | DATETIME |  | The date on which a service was stopped. |
| 67 | `PROC_MINUTES` | INTEGER |  | The length of time in minutes that this procedure took. |
| 68 | `CRD_CHARGE_SLIP_NO` | NUMERIC |  | The encounter form number associated with copay payments entered during scheduling. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |
| `SUPPLY_ID` | [OR_SPLY](OR_SPLY.md) | sole_pk | high |

