# MYC_CONVO_ABT_RX_ORD_FLG

> Prescription Flags associated with the MyChart message conversation.

**Primary key:** `THREAD_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `THREAD_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the thread record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RX_FLG_RECORD_ID` | NUMERIC |  | The prescription flag that is associated with the order record that this conversation is about. |
| 4 | `RX_FLG_RECORD_ID_RECORD_NAME` | VARCHAR |  | The flag name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `THREAD_ID` | [MYC_CONVO](MYC_CONVO.md) | sole_pk | high |

