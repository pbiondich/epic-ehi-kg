# RXMA_QUEUE_REASON

> Reasons for submission to Medication Access.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `QUEUE_REASON_C_NAME` | VARCHAR |  | Category list of reason for submission to medication access |
| 4 | `QUEUE_ENTRY_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | Instant of submission to medication access |
| 5 | `QUEUE_ENTRY_USER_ID` | VARCHAR |  | User initiating medication access request |
| 6 | `QUEUE_ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `QUEUE_TRIAGE_RSLT_C_NAME` | VARCHAR |  | Action taken to address request |
| 8 | `QUEUE_EXIT_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | Instant to consider the medication access request completed |
| 9 | `QUEUE_EXIT_USER_ID` | VARCHAR |  | User performing action to resolve the medication access request |
| 10 | `QUEUE_EXIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `QUEUE_LINKED_ORDER_ID` | NUMERIC |  | Order related to the medication access request |
| 12 | `QUEUE_COMMENT` | VARCHAR |  | Optional comment from submission |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

