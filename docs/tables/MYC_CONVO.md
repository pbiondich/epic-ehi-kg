# MYC_CONVO

> MyChart conversations.

**Primary key:** `THREAD_ID`  
**Columns:** 7  
**Org-specific columns:** 1  
**Joined by:** 23 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `THREAD_ID` | NUMERIC | PK | The unique identifier (.1 item) for the thread record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The patient this conversation is about. Currently only ever expected to be one, but that could change in the future. |
| 3 | `COMM_ID` | NUMERIC | shared | Contains a link the communication record created for a customer service conversation. Not all customer service conversations will have this link, its creation is controlled by settings. |
| 4 | `SUBJECT` | VARCHAR |  | Subject of the conversation. |
| 5 | `MYC_MSG_TYP_C_NAME` | VARCHAR | org | The MyChart message type of this conversation. This is the primary message type that will be used for messages on this conversation. |
| 6 | `PAT_TASK_ID` | VARCHAR |  | Stores related patient assigned task ID for the conversation. |
| 7 | `ENROLL_ID` | NUMERIC | FK→ | The unique identifier (.1 item) for the research study enrollment information record for the conversation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (23)

| From | Column | Confidence |
|------|--------|------------|
| [IB_MESSAGE_THREAD](IB_MESSAGE_THREAD.md) | `THREAD_ID` | high |
| [IB_MESSAGE_THREA_4](IB_MESSAGE_THREA_4.md) | `THREAD_ID` | high |
| [MYC_CONVO_ABT_ACCOUNTS](MYC_CONVO_ABT_ACCOUNTS.md) | `THREAD_ID` | high |
| [MYC_CONVO_ABT_CLAIMS](MYC_CONVO_ABT_CLAIMS.md) | `THREAD_ID` | high |
| [MYC_CONVO_ABT_COVERAGES](MYC_CONVO_ABT_COVERAGES.md) | `THREAD_ID` | high |
| [MYC_CONVO_ABT_CUST_SVC](MYC_CONVO_ABT_CUST_SVC.md) | `THREAD_ID` | high |
| [MYC_CONVO_ABT_ESTIMATES](MYC_CONVO_ABT_ESTIMATES.md) | `THREAD_ID` | high |
| [MYC_CONVO_ABT_FIN_ASST](MYC_CONVO_ABT_FIN_ASST.md) | `THREAD_ID` | high |
| [MYC_CONVO_ABT_MEDICATIONS](MYC_CONVO_ABT_MEDICATIONS.md) | `THREAD_ID` | high |
| [MYC_CONVO_ABT_MED_ADVICE](MYC_CONVO_ABT_MED_ADVICE.md) | `THREAD_ID` | high |
| [MYC_CONVO_ABT_PAT_ENC](MYC_CONVO_ABT_PAT_ENC.md) | `THREAD_ID` | high |
| [MYC_CONVO_ABT_REFERRALS](MYC_CONVO_ABT_REFERRALS.md) | `THREAD_ID` | high |
| [MYC_CONVO_ABT_RSLT_ORDERS](MYC_CONVO_ABT_RSLT_ORDERS.md) | `THREAD_ID` | high |
| [MYC_CONVO_ABT_RX_ORDER](MYC_CONVO_ABT_RX_ORDER.md) | `THREAD_ID` | high |
| [MYC_CONVO_ABT_RX_ORD_FLG](MYC_CONVO_ABT_RX_ORD_FLG.md) | `THREAD_ID` | high |
| [MYC_CONVO_AUDIENCE](MYC_CONVO_AUDIENCE.md) | `THREAD_ID` | high |
| [MYC_CONVO_ENCS](MYC_CONVO_ENCS.md) | `THREAD_ID` | high |
| [MYC_CONVO_EXPORT_AUDIT](MYC_CONVO_EXPORT_AUDIT.md) | `THREAD_ID` | high |
| [MYC_CONVO_FUTURE_MSGS](MYC_CONVO_FUTURE_MSGS.md) | `THREAD_ID` | high |
| [MYC_CONVO_MSGS](MYC_CONVO_MSGS.md) | `THREAD_ID` | high |
| [MYC_CONVO_USERS](MYC_CONVO_USERS.md) | `THREAD_ID` | high |
| [MYC_CONVO_VIEWERS](MYC_CONVO_VIEWERS.md) | `THREAD_ID` | high |
| [PAT_ENC_THREADS](PAT_ENC_THREADS.md) | `THREAD_ID` | high |

