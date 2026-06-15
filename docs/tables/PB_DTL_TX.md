# PB_DTL_TX

> The PB_DTL_TX table contains the detailed transactions associated with a billing account transaction.

**Overflow family:** [PB_DTL_TX_2](PB_DTL_TX_2.md)  
**Primary key:** `PB_TX_ID`  
**Columns:** 60  
**Org-specific columns:** 1  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_TX_ID` | VARCHAR | PK | The unique ID of the premium billing detailed transaction. |
| 2 | `PDX_TX_TYPE_C_NAME` | VARCHAR |  | Indicates the type of the transaction (i.e. premium billing, payment, etc.) |
| 3 | `PDX_TX_SENSE_C_NAME` | VARCHAR |  | Indicates whether the transaction is a credit or debit. |
| 4 | `TX_DATE` | DATETIME |  | Date that the transaction was created in the system. |
| 5 | `EFF_DATE` | DATETIME |  | Effective date of the transaction. This date represents the first day of the coverage period being billed for the transaction. |
| 6 | `REAL_DATE` | DATETIME |  | Realization date of the transaction. This date represents the cycle date of the premium billing batch that computed this transaction. |
| 7 | `PB_ACCT_ID` | VARCHAR | FK→ | The unique ID of the premium billing account associated with the detailed transaction. |
| 8 | `AMT` | NUMERIC |  | Amount of the transaction. |
| 9 | `PB_ACT_TX_ID` | VARCHAR | shared | The unique ID of the premium billing account transaction to which the detailed transaction is associated. |
| 10 | `ACCT_POST_DATE` | DATETIME |  | Account posting date of the detailed transaction. This date represents the day that the detailed transaction was posted to the premium billing account. |
| 11 | `COVERAGE_ID` | NUMERIC | FK→ | The unique ID assigned to the coverage record. |
| 12 | `BENEFIT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 13 | `RIDER_BEN_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 14 | `SUB_PAT_ID` | VARCHAR | FK→ | The unique ID of the patient associated with the detailed transaction. |
| 15 | `NUM_MEMS` | INTEGER |  | Number of members on the coverage associated with the detailed transaction. |
| 16 | `CVG_ATTR_C_NAME` | VARCHAR | org | Coverage attributes associated with the detailed transaction. |
| 17 | `PRORATE_YN` | VARCHAR |  | Indicates whether premium is being pro-rated for the detailed transaction. |
| 18 | `PDX_PRORATE_C_NAME` | VARCHAR |  | Indicates the method used for pro-rating premium. |
| 19 | `CVG_RATE_YN` | VARCHAR |  | Indicates whether coverage rates are being used on the detailed transaction. |
| 20 | `RETRO_YN` | VARCHAR |  | Indicates whether this detailed transaction is a retroactive premium adjustments. |
| 21 | `RET_RVSL_PB_TX_ID` | VARCHAR |  | The unique ID of detailed transaction that reversed this detailed transaction. |
| 22 | `RET_ADJ_PB_TX_ID` | VARCHAR |  | The unique ID of the adjustment detailed transaction if the detailed transaction has been reversed and adjusted. |
| 23 | `RET_ORIG_PB_TX_ID` | VARCHAR |  | The unique ID of the original detailed transaction if the detailed transaction is an adjustment. |
| 24 | `CANCELS_PB_TX_ID` | VARCHAR |  | The unique ID of detailed transaction which this detailed transaction voids out. |
| 25 | `OUTSTAND_AMT` | NUMERIC |  | Outstanding amount for the detailed transaction. |
| 26 | `INIT_PB_INVC_ID` | VARCHAR |  | The unique ID of initial invoice on which the detailed transaction is included. |
| 27 | `ORG_OVPST_PB_TX_ID` | VARCHAR |  | If this detail transaction is an overpost originating from the overpayment of an existing detail transaction, then this field stores the The unique ID of the original detail transaction. |
| 28 | `PDX_CLOSE_RSN_C_NAME` | VARCHAR |  | Indicates the reason the detailed transaction was closed (paid in full or balance forward). |
| 29 | `CHNG_TYPE_C_NAME` | VARCHAR |  | Indicates the type of change associated with the detailed transaction (add, delete, or change tiers). |
| 30 | `NUMBER_OF_ADULT` | INTEGER |  | For income level billing, this field stores the number of additional adult dependents |
| 31 | `NUMBER_OF_CHILD` | INTEGER |  | For income level billing, this field stores the number of child dependents |
| 32 | `NUMBER_OF_LTJOINER` | INTEGER |  | For income level billing, this field stores the number of members identified as late joiners. |
| 33 | `PREM_SAVINGS` | NUMERIC |  | Amount of this detailed transaction that is considered savings premium. |
| 34 | `REVCLOSED_PB_TX_ID` | VARCHAR |  | When using a previously closed type of exception in payment posting, this field stores the unique ID of the detailed transaction that this transaction reverses. |
| 35 | `CLSDREVBY_PB_TX_ID` | VARCHAR |  | When using a previously closed type of exception in payment posting, this field stores the unique ID of the detailed transaction that reversed this transaction. |
| 36 | `PAIDBY_PB_TXSET_ID` | VARCHAR |  | The unique ID of the transaction set that was last used to post a payment against this transaction. |
| 37 | `SAVINGS_PDX_YN` | VARCHAR |  | Whether savings premium is included in this detailed transaction. |
| 38 | `OLD_CVG_ATTR_C_NAME` | VARCHAR |  | Old coverage attributes associated with the detailed transaction. |
| 39 | `OLD_PDX_AMOUNT` | INTEGER |  | Old amount associated with the detailed transaction. |
| 40 | `LEP_YN` | VARCHAR |  | This flag indicates if a PDX represent a Medicare Part D Late Enrollment Penalty. |
| 41 | `AR_TX_TYPE_C_NAME` | VARCHAR |  | The type of transaction. This indicates if the transaction is a charge, a payment, or an adjustment. |
| 42 | `AR_TX_CODE_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 43 | `AR_TX_AMOUNT` | NUMERIC |  | The dollar amount for a transaction. |
| 44 | `AR_TX_ACCT_PB_ACCT_ID` | VARCHAR |  | The account that this transaction is posting to. |
| 45 | `AR_TX_COVERAGE_ID` | NUMERIC |  | The coverage that this transaction applies to. |
| 46 | `AR_TX_EFF_DATE` | DATETIME |  | The effective date that this transaction applies to. |
| 47 | `AR_TX_MEMBER_PAT_ID` | VARCHAR | FK→ | The member that this transaction applies to. This applies only to per-member accounts. |
| 48 | `AR_TX_SUBSCRIBER_PAT_ID` | VARCHAR | FK→ | The subscriber that this transaction applies to. |
| 49 | `AR_TX_STATUS_C_NAME` | VARCHAR |  | The current status for a transaction. |
| 50 | `AR_TX_FILED_DATE` | DATETIME |  | The date that a transaction has filed to the system. |
| 51 | `AR_TX_REVERSED_TRANSACTION_ID` | VARCHAR |  | The transaction ID that is being reversed by a given transaction. |
| 52 | `AR_TX_CORRECTED_TRANSACTION_ID` | VARCHAR |  | The transaction ID that is being corrected by a given transaction. |
| 53 | `MEDICARE_LIS_AMOUNT` | NUMERIC |  | Amount of the part D premium that was reduced for Low Income Subsidy (LIS). |
| 54 | `PREMIUM_TYPE_C_NAME` | VARCHAR |  | Premium type of the PDX. This is used to specify specific parts of the member premium such as Medicare Part C vs Medicare Part D. |
| 55 | `WRITE_OFF_FOR_PB_ACT_TX_ID` | VARCHAR |  | Stores what account transaction (PAX) the write off is for. |
| 56 | `PB_REFUND_STATUS_C_NAME` | VARCHAR |  | This item is used to track how far along through the refunding process a certain transaction is. Approved - the refund has been created in Epic but has not been distributed to the member. Ready for Check - a check for this refund is being written manually. Refund Sent - the refund has either been processed automatically or an end user has confirmed that the refund has been sent to the member via check. Canceled - the refund was approved and has since been canceled and reversed (before being set to Refund Sent). |
| 57 | `REFUNDED_PAYMENT_ID` | VARCHAR |  | This row tracks which payment should be refunded by the refund transaction it is associated with. This is determined by looking for the payment that was used to pay off the transaction being refunded. In the case of a refund for an ad hoc adjustment this value will not be set since no original payment will be found. |
| 58 | `BILLING_CONTEXT_C_NAME` | VARCHAR |  | Specify the context of this detailed transaction. |
| 59 | `INCLUDED_IN_PB_BAT_ID` | VARCHAR |  | Specify the billing batch record that includes this PDX record. |
| 60 | `TX_COMMENT` | VARCHAR |  | Specify the description of the imported detailed transaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AR_TX_MEMBER_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `AR_TX_SUBSCRIBER_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PB_ACCT_ID` | [PB_ACCT](PB_ACCT.md) | name_stem | high |
| `SUB_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [HSP_BFH_PROF_TXS](HSP_BFH_PROF_TXS.md) | `PB_TX_ID` | high |
| [PB_DTL_TX_INVC_NUM](PB_DTL_TX_INVC_NUM.md) | `PB_TX_ID` | high |
| [PB_DTL_TX_PMT_TX](PB_DTL_TX_PMT_TX.md) | `PB_TX_ID` | high |

