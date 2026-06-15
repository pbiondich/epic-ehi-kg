# HSP_BDC_RECV_TX

> This table contains recovery payment information for Denial/Correspondence (BDC) records.

**Primary key:** `BDC_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BDC_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the denial/correspondence record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RECV_PAYMENT_TX_ID` | NUMERIC |  | This column stores the hospital payment transactions posted onto this denial record. Payment transactions posted onto a bucket with open denial record on it will be linked here from this denial record. |
| 4 | `RECV_PAYMENT_TX_AMT` | NUMERIC |  | The dollar amount, corresponding to a payment transaction, posted onto this denial record. |
| 5 | `PB_RECV_PMT_TX_ID` | NUMERIC |  | This column stores the professional billing payment transactions posted onto this denial record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BDC_ID` | [BDC_INFO](BDC_INFO.md) | sole_pk | high |

