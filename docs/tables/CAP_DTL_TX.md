# CAP_DTL_TX

> The CAP_DTL_TX table contains capitation detailed transactions associated with received capitation files.

**Primary key:** `TRANSACTION_ID`  
**Columns:** 16  
**Joined by:** 10 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TRANSACTION_ID` | VARCHAR | PK | The unique identifier (.1 item) for the detail transaction record. |
| 2 | `AR_TX_TYPE_C_NAME` | VARCHAR |  | The type of transaction. This indicates if the transaction is a charge, a payment, or an adjustment. |
| 3 | `AR_TX_CODE_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `AR_TX_AMOUNT` | NUMERIC |  | The dollar amount for a transaction. |
| 5 | `AR_TX_CAP_CNTRCT_ACCT_ID` | VARCHAR |  | The account that this transaction is posting to. |
| 6 | `AR_TX_COVERAGE_ID` | NUMERIC |  | The coverage that this transaction applies to. |
| 7 | `AR_TX_EFF_DATE` | DATETIME |  | The effective date that this transaction applies to. |
| 8 | `AR_MEMBER_PAT_ID` | VARCHAR | FK→ | The member that this transaction applies to. This applies only to per-member accounts. |
| 9 | `AR_SUBSCRIBER_PAT_ID` | VARCHAR | FK→ | The subscriber that this transaction applies to. |
| 10 | `AR_TX_STATUS_C_NAME` | VARCHAR |  | The current status for a transaction. |
| 11 | `AR_TX_FILED_DATE` | DATETIME |  | The date that a transaction has filed to the system. |
| 12 | `AR_TX_REVERSAL_ID` | VARCHAR |  | The transaction ID that is being reversed by a given transaction. |
| 13 | `AR_TX_CORRECTED_ID` | VARCHAR |  | The transaction ID that is being corrected by a given transaction. |
| 14 | `CAP_TX_SUBTYPE_C_NAME` | VARCHAR |  | Stores the subtype of the capitation transaction. Used to distinguish between different types of capitation payments made to a single account in the same month. |
| 15 | `CAP_TX_ADJ_RSN_C_NAME` | VARCHAR |  | Stores the adjustment reason code for the capitation transaction. |
| 16 | `CAP_TX_PMT_DATE` | DATETIME |  | Stores the date of the captiation payment |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AR_MEMBER_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `AR_SUBSCRIBER_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

## Joined in — referenced by (10)

| From | Column | Confidence |
|------|--------|------------|
| [CAP_RECV_STATUS_FLAGS](CAP_RECV_STATUS_FLAGS.md) | `TRANSACTION_ID` | high |
| [CAP_RECV_SUBCOMPONENTS](CAP_RECV_SUBCOMPONENTS.md) | `TRANSACTION_ID` | high |
| [CLAIM_FEE_DETAILS](CLAIM_FEE_DETAILS.md) | `TRANSACTION_ID` | high |
| [FOL_INFO](FOL_INFO.md) | `TRANSACTION_ID` | high |
| [PB_ACCT_TX_DTL](PB_ACCT_TX_DTL.md) | `TRANSACTION_ID` | high |
| [PB_DTL_TX_AR_STAT_HX](PB_DTL_TX_AR_STAT_HX.md) | `TRANSACTION_ID` | high |
| [PB_DTL_TX_MEM_RATE](PB_DTL_TX_MEM_RATE.md) | `TRANSACTION_ID` | high |
| [PB_TX_MTCH_HISTORY](PB_TX_MTCH_HISTORY.md) | `TRANSACTION_ID` | high |
| [V_EHI_PAX_PB_ACCT_TX_GRP_TTL](V_EHI_PAX_PB_ACCT_TX_GRP_TTL.md) | `TRANSACTION_ID` | high |
| [V_PB_TX_DTL_SNAPSHOT](V_PB_TX_DTL_SNAPSHOT.md) | `TRANSACTION_ID` | high |

