# IB_MESSAGES_2

> The IB_MESSAGES_2 table contains basic information about In Basket messages.

**Overflow of:** [IB_MESSAGES](IB_MESSAGES.md)  
**Primary key:** `MSG_ID`  
**Columns:** 17  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MSG_ID` | VARCHAR | PK | The unique identifier (.1 item) for the task record. |
| 2 | `CCR_NOTE_ID` | VARCHAR |  | This is the note ID for a coding query message. |
| 3 | `ORDER_DAT` | NUMERIC |  | This column stores the contact date (DAT) of the order record linked to the message. |
| 4 | `ATTCHD_NOTE_REC_ID` | VARCHAR |  | Stores the note record attached to this message. |
| 5 | `NOTIF_SEND_TO_C_NAME` | VARCHAR |  | Stores the Send To Information for the Notification |
| 6 | `NOTIF_PCP_TYPE_C_NAME` | VARCHAR | org | Stores the PCP type if send to is set to PCP for Notifications |
| 7 | `NOTIF_NOTE_TYPE_C_NAME` | VARCHAR | org | Stores the note type for the Notification |
| 8 | `NOTIF_JOB_TYPE_C_NAME` | VARCHAR | org | Stores the Job Type in the Batch Print Utility for the Notification |
| 9 | `CAS_CREAT_SRC_TYP_C_NAME` | VARCHAR |  | Case create source type. |
| 10 | `SORT_ORDER` | VARCHAR |  | Additional Sort order. |
| 11 | `OR_CASE_ID` | VARCHAR | FK→ | The unique ID associated with the case record for In Basket messages of type case. This column is frequently used to link to the OR_CASE table. |
| 12 | `OR_CASE_ACTION_C_NAME` | VARCHAR | org | The category number representing the reason for the In Basket messages of type case. |
| 13 | `OR_LOG_ID` | VARCHAR |  | The unique ID associated with the log record for In Basket messages of type log. This column is frequently used to link to the OR_LOG table. |
| 14 | `OR_LOG_ACTION_C_NAME` | VARCHAR | org | The category number representing the reason for the In Basket messages of type log. |
| 15 | `EPT_CSN_ID` | NUMERIC |  | The contact serial number (CSN) for a patient contact associated with the In Basket message. This column should be replaced with IB_MESSAGE_PAT_ENCS.PAT_ENC_CSN_ID instead. Historical records will still use this column, but all new data will populate the other table and column. This will still be populated but may not contain the full set of data available in the other column and table. |
| 16 | `LINKED_EPISODE_ID` | NUMERIC |  | This column store the episode of care record ID of a linked episode. |
| 17 | `GEN_OVERDUE_MSG_ID` | VARCHAR |  | Stores the original message of an overdue message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_CASE_ID` | [OR_CASE](OR_CASE.md) | name_stem | high |

## Joined in

Inbound joins are tracked on the logical base [IB_MESSAGES](IB_MESSAGES.md).

