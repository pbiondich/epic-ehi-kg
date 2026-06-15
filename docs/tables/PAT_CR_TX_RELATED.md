# PAT_CR_TX_RELATED

> This table contains related response information about the credit card transaction associated with an e-visit encounter that is stored in the patient record when the encounter is created.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 17  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The contact serial number is unique across all patients and all contacts. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The ID of the contact owner. |
| 6 | `CR_TX_AMOUNT_AUTH` | NUMERIC |  | The amount authorized on the credit card. |
| 7 | `CR_TX_INSTANT` | DATETIME (Local) |  | The instant the status was updated. |
| 8 | `CR_TX_STATUS_C_NAME` | VARCHAR |  | The status of the transaction. |
| 9 | `CARDHOLDER_NAME` | VARCHAR |  | To store the name of the pre-auth credit card holder . |
| 10 | `CREDIT_CARD_BRAND_C_NAME` | VARCHAR | org | To store the card brand of the pre-auth credit card |
| 11 | `EXP_MONTH` | VARCHAR |  | To store the expiration month of the pre-auth credit card |
| 12 | `EXP_YEAR` | VARCHAR |  | To store the expiration year of the pre-auth credit |
| 13 | `TX_SOURCE_C_NAME` | VARCHAR |  | Stores the transaction source application for copay only pre-authorized transactions. For example, it will store "MyChart Web" for a payment made via MyChart website. |
| 14 | `DIGITAL_WALLET_C_NAME` | VARCHAR |  | Stores the digital wallet used to make the credit card payment |
| 15 | `CR_LAST_FOUR` | VARCHAR |  | Stores the last four digits of the payment method used to make a pre-authorization for a copay. |
| 16 | `PAT_PMT_COLL_WKFL_C_NAME` | VARCHAR |  | The payment collection workflow category used by billing for reporting. See ECT-41109 for possible values. |
| 17 | `PAT_PMT_MYC_AUTH_C_NAME` | VARCHAR |  | The MyChart authentication method at the time of preauthorization. See ECT-41110 for possible values. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

