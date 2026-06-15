# HSP_ACCT_CONS_SP_PMT_ADJ

> The HSP_ACCT_CONS_SP_PMT_ADJ table contains information about the payment & adjustment documentation lines associated with a received self-pay hospital account. As a partial example, this includes common payment & adjustment information like the deposit date, reference number, description, and amount.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the hosp acct record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PMT_ADJ_UNIQUE_IDENT` | VARCHAR |  | An identifier unique to this payment/adjustment documentation line related group at the HAR level. No other payment/adjustment documentation lines on the same HAR should share this identifier. |
| 4 | `PMT_ADJ_DEPOSIT_DATE` | DATETIME |  | The deposit date for a self-pay adjustment or payment. This date is when the adjustment or payment was deposited in the source system. |
| 5 | `PMT_ADJ_POST_DATE` | DATETIME |  | The original post date for a self-pay adjustment or payment. This date is when the adjustment or payment was posted in the source system. |
| 6 | `PMT_ADJ_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 7 | `PMT_ADJ_REF_NUM` | VARCHAR |  | The reference number (e.g. check number) for an self-pay adjustment or payment. |
| 8 | `PMT_ADJ_AMOUNT` | NUMERIC |  | The credit or debit amount for an self-pay adjustment or payment. |
| 9 | `PMT_ADJ_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 10 | `PMT_ADJ_DESCRIPTION` | VARCHAR |  | A description of a self-pay adjustment or payment. Can be supplied by the source system as an override for the procedure description. |
| 11 | `PMT_ADJ_REVERSAL_DATE` | DATETIME |  | The date that this payment or adjustment documentation line was reversed. This date is set to the day the documentation line was marked as reversed by the source system. If this item is blank, then the charge has not been reversed. |
| 12 | `PMT_ADJ_ORIG_IDENT` | VARCHAR |  | An identifier for a self-pay adjustment or payment. If this is from another system, this is the ID the source system uses. If this is from the same system, this is the original transaction ID for the source service area (HTR for HB, ETR for PB). |
| 13 | `PMT_ADJ_UPDATE_DATE` | DATETIME |  | The date that this adjustment or payment documentation line was sent to the consolidated self-pay service area. This date is set to the day the documentation line was first imported from the source system. |
| 14 | `PMT_ADJ_HTR_ON_BILLING_ACCT_ID` | NUMERIC |  | If this payment/adjustment documentation line corresponds to an HB transaction posted on the insourced hospital account (for example, a patient payment that was posted directly to the target service area hospital account), this item stores a pointer to that transaction. |
| 15 | `PMT_ADJ_CONS_SP_DOCLN_STS_C_NAME` | VARCHAR |  | The current active status of the documentation line. |
| 16 | `PMT_EOB_DEDUCTIBLE_AMOUNT` | NUMERIC |  | Deductible amount from related payment transaction. |
| 17 | `PMT_EOB_COINSURANCE_AMOUNT` | NUMERIC |  | Coinsurance amount from related payment transaction. |
| 18 | `PMT_EOB_COPAY_AMOUNT` | NUMERIC |  | Copay amount from related payment transaction. |
| 19 | `PMT_EOB_NON_COVERED_AMOUNT` | NUMERIC |  | Non-covered amount from related payment transaction. |
| 20 | `PMT_ADJ_PAYER_NAME` | VARCHAR |  | The payer name for an adjustment or payment documentation line. Will fallback on I HAR 3488. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

