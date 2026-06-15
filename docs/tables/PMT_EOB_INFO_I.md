# PMT_EOB_INFO_I

> The PMT_EOB_INFO_I table contains the Explanation of Benefits information given a transaction ID. It contains data that is not multiple response given a transaction ID.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 40

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier associated with the transaction for this row. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PEOB_TX_ID` | NUMERIC |  | The transaction ID of the matching charge. |
| 4 | `CVD_AMT` | NUMERIC |  | The covered amount for that transaction. |
| 5 | `NONCVD_AMT` | NUMERIC |  | The non-covered amount for that transaction. |
| 6 | `DED_AMT` | NUMERIC |  | The deducted amount for that transaction. |
| 7 | `COPAY_AMT` | NUMERIC |  | The copay amount for that transaction. |
| 8 | `COINS_AMT` | NUMERIC |  | The coinsurance amount for that transaction. |
| 9 | `COB_AMT` | NUMERIC |  | The Coordination of Benefits amount for that transaction. |
| 10 | `PAID_AMT` | NUMERIC |  | The paid amount for that transaction. |
| 11 | `ICN` | VARCHAR |  | The internal control number for that transaction. |
| 12 | `DENIAL_CODES` | VARCHAR |  | The denial code for the transaction. |
| 13 | `PEOB_ACTION_NAME_C_NAME` | VARCHAR |  | The Explanation Of Benefits action category ID for the transaction. |
| 14 | `ACTION_AMT` | NUMERIC |  | The action amount for this transaction. |
| 15 | `ACCOUNT_ID` | NUMERIC | FK→ | The Account Id of the transfer to self-pay action or next responsible party to self-pay action performed in insurance payment posting. |
| 16 | `COVERAGE_ID` | NUMERIC | FK→ | The Action Coverage of the next responsible party action or resubmit insurance action performed in insurance payment posting. |
| 17 | `ACTION_ASN_NAME_C_NAME` | VARCHAR |  | The action assignment category ID for the transaction. |
| 18 | `COMMENTS` | VARCHAR |  | The comments associated the Explanation of Benefits for a transaction. |
| 19 | `INFO_LINES` | VARCHAR |  | The info lines in PMT_EOB_INFO_II. |
| 20 | `WIN_DENIAL_ID` | VARCHAR |  | The winning denial remittance code. |
| 21 | `WIN_DENIAL_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 22 | `ACTION_EOB` | VARCHAR |  | The Explanation of Benefits code for actions (next responsible party or resubmit) in payment posting associated with the transaction. |
| 23 | `INVOICE_NUM` | VARCHAR |  | The invoice number for the transaction. |
| 24 | `SUMMARY` | VARCHAR |  | Contains any paid, adjustment, copay, coinsurance, or allowed amount for a transaction. |
| 25 | `TX_MATCH_DATE` | DATETIME |  | The date when the charge was matched to the payment. |
| 26 | `CROSSOVER_C_NAME` | VARCHAR |  | Indicates the crossover scenario of this payment transaction at the time of payment posting. The crossover scenario value describes whether this payment transaction is a regular payment, a primary payment (and whether or not the crossover payor has paid), or a crossover payment (and whether or not the primary payor has paid). |
| 27 | `NON_PRIMARY_SYS_YN` | VARCHAR |  | Indicates whether the system determines this payment transaction as a non-primary payment at the time of payment posting based on crossover information, invoice information, and previous payments information. Y indicates the system determines this payment transaction as a non-primary payment at the time of payment posting based on crossover information, invoice information, and previous payments information. A null value indicates the system does not determine this payment transaction as a non-primary payment at the time of payment posting based on crossover information, invoice information, and previous payments information. |
| 28 | `NON_PRIMARY_USR_YN` | VARCHAR |  | Indicates whether the user determines this payment transaction as a non-primary payment at the time of payment posting. The value of the Non-primary posting (user) is usually the same as the system determined non-primary posting value. However, users can override the system determined non-primary posting value based on the EOB information. Y indicates the user determines this payment transaction as a non-primary payment at the time of payment posting. |
| 29 | `PEOB_ACTION_C_NAME` | VARCHAR |  | Indicates the Next Responsible Party, Resubmit Insurance or Transfer to Self-Pay action taken on the charge. |
| 30 | `INV_ID` | NUMERIC |  | Invoice ID that is associated with one payment Explanation of Benefits line. Use this field along with INV_LINE to link to the proper record in the INV_CLM_LN_ADDL table. |
| 31 | `INV_LINE` | INTEGER |  | Line count of one invoice record for internal calculation use. It is different from claim form line. Use this field along with INV_ID to link to the associated record in the INV_CLM_LN_ADDL table. |
| 32 | `NO_MATCHED_CHGS_YN` | VARCHAR |  | This column is set to Y when all charges associated with this EOB line have been unmatched from the payment. |
| 33 | `PEOB_ACCOUNT_ID` | NUMERIC |  | The ID of the guarantor on the invoice associated with the payment. If there is no associated invoice, this column stores the ID of the guarantor from the charge. |
| 34 | `PEOB_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 35 | `PEOB_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 36 | `PEOB_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 37 | `PEOB_BILL_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 38 | `PEOB_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 39 | `PEOB_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 40 | `PEOB_MTCH_CHG_TX_ID` | NUMERIC |  | The ID of the first matching charge transaction on the invoice associated with the payment. If there is no associated invoice, this column stores the ID of the charge from the Explanation of Benefits master file. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

