# PB_ACCT_TX_INV_NUM

> The PB_ACCT_TX_INV_NUM table includes a list of invoices and amounts associated with a premium billing account transaction.

**Primary key:** `PB_ACT_TX_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_ACT_TX_ID` | VARCHAR | PK shared | The unique ID of the premium account transaction. |
| 2 | `LINE` | INTEGER | PK | Line counter of the premium billing invoice history of the transaction. |
| 3 | `PB_INVC_ID` | VARCHAR | FK→ | The unique ID of the premium billing invoice. |
| 4 | `INVOICE_AMT` | NUMERIC |  | Amount of the premium account transaction that appeared on the related premium billing invoice. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_INVC_ID` | [PB_INVOICE](PB_INVOICE.md) | sole_pk | high |

