# PB_ACCT_TX_DTL

> This table stores the linkages between the account posting transactions and their originating detail transactions.

**Primary key:** `TRANSACTION_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TRANSACTION_ID` | VARCHAR | PK FK→ | The unique identifier for the account transaction record resulting from a premium billing account posting. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DTL_TX_ID` | VARCHAR |  | The unique ID of the premium billing detailed transaction. |
| 4 | `DTL_TX_AMOUNT` | NUMERIC |  | The amount on the associated detailed transaction that contributed towards the account transaction at the time of posting. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `TRANSACTION_ID` | [CAP_DTL_TX](CAP_DTL_TX.md) | sole_pk | high |

