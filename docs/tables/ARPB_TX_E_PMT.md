# ARPB_TX_E_PMT

> Contains information on electronically made payments.

**Primary key:** `TX_ID`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `RESPONSE_TAG` | VARCHAR |  | Authorization code sent back by the merchant |
| 3 | `APPROVAL_CODE` | VARCHAR |  | Transaction ID sent back by the merchant |
| 4 | `PMT_INSTANT_DTTM` | DATETIME (Local) |  | Instant at which the electronic payment was made. |
| 5 | `CARD_BRAND_C_NAME` | VARCHAR | org | The card brand category ID used for the transaction. |
| 6 | `TOKEN_NICKNAME` | VARCHAR |  | A helpful name to identify the payment method. |
| 7 | `ACCT_HOLDER_NAME` | VARCHAR |  | The name of the credit card account holder or bank account holder. |
| 8 | `LAST_4_DIGITS` | VARCHAR |  | The last 4 digits of the card or bank account used for the transaction. |
| 9 | `BANK_ACCT_TYPE_C_NAME` | VARCHAR |  | The bank account type for bank account transactions. |
| 10 | `DIGITAL_WALLET_C_NAME` | VARCHAR |  | Holds the digital wallet used for an electronic payment. Stored on payments made from a digital wallet and on reversals. This item is not stored on refund transactions. |
| 11 | `SAVED_PMT_DIGITAL_WALLET_C_NAME` | VARCHAR |  | Holds the digital wallet of the saved payment method used to make the payment |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

