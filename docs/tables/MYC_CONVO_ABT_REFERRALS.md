# MYC_CONVO_ABT_REFERRALS

> Referrals associated with the MyChart message conversation.

**Primary key:** `THREAD_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `THREAD_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the thread record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REFERRAL_ID` | NUMERIC | FK→ | This is the referral that this conversation is about. |
| 4 | `AUTH_REQUEST_ID` | NUMERIC | FK→ | This is the authorization request that this conversation is about. |
| 5 | `INFO_REQ_CSN_ID` | NUMERIC |  | This is the Information Request that this conversation is about. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_REQUEST_ID` | [AUTH_REQUEST](AUTH_REQUEST.md) | sole_pk | high |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |
| `THREAD_ID` | [MYC_CONVO](MYC_CONVO.md) | sole_pk | high |

