# MYC_CONVO_ENCS

> Contains the list of encounters that this message is directly connected to; the encounters created from sending a message. This is not the list of encounters that the conversation is about - for those encounters, see MYC_CONVO_ABT_PAT_ENCS.

**Primary key:** `THREAD_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `THREAD_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the thread record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | Contains the list of encounters that this conversation is attached to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `THREAD_ID` | [MYC_CONVO](MYC_CONVO.md) | sole_pk | high |

