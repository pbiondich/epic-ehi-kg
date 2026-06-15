# MYC_MESG_TRANS_INF

> This table contains items which define a credit card transaction.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The unique ID is used to identify a MyChart message record. A new record is created each time a patient sends a message from MyChart to a system user and each time a system user sends a message to MyChart patient. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CR_TX_INSTANT` | DATETIME (Local) |  | The instant the transaction status was updated. |
| 4 | `CR_TX_STATUS_C_NAME` | VARCHAR |  | The status of this transaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

