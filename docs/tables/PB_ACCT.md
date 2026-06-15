# PB_ACCT

> Stores information about Premium Billing accounts.

**Primary key:** `PB_ACCT_ID`  
**Columns:** 23  
**Org-specific columns:** 1  
**Joined by:** 19 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_ACCT_ID` | VARCHAR | PK | The unique ID for the premium billing account. |
| 2 | `ACCOUNT_NAME` | VARCHAR |  | Name for the premium billing account. |
| 3 | `PBA_REC_STAT_C_NAME` | VARCHAR |  | Displays the status of the premium billing account record (i.e. active or deleted). |
| 4 | `EXT_IDENT` | VARCHAR |  | External ID for the premium billing account. |
| 5 | `PB_FORMAT_ID` | VARCHAR | FK→ | The unique ID for the premium billing invoice format that is used when printing premium billing invoices for the premium billing account. |
| 6 | `PB_FORMAT_ID_FORMAT_NAME` | VARCHAR |  | Name of the premium billing invoice format |
| 7 | `DELINQUENCY_DATE` | DATETIME |  | Date the premium billing account was last delinquent. |
| 8 | `DELINQUENT_STAT_C_NAME` | VARCHAR | org | Delinquency status of the premium billing account. |
| 9 | `DELINQ_PB_INVC_ID` | VARCHAR |  | The unique ID for the last invoice for which the premium billing account was delinquent. |
| 10 | `POST_PMT_ON_INV_YN` | VARCHAR |  | This Yes/No flag indicates whether payments should automatically be posted to the premium billing account when the premium billing account is invoiced. |
| 11 | `INDIVIDUAL_BILL_YN` | VARCHAR |  | This Yes/No flag indicates whether this account is an individual billing account. |
| 12 | `UPDATE_DATE` | DATETIME (Local) |  | The extract date and time of the record for this table. |
| 13 | `OWNING_BUSSEG_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 14 | `AUTO_PAY_ACTIVE_YN` | VARCHAR |  | Indicates whether auto pay is currently active for this account. Y is stored if it is active, N otherwise. |
| 15 | `AUTO_PAY_CARD_ID` | NUMERIC |  | Stores the unique identifier of the payment card currently being used for auto pay. |
| 16 | `AUTO_PAY_PAYMENT_DAY` | INTEGER |  | Stores the day of the month auto pay is currently scheduled to occur on. |
| 17 | `AUTO_PAY_NEXT_PAYMENT_DATE` | DATETIME |  | Stores the next date auto pay is currently scheduled to occur on. |
| 18 | `ORIGINAL_SUBSCRIBER_PAT_ID` | VARCHAR | FK→ | Stores the original subscriber that an individual account was created for. |
| 19 | `BUCKET_STATUS_C_NAME` | VARCHAR |  | The account status represents the overall state of an account. This is composite of the premium bucket statuses for the buckets on an account. An account with a status of "New" does not have any transactions filed to it. An account with a status of "Open - Unreconciled" as at least one bucket that has a status of "Open - Unreconciled". An account with the status of "Open - Reconciled" has been fully reconciled and contains transactions that have not been invoiced. An account with a status of "Closed" has all buckets reconciled and invoiced. |
| 20 | `ASGN_COLL_USER_ID` | VARCHAR |  | This is the user that is assigned to this account to track and manage their collections process. |
| 21 | `ASGN_COLL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 22 | `SEC_PB_FORMAT_ID` | VARCHAR |  | The override setting for the secondary paper invoice format that will be used on the account. |
| 23 | `SEC_PB_FORMAT_ID_FORMAT_NAME` | VARCHAR |  | Name of the premium billing invoice format |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORIGINAL_SUBSCRIBER_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `PB_FORMAT_ID` | [PB_FORMAT](PB_FORMAT.md) | sole_pk | high |

## Joined in — referenced by (19)

| From | Column | Confidence |
|------|--------|------------|
| [COVERAGE](COVERAGE.md) | `PB_ACCT_ID` | high |
| [DELINQUENCY_HISTORY](DELINQUENCY_HISTORY.md) | `PB_ACCT_ID` | high |
| [MC_NOTIFICATIONS](MC_NOTIFICATIONS.md) | `PB_ACCT_ID` | high |
| [PBI_ALL](PBI_ALL.md) | `PB_ACCT_ID` | high |
| [PB_ACCT_AUTO_PAY_HX](PB_ACCT_AUTO_PAY_HX.md) | `PB_ACCT_ID` | high |
| [PB_ACCT_BILLING_ADDR](PB_ACCT_BILLING_ADDR.md) | `PB_ACCT_ID` | high |
| [PB_ACCT_TX](PB_ACCT_TX.md) | `PB_ACCT_ID` | high |
| [PB_ACCT_TYPE](PB_ACCT_TYPE.md) | `PB_ACCT_ID` | high |
| [PB_COLL_HX_NOTE_TBL](PB_COLL_HX_NOTE_TBL.md) | `PB_ACCT_ID` | high |
| [PB_COLL_PROCESS_TBL](PB_COLL_PROCESS_TBL.md) | `PB_ACCT_ID` | high |
| [PB_COLL_PROC_TXS](PB_COLL_PROC_TXS.md) | `PB_ACCT_ID` | high |
| [PB_COLL_STEP_HX_TBL](PB_COLL_STEP_HX_TBL.md) | `PB_ACCT_ID` | high |
| [PB_COLL_STEP_HX_TXS](PB_COLL_STEP_HX_TXS.md) | `PB_ACCT_ID` | high |
| [PB_DTL_TX](PB_DTL_TX.md) | `PB_ACCT_ID` | high |
| [PB_INVOICE](PB_INVOICE.md) | `PB_ACCT_ID` | high |
| [PB_TX_SET](PB_TX_SET.md) | `PB_ACCT_ID` | high |
| [V_EHI_PBA_NOTES_MC_PBA](V_EHI_PBA_NOTES_MC_PBA.md) | `PB_ACCT_ID` | high |
| [V_EHI_PBA_PB_ACCT](V_EHI_PBA_PB_ACCT.md) | `PB_ACCT_ID` | high |
| [V_EHI_PBA_PB_ACCT_ELEC_NT_HX](V_EHI_PBA_PB_ACCT_ELEC_NT_HX.md) | `PB_ACCT_ID` | high |

