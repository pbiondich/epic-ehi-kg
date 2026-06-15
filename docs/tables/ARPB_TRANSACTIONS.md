# ARPB_TRANSACTIONS

> This table contains information about professional billing transactions.

**Primary key:** `TX_ID`  
**Columns:** 67  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | A transaction's unique internal identification number. A patient's record can include charges, payments, or adjustments and the patient's account balance will reflect these transactions. |
| 2 | `POST_DATE` | DATETIME |  | The date when a transaction is entered into the billing system. This differs from the service date, which is the date when the service was performed. |
| 3 | `SERVICE_DATE` | DATETIME |  | The date a medical service is performed. |
| 4 | `TX_TYPE_C_NAME` | VARCHAR |  | The type of this transaction: Charge, payment or adjustment. |
| 5 | `ACCOUNT_ID` | NUMERIC | FK→ | The internal ID of the record that maintains the patient's transactions. A patient may use more than one account and an account may contain more than one patient. |
| 6 | `DEBIT_CREDIT_FLAG_NAME` | VARCHAR |  | This column contains a 1 if the transaction is a debit and a -1 if the transaction is a credit. A charge is always a debit, a payment is always a credit, and an adjustment can be either a debit or a credit. |
| 7 | `SERV_PROVIDER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `BILLING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 9 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 10 | `POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 11 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 12 | `SERVICE_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 13 | `MODIFIER_ONE` | VARCHAR |  | The first procedure modifier associated with this transaction. This is the external modifier, as it would be printed on the claim. |
| 14 | `MODIFIER_TWO` | VARCHAR |  | The second procedure modifier associated with this transaction. This is the external modifier, as it would be printed on the claim. |
| 15 | `MODIFIER_THREE` | VARCHAR |  | The third procedure modifier associated with this transaction. This is the external modifier, as it would be printed on the claim. |
| 16 | `MODIFIER_FOUR` | VARCHAR |  | The fourth procedure modifier associated with this transaction. This is the external modifier, as it would be printed on the claim. |
| 17 | `PRIMARY_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 18 | `DX_TWO_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 19 | `DX_THREE_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 20 | `DX_FOUR_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 21 | `DX_FIVE_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 22 | `DX_SIX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 23 | `PROCEDURE_QUANTITY` | NUMERIC |  | The quantity as entered in Charge Entry for the procedure of this transaction (TX_ID). If the row has a DETAIL_TYPE value of 10-13, this column displays a negative value. If the row has a DETAIL_TYPE value of 20-33, 43-45, 50, or 51, this column displays a zero. |
| 24 | `AMOUNT` | NUMERIC |  | The original amount of this transaction. |
| 25 | `OUTSTANDING_AMT` | NUMERIC |  | The outstanding amount of the transaction. |
| 26 | `INSURANCE_AMT` | NUMERIC |  | The insurance portion of the transaction. |
| 27 | `PATIENT_AMT` | NUMERIC |  | The patient or self-pay portion of the transaction. |
| 28 | `VOID_DATE` | DATETIME |  | If this transaction is voided, this column will have the date in which this transaction is voided. |
| 29 | `LAST_ACTION_DATE` | DATETIME |  | This column contains the most recent date when an action is performed on this transaction. |
| 30 | `PROV_SPECIALTY_C_NAME` | VARCHAR | org | This column contains the provider specialty of the provider associated with the transaction. The procedure category of the charge on the transaction may affect what specialty is recorded here and in the "Encounter Specialty" displayed in Hyperspace. |
| 31 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 32 | `TOTAL_MATCH_AMT` | NUMERIC |  | This column contains the total amount matched to the transaction, including adjustments. |
| 33 | `TOTAL_MTCH_INS_AMT` | NUMERIC |  | This column contains the total insurance amount matched to the transaction, including adjustments. |
| 34 | `TOTAL_MTCH_ADJ` | NUMERIC |  | This column contains the total adjustment amount matched to the transaction. |
| 35 | `TOTAL_MTCH_INS_ADJ` | NUMERIC |  | This column contains the total insurance adjustment amount matched to the transaction. |
| 36 | `REPOST_ETR_ID` | NUMERIC |  | This is the repost source transaction. |
| 37 | `REPOST_TYPE_C_NAME` | VARCHAR |  | The repost type category ID for the transaction. |
| 38 | `DISCOUNT_TYPE_C_NAME` | VARCHAR | org | The discount type category ID for the transaction. |
| 39 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The Contact Serial Number for the patient encounter with which this transaction is associated. This number is unique across all patients and encounters in your system. |
| 40 | `ENC_FORM_NUM` | VARCHAR |  | The encounter form number corresponding to the charge transaction. If you are not using encounter forms, a negative number is stored in this item. |
| 41 | `BEN_SELF_PAY_AMT` | NUMERIC |  | Stores the adjudicated self-pay amount calculated by the benefits engine |
| 42 | `BEN_ADJ_COPAY_AMT` | NUMERIC |  | Stores the copay part of the adjudicated self-pay amount calculated by the benefits engine |
| 43 | `BEN_ADJ_COINS_AMT` | NUMERIC |  | Stores the coinsurance part of the adjudicated self-pay amount calculated by the benefits engine |
| 44 | `VISIT_NUMBER` | VARCHAR |  | This item stores the visit number for this transaction. |
| 45 | `REFERRAL_ID` | NUMERIC | FK→ | This item stores the Referral (RFL) ID for this transaction. |
| 46 | `ORIGINAL_EPM_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 47 | `ORIGINAL_FC_C_NAME` | VARCHAR | org | This item stores the original financial class for this transaction. |
| 48 | `ORIGINAL_CVG_ID` | NUMERIC |  | This item stores the original coverage (CVG) ID for this transaction. |
| 49 | `PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 50 | `COVERAGE_ID` | NUMERIC | FK→ | This item stores the current coverage (CVG) ID for this transaction. |
| 51 | `ASGN_YN` | VARCHAR |  | This item stores the assignment flag for a coverage. This item is set to Yes if the charge is currently assigned to the payor in the PAYOR_ID column. |
| 52 | `FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 53 | `PAYMENT_SOURCE_C_NAME` | VARCHAR | org | This item stores the payment source for credit transactions. This is a list of possible sources including Cash, Check, Credit Card, etc. |
| 54 | `USER_ID` | VARCHAR | FK→ | This item stores the user who posted the transaction. |
| 55 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 56 | `NOT_BILL_INS_YN` | VARCHAR |  | Indicates whether the transaction is marked for do not bill insurance. |
| 57 | `CHG_ROUTER_SRC_ID` | VARCHAR |  | This item stores the universal charge line (UCL) ID for this transaction. |
| 58 | `RECEIVE_DATE` | DATETIME |  | This item stores the charge entry batch receive date. |
| 59 | `CE_CODED_DATE` | DATETIME |  | The date this charge session was coded, from charge entry. |
| 60 | `PANEL_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 61 | `BILL_AREA_ID` | NUMERIC | FK→ | Networked to BIL: the Bill Area for this transaction. |
| 62 | `BILL_AREA_ID_BILL_AREA_NAME` | VARCHAR |  | The record name of this bill area, financial subdivision, or financial division. |
| 63 | `CREDIT_SRC_MODULE_C_NAME` | VARCHAR |  | The module that creates a payment or credit adjustment |
| 64 | `UPDATE_DATE` | DATETIME (Local) |  | The date that this row was last updated. |
| 65 | `CLAIM_DATE` | DATETIME |  | The most recent date that this transaction has been on an accepted claim run. |
| 66 | `IPP_INV_NUMBER` | VARCHAR |  | This item stores the original invoice number that user posts to in GUI payment posting or remittance. |
| 67 | `IPP_INV_ID` | NUMERIC |  | This item stores the original invoice ID that user posts to in graphical user interface (GUI) payment posting or remittance. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `BILL_AREA_ID` | [V_BIL_ALL](V_BIL_ALL.md) | sole_pk | high |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

