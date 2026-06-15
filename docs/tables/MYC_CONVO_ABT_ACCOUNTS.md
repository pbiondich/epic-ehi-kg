# MYC_CONVO_ABT_ACCOUNTS

> Guarantor accounts associated with MyChart message conversation.

**Primary key:** `THREAD_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `THREAD_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the thread record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACCOUNT_ID` | NUMERIC | FK→ | This is the guarantor account that this conversation is about. |
| 4 | `GUAR_BILL_SYS_TYPE_C_NAME` | VARCHAR |  | This the account type (PB, HB, SBO) for the guarantor account for this conversation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `THREAD_ID` | [MYC_CONVO](MYC_CONVO.md) | sole_pk | high |

